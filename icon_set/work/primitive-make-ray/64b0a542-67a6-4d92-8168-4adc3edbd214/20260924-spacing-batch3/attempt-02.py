from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='64b0a542-67a6-4d92-8168-4adc3edbd214'
SOURCE_PATH='pictographic-primitives/_uncategorized_30/patentee_64b0a542-67a6-4d92-8168-4adc3edbd214.svg'
AUTHOR='gpt-6'
PLAN='Seal owns exact 6-8-10 attachment nodes; open ribbon tails avoid enclosed slivers. Drop folded corner, writing, and ribbon notch.'
CONSTRUCTION_REFERENCE='Lucide award open ribbon construction; file-clock interrupted page'
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
        self.add_polyline('page',(24,34),(8,34),(8,4),(40,4),(40,26))
        self.add_arc('seal-main',(24,34),(40,26),radius_x=10,large_arc=True)
        self.add_arc('seal-lower-right',(40,26),(36,34),radius_x=10)
        self.add_arc('seal-bottom',(36,34),(24,34),radius_x=10)
        self.add_contour('seal','seal-main','seal-lower-right','seal-bottom',closed=True)
        self.relate('connect','seal','page')
        self.add_line('ribbon-left',(24,34),(20,44))
        self.add_line('ribbon-right',(36,34),(40,44))
        self.relate('connect','ribbon-left','seal');self.relate('connect','ribbon-right','seal')
