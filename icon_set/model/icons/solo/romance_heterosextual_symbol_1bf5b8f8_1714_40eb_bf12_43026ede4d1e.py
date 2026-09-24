from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='1bf5b8f8-1714-40eb-bf12-43026ede4d1e'
SOURCE_PATH='pictographic-primitives/_uncategorized_33/romance heterosextual symbol_1bf5b8f8-1714-40eb-bf12-43026ede4d1e.svg'
AUTHOR='gpt-6'
PLAN='A romance heart with male and female gender attachments. Heart, male shaft and female stem use actual shared nodes. Arrow and cross remain distinct; intentional upper-right male arrow.'
CONSTRUCTION_REFERENCE='Lucide heart paired circular lobes; source male/female attachments'
class Drawing(Solo48):
    icon_id='romance-heterosextual-symbol'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('romance', 'heterosextual', 'symbol')
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
        # The heart is the gender symbol's shared ring; remove redundant nested circle.
        self.add_arc('heart-left',(8,18),(20,18),radius_x=6)
        self.add_arc('heart-right',(20,18),(32,18),radius_x=6)
        self.add_line('heart-down',(32,18),(20,31))
        self.add_line('heart-up',(20,31),(8,18))
        self.add_contour('heart','heart-left','heart-right','heart-down','heart-up',closed=True)
        self.add_line('male-shaft',(32,18),(40,4))
        self.add_polyline('male-head',(32,4),(40,4),(40,12))
        self.relate('connect','male-shaft','heart');self.relate('connect','male-shaft','male-head')
        self.add_polyline('female-stem',(20,31),(20,40),(20,44))
        self.add_polyline('female-cross',(12,40),(20,40),(28,40))
        self.relate('connect','female-stem','heart');self.relate('connect','female-stem','female-cross')

FINAL_OMISSIONS = 'Merge nested circular gender ring with heart boundary.'
VISUAL_REVIEW = 'Heart, male shaft and female stem use actual shared nodes. Arrow and cross remain distinct; intentional upper-right male arrow.'
