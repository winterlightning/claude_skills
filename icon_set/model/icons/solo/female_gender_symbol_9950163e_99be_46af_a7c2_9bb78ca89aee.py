"""The female gender symbol (Venus): a circle on a stem with a crossbar.

Symbol plan: mirrored about x=24. The ring is an r14 circle of four quarter arcs centred
(24,18); the stem drops from its lowest point to the bottom edge, and the crossbar
crosses the stem 9 below the ring (y=41), as low on the stem as the reference's.
Lucide construction: 'venus' - circle, stem and crossbar.
Keyshape VRECT_M: centerline x 10..38 (ring sides), y 4..44 (ring top, stem foot).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "9950163e-99be-46af-a7c2-9bb78ca89aee"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__female-gender-symbol-solo-source-9950163e/20260926T035939Z-thuan-mac/reference/gender female_9950163e-99be-46af-a7c2-9bb78ca89aee.svg"
AUTHOR = "claude-opus-5-5"


class FemaleGenderSymbolSoloSource9950163e(Solo48):
    icon_id = "female-gender-symbol-solo-source-9950163e-solo"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/gender"
    aliases = ("gender-female", "venus", "female-symbol")
    keywords = ("female", "woman", "gender", "venus", "sex", "girl", "feminine", "symbol")

    def build(self) -> None:
        n, e, s, w = (24, 4), (38, 18), (24, 32), (10, 18)
        self.add_arc("ring-ne", n, e, radius_x=14, sweep=True)
        self.add_arc("ring-se", e, s, radius_x=14, sweep=True)
        self.add_arc("ring-sw", s, w, radius_x=14, sweep=True)
        self.add_arc("ring-nw", w, n, radius_x=14, sweep=True)
        self.add_contour("ring", "ring-ne", "ring-se", "ring-sw", "ring-nw", closed=True)
        self.add_line("stem", s, (24, 44))
        self.add_line("crossbar", (18, 41), (30, 41))
        self.relate("connect", "ring", "stem")
        self.relate("connect", "stem", "crossbar")
