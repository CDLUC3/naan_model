# naan_model

The ARK identifier NAAN model used by the registry and resolver services.

For JSON-schema generation, `pydantic` is required:
```
pip install pydantic
```

The public view and full view have different schemas, they can be generated like:
```
$python naan_reg_json.py -s > schema/naan_schema.json
```
and
```
$python naan_reg_json.py -s -p > schema/public/naan_schema.json
```

Schema documentation can be generated if `json-schema-for-humans` is installed:
```
pip install json-schema-for-humans
```

To generate the schema documentation:
```
generate-schema-doc --config-file docs_config.yaml ./schema/naan_schema.json ./schema/
generate-schema-doc --config-file docs_config.yaml --config template_name=md ./schema/naan_schema.json ./schema/
generate-schema-doc --config-file docs_config.yaml ./schema/public/naan_schema.json ./schema/public/
generate-schema-doc --config-file docs_config.yaml --config template_name=md ./schema/public/naan_schema.json ./schema/public/
```

## Acknowledgement

This work is supported by the California Digital Library.
