"""crowdin logo. Plan: four coherent swept strokes preserve the nested, interrupted C-band arrangement. HRECT_L extremes (4,8)-(44,40). No useful local Lucide logo match. Tapered ribbon double outlines reduced to their four centerline strokes to remove undersized enclosed slivers; deliberate asymmetric sweep retained."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e89d9bcb-0e93-4a07-abd4-7740608fbbd7'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_13/crowdin logo_e89d9bcb-0e93-4a07-abd4-7740608fbbd7.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'crowdin-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('crowdin', 'logo')
    def path(self,n,start,steps,closed=False):
        here=start;members=[]
        for k,step in enumerate(steps):
            ident=f'{n}-{k}';members.append(ident)
            if len(step)==2:
                self.add_line(ident,here,step);here=step
            else:
                end,rx,ry,sweep=step
                self.add_arc(ident,here,end,radius_x=rx,radius_y=ry,sweep=sweep);here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,q=0):
        if q==0:self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True)
        else:self.path(n,(l+q,t),[(r-q,t),((r,t+q),q,q,True),(r,b-q),((r-q,b),q,q,True),(l+q,b),((l,b-q),q,q,True),(l,t+q),((l+q,t),q,q,True)],True)
    def build(self):
        self.add_bezier('outer-upper',(44,8),((22,8),(8,8),(4,19)))
        self.add_bezier('outer-lower',(4,29),((4,36),(10,40),(24,40)))
        self.add_bezier('inner-upper',(44,18),((34,18),(28,18),(24,24)))
        self.add_bezier('inner-lower',(28,32),((28,34),(34,34),(40,34)))
