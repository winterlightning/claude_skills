from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='c0e31e5f-9872-4414-9334-38d9e1e42539'
SOURCE_PATH='pictographic-primitives/_uncategorized_33/romance pride gay lgbt heart_c0e31e5f-9872-4414-9334-38d9e1e42539.svg'
AUTHOR='gpt-6'
PLAN='A rainbow above a heart. Shared horizontal center; mirrored heart lobes and evenly nested rainbow bands. Flattened arcs provide room above heart.'
CONSTRUCTION_REFERENCE='Lucide rainbow concentric arcs; heart mirrored lobes'
class Drawing(Solo48):
    icon_id='romance-pride-gay-lgbt-heart'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('romance', 'pride', 'gay', 'lgbt', 'heart')
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
        self.add_arc('rainbow-outer',(4,20),(44,20),radius_x=20,radius_y=12)
        self.add_arc('rainbow-inner',(13,20),(35,20),radius_x=11,radius_y=3)
        self.add_arc('heart-left',(16,32),(24,32),radius_x=4)
        self.add_arc('heart-right',(24,32),(32,32),radius_x=4)
        self.add_line('heart-down',(32,32),(24,40))
        self.add_line('heart-up',(24,40),(16,32))
        self.add_contour('heart','heart-left','heart-right','heart-down','heart-up',closed=True)

FINAL_OMISSIONS = 'Reduce rainbow to two arcs and remove baseline.'
VISUAL_REVIEW = 'Shared horizontal center; mirrored heart lobes and evenly nested rainbow bands. Flattened arcs provide room above heart.'
