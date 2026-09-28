"""Bitcoin and Dollar Balance Scale. Reference retains the complete subject following saved user classification.
Plan: SQUARE envelope; shared page/currency dimensions and true beam attachment nodes.
Lucide files informs page contour continuity; dollar-sign informs paired currency bowls.
Source supplies count, relative placement and intentional asymmetry. Decorative thickness omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '40a6f5d9-1d48-449a-9169-f46dd5fad662'
SOURCE_PATH = 'pictographic-primitives/finance/crypto currency bitcoin dollar equal_40a6f5d9-1d48-449a-9169-f46dd5fad662.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'bitcoin-and-dollar-balance-scale'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'finance'
    categories = ('primitives', 'finance')
    aliases = ()
    keywords = ('bitcoin', 'and', 'dollar', 'balance', 'scale')

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
        def bitcoin(x,y):
            nodes=[(x+6,y+8),(x,y+8),(x-6,y+8),(x-6,y),(x-6,y-8),(x,y-8),(x+6,y-8)]
            for j,(a,b) in enumerate(zip(nodes,nodes[1:]),1): self.add_line('bitcoin-spine-'+str(j),a,b)
            self.add_arc('bitcoin-upper',(x+6,y-8),(x+6,y),radius_x=4,radius_y=4)
            self.add_arc('bitcoin-lower',(x+6,y),(x+6,y+8),radius_x=4,radius_y=4)
            self.add_contour('bitcoin','bitcoin-spine-1','bitcoin-spine-2','bitcoin-spine-3','bitcoin-spine-4','bitcoin-spine-5','bitcoin-spine-6','bitcoin-upper','bitcoin-lower',closed=True)
            self.add_line('bitcoin-bar',(x-6,y),(x+6,y))
            self.relate('connect','bitcoin','bitcoin-bar')
            for label,dy in [('top',-8),('bottom',8)]:
                self.add_line('bitcoin-'+label,(x,y+dy),(x,y+dy+(2 if dy>0 else -2)))
                self.relate('connect','bitcoin','bitcoin-'+label)

        bitcoin(12,16)
        dollar(36,16)
        self.add_polyline('beam',(6,34),(24,34),(42,34))
        self.add_polyline('fulcrum',(24,34),(32,42),(16,42),closed=True)
        self.relate('connect','beam','fulcrum')
