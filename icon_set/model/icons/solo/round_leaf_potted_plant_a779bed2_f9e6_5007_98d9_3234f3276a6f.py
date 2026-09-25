"""Three broad rounded leaves above a bowl pot. Lucide sprout informs the paired leaf contours; central leaf is partially hidden as in the source."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a779bed2-f9e6-5007-98d9-3234f3276a6f'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/indoor plant_a779bed2-f9e6-5007-98d9-3234f3276a6f.svg'
AUTHOR = 'gpt-6'


class RoundLeafPottedPlant(Solo48):
    icon_id = 'round-leaf-potted-plant'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "decoration"
    aliases = ()
    keywords = ('plant', 'decoration', 'foliage', 'indoor')

    def build(self) -> None:
        # VRECT_XL extremes (6,6)-(42,42).
        self.add_bezier('central-left', (17, 10), *(((18.40229829, 7.16125546), (21.17149985, 6), (24, 6)),))
        self.add_bezier('central-right', (24, 6), *(((26.82850015, 6), (29.59770171, 7.16125546), (31, 10)),))
        self.add_contour("central-leaf", "central-left", "central-right")
        self.add_arc("left-upper", (6,10), (17,10), radius_x=12, radius_y=5)
        self.add_arc("left-inner", (17,10), (24,24), radius_x=7, radius_y=14)
        self.add_bezier('left-lower', (24, 24), *(((13.89903423, 23.55169861), (6, 18.51787363), (6, 10)),))
        self.add_contour("left-leaf", "left-upper", "left-inner", "left-lower", closed=True)
        self.add_bezier('right-lower', (42, 10), *(((42, 18.51787363), (34.10096577, 23.55169861), (24, 24)),))
        self.add_arc("right-inner", (24,24), (31,10), radius_x=7, radius_y=14)
        self.add_arc("right-upper", (31,10), (42,10), radius_x=12, radius_y=5)
        self.add_contour("right-leaf", "right-lower", "right-inner", "right-upper", closed=True)
        self.relate("connect", "central-leaf", "left-leaf")
        self.relate("connect", "central-leaf", "right-leaf")
        self.relate("connect", "left-leaf", "right-leaf")
        self.add_line("stem", (24,24), (24,33))
        self.relate("connect", "stem", "left-leaf")
        self.relate("connect", "stem", "right-leaf")
        self.add_polyline("mouth", (11,33), (24,33), (37,33))
        self.add_bezier('bowl-right', (37, 33), *(((35.19875485, 38.59330912), (29.86937563, 42), (24, 42)),))
        self.add_bezier('bowl-left', (24, 42), *(((18.13062437, 42), (12.80124515, 38.59330912), (11, 33)),))
        self.add_contour("bowl", "bowl-right", "bowl-left")
        self.relate("connect", "mouth", "bowl")
        self.relate("connect", "stem", "mouth")
