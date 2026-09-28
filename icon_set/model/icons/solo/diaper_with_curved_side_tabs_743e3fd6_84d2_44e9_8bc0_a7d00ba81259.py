"""A diaper has a broad waistband, inward curved tabs and shaped leg seams. HRECT_L 4..44 x 8..40 preserves broad silhouette. Source supplies tabs and leg openings; no useful Lucide diaper match. Outer contour owns split side and seam nodes; left geometry mirrors around x24. Omit tiny material contours."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '743e3fd6-84d2-44e9-8bc0-a7d00ba81259'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_15/diaper_743e3fd6-84d2-44e9-8bc0-a7d00ba81259.svg'
AUTHOR = 'gpt-6-astra'
class Drawing(Solo48):
    icon_id = 'diaper-with-curved-side-tabs'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ['Diaper with Curved Side Tabs']
    keywords = ['diaper', 'baby', 'waistband', 'tabs', 'infant', 'clothing', 'care']
    def build(self):
        self.add_line('waist',(4,8),(44,8))
        for side in (-1,1):
            x=lambda v:24+side*v
            p=str(side)
            self.add_line(p+'side-top',(x(20),8),(x(20),16))
            self.add_line(p+'side-mid',(x(20),16),(x(20),24))
            self.add_bezier(p+'lower',(x(20),24),((x(20),32),(x(12),40),(x(4),40)))
            self.add_line(p+'tab-top',(x(20),16),(x(12),16))
            self.add_arc(p+'tab-round',(x(12),16),(x(12),24),radius_x=4,sweep=side<0)
            self.add_line(p+'tab-bottom',(x(12),24),(x(20),24))
            self.add_contour(p+'tab',p+'tab-top',p+'tab-round',p+'tab-bottom')
            self.add_bezier(p+'leg',(x(20),24),((x(9),24),(x(4),29),(x(4),40)))
            self.relate('connect','waist',p+'side-top')
            self.relate('connect',p+'side-top',p+'side-mid',p+'tab')
            self.relate('connect',p+'side-mid',p+'lower',p+'tab',p+'leg')
            self.relate('connect',p+'lower',p+'leg')
        self.add_line('crotch',(20,40),(28,40))
        for side in (-1,1):
            self.relate('connect','crotch',str(side)+'lower',str(side)+'leg')
