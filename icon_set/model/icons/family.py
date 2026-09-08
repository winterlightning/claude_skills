"""The shared base of the three authored families.

A family is a folder, a profile and a job, bound together by the profile
contract. ``FamilyIcon`` reads the profile *from the family name*, so a subclass
can say which family it belongs to but never which canvas it draws on -- the
contract decides that, and the registry refuses a module that lands in the
wrong folder. This is what keeps the 32, 48 and 64 profiles from injecting into
one another.

Concrete bases:

- :class:`~icon_set.model.icons.sub._base.Sub32` -- ``sub`` on SUB32
- :class:`~icon_set.model.icons.solo._base.Solo48` -- ``solo`` on SOLO48
- :class:`~icon_set.model.icons.container._base.Container64` -- ``container``
  on CONTAINER64
"""

from __future__ import annotations

from ..keyshapes import Keyshape, approved_free_spec
from ..profiles import Profile
from .base import Icon


class FamilyIcon(Icon):
    """An icon authored in one of the three families.

    Subclasses set ``icon_id``, ``keyshape``, ``semantic_kind``, ``category``,
    ``aliases`` and ``keywords`` as class attributes and author geometry in
    ``build()``. The profile is not a class attribute: it is resolved from
    ``family`` through the contract at construction.

    A FREE keyshape is looked up in the approved exceptions contract under
    ``(icon_id, profile)``, so an unapproved FREE fails construction rather
    than release.
    """

    #: Set once per family base; every subject inherits it.
    family: str = ""

    icon_id: str = ""
    keyshape: Keyshape = Keyshape.SQUARE
    semantic_role: str = "MAIN"
    semantic_kind: str = "noun"
    category: str = ""
    aliases: tuple[str, ...] = ()
    keywords: tuple[str, ...] = ()

    def __init__(self) -> None:
        cls = type(self)
        if not cls.family:
            raise TypeError(f"{cls.__name__} declares no family; use a family base")
        profile = Profile.for_family(cls.family)
        keyshape = cls.keyshape
        free = None
        if keyshape is Keyshape.FREE:
            free = approved_free_spec(cls.icon_id, profile)
            if free is None:
                raise ValueError(
                    f"{cls.icon_id!r} uses FREE on {profile.name} without a record "
                    "in model/contracts/exceptions.v1.json"
                )
        super().__init__(
            cls.icon_id,
            profile,
            semantic_role=cls.semantic_role,
            keyshape=keyshape,
            free_keyshape=free,
        )
        self.add_anchor("center", profile.spec.center)
        self.place_family_anchors()
        self.build()

    def place_family_anchors(self) -> None:
        """Hook for a family to add its own anchors before ``build()``."""

    def build(self) -> None:  # pragma: no cover - overridden by every subject
        raise NotImplementedError
