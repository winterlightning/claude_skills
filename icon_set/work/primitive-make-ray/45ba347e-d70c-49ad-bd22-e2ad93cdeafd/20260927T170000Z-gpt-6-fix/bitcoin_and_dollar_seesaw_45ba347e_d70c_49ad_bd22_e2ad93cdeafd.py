"""Bitcoin and Dollar Seesaw. Reference retains the complete subject following saved user classification.
Plan: SQUARE envelope; shared page/currency dimensions and true beam attachment nodes.
Lucide files informs page contour continuity; dollar-sign informs paired currency bowls.
Source supplies count, relative placement and intentional asymmetry. Decorative thickness omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '45ba347e-d70c-49ad-bd22-e2ad93cdeafd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bitcoin-and-dollar-seesaw/20260927T164353Z-thuan-mac-1/reference/crypto currency bitcoin dollar unequal_45ba347e-d70c-49ad-bd22-e2ad93cdeafd.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'bitcoin-and-dollar-seesaw'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'finance'
    categories = ('primitives', 'finance')
    aliases = ()
    keywords = ('bitcoin', 'and', 'dollar', 'seesaw')

    def build(self):

        def dollar(x,y):
            self.add_line('dollar-top',(x+6,y-8),(x,y-8))
            self.add_arc('dollar-a',(x,y-8),(x,y),radius_x=6,radius_y=4,sweep=False)
            self.add_arc('dollar-b',(x,y),(x,y+8),radius_x=6,radius_y=4)
            self.add_line('dollar-foot',(x,y+8),(x-6,y+8))
            self.add_contour('dollar','dollar-top','dollar-a','dollar-b','dollar-foot')
            self.add_line('dollar-stem-top',(x,y-10),(x,y-8))
            self.relate('connect','dollar','dollar-stem-top')
        def bitcoin(x,y):
            nodes=[(x+6,y+8),(x,y+8),(x-6,y+8),(x-6,y),(x-6,y-8),(x,y-8),(x+6,y-8)]
            for j,(a,b) in enumerate(zip(nodes,nodes[1:]),1): self.add_line('bitcoin-spine-'+str(j),a,b)
            self.add_arc('bitcoin-upper',(x+6,y-8),(x+6,y),radius_x=4,radius_y=4)
            self.add_arc('bitcoin-lower',(x+6,y),(x+6,y+8),radius_x=4,radius_y=4)
            self.add_contour('bitcoin','bitcoin-spine-1','bitcoin-spine-2','bitcoin-spine-3','bitcoin-spine-4','bitcoin-spine-5','bitcoin-spine-6','bitcoin-upper','bitcoin-lower',closed=True)
            self.add_line('bitcoin-bar',(x-6,y),(x+6,y))
            self.relate('connect','bitcoin','bitcoin-bar')
            for label,dy in [('top',-8)]:
                self.add_line('bitcoin-'+label,(x,y+dy),(x,y+dy+(2 if dy>0 else -2)))
                self.relate('connect','bitcoin','bitcoin-'+label)

        bitcoin(12,16)
        dollar(36,16)
        self.add_polyline('beam',(6,34),(24,33),(42,32))
        self.add_polyline('fulcrum',(24,33),(12,42),(36,42),(24,33),closed=True)
        self.relate('connect','beam','fulcrum')
