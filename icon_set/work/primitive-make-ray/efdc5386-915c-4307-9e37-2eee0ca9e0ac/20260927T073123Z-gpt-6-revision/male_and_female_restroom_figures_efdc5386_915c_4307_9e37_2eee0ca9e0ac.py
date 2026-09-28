'Two front-facing figures stand side by side with circular heads. The left wears a straight-sided outfit with a short chest mark, while the right wears a flared dress with a V neckline.\n\nConstruction: Two front-facing restroom figures distinguished by straight and skirt-shaped bodies. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'efdc5386-915c-4307-9e37-2eee0ca9e0ac'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__male-and-female-restroom-figures/20260927T072903Z-thuan-mac-1/reference/toilet sign 1_efdc5386-915c-4307-9e37-2eee0ca9e0ac.svg'
AUTHOR = "gpt-6"

class MaleAndFemaleRestroomFigures(Solo48):
    icon_id = 'male-and-female-restroom-figures'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('restroom', 'toilet', 'male', 'female', 'people', 'wayfinding')

    def build(self):
        # Two separated, full-height restroom figures.
        for side,cx in [('man',12),('woman',36)]:
            self.add_arc(side+'-head-a',(cx-4,10),(cx+4,10),radius_x=4)
            self.add_arc(side+'-head-b',(cx+4,10),(cx-4,10),radius_x=4)
            self.add_contour(side+'-head',side+'-head-a',side+'-head-b',closed=True)
        self.add_polyline('man-outline',(8,22),(16,22),(18,25),(18,32),(16,32),(16,42))
        self.add_polyline('man-left',(8,22),(6,25),(6,32),(8,32),(8,42))
        self.add_line('man-bridge',(8,32),(16,32))
        self.relate('connect','man-outline','man-bridge')
        self.relate('connect','man-left','man-bridge')
        self.add_polyline('dress',(34,22),(30,34),(42,34),(38,22))
        self.add_line('woman-left-leg',(32,34),(32,42))
        self.add_line('woman-right-leg',(40,34),(40,42))
        self.relate('connect','dress','woman-left-leg')
        self.relate('connect','dress','woman-right-leg')
