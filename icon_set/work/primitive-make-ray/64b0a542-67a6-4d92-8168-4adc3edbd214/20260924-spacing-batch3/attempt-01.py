from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='64b0a542-67a6-4d92-8168-4adc3edbd214'
SOURCE_PATH='pictographic-primitives/_uncategorized_30/patentee_64b0a542-67a6-4d92-8168-4adc3edbd214.svg'
AUTHOR='gpt-6'
PLAN='Patent document, folded corner and circular award with two ribbon tails; omit writing to open spacing.'
CONSTRUCTION_REFERENCE='Lucide file-clock open document boundary; award ribbon'
class Drawing(Solo48):
    icon_id='patentee'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('patentee',)
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
        self.add_polyline('page',(20,34),(8,34),(8,4),(30,4),(40,14),(40,26))
        self.add_polyline('fold',(30,4),(30,14),(40,14))
        self.relate('connect','fold','page')
        self.circle('seal',30,34,10)
        self.relate('connect','seal','page')
        self.add_polyline('ribbon',(24,42),(24,44),(30,42),(36,44),(36,42))
