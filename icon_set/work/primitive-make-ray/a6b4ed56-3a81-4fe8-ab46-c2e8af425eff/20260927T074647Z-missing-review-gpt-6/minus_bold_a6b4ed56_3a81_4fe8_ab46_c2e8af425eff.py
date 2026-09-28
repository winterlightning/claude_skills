"""Revision of minus-bold. The rejected square lost the original horizontal capsule. Narrowed and rounded the silhouette to read as a bold minus.
Symbol plan: redraw the original subject with one coherent SOLO48 construction.
"""
"""Minus bold (state), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a6b4ed56-3a81-4fe8-ab46-c2e8af425eff'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__minus-bold/20260927T074149Z-thuan-mac-1/reference/minus bold_a6b4ed56-3a81-4fe8-ab46-c2e8af425eff.svg'
AUTHOR = "gpt-6"

class MinusBold(Solo48):
    icon_id = 'minus-bold'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('minus', 'bold', 'state')

    def build(self):
        p = [(18,10),(30,10),(44,24),(30,38),(18,38),(4,24),(18,10)]
        self.add_line('top',p[0],p[1])
        self.add_arc('right-top',p[1],p[2],radius_x=14)
        self.add_arc('right-bottom',p[2],p[3],radius_x=14)
        self.add_line('bottom',p[3],p[4])
        self.add_arc('left-bottom',p[4],p[5],radius_x=14)
        self.add_arc('left-top',p[5],p[6],radius_x=14)
        self.add_contour('minus','top','right-top','right-bottom','bottom','left-bottom','left-top',closed=True)
