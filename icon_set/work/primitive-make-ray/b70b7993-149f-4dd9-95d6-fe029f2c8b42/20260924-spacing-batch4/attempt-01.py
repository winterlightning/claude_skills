from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='b70b7993-149f-4dd9-95d6-fe029f2c8b42'
SOURCE_PATH='pictographic-primitives/_uncategorized_33/saving bear increase_b70b7993-149f-4dd9-95d6-fe029f2c8b42.svg'
AUTHOR='gpt-6'
PLAN='Bear head under upward financial arrow. Remove nested muzzle outline and crease; retain nose and two ears.'
CONSTRUCTION_REFERENCE='Lucide trending-up coherent arrow; source bear silhouette, no exact Lucide bear match'
class Drawing(Solo48):
    icon_id='saving-bear-increase'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('saving', 'bear', 'increase')
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
        self.add_polyline('trend',(6,20),(18,8),(30,10),(42,6))
        self.add_polyline('arrow',(34,6),(42,6),(42,14));self.relate('connect','trend','arrow')
        self.add_bezier('bear',(16,27),((12,20),(20,19),(22,25)),((25,24),(29,24),(32,25)),((35,19),(41,21),(38,28)),((45,39),(38,42),(27,42)),((16,42),(10,39),(16,27)))
        self.add_contour('bear-outline','bear',closed=True)
        self.add_dot('nose',(27,33))
