from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='ea945a43-10ca-4ee5-a157-515c7b4149fa'
SOURCE_PATH='pictographic-primitives/_uncategorized_33/road lock_ea945a43-10ca-4ee5-a157-515c7b4149fa.svg'
AUTHOR='gpt-6'
PLAN='A lock containing a receding road. Symmetric shackle and road meet split body nodes; road narrowed at its bottom to provide legal side-wall gaps.'
CONSTRUCTION_REFERENCE='Lucide lock arched shackle and body'
class Drawing(Solo48):
    icon_id='road-lock'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('road', 'lock')
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
        # Split body walls at true shackle and road nodes.
        self.add_polyline('body',(8,24),(14,24),(34,24),(40,24),(40,44),(32,44),(16,44),(8,44),closed=True)
        self.add_line('shackle-left',(14,24),(14,14))
        self.add_arc('shackle-top',(14,14),(34,14),radius_x=10)
        self.add_line('shackle-right',(34,14),(34,24))
        self.add_contour('shackle','shackle-left','shackle-top','shackle-right')
        self.relate('connect','shackle','body')
        self.add_polyline('road',(16,44),(20,32),(28,32),(32,44))
        self.relate('connect','road','body')

FINAL_OMISSIONS = 'Remove center road dash.'
VISUAL_REVIEW = 'Symmetric shackle and road meet split body nodes; road narrowed at its bottom to provide legal side-wall gaps.'
