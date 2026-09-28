"""astronomy planet saturn 1. Plan: circular planet and rising ring share two exact Pythagorean intersection nodes. Square extremes (6,6)-(42,42) reached by ring tips; slight perspective bends at the planet rim retain the diagonal ring. Lucide circle-slash informs the coherent circular silhouette."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd3179da3-e2e2-4329-8932-7b3c8044a535'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__planet-with-diagonal-ring-solo/20260927T143814Z-thuan-mac-1/reference/astronomy planet saturn 1_d3179da3-e2e2-4329-8932-7b3c8044a535.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'planet-with-diagonal-ring-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('astronomy', 'planet', 'saturn', '1')
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
        # Curved end caps turn the diagonal crossing into an orbital ring.
        self.path('planet',(33,12),[((36,33),15,15,True),((15,36),15,15,True),((12,15),15,15,True),((33,12),15,15,True)],True)
        self.add_polyline('ring-spine',(6,42),(15,36),(33,12),(42,6))
        self.relate('connect','planet','ring-spine')
        self.add_line('ring-near-end',(6,42),(6,38))
        self.add_line('ring-far-end',(42,6),(42,10))
        self.relate('connect','ring-spine','ring-near-end')
        self.relate('connect','ring-spine','ring-far-end')

# Revision comparison: The rejected diagonal read as a plain slash across a circle.
# Revision: Added short orbital end turns to the diagonal ring.
