"""Operator symbols.

SQUARE gives the crossing operators their 28x28 envelope; the divide bar needs
the taller HRECT_L so its points clear the bar by more than the SUB32 minimum.
Every intentional crossing is declared with a scoped ``connect`` relationship.
"""

from __future__ import annotations

from ...keyshapes import Keyshape
from ._base import Sub32


class Plus(Sub32):
    icon_id = "plus"
    keyshape = Keyshape.SQUARE
    semantic_kind = "verb"
    category = "primitives/operator"
    aliases = ("add", "new")
    keywords = ("add", "create", "increase", "math")

    def build(self) -> None:
        self.add_line("bar-horizontal", (2, 16), (30, 16))
        self.add_line("bar-vertical", (16, 2), (16, 30))
        self.relate("connect", "bar-horizontal", "bar-vertical")


class Close(Sub32):
    icon_id = "close"
    keyshape = Keyshape.SQUARE
    semantic_kind = "verb"
    category = "primitives/operator"
    aliases = ("x", "cross", "multiply", "remove")
    keywords = ("cancel", "delete", "dismiss", "times")

    def build(self) -> None:
        self.add_line("stroke-down", (2, 2), (30, 30))
        self.add_line("stroke-up", (30, 2), (2, 30))
        self.relate("connect", "stroke-down", "stroke-up")


class Asterisk(Sub32):
    icon_id = "asterisk"
    keyshape = Keyshape.SQUARE
    semantic_kind = "modifier"
    category = "primitives/operator"
    aliases = ("star-note", "footnote", "required")
    keywords = ("footnote", "required", "wildcard")

    def build(self) -> None:
        self.add_line("bar-horizontal", (2, 16), (30, 16))
        self.add_line("bar-vertical", (16, 2), (16, 30))
        self.add_line("stroke-down", (2, 2), (30, 30))
        self.add_line("stroke-up", (30, 2), (2, 30))
        for other in ("bar-vertical", "stroke-down", "stroke-up"):
            self.relate("connect", "bar-horizontal", other)
        self.relate("connect", "bar-vertical", "stroke-down")
        self.relate("connect", "bar-vertical", "stroke-up")
        self.relate("connect", "stroke-down", "stroke-up")


class Equals(Sub32):
    icon_id = "equals"
    keyshape = Keyshape.HRECT_S
    semantic_kind = "state"
    category = "primitives/operator"
    aliases = ("equal", "same")
    keywords = ("math", "identical", "balance")

    def build(self) -> None:
        self.add_line("bar-top", (2, 10), (30, 10))
        self.add_line("bar-bottom", (2, 22), (30, 22))


class Divide(Sub32):
    icon_id = "divide"
    keyshape = Keyshape.HRECT_L
    semantic_kind = "verb"
    category = "primitives/operator"
    aliases = ("obelus",)
    keywords = ("math", "split", "ratio")

    def build(self) -> None:
        self.add_line("bar", (2, 16), (30, 16))
        self.add_dot("point-top", (16, 6))
        self.add_dot("point-bottom", (16, 26))


class Hash(Sub32):
    icon_id = "hash"
    keyshape = Keyshape.SQUARE
    semantic_kind = "modifier"
    category = "primitives/operator"
    aliases = ("grid", "pound", "number")
    keywords = ("tag", "channel", "table", "lattice")

    def build(self) -> None:
        self.add_line("rail-left", (11, 2), (11, 30))
        self.add_line("rail-right", (21, 2), (21, 30))
        self.add_line("rung-top", (2, 11), (30, 11))
        self.add_line("rung-bottom", (2, 21), (30, 21))
        for rail in ("rail-left", "rail-right"):
            for rung in ("rung-top", "rung-bottom"):
                self.relate("connect", rail, rung)


class Check(Sub32):
    icon_id = "check"
    keyshape = Keyshape.HRECT_L
    semantic_kind = "state"
    category = "primitives/mark"
    aliases = ("tick", "done", "confirm")
    keywords = ("accept", "success", "complete", "ok")

    def build(self) -> None:
        self.add_polyline("mark", (2, 17), (11, 26), (30, 6))


class Menu(Sub32):
    icon_id = "menu"
    keyshape = Keyshape.HRECT_L
    semantic_kind = "modifier"
    category = "primitives/mark"
    aliases = ("hamburger", "bars", "list")
    keywords = ("navigation", "lines", "rows")

    def build(self) -> None:
        self.add_line("bar-top", (2, 6), (30, 6))
        self.add_line("bar-middle", (2, 16), (30, 16))
        self.add_line("bar-bottom", (2, 26), (30, 26))


class Tilde(Sub32):
    icon_id = "tilde"
    keyshape = Keyshape.HRECT_M
    semantic_kind = "modifier"
    category = "primitives/operator"
    aliases = ("wave", "approximately", "squiggle")
    keywords = ("approximate", "sine", "flow")

    def build(self) -> None:
        # Half-ellipses, not semicircles: rx 7 spans the width in two crests
        # while ry 8 lifts each crest exactly onto the HRECT_M edge.
        self.add_arc("crest", (2, 16), (16, 16), radius_x=7, radius_y=8, sweep=True)
        self.add_arc("trough", (16, 16), (30, 16), radius_x=7, radius_y=8, sweep=False)
        self.add_contour("wave", "crest", "trough")
