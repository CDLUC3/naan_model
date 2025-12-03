import argparse
import json
import os
import sys
from pathlib import Path
import tempfile
import duckdb

#!/usr/bin/env python3
"""
load_duckdb.py

Command-line tool to populate a DuckDB database from JSON files found under a folder hierarchy.

Usage examples:
    python load_duckdb.py --root ./data --db mydb.duckdb

"""

def merge_json_files(root_dir, output_file_path):
    """
    Merges all JSON files found within a root directory and its subdirectories
    into a single JSON file.

    Args:
        root_dir (str): The path to the root directory containing JSON files.
        output_file_path (str): The path to the output JSON file.
    """
    merged_data = []

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            # Exclude the metadata.json file from the combined results            
            if filename.endswith(".json") and "metadata" not in filename:
                file_path = os.path.join(dirpath, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        merged_data.append(data)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON from {file_path}: {e}")
                except Exception as e:
                    print(f"An error occurred while processing {file_path}: {e}")

    try:
        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            json.dump(merged_data, outfile, indent=2)
        print(f"Successfully merged JSON files into {output_file_path}")
    except Exception as e:
        print(f"Error writing merged data to {output_file_path}: {e}")


def quote_path(p: Path) -> str:
    # escape single quotes for SQL literal
    s = str(p).replace("'", "''")
    return f"'{s}'"


def main(argv=None):
    p = argparse.ArgumentParser(description="Populate a DuckDB database with JSON files from a folder tree.")
    p.add_argument("--root", "-r", required=True, help="Root folder to search for JSON files")
    p.add_argument("--db", "-d", default=":memory:", help="DuckDB database file path (default :memory:)")
    p.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    args = p.parse_args(argv)
    
    with tempfile.NamedTemporaryFile(delete_on_close=False) as ftmp:
        ftmp.close()
        merge_json_files("../naan_reg_priv/naan_records", ftmp.name)
        try:
            conn = duckdb.connect(database=args.db)
        except Exception as e:
            print("Cannot connect to DuckDB:", e, file=sys.stderr)
            sys.exit(3)
        sql = f"CREATE TABLE records AS SELECT * FROM read_json_auto({quote_path(ftmp.name)});"
        conn.execute(sql)
        sql = "select count(*) as n from records;"
        conn.query(sql)
        print(f"Loaded {conn.fetchone()[0]} records.")


if __name__ == "__main__":
        main()