"""Chevrons.

Single chevrons fill the narrow HRECT_M / VRECT_M so the bare angle reads at
native size without crowding the canvas. Double chevrons need SQUARE: the two
angles sit 8 units apart on centerlines at their closest approach, comfortably
past the SUB32 minimum of 7.
"""

from __future__ import annotations

from ...keyshapes import Keyshape
from ._base import Sub32


class _Chevron(Sub32):
    semantic_kind = "modifier"
    category = "primitives/chevron"


class ChevronUp(_Chevron):
    icon_id = "chevron-up"
    keyshape = Keyshape.HRECT_M
    aliases = ("caret-up", "collapse")
    keywords = ("up", "less", "collapse", "expand-less")

    def build(self) -> None:
        self.add_polyline("angle", (2, 24), (16, 8), (30, 24))


class ChevronDown(_Chevron):
    icon_id = "chevron-down"
    keyshape = Keyshape.HRECT_M
    aliases = ("caret-down", "expand", "dropdown")
    keywords = ("down", "more", "expand", "select")

    def build(self) -> None:
        self.add_polyline("angle", (2, 8), (16, 24), (30, 8))


class ChevronLeft(_Chevron):
    icon_id = "chevron-left"
    keyshape = Keyshape.VRECT_M
    aliases = ("caret-left", "back")
    keywords = ("left", "previous", "back", "prior")

    def build(self) -> None:
        self.add_polyline("angle", (24, 2), (8, 16), (24, 30))


class ChevronRight(_Chevron):
    icon_id = "chevron-right"
    keyshape = Keyshape.VRECT_M
    aliases = ("caret-right", "forward", "disclosure")
    keywords = ("right", "next", "forward", "more")

    def build(self) -> None:
        self.add_polyline("angle", (8, 2), (24, 16), (8, 30))


class ChevronsUp(_Chevron):
    icon_id = "chevrons-up"
    keyshape = Keyshape.SQUARE
    aliases = ("double-chevron-up", "collapse-all")
    keywords = ("top", "first", "fast", "collapse")

    def build(self) -> None:
        self.add_polyline("angle-lead", (2, 13), (16, 2), (30, 13))
        self.add_polyline("angle-trail", (2, 30), (16, 19), (30, 30))


class ChevronsDown(_Chevron):
    icon_id = "chevrons-down"
    keyshape = Keyshape.SQUARE
    aliases = ("double-chevron-down", "expand-all")
    keywords = ("bottom", "last", "fast", "expand")

    def build(self) -> None:
        self.add_polyline("angle-lead", (2, 2), (16, 13), (30, 2))
        self.add_polyline("angle-trail", (2, 19), (16, 30), (30, 19))


class ChevronsLeft(_Chevron):
    icon_id = "chevrons-left"
    keyshape = Keyshape.SQUARE
    aliases = ("double-chevron-left", "rewind")
    keywords = ("first", "start", "rewind", "previous")

    def build(self) -> None:
        self.add_polyline("angle-lead", (13, 2), (2, 16), (13, 30))
        self.add_polyline("angle-trail", (30, 2), (19, 16), (30, 30))


class ChevronsRight(_Chevron):
    icon_id = "chevrons-right"
    keyshape = Keyshape.SQUARE
    aliases = ("double-chevron-right", "fast-forward")
    keywords = ("last", "end", "forward", "next")

    def build(self) -> None:
        self.add_polyline("angle-lead", (2, 2), (13, 16), (2, 30))
        self.add_polyline("angle-trail", (19, 2), (30, 16), (19, 30))
