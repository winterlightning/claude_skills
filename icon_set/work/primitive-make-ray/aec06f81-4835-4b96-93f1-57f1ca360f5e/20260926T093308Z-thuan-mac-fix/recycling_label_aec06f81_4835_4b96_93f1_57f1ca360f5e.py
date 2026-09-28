from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "aec06f81-4835-4b96-93f1-57f1ca360f5e"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__recycling-label/20260926T093246Z-thuan-mac/reference/recycling label_aec06f81-4835-4b96-93f1-57f1ca360f5e.svg"
AUTHOR = "claude-opus-5-5"
PLAN='A diagonal recycling tag with a separate leaf. Leaf halves and stem share the explicit node30,39. Intentional diagonal tag and offset leaf; clear negative space in both themes.'
CONSTRUCTION_REFERENCE='Lucide tag clipped tip; leaf coherent outline'
class Drawing(Solo48):
    icon_id='recycling-label'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
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
        # Symbol plan (SQUARE 6..42): tag on the 45-degree axis, pointed end at
        # the top right. Long edges x+y=28 and x+y=52 (centre x+y=40), square tip
        # (34,6) with equal 12-long horizontal and vertical chamfers, end edge
        # (6,22)-(18,34). Eyelet dot (26,14), 8 from the chamfers and 8.5 from
        # the long edges. Leaf: lens mirrored about x+y=72 from base (32,40) to
        # tip (42,30), with a short stem to (30,42).
        self.add_polyline('tag', (22, 6), (34, 6), (34, 18), (18, 34), (6, 22), closed=True)
        self.add_dot('eyelet', (26, 14))
        self.add_bezier('leaf-outer', (32, 40), ((39, 40), (42, 35), (42, 30)))
        self.add_bezier('leaf-inner', (42, 30), ((37, 30), (32, 33), (32, 40)))
        self.add_contour('leaf', 'leaf-outer', 'leaf-inner', closed=True)
        self.add_line('stem', (32, 40), (30, 42)); self.relate('connect', 'stem', 'leaf')
