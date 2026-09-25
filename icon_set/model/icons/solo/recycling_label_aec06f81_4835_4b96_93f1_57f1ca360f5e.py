from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='aec06f81-4835-4b96-93f1-57f1ca360f5e'
SOURCE_PATH='pictographic-primitives/_uncategorized_32/recycling label_aec06f81-4835-4b96-93f1-57f1ca360f5e.svg'
AUTHOR='gpt-6'
PLAN='A diagonal recycling tag with a separate leaf. Leaf halves and stem share the explicit node30,39. Intentional diagonal tag and offset leaf; clear negative space in both themes.'
CONSTRUCTION_REFERENCE='Lucide tag clipped tip; leaf coherent outline'
class Drawing(Solo48):
    icon_id='recycling-label'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('recycling', 'label')
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
        self.add_polyline('tag',(6,22),(22,6),(38,6),(38,14),(14,38),closed=True)
        self.add_dot('eyelet',(25,15))
        self.add_bezier('leaf-left',(42,30),((32,29),(27,35),(30,39)))
        self.add_bezier('leaf-right',(30,39),((34,44),(42,42),(42,30)))
        self.add_contour('leaf','leaf-left','leaf-right',closed=True)
        self.add_line('stem',(26,42),(30,39));self.relate('connect','stem','leaf')

FINAL_OMISSIONS = 'Reduce eyelet to a dot and drop leaf vein; rebalance tag edges.'
VISUAL_REVIEW = 'Leaf halves and stem share the explicit node30,39. Intentional diagonal tag and offset leaf; clear negative space in both themes.'
