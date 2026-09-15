"""Frozen profile constants (ICON_SYSTEM_PLAN.md section 2).

``Profile.spec`` is the single access path for canvas size, interior guide,
MIC, and the rational keyshape scale. Values are read from the locked profile
contract; nothing here restates a number.

A profile is named for the family that owns it plus its canvas size --
``SUB32``, ``SOLO48``, ``CONTAINER64`` -- and ``Profile.family`` returns that
owner. The binding is one-to-one and read from the contract, so no family can
author on another family's canvas.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from . import contracts

_PROFILE = contracts.icon_profile()
_STYLE = _PROFILE["style"]
_TOLERANCES = _PROFILE["tolerances"]

GRID: int = _STYLE["grid"]
STROKE_WIDTH: int = _STYLE["stroke_width"]
STROKE: str = _STYLE["stroke"]
FILL: str = _STYLE["fill"]
LINE_CAP: str = _STYLE["line_cap"]
LINE_JOIN: str = _STYLE["line_join"]

#: Half the stroke: the exact radius of the disc whose Minkowski sum with the
#: centerline is the painted envelope, because every cap and join is round.
ENVELOPE_RADIUS: float = STROKE_WIDTH / 2.0

RECT_FIT_TOLERANCE: float = float(_TOLERANCES["rect_family_fit"])
CIRCLE_TOUCH_TOLERANCE: float = float(_TOLERANCES["circle_touch"])
CANVAS_OVERFLOW_TOLERANCE: float = float(_TOLERANCES["canvas_overflow"])
MIC_FLATTENING_TOLERANCE: float = float(_TOLERANCES["mic_flattening"])

#: Absorbs floating-point construction error, never a design allowance. An SVG
#: arc's centre is derived from its endpoints through a square root, so an
#: extremum that is mathematically exact can land ~1e-15 away from its integer.
#: Added on top of the design tolerances above; raising it to make artwork fit
#: is a rule change, not a repair.
NUMERIC_EPSILON: float = float(_TOLERANCES["numeric_epsilon"])

SEMANTIC_ROLES: tuple[str, ...] = tuple(_PROFILE["semantic_roles"])


@dataclass(frozen=True)
class ProfileSpec:
    canvas_size: int
    family: str
    interior_guide_inset: int
    mic: int
    equal_stroke_centerline_min: int
    keyshape_scale_numerator: int
    keyshape_scale_denominator: int
    semantic_use: str = ""

    @property
    def interior_guide_size(self) -> int:
        return self.canvas_size - 2 * self.interior_guide_inset

    @property
    def interior_guide_bounds(self) -> tuple[int, int, int, int]:
        edge = self.canvas_size - self.interior_guide_inset
        inset = self.interior_guide_inset
        return (inset, inset, edge, edge)

    @property
    def center(self) -> tuple[int, int]:
        half, remainder = divmod(self.canvas_size, 2)
        if remainder:
            raise ValueError("canvas size must be even to have an integer center")
        return (half, half)

    def scale_keyshape_value(self, value: int) -> int:
        scaled, remainder = divmod(
            value * self.keyshape_scale_numerator,
            self.keyshape_scale_denominator,
        )
        if remainder:
            raise ValueError("keyshape scaling must produce an integer")
        return scaled


def _spec(name: str) -> ProfileSpec:
    data = _PROFILE["profiles"][name]
    return ProfileSpec(
        canvas_size=data["canvas_size"],
        family=data["family"],
        interior_guide_inset=data["interior_guide_inset"],
        mic=data["mic"],
        equal_stroke_centerline_min=data["equal_stroke_centerline_min"],
        keyshape_scale_numerator=data["keyshape_scale_numerator"],
        keyshape_scale_denominator=data["keyshape_scale_denominator"],
        semantic_use=data["semantic_use"],
    )


class Profile(Enum):
    SUB32 = _spec("SUB32")
    SOLO48 = _spec("SOLO48")
    CONTAINER64 = _spec("CONTAINER64")

    @property
    def spec(self) -> ProfileSpec:
        return self.value

    @property
    def family(self) -> str:
        """The one family allowed to author on this profile."""
        return self.spec.family

    @classmethod
    def for_family(cls, family: str) -> "Profile":
        """The one profile a family authors on, read from the contract."""
        try:
            return cls[_PROFILE["families"][family]["profile"]]
        except KeyError as error:
            known = sorted(k for k in _PROFILE["families"] if not k.startswith("_"))
            raise ValueError(f"unknown family {family!r}; known: {known}") from error


# The contract's two tables must agree with each other and with this enum.
for _name, _row in _PROFILE["families"].items():
    if _name.startswith("_"):
        continue
    assert _PROFILE["profiles"][_row["profile"]]["family"] == _name, _name
    assert Profile[_row["profile"]].family == _name, _name
assert {p.name for p in Profile} == set(_PROFILE["profiles"]), "enum drifted from contract"
del _name, _row
