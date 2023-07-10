import dataclasses
import datetime
import typing

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


@dataclasses.dataclass
class NAAN_who(PublicNAAN_who):
    """Organization responsible for NAAN"""

    address: str = dataclasses.field(
        default=None, metadata=dict(description="Physical address of organization")
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


@dataclasses.dataclass
class PublicNAAN:
    what: str = dataclasses.field(
        metadata=dict(description="The NAAN value, e.g. 12345")
    )
    where: str = dataclasses.field(
        metadata=dict(description="URL of service endpoint accepting ARK identifiers.")
    )
    target: str = dataclasses.field(
        metadata=dict(
            description=(
                "URL of service endpoint accepting ARK identifiers including subsitution"
                "parameters $arkpid for full ARK or $pid for NAAN/suffix."
            )
        )
    )
    when: datetime.datetime = dataclasses.field(
        metadata=dict(description="Date when this record was last modified.")
    )
    who: PublicNAAN_who
    na_policy: NAAN_how
    test_identifier: str = dataclasses.field(
        default=None,
        metadata=dict(
            description=(
                "A specific, concrete ARK that you plan to support and that you will permit us to"
                "use periodically for testing service availability."
            )
        )
    )
    service_provider: str = dataclasses.field(
        default=None,
        metadata=dict(
            description=(
                'A "service provider" is different from the NAAN holder organization. It provides '
                "technical assistance to the the NAAN organization such as content hosting, access, "
                "discovery, etc."
            )
        )
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
        )
    )

    def as_flat(self) -> dict:
        return {
            "what": self.what,
            "who": self.who.name,
            "where": self.where,
            "when": self.when,
        }


@dataclasses.dataclass
class NAAN(PublicNAAN):
    who: NAAN_who
    why: str = dataclasses.field(
        default='ARK',
        metadata=dict(description="Purpose for this record, 'ARK'")
    )
    contact: NAAN_contact=None
    alternate_contact: NAAN_contact=None
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
        public = PublicNAAN(
            self.what, self.where, self.target, self.when, public_who, self.na_policy,
            self.test_identifier, self.service_provider, self.purpose
        )
        return public

