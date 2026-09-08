"""Glyphs whose short axis is stroke-defined.

No standard keyshape has a 4-unit axis and the smallest standard minor
dimension is 16, so a bar, a point, and the typographic marks built from them
cannot fill one without becoming a different symbol. Each uses ``Keyshape.FREE``
against an approved record in ``model/contracts/exceptions.v1.json``; the base
class refuses to construct one that has no approval.
"""

from __future__ import annotations

from ...keyshapes import Keyshape
from ._base import Sub32


class _FreeGlyph(Sub32):
    keyshape = Keyshape.FREE
    category = "primitives/mark"


class Minus(_FreeGlyph):
    icon_id = "minus"
    semantic_kind = "verb"
    category = "primitives/operator"
    aliases = ("remove", "subtract", "dash", "hyphen")
    keywords = ("remove", "collapse", "decrease", "math")

    def build(self) -> None:
        self.add_line("bar", (2, 16), (30, 16))


class Bar(_FreeGlyph):
    icon_id = "bar"
    semantic_kind = "modifier"
    aliases = ("pipe", "vertical-bar", "divider-vertical")
    keywords = ("separator", "column", "cursor", "rule")

    def build(self) -> None:
        self.add_line("bar", (16, 2), (16, 30))


class Dot(_FreeGlyph):
    icon_id = "dot"
    semantic_kind = "state"
    aliases = ("point", "period", "bullet")
    keywords = ("status", "unread", "marker", "current")

    def build(self) -> None:
        self.add_dot("point", (16, 16))


class Exclamation(_FreeGlyph):
    icon_id = "exclamation"
    semantic_kind = "state"
    aliases = ("alert", "warning", "bang")
    keywords = ("attention", "error", "important", "caution")

    def build(self) -> None:
        self.add_line("stem", (16, 2), (16, 20))
        self.add_dot("point", (16, 30))


class Ellipsis(_FreeGlyph):
    icon_id = "ellipsis"
    semantic_kind = "modifier"
    aliases = ("more", "dots-horizontal", "overflow")
    keywords = ("more", "menu", "options", "truncate")

    def build(self) -> None:
        self.add_dot("point-left", (4, 16))
        self.add_dot("point-middle", (16, 16))
        self.add_dot("point-right", (28, 16))


class DotsVertical(_FreeGlyph):
    icon_id = "dots-vertical"
    semantic_kind = "modifier"
    aliases = ("more-vertical", "kebab", "overflow-vertical")
    keywords = ("menu", "options", "more", "actions")

    def build(self) -> None:
        self.add_dot("point-top", (16, 4))
        self.add_dot("point-middle", (16, 16))
        self.add_dot("point-bottom", (16, 28))
