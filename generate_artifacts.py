"""Script to generate artifacts from the NAAN model.

This script will output json-schema and markdown documentation for the
public and private views of the naan_model.

The default output is to the folder ./schema relative to the location
of this file.
"""
import argparse
import json
import logging
import os
import sys

import pydantic
import json_schema_for_humans.generate
import json_schema_for_humans.generation_configuration

import naan_model

DEFAULT_OUTPUT = os.path.join(os.path.dirname(__file__), "./schema")


def generate_json_schema(public_only: bool = False):
    if public_only:
        schema = pydantic.TypeAdapter(naan_model.PublicNAAN).json_schema()
    else:
        schema = pydantic.TypeAdapter(naan_model.NAAN).json_schema()
    return schema


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-d",
        "--docspath",
        default=DEFAULT_OUTPUT,
        help=f"Base path for generate documents ({DEFAULT_OUTPUT})",
    )
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)
    public_dir = os.path.join(args.docspath, "public")
    private_dir = os.path.join(args.docspath, "private")
    os.makedirs(public_dir, exist_ok=True)
    os.makedirs(private_dir, exist_ok=True)
    with open(os.path.join(private_dir, "schema.json"), "w") as dst:
        json.dump(generate_json_schema(), dst, indent=2)
    with open(os.path.join(public_dir, "schema.json"), "w") as dst:
        json.dump(generate_json_schema(public_only=True), dst, indent=2)

    docs_config_md = (
        json_schema_for_humans.generation_configuration.GenerationConfiguration(
            copy_css=True,
            description_is_markdown=True,
            minify=False,
            show_toc=True,
            template_name="md",
            with_footer=True,
            footer_show_time=True,
        )
    )
    for dest_dir in (
        private_dir,
        public_dir,
    ):
        json_schema_for_humans.generate.generate_from_filename(
            os.path.join(dest_dir, "schema.json"),
            os.path.join(dest_dir, "schema.md"),
            config=docs_config_md,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
