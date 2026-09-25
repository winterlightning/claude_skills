"""The text 5G surrounded by network framing marks.
Plan: SQUARE fits the complete lettering with paired upper and lower frame marks.
Reduction: Removed four side ticks; simplified the lower brackets to horizontal strokes and made 5G angular.
Construction: Lucide scan: separated framing corners; source owns the hand-authored lettering.
Layout: Outer frame marks mirror around x24; unequal 5 and G shapes preserve readable typography."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='9dc361bf-d268-4878-852c-ebdc9f66c69b'
SOURCE_PATH = 'pictographic-primitives/technology/network 5g_9dc361bf-d268-4878-852c-ebdc9f66c69b.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id='network-5g'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'technology'
    aliases=()
    keywords=('network', '5g')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,x,y,w,h,r=2):
        p=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i in range(8):
            k=n+'-'+str(i);ids.append(k)
            if i%2:self.add_arc(k,p[i],p[(i+1)%8],radius_x=r)
            else:self.add_line(k,p[i],p[(i+1)%8])
        self.add_contour(n,*ids,closed=True)

    def build(self):
        for side in (-1,1):
            def p(x,y):return (24+side*x,y)
            self.add_polyline('top-'+str(side),p(18,6),p(10,6),p(8,8))
            self.add_line('bottom-'+str(side),p(18,42),p(10,42))
        self.add_polyline('five-top',(20,17),(10,17),(10,25),(15,25))
        self.add_arc('five-bowl',(15,25),(15,33),radius_x=4)
        self.add_line('five-foot',(15,33),(10,33))
        self.relate('connect','five-top','five-bowl');self.relate('connect','five-bowl','five-foot')
        self.add_polyline('g',(39,17),(29,17),(29,33),(39,33),(39,25),(35,25))


