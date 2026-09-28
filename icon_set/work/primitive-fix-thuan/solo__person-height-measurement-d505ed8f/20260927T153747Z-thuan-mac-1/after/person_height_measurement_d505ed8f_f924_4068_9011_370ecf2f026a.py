"""Person Height Measurement.
Plan: (8,4)-(40,44). Tall measuring rule with four ticks beside circular-headed standing figure. Rule reduced to one edge; head bottom16 to torso24 gives exact8 centerline gap.
References: supplied original source; human_ref/full_body_ref.png; Lucide ruler and person-standing: ticks and minimal figure.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd505ed8f-f924-4068-9011-370ecf2f026a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-height-measurement-d505ed8f/20260927T153747Z-thuan-mac-1/reference/virtual measuring_d505ed8f-f924-4068-9011-370ecf2f026a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-height-measurement-d505ed8f'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('person-height-measurement',)
    keywords = ('person', 'height', 'measurement')

    def build(self):
        # Full length measuring rule and a broad shouldered human silhouette.
        self.add_line('ruler', (8, 4), (8, 44))
        for index, y in enumerate((10, 20, 30, 40)):
            self.add_line(f'tick-{index}', (8, y), (14, y))
            self.relate('connect', 'ruler', f'tick-{index}')
        self.add_arc('head-upper', (28, 10), (40, 10), radius_x=6)
        self.add_arc('head-lower', (40, 10), (28, 10), radius_x=6)
        self.add_contour('head', 'head-upper', 'head-lower', closed=True)
        self.add_polyline('body', (30, 24), (38, 24), (40, 30), (40, 36), (38, 36), (38, 44), (30, 44), (30, 36), (28, 36), (28, 30), closed=True)
