#!/usr/bin/env python3
"""
validate.py

Validate a NAAN or shoulder JSON record against the schema.

Usage:
    python validate.py data.json schema.json
"""

import argparse
import json
import os
import sys
import logging
from pathlib import Path
import compact_json
import jsonschema
from jsonschema import exceptions, validators


def get_logger():
    return logging.getLogger("validator")


def load_json(path: Path):
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(2)
    except json.JSONDecodeError as exc:
        print(f"Error: invalid JSON in {path}: {exc}", file=sys.stderr)
        sys.exit(2)

def validate_record(validator, instance_path, formatter=None)->int:
    L = get_logger()
    L.debug("Loading instance: %s", instance_path)
    instance = load_json(instance_path)
    instance_name = instance.get("what", instance_path)
    
    errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))

    if not errors:
        L.info(f"Record {instance_name} is valid.")
        return 0

    # There are validation errors
    L.error(f"Validation of {instance_name} failed: {len(errors)} error(s) found.")
    print("=====")
    print(f"Source: {instance_name}")
    for i, err in enumerate(errors, start=1):
        # Human-friendly location (path within instance)
        instance_path = "/".join(str(p) for p in err.path) or "(root)"
        schema_path = "/".join(str(p) for p in err.schema_path) or "(root)"
        print(f"[{i}] {err.message}")
        print(f"    instance path: {instance_path}")
        print(f"    schema path:   {schema_path}")
        if formatter is not None:
            # Show the failing instance and the part of schema that failed, if available
            try:
                # err.instance may be any python object; json.dumps may fail for some types
                inst_str = formatter.serialize(err.instance)
            except Exception:
                inst_str = repr(err.instance)
            try:
                sch_fragment = formatter.serialize(err.schema)
            except Exception:
                sch_fragment = repr(err.schema)
            print(f"    failing instance: {inst_str}")
            print(f"    failing schema fragment: {sch_fragment}")
    return 1

def list_source_files(root):
    if os.path.isfile(root):
        yield root
        return
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            # Exclude the metadata.json file from the combined results            
            if filename.endswith(".json") and "metadata" not in filename:
                file_path = os.path.join(dirpath, filename)
                yield Path(file_path)


def main():
    parser = argparse.ArgumentParser(description="Validate a JSON file against a JSON Schema.")
    parser.add_argument("json_file", type=Path, help="Path to the JSON file to validate.")
    parser.add_argument(
        "-s",
        "--schema", 
        default=os.environ.get("NAAN_SCHEMA", "schema/naan_schema.json"), 
        type=Path, 
        help="Path to the JSON Schema file.")
    parser.add_argument(
        "-l",
        "--loglevel",
        default="INFO",
        help="Logging level (DEBUG, *INFO*, WARNING, ERROR, CRITICAL).",
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")

    args = parser.parse_args()
    log_level = logging.getLevelNamesMapping()[args.loglevel.upper()]
    logging.basicConfig(level=log_level)
    L = get_logger()
    formatter = None
    if args.verbose:
        formatter = compact_json.Formatter()
        formatter.indent_spaces = 2
        formatter.max_inline_complexity = 5
        formatter.json_eol_style = compact_json.EolStyle.LF

    L.debug("Loading schema: %s", args.schema)
    schema = load_json(args.schema)

    # Choose the appropriate validator for the schema version
    ValidatorClass = validators.validator_for(schema)
    ValidatorClass.check_schema(schema)
    validator = ValidatorClass(schema, format_checker=jsonschema.FormatChecker())
    error_count = 0
    for file_name in list_source_files(args.json_file):
        error_count += validate_record(validator, file_name, formatter=formatter)
    sys.exit(error_count)


if __name__ == "__main__":
    main()