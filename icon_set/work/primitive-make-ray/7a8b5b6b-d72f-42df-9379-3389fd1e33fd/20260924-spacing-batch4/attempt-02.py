from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='7a8b5b6b-d72f-42df-9379-3389fd1e33fd'
SOURCE_PATH='pictographic-primitives/_uncategorized_33/self driving car_7a8b5b6b-d72f-42df-9379-3389fd1e33fd.svg'
AUTHOR='gpt-6'
PLAN='Symmetric frontal car and two radio arcs. Drop headlights, simplify wheel outlines to short stems, split body at true roof/wheel junctions.'
CONSTRUCTION_REFERENCE='Lucide car-front roof/fascia/wheels; wifi nested arcs'
class Drawing(Solo48):
    icon_id='self-driving-car'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('self', 'driving', 'car')
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
        self.add_polyline('body',(6,32),(12,32),(36,32),(42,32),(42,40),(36,40),(12,40),(6,40),closed=True)
        self.add_polyline('roof',(12,32),(16,24),(32,24),(36,32));self.relate('connect','roof','body')
        for i,x in enumerate((12,36)):
            self.add_line(f'wheel-{i}',(x,40),(x,42));self.relate('connect',f'wheel-{i}','body')
        self.add_arc('radio-outer',(12,10),(36,10),radius_x=12,radius_y=4)
        self.add_arc('radio-inner',(18,16),(30,16),radius_x=6,radius_y=1)
