"""Smart Fitness Wristband.

Symbol plan: Open fitness cuff with four 2x2 indicator dots. One continuous C-shaped band with rounded end transitions and a broad face. Shared dot pitch 8. No useful exact Lucide match; omit top/bottom panel seams.
Keyshape SQUARE; exact visible bounds (4, 4, 44, 44).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'd3a6f1cd-25ad-407a-a630-dee7b1c015ab'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__open-fitness-wristband-with-four-indicator-dots/20260927T133654Z-thuan-mac-1/reference/wearable smart watch app_d3a6f1cd-25ad-407a-a630-dee7b1c015ab.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'open-fitness-wristband-with-four-indicator-dots'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    categories = ('primitives', 'devices')
    aliases = ()
    keywords = ('smart', 'fitness', 'wristband')

    def build(self):
        self.add_arc('outer-top',(6,24),(24,6),radius_x=18)
        self.add_arc('outer-tr',(24,6),(42,16),radius_x=18,radius_y=10)
        self.add_line('end-tr',(42,16),(40,16))
        
        self.add_arc('inner',(40,16),(40,32),radius_x=6,radius_y=8,sweep=False)
        self.add_line('end-br',(40,32),(42,32))
        self.add_arc('outer-br',(42,32),(24,42),radius_x=18,radius_y=10)
        self.add_arc('outer-bottom',(24,42),(6,24),radius_x=18)
        self.add_contour('band','outer-top','outer-tr','end-tr','inner','end-br','outer-br','outer-bottom',closed=True)
        # Short seam strokes show the overlap of the open cuff ends.
        self.add_bezier('upper-fold',(24,6),((29,8),(31,11),(32,14)))
        self.add_bezier('lower-fold',(32,34),((31,37),(29,40),(24,42)))
        self.relate('connect','upper-fold','band')
        self.relate('connect','lower-fold','band')
        for i,x in enumerate((16,24)):
            for j,y in enumerate((20,28)):self.add_dot(f'indicator-{i}-{j}',(x,y))
