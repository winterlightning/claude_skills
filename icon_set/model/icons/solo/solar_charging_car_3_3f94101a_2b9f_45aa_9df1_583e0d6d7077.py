from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f94101a-2b9f-45aa-9df1-583e0d6d7077'
SOURCE_PATH = 'icon_set/work/todo-references/solar charging car 3_3f94101a-2b9f-45aa-9df1-583e0d6d7077.svg'
AUTHOR = 'gpt-6'
# Plan: Solar panel and sun beside a charging column marked with a lightning bolt.
# References: sun: circular center and radial rays; simple panel grid and rounded charging enclosure.
# Reduction: Reduced sun to four cardinal rays; retained four panel cells and charging bolt.

class AuthoredIcon(Solo48):
    icon_id = 'solar-charging-car-3'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('solar', 'charging', 'car', '3')

    def build(self):
        self.box('charger',30,6,42,42,3)
        self.add_polyline('bolt',(37,15),(34,22),(38,22),(35,29))
        self.circle('sun',15,14,4)
        for n,a,b in [('north',(15,6),(15,7)),('west',(6,14),(7,14)),('east',(23,14),(24,14)),('south',(15,22),(15,23))]:self.add_line(n,a,b)
        self.add_polyline('panel',(8,30),(22,30),(25,42),(6,42),closed=True)
        self.add_line('column',(15,30),(15,42));self.add_line('row',(7,36),(23,36))
        self.relate('connect','column','panel');self.relate('connect','row','panel');self.relate('connect','row','column')

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
