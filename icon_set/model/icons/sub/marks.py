"""Slashes and paired bars.

A single diagonal fills VRECT_XL exactly: its round caps extend the 28x32
centerline box by 2 on every side. The paired bars fill the narrow VRECT_S,
where 12 units of centerline spacing clear the SUB32 minimum of 7.
"""

from __future__ import annotations

from ...keyshapes import Keyshape
from ._base import Sub32

AUTHOR = 'astra-chatgpt'


class Slash(Sub32):
    icon_id = "slash"
    keyshape = Keyshape.VRECT_XL
    semantic_kind = "modifier"
    category = "primitives/mark"
    aliases = ("divider", "forward-slash", "prohibited-bar")
    keywords = ("separator", "or", "disabled", "path")

    def build(self) -> None:
        self.add_line("stroke", (28, 2), (4, 30))


class Backslash(Sub32):
    icon_id = "backslash"
    keyshape = Keyshape.VRECT_XL
    semantic_kind = "modifier"
    category = "primitives/mark"
    aliases = ("back-slash",)
    keywords = ("separator", "escape", "path")

    def build(self) -> None:
        self.add_line("stroke", (4, 2), (28, 30))


class Pause(Sub32):
    icon_id = "pause"
    keyshape = Keyshape.VRECT_S
    semantic_kind = "verb"
    category = "primitives/control"
    aliases = ("hold", "parallel-bars")
    keywords = ("pause", "suspend", "wait", "media")

    def build(self) -> None:
        self.add_line("bar-left", (10, 2), (10, 30))
        self.add_line("bar-right", (22, 2), (22, 30))


class SkipForward(Sub32):
    icon_id = "skip-forward"
    keyshape = Keyshape.SQUARE
    semantic_kind = "verb"
    category = "primitives/control"
    aliases = ("next-track", "fast-forward-end")
    keywords = ("next", "end", "skip", "media")

    def build(self) -> None:
        # The apex stops at x 19 so it clears the rail by 11 centerline units,
        # well past the SUB32 minimum rather than sitting on it.
        self.add_polyline("wedge", (2, 2), (19, 16), (2, 30), closed=True)
        self.add_line("rail", (30, 2), (30, 30))


class SkipBack(Sub32):
    icon_id = "skip-back"
    keyshape = Keyshape.SQUARE
    semantic_kind = "verb"
    category = "primitives/control"
    aliases = ("previous-track", "rewind-start")
    keywords = ("previous", "start", "skip", "media")

    def build(self) -> None:
        self.add_polyline("wedge", (30, 2), (13, 16), (30, 30), closed=True)
        self.add_line("rail", (2, 2), (2, 30))
