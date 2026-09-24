from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='3f77b04c-ad63-443d-a816-599e467435a6'
SOURCE_PATH='pictographic-primitives/_uncategorized_30/permafrost_3f77b04c-ad63-443d-a816-599e467435a6.svg'
AUTHOR='gpt-6'
PLAN='Six-way snowflake in rounded square, common center junction. Omit fork twigs to keep at least8 from frame.'
CONSTRUCTION_REFERENCE='Lucide snowflake radial repeat definition'
class Drawing(Solo48):
    icon_id='permafrost'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('permafrost',)
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
        self.box('frame',6,6,42,42)
        ends=[(24,15),(33,19),(33,29),(24,33),(15,29),(15,19)]
        for i,p in enumerate(ends):self.add_line(f'arm-{i}',(24,24),p)
        self.relate('connect',*[f'arm-{i}' for i in range(6)])
