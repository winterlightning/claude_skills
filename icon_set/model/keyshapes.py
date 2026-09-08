"""Frozen keyshape tokens and the rational 1x / 1.5x / 2x resolver.

All standard dimensions are centered *visible-ink* bounds. SOLO48 is exactly
the SUB32 base multiplied by 3/2; CONTAINER64 is exactly the base multiplied
by 2. Every resolution is integer arithmetic; nothing here uses floats.

The ten base sizes are read from ``keyshapes.v1.json`` rather than restated
here, so the contract is the only place a keyshape dimension is written and a
proposal measured through ``icon_set/scripts/profile_lab.py`` reaches the enum
like any other contract value.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from . import contracts
from .profiles import ENVELOPE_RADIUS, Profile

_KEYSHAPES = contracts.keyshapes()
_BASE = {row["name"]: row for row in _KEYSHAPES["base"]}

#: Identifiers deliberately reserved but not valid v1 enum values. Requesting
#: one must fail until a fifth base size is explicitly approved.
RESERVED_TOKENS: frozenset[str] = frozenset(_KEYSHAPES["reserved_tokens"])


class ReservedKeyshapeError(ValueError):
    """Raised when a reserved XS identifier is requested."""


@dataclass(frozen=True)
class KeyshapeSize:
    width: int
    height: int

    def for_profile(self, profile: Profile) -> "KeyshapeSize":
        scale = profile.spec.scale_keyshape_value
        return KeyshapeSize(scale(self.width), scale(self.height))


def _base(name: str) -> tuple[str, "KeyshapeSize", str]:
    """Token, size and orientation for one base keyshape, from the contract."""
    row = _BASE[name]
    return (row["token"], KeyshapeSize(row["width"], row["height"]), row["orientation"])


class Keyshape(Enum):
    CIRCLE = _base("CIRCLE")
    SQUARE = _base("SQUARE")
    HRECT_XL = _base("HRECT_XL")
    HRECT_L = _base("HRECT_L")
    HRECT_M = _base("HRECT_M")
    HRECT_S = _base("HRECT_S")
    VRECT_XL = _base("VRECT_XL")
    VRECT_L = _base("VRECT_L")
    VRECT_M = _base("VRECT_M")
    VRECT_S = _base("VRECT_S")
    FREE = ("free", None, "free")

    def __init__(
        self,
        token: str,
        base_size: KeyshapeSize | None,
        orientation: str,
    ) -> None:
        self.token = token
        self.base_size = base_size
        self.orientation = orientation

    @property
    def is_radial(self) -> bool:
        return self.orientation == "radial"

    def size_for(self, profile: Profile) -> KeyshapeSize:
        if self.base_size is None:
            raise ValueError("FREE requires explicit approved dimensions")
        return self.base_size.for_profile(profile)

    def bounds_for(self, profile: Profile) -> tuple[int, int, int, int]:
        size = self.size_for(profile)
        canvas = profile.spec.canvas_size
        left, x_remainder = divmod(canvas - size.width, 2)
        top, y_remainder = divmod(canvas - size.height, 2)
        if x_remainder or y_remainder:
            raise ValueError("keyshape must center on the integer grid")
        return (left, top, left + size.width, top + size.height)

    def visible_radius_for(self, profile: Profile) -> float:
        """Painted radius for the radial token; only CIRCLE has one."""
        if not self.is_radial:
            raise ValueError(f"{self.name} is not a radial keyshape")
        return self.size_for(profile).width / 2.0

    def centerline_radius_for(self, profile: Profile) -> float:
        return self.visible_radius_for(profile) - ENVELOPE_RADIUS


def resolve_token(name: str) -> Keyshape:
    """Look a keyshape up by enum name, failing loudly on reserved tokens."""
    upper = name.upper().replace("-", "_")
    if upper in RESERVED_TOKENS:
        raise ReservedKeyshapeError(
            f"{upper} is a reserved identifier, not a valid v1 keyshape; "
            "a fifth base size must be explicitly approved first"
        )
    try:
        return Keyshape[upper]
    except KeyError as error:
        raise ValueError(f"unknown keyshape token: {name!r}") from error


@dataclass(frozen=True)
class FreeKeyshapeSpec:
    left: int
    top: int
    right: int
    bottom: int
    rationale: str
    approval_id: str | None = None

    @property
    def width(self) -> int:
        return self.right - self.left

    @property
    def height(self) -> int:
        return self.bottom - self.top

    def bounds_for(self, profile: Profile) -> tuple[int, int, int, int]:
        canvas = profile.spec.canvas_size
        if not (
            0 <= self.left < self.right <= canvas
            and 0 <= self.top < self.bottom <= canvas
        ):
            raise ValueError("FREE bounds must be positive and inside the canvas")
        return (self.left, self.top, self.right, self.bottom)


def approved_free_spec(icon_id: str, profile: Profile) -> FreeKeyshapeSpec | None:
    """Build the FreeKeyshapeSpec recorded in the exceptions contract."""
    record = contracts.approved_free_keyshapes().get((icon_id, profile.name))
    if record is None:
        return None
    left, top, right, bottom = record["bounds"]
    return FreeKeyshapeSpec(
        left, top, right, bottom,
        rationale=record["rationale"],
        approval_id=record["approval_id"],
    )


# The enum takes its numbers from the contract, so the two cannot drift; what
# is still worth asserting at import is that the two tables name the same ten
# shapes. A contract that adds or drops a base size needs an enum member for
# it, and a member with no contract row would have failed in `_base` above.
assert {shape.name for shape in Keyshape if shape is not Keyshape.FREE} == set(_BASE), (
    "keyshape enum and contract disagree on which base sizes exist"
)
