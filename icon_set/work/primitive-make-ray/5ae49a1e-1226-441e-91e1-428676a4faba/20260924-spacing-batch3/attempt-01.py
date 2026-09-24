from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='5ae49a1e-1226-441e-91e1-428676a4faba'
SOURCE_PATH='pictographic-primitives/_uncategorized_30/pegboard_5ae49a1e-1226-441e-91e1-428676a4faba.svg'
AUTHOR='gpt-6'
PLAN='Square board owns a centered three-by-three series at pitch9. Reduce tiny hole outlines to solid circular perforation marks.'
CONSTRUCTION_REFERENCE='No exact Lucide match; shared rounded-frame construction from image'
class Drawing(Solo48):
    icon_id='nine-hole-square-pegboard'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('pegboard',)
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
        self.box('board',6,6,42,42)
        for y in (15,24,33):
            for x in (15,24,33):self.add_dot(f'hole-{x}-{y}',(x,y))
