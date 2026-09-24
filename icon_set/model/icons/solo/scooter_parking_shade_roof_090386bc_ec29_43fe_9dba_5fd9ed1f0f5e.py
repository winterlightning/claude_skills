from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='090386bc-ec29-43fe-9dba-5fd9ed1f0f5e'
SOURCE_PATH='pictographic-primitives/_uncategorized_33/scooter parking shade roof_090386bc-ec29-43fe-9dba-5fd9ed1f0f5e.svg'
AUTHOR='gpt-6'
PLAN='A scooter under a pitched shelter roof. Equal wheel radii and baseline; wheel tops and seat attachment are explicit shared nodes. Symmetric roof with intentionally directional scooter.'
CONSTRUCTION_REFERENCE='Lucide bike equal wheels and coherent steering construction'
class Drawing(Solo48):
    icon_id='scooter-parking-shade-roof'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('scooter', 'parking', 'shade', 'roof')
    def circle(self,n,x,y,r):
        ps=[(x-r,y),(x,y-r),(x+r,y),(x,y+r)]
        for j,a in enumerate(ps):self.add_arc(f'{n}-{j}',a,ps[(j+1)%4],radius_x=r)
        self.add_contour(n,*[f'{n}-{j}' for j in range(4)],closed=True)
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
        self.add_polyline('roof',(4,18),(24,8),(44,18))
        self.circle('rear-wheel',13,37,3)
        self.circle('front-wheel',36,37,3)
        self.add_polyline('deck',(13,34),(18,34),(24,34),(36,34))
        self.relate('connect','deck','rear-wheel');self.relate('connect','deck','front-wheel')
        self.add_polyline('seat',(10,26),(18,26),(18,34))
        self.relate('connect','seat','deck')
        self.add_polyline('steering',(27,25),(32,25),(36,34));self.relate('connect','steering','deck');self.relate('connect','steering','front-wheel')

FINAL_OMISSIONS = 'Remove fenders and rear body detail; retain seat, deck, steering and wheels.'
VISUAL_REVIEW = 'Equal wheel radii and baseline; wheel tops and seat attachment are explicit shared nodes. Symmetric roof with intentionally directional scooter.'
