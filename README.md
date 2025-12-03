# naan_model

JSON schema and validator for ARK identifier NAAN and Shoulder records.

This repository contains a JSON Schema document that can be used to validate the 
structure of NAAN and Shoulder records maintained in the NAAN registry. Also 
included is a python script to validate records and a utility for loading all
records into a DuckDB instance to facilitate bulk analysis of the records.

## Operation

The `validate.py` script evaluates one or more JSON records against the 
`naan_schema.json` JSON schema document and reports on the outcome.

Validate a single file:
```
$ python validate.py  ../naan_reg_priv/naan_records/6/61910.json 
INFO:validator:Record 61910 is valid.
```

Validate a folder (including sub-folders):
```
$ python validate.py -l INFO ../naan_reg_priv/naan_records/  
INFO:validator:Record 99152/h3 is valid.
INFO:validator:Record 99152/r5 is valid.
INFO:validator:Record 99152/t8 is valid.
...
```

The script will have an exit code indicative of the number of erroneous 
documents. Hence, exit code 0 mean no errors, exit code 10 means 10 erroneous 
documents.

## Installation

```
export UV_PYTHON=3.12
uv env .venv
source .venv/bin/activate
uv sync
```

## Acknowledgement

This work is supported by the California Digital Library.
