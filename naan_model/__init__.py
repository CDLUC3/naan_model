import dataclasses
import datetime
import json
import typing

class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.isoformat(timespec='seconds').replace("+00:00", "Z")
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)

@dataclasses.dataclass
class PublicNAAN_who:
    """Publicly visible information for organization responsible for NAAN"""

    name: str = dataclasses.field(
        metadata=dict(description="Official organization name")
    )
    acronym: typing.Optional[str] = dataclasses.field(
        default=None,
        metadata=dict(description="Optional display acronym derived from DNS name"),
    )

    @classmethod
    def from_dict(cls, data: dict) -> "PublicNAAN_who":
        name = data.get("name", None)
        if name is None:
            raise ValueError(f"name is required for PublicNAAN_who")
        return cls(
            name=data.get("name"),
            acronym=data.get("acronym", None)
        )


@dataclasses.dataclass
class NAAN_who(PublicNAAN_who):
    """Organization responsible for NAAN"""

    address: typing.Optional[str] = dataclasses.field(
        default=None, metadata=dict(description="Physical address of organization")
    )

    @classmethod
    def from_dict(cls, data: dict) -> "NAAN_who":
        public_who = super(NAAN_who, cls).from_dict(data)
        return cls(
            name=public_who.name,
            acronym=public_who.acronym,
            address=data.get("address", None)
        )


@dataclasses.dataclass
class NAAN_how:
    """Policy and tenure of NAAN management"""

    orgtype: str = dataclasses.field(
        metadata=dict(
            description="Organization type, FP = For profit, NP = Not for profit."
        )
    )
    policy: str = dataclasses.field(
        metadata=dict(
            description=(
                "Which practices do you plan to implement when you assign the base name "
                "of your ARKs? The ARK base name is between your NAAN and any suffix; for "
                "example, in ark:12345/x6np1wh8k/c3.xsl the base name is x6np1wh8k. This "
                "information can help others make the best use of your ARKs. Please submit "
                "updates as your practices evolve. "
                "\n"
                "'''\n"
                "NR = No re-assignment. Once a base identifier-to-object association\n"
                "     has been made public, that association shall remain unique into\n"
                "     the indefinite future.\n"
                "OP = Opacity. Base identifiers shall be assigned with no widely\n"
                "     recognizable semantic information.\n"
                "CC = A check character is generated in assigned identifiers to guard\n"
                "     against common transcription errors.\n"
                "'''\n"
            )
        )
    )
    tenure: str = dataclasses.field(
        metadata=dict(description="<start year YYYY of role tenure>[-<end of tenure> ]")
    )
    policy_url: typing.Optional[str] = dataclasses.field(
        default=None, metadata=dict(description="URL to narrative policy statement")
    )

    @classmethod
    def from_dict(cls, data: dict) -> 'NAAN_how':
        orgtype = data.get("orgtype")
        if orgtype is None:
            raise ValueError("orgtype is required for NAAN_how")
        policy = data.get("policy")
        if policy is None:
            raise ValueError("policy is required for NAAN_how")
        tenure = data.get("tenure")
        if tenure is None:
            raise ValueError("tenure is required for NAAN_how")
        return NAAN_how(
            orgtype=orgtype,
            policy=policy,
            tenure=tenure,
            policy_url=data.get("policy_url", None)
        )


@dataclasses.dataclass
class NAAN_contact:
    name: str = dataclasses.field(metadata=dict(description="Name of contact"))
    unit: typing.Optional[str] = dataclasses.field(
        default=None, metadata=dict(description="Name of contact organization")
    )
    tenure: typing.Optional[str] = dataclasses.field(
        default=None,
        metadata=dict(
            description="<start year YYYY of role tenure>[-<end of tenure> ]"
        ),
    )
    email: typing.Optional[str] = dataclasses.field(
        default=None, metadata=dict(description="Email address of contact")
    )
    phone: typing.Optional[str] = dataclasses.field(
        default=None, metadata=dict(description="Telephone number for contact")
    )

    @classmethod
    def from_dict(cls, data: dict) -> "NAAN_contact":
        name = data.get("name")
        if name is None:
            raise ValueError("name is required for NAAN_contact")
        return NAAN_contact(
            name=name,
            unit=data.get("unit", None),
            tenure=data.get("tenure", None),
            email=data.get("email", None),
            phone=data.get("phone", None)
        )


@dataclasses.dataclass
class Target:
    url_template: str = dataclasses.field(
        metadata=dict(
            description="A URL template that will be used to form the redirect target for matching identifiers.")
    )
    redirect_code: int = dataclasses.field(
        default=301,
        metadata=dict(description="The HTTP status code that will be used to redirect requests.")
    )
    media_type: typing.Optional[str] = dataclasses.field(
        default=None,
        metadata=dict(description="IANA media type for this this target will be used.")
    )

    def __post_init__(self):
        for field in dataclasses.fields(self):
            if not isinstance(field.default, dataclasses._MISSING_TYPE) and getattr(self, field.name) is None:
                setattr(self, field.name, field.default)

    @classmethod
    def from_dict(cls, data:dict) -> "Target":
        url_template = data.get("url_template")
        if url_template is None:
            raise ValueError("url_template is required for Target")
        return Target(
            url_template=url_template,
            redirect_code=data.get("redirect_code"),
            media_type=data.get("media_type", None)
        )


@dataclasses.dataclass
class PublicNAAN:
    what: str = dataclasses.field(
        metadata=dict(description="The NAAN value, e.g. 12345 as a string.")
    )
    where: str = dataclasses.field(
        metadata=dict(description="URL of service endpoint accepting ARK identifiers.")
    )
    target: typing.List[Target] = dataclasses.field(
        metadata=dict(
            description=(
                "List of Targets that define the redirect location and status code for "
                "a media_type"
            )
        )
    )
    when: datetime.datetime = dataclasses.field(
        metadata=dict(description="Date when this record was last modified.")
    )
    who: PublicNAAN_who
    na_policy: NAAN_how
    alternate_who: typing.Optional[PublicNAAN_who] = None
    test_identifier: str = dataclasses.field(
        default=None,
        metadata=dict(
            description=(
                "A specific, concrete ARK that you plan to support and that you will permit us to "
                "use periodically for testing service availability."
            )
        ),
    )
    service_provider: typing.Optional[str] = dataclasses.field(
        default=None,
        metadata=dict(
            description=(
                'A "service provider" is different from the NAAN holder organization. It provides '
                "technical assistance to the the NAAN organization such as content hosting, access, "
                "discovery, etc."
            )
        ),
    )
    purpose: str = dataclasses.field(
        default="unspecified",
        metadata=dict(
            description=(
                "What are you planning to assign ARKs to using the requested NAAN?"
                "Options: "
                "documents(text or page images, eg, journal articles, technical reports); "
                "audio - and / or video - based objects; "
                "non-text, non-audio / visual documents(eg, maps, posters, musical scores); "
                "datasets (eg, spreadsheets, collections of spreadsheets); "
                "records (eg, bibliographic records, archival finding aids); "
                "physical objects(eg, fine art, archaeological artifacts, scientific samples)"
                "concepts (eg, vocabulary terms, disease codes); "
                "agents (people, groups, and institutions as actors, eg, creators, contributors, publishers, performers, etc); "
                "other; "
                "unspecified; "
            )
        ),
    )

    def __post_init__(self):
        for field in dataclasses.fields(self):
            # If there is a default and the value of the field is none we can assign a value
            if not isinstance(field.default, dataclasses._MISSING_TYPE) and getattr(self, field.name) is None:
                setattr(self, field.name, field.default)


    def as_flat(self) -> dict:
        return {
            "what": self.what,
            "who": self.who.name,
            "where": self.where,
            "when": self.when,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "PublicNAAN":
        who = PublicNAAN_who.from_dict(data.get('who', {}))
        na_policy = NAAN_how.from_dict(data.get('na_policy', {}))
        alternate_who = None
        a_data = data.get("alternate_who", None)
        if a_data is not None:
            alternate_who = PublicNAAN_who.from_dict(a_data)
        target = []
        t_data = data.get("target", None)
        if isinstance(t_data, dict):
            target = [Target.from_dict(data.get("target", {})), ]
        elif isinstance(t_data, list):
            for t in t_data:
                target.append(Target.from_dict(t))
        when = data.get("when", "")
        when = datetime.datetime.strptime(when, "%Y-%m-%dT%H:%M:%S%z")
        return PublicNAAN(
            what=data.get("what"),
            where=data.get("where"),
            target=target,
            when=when,
            who=who,
            na_policy=na_policy,
            alternate_who=alternate_who,
            test_identifier=data.get("test_identifier"),
            service_provider=data.get("service_provider"),
            purpose=data.get("purpose")
        )


@dataclasses.dataclass
class NAAN(PublicNAAN):
    who: NAAN_who
    why: str = dataclasses.field(
        default="ARK", metadata=dict(description="Purpose for this record, 'ARK'")
    )
    alternate_who: typing.Optional[NAAN_who] = None
    contact: typing.Optional[NAAN_contact] = None
    alternate_contact: typing.Optional[NAAN_contact] = None
    comments: typing.Optional[typing.List[dict]] = dataclasses.field(
        default=None, metadata=dict(description="Comments about NAAN record")
    )
    provider: typing.Optional[str] = dataclasses.field(
        default=None, metadata=dict(description="")
    )

    @property
    def key(self) -> str:
        return self.what

    def as_public(self) -> PublicNAAN:
        public_who = PublicNAAN_who(self.who.name, self.who.acronym)
        public_alt_who = (
            None
            if self.alternate_who is None
            else PublicNAAN_who(self.alternate_who.name, self.alternate_who.acronym)
        )
        public = PublicNAAN(
            self.what,
            self.where,
            self.target,
            self.when,
            public_who,
            self.na_policy,
            public_alt_who,
            self.test_identifier,
            self.service_provider,
            self.purpose,
        )
        return public

    @classmethod
    def from_dict(cls, data: dict) -> "NAAN":
        who = NAAN_who.from_dict(data.get('who', {}))
        na_policy = NAAN_how.from_dict(data.get('na_policy', {}))
        alternate_who = None
        a_data = data.get("alternate_who", None)
        if a_data is not None:
            alternate_who = PublicNAAN_who.from_dict(a_data)
        target = []
        t_data = data.get("target", None)
        if isinstance(t_data, dict):
            target = [Target.from_dict(data.get("target", {})), ]
        elif isinstance(t_data, list):
            for t in t_data:
                target.append(Target.from_dict(t))
        when = data.get("when", "")
        when = datetime.datetime.strptime(when, "%Y-%m-%dT%H:%M:%S%z")
        return NAAN(
            what=data.get("what"),
            where=data.get("where"),
            target=target,
            when=when,
            who=who,
            na_policy=na_policy,
            alternate_who=alternate_who,
            test_identifier=data.get("test_identifier"),
            service_provider=data.get("service_provider"),
            purpose=data.get("purpose")
        )


def naan_record_from_json(data:typing.Union[str, dict]) -> NAAN:
    if isinstance(data, str):
        data = json.loads(data)
    return NAAN.from_dict(data)


def naan_record_to_json(naan:typing.Union[NAAN, PublicNAAN], **kwparams) -> str:
    kwparams["cls"] = EnhancedJSONEncoder
    return json.dumps(naan, **kwparams)
