"""baggage weight. Plan: VRECT_L extremes (8,4)-(40,44); circular gauge above suitcase. Gauge radius ten and a centered upright needle leave nine units of clearance; integrated raised grip avoids an undersized separate handle hole. Lucide luggage informs shared rounded case corners. Decorative case stripes omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ee2a071e-6904-4d7d-a879-a7315aec3bd6'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_05/baggage weight_ee2a071e-6904-4d7d-a879-a7315aec3bd6.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'baggage-weight'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('baggage', 'weight')
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
        self.circle('dial',24,14,10)
        self.add_line('needle',(24,14),(24,13))
        # Merge the handle opening with the suitcase interior; retain its raised outline.
        self.path('case',(11,36),[(20,36),(20,33),(28,33),(28,36),(37,36),((40,39),3,3,True),(40,41),((37,44),3,3,True),(11,44),((8,41),3,3,True),(8,39),((11,36),3,3,True)],True)
