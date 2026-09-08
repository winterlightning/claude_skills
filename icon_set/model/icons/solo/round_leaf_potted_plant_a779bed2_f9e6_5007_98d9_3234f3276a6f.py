"""Three broad rounded leaves above a bowl pot. Lucide sprout informs the paired leaf contours; central leaf is partially hidden as in the source."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a779bed2-f9e6-5007-98d9-3234f3276a6f'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/indoor plant_a779bed2-f9e6-5007-98d9-3234f3276a6f.svg'
AUTHOR = 'gpt-6'


class RoundLeafPottedPlant(Solo48):
    icon_id = 'round-leaf-potted-plant'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/plants"
    aliases = ()
    keywords = ('plant', 'decoration', 'foliage', 'indoor')

    def build(self) -> None:
        # VRECT_XL extremes (5,2)-(43,46).
        self.add_arc("central-left", (17,10), (24,2), radius_x=7, radius_y=8)
        self.add_arc("central-right", (24,2), (31,10), radius_x=7, radius_y=8)
        self.add_contour("central-leaf", "central-left", "central-right")
        self.add_arc("left-upper", (5,10), (17,10), radius_x=12, radius_y=5)
        self.add_arc("left-inner", (17,10), (24,26), radius_x=7, radius_y=16)
        self.add_arc("left-lower", (24,26), (5,10), radius_x=19, radius_y=16)
        self.add_contour("left-leaf", "left-upper", "left-inner", "left-lower", closed=True)
        self.add_arc("right-lower", (43,10), (24,26), radius_x=19, radius_y=16)
        self.add_arc("right-inner", (24,26), (31,10), radius_x=7, radius_y=16)
        self.add_arc("right-upper", (31,10), (43,10), radius_x=12, radius_y=5)
        self.add_contour("right-leaf", "right-lower", "right-inner", "right-upper", closed=True)
        self.relate("connect", "central-leaf", "left-leaf")
        self.relate("connect", "central-leaf", "right-leaf")
        self.relate("connect", "left-leaf", "right-leaf")
        self.add_line("stem", (24,26), (24,33))
        self.relate("connect", "stem", "left-leaf")
        self.relate("connect", "stem", "right-leaf")
        self.add_polyline("mouth", (11,33), (24,33), (37,33))
        self.add_arc("bowl-right", (37,33), (24,46), radius_x=13)
        self.add_arc("bowl-left", (24,46), (11,33), radius_x=13)
        self.add_contour("bowl", "bowl-right", "bowl-left")
        self.relate("connect", "mouth", "bowl")
        self.relate("connect", "stem", "mouth")
