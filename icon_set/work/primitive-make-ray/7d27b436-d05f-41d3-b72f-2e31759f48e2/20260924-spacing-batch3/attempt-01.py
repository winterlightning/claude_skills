from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='7d27b436-d05f-41d3-b72f-2e31759f48e2'
SOURCE_PATH='pictographic-primitives/_uncategorized_29/onam 1_7d27b436-d05f-41d3-b72f-2e31759f48e2.svg'
AUTHOR='gpt-6'
PLAN='Six flower lobes form one coherent outline inside circular rim; omit central hexagon to open negative space.'
CONSTRUCTION_REFERENCE='Lucide flower coherent petal boundary'
class Drawing(Solo48):
    icon_id='onam-1'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('onam', '1')
    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def box(self,n,l,t,r,b,k=4):
        ps=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k)]
        ns=[]
        for j,a in enumerate(ps):
            z=ps[(j+1)%8]
            if a==z: continue
            m=f'{n}-{j}'; ns.append(m)
            if j%2:self.add_arc(m,a,z,radius_x=k)
            else:self.add_line(m,a,z)
        self.add_contour(n,*ns,closed=True)
    def cross(self,n,x,y,r):
        ns=[]
        for j,p in enumerate([(x-r,y),(x+r,y),(x,y-r),(x,y+r)]):
            m=f'{n}-{j}';ns.append(m);self.add_line(m,(x,y),p)
        self.relate('connect',*ns)
    def build(self):
        self.circle('rim',24,24,20)
        self.add_bezier('petals',(24,12),((28,12),(28,17),(28,17)),((32,14),(36,16),(34,20)),((33,23),(32,24),(32,24)),((36,27),(36,30),(32,32)),((30,33),(28,31),(28,31)),((28,36),(20,36),(20,31)),((16,34),(12,30),(16,24)),((12,18),(16,14),(20,17)),((20,17),(20,12),(24,12)))
        self.add_contour('flower','petals',closed=True)
