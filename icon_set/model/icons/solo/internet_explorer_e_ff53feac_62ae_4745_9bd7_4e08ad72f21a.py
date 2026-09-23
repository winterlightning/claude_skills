"""A broad Internet Explorer-style lowercase e outline.

Symbol plan: the open outer sweep curls around a lower bowl and right tab;
a smaller upper bowl closes onto its own horizontal bar. The directional
right opening is intentionally asymmetric. Lucide at-sign informed the open
outer sweep and nested rounded counter.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "ff53feac-62ae-4745-9bd7-4e08ad72f21a"
SOURCE_PATH = "pictographic-primitives/_uncategorized_27/microsoft internet explorer logo_ff53feac-62ae-4745-9bd7-4e08ad72f21a.svg"
AUTHOR = "gpt-6"


class InternetExplorerE(Solo48):
    icon_id = "internet-explorer-e"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/logos"
    aliases = ("internet explorer logo", "lowercase e outline")
    keywords = ("browser", "internet", "letter", "e")

    def build(self) -> None:
        self.add_arc("outer-upper-left", (8, 12), (24, 4), radius_x=20, sweep=True)
        self.add_arc("outer-upper-right", (24, 4), (44, 24), radius_x=20, sweep=True)
        self.add_line("outer-right-tab", (44, 24), (42, 28))
        self.add_line("middle-bar", (42, 28), (14, 28))
        self.add_arc("lower-bowl-left", (14, 28), (24, 36), radius_x=10, radius_y=8, sweep=False)
        self.add_arc("lower-bowl-right", (24, 36), (40, 32), radius_x=16, radius_y=4, sweep=False)
        self.add_line("lower-right-tab", (40, 32), (40, 36))
        self.add_arc("outer-bottom-right", (40, 36), (24, 44), radius_x=20, sweep=True)
        self.add_arc("outer-bottom-left", (24, 44), (4, 24), radius_x=20, sweep=True)
        self.add_contour("e-main", "outer-upper-left", "outer-upper-right", "outer-right-tab", "middle-bar", "lower-bowl-left", "lower-bowl-right", "lower-right-tab", "outer-bottom-right", "outer-bottom-left")
        self.add_arc("inner-bowl-left", (15, 19), (24, 13), radius_x=9, radius_y=6, sweep=True)
        self.add_arc("inner-bowl-right", (24, 13), (32, 19), radius_x=8, radius_y=6, sweep=True)
        self.add_line("inner-bar", (32, 19), (15, 19))
        self.add_contour("e-upper-counter", "inner-bowl-left", "inner-bowl-right", "inner-bar", closed=True)
