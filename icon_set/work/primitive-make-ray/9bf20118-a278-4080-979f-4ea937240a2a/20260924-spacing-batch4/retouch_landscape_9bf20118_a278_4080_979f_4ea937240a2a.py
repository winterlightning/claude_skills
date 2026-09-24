from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='9bf20118-a278-4080-979f-4ea937240a2a'
SOURCE_PATH='pictographic-primitives/_uncategorized_32/retouch landscape_9bf20118-a278-4080-979f-4ea937240a2a.svg'
AUTHOR='gpt-6'
PLAN='Open picture boundary, sun and mountain, upper-right retouch wand and sparkle. Drop second mountain to open spacing.'
CONSTRUCTION_REFERENCE='Lucide wand-sparkles diagonal wand; image frame'
class Drawing(Solo48):
    icon_id='retouch-landscape'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('retouch', 'landscape')
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
        self.add_polyline('frame',(23,14),(6,14),(6,42),(42,42),(42,35))
        self.circle('sun',16,24,2)
        self.add_polyline('mountain',(17,42),(29,27),(42,42))
        self.relate('connect','mountain','frame')
        self.add_line('wand',(31,16),(42,27))
        self.add_line('spark-up',(34,6),(34,7))
        self.add_line('spark-right',(42,8),(42,9))
