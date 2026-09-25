"""microsoft internet explorer logo: standalone repair of supplied reference.

Plan: Round lowercase e silhouette. Keyshape CIRCLE.
Reduction: Converted double outlined e to single-stroke e with a large upper counter. Brand-specific outline is simplified.
Construction references: local Lucide originals and atomic-debug: none.

All geometry is authored for SOLO48; earlier runs remain unchanged.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "ff53feac-62ae-4745-9bd7-4e08ad72f21a"
SOURCE_PATH = "pictographic-primitives/_uncategorized_27/microsoft internet explorer logo_ff53feac-62ae-4745-9bd7-4e08ad72f21a.svg"
AUTHOR = "gpt-6"


class InternetExplorerE(Solo48):
    icon_id = 'internet-explorer-e'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
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
