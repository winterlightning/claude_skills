"""A broad Internet Explorer-style lowercase e outline.

Symbol plan: the open outer sweep curls around a lower bowl and right tab;
a smaller upper bowl closes onto its own horizontal bar. The directional
right opening is intentionally asymmetric. Lucide at-sign informed the open
outer sweep and nested rounded counter.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

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
        # One open lowercase e stroke with a broad upper counter; no double rim.
        self.add_line("crossbar", (4,24), (44,24))
        self.add_arc("upper-right", (44,24), (24,4), radius_x=20, sweep=False)
        self.add_arc("upper-left", (24,4), (4,24), radius_x=20, sweep=False)
        self.add_contour("upper-loop", "crossbar", "upper-right", "upper-left", closed=True)
        self.add_arc("lower-left", (4,24), (24,44), radius_x=20, sweep=False)
        self.add_arc("lower-right", (24,44), (40,36), radius_x=20, sweep=False)
        self.add_contour("lower-sweep", "lower-left", "lower-right")
        self.relate("connect", "lower-left", "crossbar")
        self.relate("connect", "lower-left", "upper-left")
