import dataclasses
import datetime
import json

import pydantic
import pydantic.type_adapter
import pytest

import naan_model

test_data = [
    (
        naan_model.PublicNAAN,
        naan_model.PublicNAAN(
            what="12345",
            where="https://example.net/",
            target=[
                naan_model.Target(
                    url_template="https://example.net/$arkpid",
                    redirect_code=301,
                    media_type=None
                ),
            ],
            when=datetime.datetime(2023, 7, 11, 6, 30, 00, tzinfo=datetime.UTC),
            who=naan_model.PublicNAAN_who(
                name="Dave",
                acronym=None,
            ),
            na_policy=naan_model.NAAN_how(
                orgtype="NP",
                policy="(:unkn) unknown",
                tenure="2023",
                policy_url=None
            ),
            test_identifier="ark:12345/test",
            service_provider=None,
            purpose="unspecified"
        ),
        json.dumps({
            "what": "12345",
            "where": "https://example.net/",
            "target": [
                {
                    "url_template": "https://example.net/$arkpid",
                    "redirect_code": 301,
                    "media_type": None
                },
            ],
            "when": "2023-07-11T06:30:00Z",
            "who": {
                "name": "Dave",
                "acronym": None
            },
            "na_policy": {"orgtype": "NP", "policy": "(:unkn) unknown", "tenure": "2023", "policy_url": None},
            "alternate_who": None,
            "test_identifier": "ark:12345/test",
            "service_provider": None,
            "purpose": "unspecified"
        }),
    )
]

@pytest.mark.parametrize("mclass,A,B", test_data)
def test_public_json_out(mclass, A, B):
    # Convert input public model to JSON
    json_data = pydantic.RootModel[mclass](A).model_dump_json()
    # Compare de-serialized JSON
    assert json.loads(json_data) == json.loads(B)


@pytest.mark.parametrize("mclass,A,B", test_data)
def test_public_json_in(mclass, A, B):
    adapter = pydantic.TypeAdapter(mclass)
    parsed = adapter.validate_json(B)
    assert A == parsed


@pytest.mark.parametrize("mclass,A,B", test_data)
def test_load_json(mclass, A, B):
    parsed = naan_model.naan_record_from_json(B)
    assert parsed.__class__ == naan_model.NAAN
    pub = parsed.as_public()
    assert pub.__class__ == naan_model.PublicNAAN
    assert pub == A

@pytest.mark.parametrize("mclass,A,B", test_data)
def test_load_json_in(mclass, A, B):
    serialized = naan_model.naan_record_to_json(A)
    assert serialized == B
