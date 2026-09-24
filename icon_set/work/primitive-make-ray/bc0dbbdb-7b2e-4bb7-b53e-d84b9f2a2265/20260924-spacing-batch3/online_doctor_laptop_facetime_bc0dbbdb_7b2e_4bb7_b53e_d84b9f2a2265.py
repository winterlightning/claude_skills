from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='bc0dbbdb-7b2e-4bb7-b53e-d84b9f2a2265'
SOURCE_PATH='pictographic-primitives/_uncategorized_29/online doctor laptop facetime_bc0dbbdb-7b2e-4bb7-b53e-d84b9f2a2265.svg'
AUTHOR='gpt-6'
PLAN='A doctor beside a laptop. Head bottom18 and shoulder crest26 give exact8 centerline /4 ink gap; head aligns with shoulder center33. Laptop arrangement intentionally asymmetric.'
CONSTRUCTION_REFERENCE='human_ref/user.svg; Lucide laptop tapered base'
class Drawing(Solo48):
    icon_id='online-doctor-laptop-facetime'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('online', 'doctor', 'laptop', 'facetime')
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
        self.circle('head',33,13,5)
        self.add_arc('shoulder',(22,36),(44,36),radius_x=11,radius_y=10)
        self.add_line('right-side',(44,36),(44,40))
        self.add_contour('body','shoulder','right-side')
        self.add_polyline('screen',(4,40),(4,23),(10,23))
        self.add_polyline('laptop',(4,40),(14,40),(12,32),(4,32))
        self.relate('connect','screen','laptop')
        self.cross('medical',33,37,2)

FINAL_OMISSIONS = 'Simplify laptop keyboard and reduce medical cross.'
VISUAL_REVIEW = 'Head bottom18 and shoulder crest26 give exact8 centerline /4 ink gap; head aligns with shoulder center33. Laptop arrangement intentionally asymmetric.'
