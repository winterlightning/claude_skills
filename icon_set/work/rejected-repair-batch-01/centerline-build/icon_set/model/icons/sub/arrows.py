"""Directional arrows.

Each arrow is one shaft plus one head whose apex is the shaft's own endpoint,
so the two contours share a drawn point and read as a single connected
component. Cardinal arrows fill VRECT_L / HRECT_L; the double-headed pair fills
the narrower VRECT_M / HRECT_M; diagonals fill SQUARE corner to corner.
"""

from __future__ import annotations

from ...keyshapes import Keyshape
from ._base import Sub32

AUTHOR = 'astra-chatgpt'


class _Arrow(Sub32):
    semantic_kind = "verb"
    category = "primitives/arrow"


class ArrowUp(_Arrow):
    icon_id = "arrow-up"
    keyshape = Keyshape.VRECT_L
    aliases = ("north", "ascend")
    keywords = ("up", "increase", "upload", "sort")

    def build(self) -> None:
        self.add_line("shaft", (16, 2), (16, 30))
        self.add_polyline("head", (6, 12), (16, 2), (26, 12))
        self.relate("connect", "shaft", "head")
        self.add_anchor("tip", (16, 2))


class ArrowDown(_Arrow):
    icon_id = "arrow-down"
    keyshape = Keyshape.VRECT_L
    aliases = ("south", "descend")
    keywords = ("down", "decrease", "download", "sort")

    def build(self) -> None:
        self.add_line("shaft", (16, 2), (16, 30))
        self.add_polyline("head", (6, 20), (16, 30), (26, 20))
        self.relate("connect", "shaft", "head")
        self.add_anchor("tip", (16, 30))


class ArrowLeft(_Arrow):
    icon_id = "arrow-left"
    keyshape = Keyshape.HRECT_L
    aliases = ("west", "back")
    keywords = ("left", "previous", "return", "undo")

    def build(self) -> None:
        self.add_line("shaft", (2, 16), (30, 16))
        self.add_polyline("head", (14, 6), (2, 16), (14, 26))
        self.relate("connect", "shaft", "head")
        self.add_anchor("tip", (2, 16))


class ArrowRight(_Arrow):
    icon_id = "arrow-right"
    keyshape = Keyshape.HRECT_L
    aliases = ("east", "forward", "next")
    keywords = ("right", "next", "continue", "submit")

    def build(self) -> None:
        self.add_line("shaft", (2, 16), (30, 16))
        self.add_polyline("head", (18, 6), (30, 16), (18, 26))
        self.relate("connect", "shaft", "head")
        self.add_anchor("tip", (30, 16))


class ArrowUpRight(_Arrow):
    icon_id = "arrow-up-right"
    keyshape = Keyshape.SQUARE
    aliases = ("north-east", "external-link")
    keywords = ("diagonal", "open", "outbound", "expand")

    def build(self) -> None:
        self.add_line("shaft", (2, 30), (30, 2))
        self.add_polyline("head", (16, 2), (30, 2), (30, 16))
        self.relate("connect", "shaft", "head")
        self.add_anchor("tip", (30, 2))


class ArrowUpLeft(_Arrow):
    icon_id = "arrow-up-left"
    keyshape = Keyshape.SQUARE
    aliases = ("north-west",)
    keywords = ("diagonal", "back", "inbound")

    def build(self) -> None:
        self.add_line("shaft", (30, 30), (2, 2))
        self.add_polyline("head", (2, 16), (2, 2), (16, 2))
        self.relate("connect", "shaft", "head")
        self.add_anchor("tip", (2, 2))


class ArrowDownRight(_Arrow):
    icon_id = "arrow-down-right"
    keyshape = Keyshape.SQUARE
    aliases = ("south-east",)
    keywords = ("diagonal", "descend", "expand")

    def build(self) -> None:
        self.add_line("shaft", (2, 2), (30, 30))
        self.add_polyline("head", (30, 16), (30, 30), (16, 30))
        self.relate("connect", "shaft", "head")
        self.add_anchor("tip", (30, 30))


class ArrowDownLeft(_Arrow):
    icon_id = "arrow-down-left"
    keyshape = Keyshape.SQUARE
    aliases = ("south-west",)
    keywords = ("diagonal", "collapse", "inbound")

    def build(self) -> None:
        self.add_line("shaft", (30, 2), (2, 30))
        self.add_polyline("head", (16, 30), (2, 30), (2, 16))
        self.relate("connect", "shaft", "head")
        self.add_anchor("tip", (2, 30))


class ArrowsVertical(_Arrow):
    icon_id = "arrows-vertical"
    keyshape = Keyshape.VRECT_M
    aliases = ("arrow-up-down", "sort-vertical", "resize-vertical")
    keywords = ("swap", "sort", "height", "both")

    def build(self) -> None:
        self.add_line("shaft", (16, 2), (16, 30))
        self.add_polyline("head-top", (8, 10), (16, 2), (24, 10))
        self.add_polyline("head-bottom", (8, 22), (16, 30), (24, 22))
        self.relate("connect", "shaft", "head-top")
        self.relate("connect", "shaft", "head-bottom")


class ArrowsHorizontal(_Arrow):
    icon_id = "arrows-horizontal"
    keyshape = Keyshape.HRECT_M
    aliases = ("arrow-left-right", "resize-horizontal")
    keywords = ("swap", "width", "transfer", "both")

    def build(self) -> None:
        self.add_line("shaft", (2, 16), (30, 16))
        self.add_polyline("head-left", (10, 8), (2, 16), (10, 24))
        self.add_polyline("head-right", (22, 8), (30, 16), (22, 24))
        self.relate("connect", "shaft", "head-left")
        self.relate("connect", "shaft", "head-right")
