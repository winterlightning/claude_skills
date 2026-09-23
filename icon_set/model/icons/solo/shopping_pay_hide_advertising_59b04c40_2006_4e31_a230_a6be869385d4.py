from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '59b04c40-2006-4e31-a230-a6be869385d4'
SOURCE_PATH = 'icon_set/work/todo-references/shopping pay hide advertising_59b04c40-2006-4e31-a230-a6be869385d4.svg'
AUTHOR = 'gpt-6'
# Plan: Dollar coin crossed by a rising diagonal suppression slash.
# Construction references: No exact local Lucide match; circular badge and handwritten dollar curves.
# Reduction: No defining parts omitted.

class AuthoredIcon(Solo48):
    icon_id = 'shopping-pay-hide-advertising'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('shopping', 'pay', 'hide', 'advertising')

    def build(self):
        self.circle('coin',24,25,17)
        self.add_bezier('dollar',(29,18),((18,14),(17,26),(24,25)),((33,25),(29,36),(20,32)))
        self.add_line('dollar-stem',(24,12),(24,37));self.relate('connect','dollar','dollar-stem')
        self.add_line('slash',(6,42),(42,6))
        self.relate('connect','slash','coin');self.relate('connect','slash','dollar');self.relate('connect','slash','dollar-stem')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,l,t,r,b,q=3):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)

    def shield(self):
        self.add_bezier('crown-left',(8,12),((15,12),(21,7),(24,4)))
        self.add_bezier('crown-right',(24,4),((27,7),(33,12),(40,12)))
        self.add_line('wall-right',(40,12),(40,23))
        self.add_bezier('base-right',(40,23),((40,33),(33,40),(24,44)))
        self.add_bezier('base-left',(24,44),((15,40),(8,33),(8,23)))
        self.add_line('wall-left',(8,23),(8,12))
        self.add_contour('shield','crown-left','crown-right','wall-right','base-right','base-left','wall-left',closed=True)
