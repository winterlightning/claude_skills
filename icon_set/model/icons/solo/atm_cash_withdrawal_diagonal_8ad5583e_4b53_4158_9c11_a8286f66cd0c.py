"""ATM Cash Withdrawal. Reference retains the complete subject following saved user classification.
Plan: SQUARE envelope; shared page/currency dimensions and true beam attachment nodes.
Lucide files informs page contour continuity; dollar-sign informs paired currency bowls.
Source supplies count, relative placement and intentional asymmetry. Decorative thickness omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8ad5583e-4b53-4158-9c11-a8286f66cd0c'
SOURCE_PATH = 'pictographic-primitives/finance/withdraw_8ad5583e-4b53-4158-9c11-a8286f66cd0c.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'atm-cash-withdrawal-diagonal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'finance'
    categories = ('primitives', 'finance')
    aliases = ()
    keywords = ('atm', 'cash', 'withdrawal')

    def build(self):

        def dollar(x,y):
            self.add_line('dollar-top',(x+6,y-8),(x,y-8))
            self.add_arc('dollar-a',(x,y-8),(x,y),radius_x=6,radius_y=4,sweep=False)
            self.add_arc('dollar-b',(x,y),(x,y+8),radius_x=6,radius_y=4)
            self.add_line('dollar-foot',(x,y+8),(x-6,y+8))
            self.add_contour('dollar','dollar-top','dollar-a','dollar-b','dollar-foot')
            self.add_line('dollar-stem-top',(x,y-10),(x,y-8))
            self.add_line('dollar-stem-bottom',(x,y+8),(x,y+10))
            self.relate('connect','dollar','dollar-stem-top')
            self.relate('connect','dollar','dollar-stem-bottom')
        # Slanted note emerges from a single slit bar; no duplicate thickness edge.
        self.add_polyline('slot',(6,6),(12,6),(42,6))
        self.add_polyline('note',(12,6),(6,42),(36,42),(42,6))
        self.relate('connect','slot','note')
        dollar(24,24)
