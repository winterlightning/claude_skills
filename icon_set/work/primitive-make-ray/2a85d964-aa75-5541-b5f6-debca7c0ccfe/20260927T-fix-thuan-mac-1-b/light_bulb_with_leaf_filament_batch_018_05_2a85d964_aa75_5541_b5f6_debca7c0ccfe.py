"""Eco light bulb with a leaf in place of the filament.

Symbol plan: bulb head = r14 arc about (24,18) from (10,18) over the top to
(38,18); the glass tapers into the neck with mirrored cubics leaving the
equator vertically and landing on the band (16,34)/(32,34). Base cap = the
band plus sides to y=40 and r4 rounded bottom corners (floor y=44). Leaf =
lens of two r6 arcs from (20,22) to the tip (28,14), tilted 45 degrees like
the reference, with a short stem below its base; every leaf point stays 8
from the glass.
Revision: the rejected drawing's leaf was a diamond with a square opening
and the glass met the neck at hard corners; the reference has a pointed
lens-shaped leaf and a smoothly tapering bulb.
Reduced: the stem stops above the base (a longer stem would run under 8 from
the tapering glass).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "2a85d964-aa75-5541-b5f6-debca7c0ccfe"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__light-bulb-with-leaf-filament-batch-018-05/20260927T153253Z-thuan-mac-1/reference/light bulb eco_2a85d964-aa75-5541-b5f6-debca7c0ccfe.svg"
AUTHOR = "claude-opus-5-5"


class LightBulbWithLeafFilament(Solo48):
    icon_id = "light-bulb-with-leaf-filament-batch-018-05"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "ecology"
    categories = ("primitives", "ecology")
    aliases = ("light bulb eco", "green energy")
    keywords = ("light bulb", "eco", "leaf", "green", "energy", "idea", "sustainable")

    def build(self) -> None:
        self.add_arc("glass-top", (10, 18), (38, 18), radius_x=14, sweep=True)
        self.add_bezier("glass-right", (38, 18), ((38, 25), (32, 28), (32, 34)))
        self.add_line("cap-right", (32, 34), (32, 40))
        self.add_arc("cap-corner-right", (32, 40), (28, 44), radius_x=4, sweep=True)
        self.add_line("cap-floor", (28, 44), (20, 44))
        self.add_arc("cap-corner-left", (20, 44), (16, 40), radius_x=4, sweep=True)
        self.add_line("cap-left", (16, 40), (16, 34))
        self.add_bezier("glass-left", (16, 34), ((16, 28), (10, 25), (10, 18)))
        self.add_contour("bulb", "glass-top", "glass-right", "cap-right", "cap-corner-right",
                         "cap-floor", "cap-corner-left", "cap-left", "glass-left", closed=True)
        self.add_line("band", (16, 34), (32, 34))
        self.relate("connect", "bulb", "band")

        self.add_arc("leaf-upper", (20, 22), (28, 14), radius_x=6, sweep=True)
        self.add_arc("leaf-lower", (28, 14), (20, 22), radius_x=6, sweep=True)
        self.add_contour("leaf", "leaf-upper", "leaf-lower", closed=True)
        self.add_line("stem", (20, 22), (22, 26))
        self.relate("connect", "leaf", "stem")
