from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='a119cf45-d021-460f-b469-9d1f28774714'
SOURCE_PATH='pictographic-primitives/_uncategorized_28/multiple users wifi_a119cf45-d021-460f-b469-9d1f28774714.svg'
AUTHOR='gpt-6'
PLAN='Three repeated busts with exact head bottom28 to shoulder top36 gap8; radio bands above.'
CONSTRUCTION_REFERENCE='human_ref/user.svg; Lucide wifi nested arcs'
class Drawing(Solo48):
    icon_id='multiple-users-wifi'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('multiple', 'users', 'wifi')
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
        self.add_arc('wifi-outer',(6,14),(42,14),radius_x=18,radius_y=8)
        self.add_arc('wifi-inner',(16,16),(32,16),radius_x=8,radius_y=2)
        for n,x,r in [('left',9,2),('middle',24,3),('right',39,2)]:
            self.circle(n+'-head',x,28-r,r)
            self.add_arc(n+'-shoulder',(x-3,42),(x+3,42),radius_x=3,radius_y=6)
