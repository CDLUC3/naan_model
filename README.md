# naan_model

The ARK identifier NAAN model used by the registry and resolver services.

> **Note** 
> :information_source: (2023-07-11) This model is currently a draft and is not deployed in production systems.

This repository provides a model for ARK NAAN registry entries and includes the internal private view (with contact information) and a public view which excludes contact information from the model.

The model is implemented using Python dataclasses form which a [JSON-Schema](https://json-schema.org/specification.html) is generated using [`pydantic`](https://docs.pydantic.dev/latest/usage/json_schema/). A markdown rendering of the schema is also generated using [`json-schema-for-humans`](https://github.com/coveooss/json-schema-for-humans).

The python code is located in the [`naan_model`](./naan_model) package, and the generated JSON-schema and markdown are located in the [`schema/`](./schema) folder.

## Acknowledgement

This work is supported by the California Digital Library.
