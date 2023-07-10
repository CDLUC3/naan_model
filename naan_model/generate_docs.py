
import argparse
import json
import logging
import sys

import pydantic
import naan_model

def generate_json_schema(public_only: bool = False):
    if public_only:
        schema = pydantic.TypeAdapter(naan_model.PublicNAAN).json_schema()
    else:
        schema = pydantic.TypeAdapter(naan_model.NAAN).json_schema()
    print(json.dumps(schema, indent=2))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-p", "--public", action="store_true", help="Output public content only."
    )
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO)
    generate_json_schema(public_only=args.public)
    return 0


if __name__ == "__main__":
    sys.exit(main())