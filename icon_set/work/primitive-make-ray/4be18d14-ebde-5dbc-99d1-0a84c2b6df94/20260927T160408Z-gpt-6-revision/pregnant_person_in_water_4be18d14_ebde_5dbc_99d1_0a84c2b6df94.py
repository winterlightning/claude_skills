"""Pregnant Person in Water.
Plan: (6,6)-(42,42). Left-facing pregnant profile immersed in a broad water wave. Head bottom14 to shoulder22 gives exact8 gap; second wave and inner arm omitted to preserve belly silhouette.
References: supplied original source; human_ref/user.svg: circular head and curved body; source left-facing belly and water.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4be18d14-ebde-5dbc-99d1-0a84c2b6df94'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__pregnant-person-in-water-4be18d14/20260927T153747Z-thuan-mac-1/reference/prenatal massage wave_4be18d14-ebde-5dbc-99d1-0a84c2b6df94.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'pregnant-person-in-water-4be18d14'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('pregnant-person-in-water',)
    keywords = ('pregnant', 'person', 'in', 'water')

    def build(self):
        # A left-facing pregnant profile rises from the waves with rounded shoulders.
        self.add_arc('head-top', (24, 10), (32, 10), radius_x=4)
        self.add_arc('head-bottom', (32, 10), (24, 10), radius_x=4)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_bezier('belly', (12, 40), ((8, 35), (12, 30), (20, 29)), ((25, 27), (24, 25), (24, 24)))
        self.add_arc('shoulders', (24, 24), (34, 24), radius_x=5, radius_y=2, sweep=True)
        self.add_bezier('back', (34, 24), ((36, 27), (36, 32), (36, 40)))
        self.relate('connect', 'belly', 'shoulders')
        self.relate('connect', 'shoulders', 'back')
        self.add_polyline('water', (6, 42), (12, 40), (18, 42), (24, 40), (30, 42), (36, 40), (42, 42))
        self.relate('connect', 'belly', 'water')
        self.relate('connect', 'back', 'water')
