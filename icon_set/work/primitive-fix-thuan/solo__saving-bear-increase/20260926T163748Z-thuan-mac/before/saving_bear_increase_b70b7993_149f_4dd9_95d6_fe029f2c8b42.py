from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='b70b7993-149f-4dd9-95d6-fe029f2c8b42'
SOURCE_PATH='pictographic-primitives/_uncategorized_33/saving bear increase_b70b7993-149f-4dd9-95d6-fe029f2c8b42.svg'
AUTHOR='gpt-6'
PLAN='A bear head below a rising financial arrow. Matched circular ear radii, broad curved cheeks and centered nose. Face is balanced about x27; financial arrow is intentionally directional.'
CONSTRUCTION_REFERENCE='Lucide trending-up; supplied bear round-ear silhouette'
class Drawing(Solo48):
    icon_id='saving-bear-increase'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
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
        self.add_arc('ear-left',(15,24),(21,24),radius_x=3)
        self.add_line('forehead',(21,24),(33,24))
        self.add_arc('ear-right',(33,24),(39,24),radius_x=3)
        self.add_bezier('cheek-right',(39,24),((46,36),(38,42),(27,42)))
        self.add_bezier('cheek-left',(27,42),((16,42),(8,36),(15,24)))
        self.add_contour('bear','ear-left','forehead','ear-right','cheek-right','cheek-left',closed=True)
        self.add_dot('nose',(27,33))

FINAL_OMISSIONS = 'Remove nested muzzle outline and crease; retain central nose.'
VISUAL_REVIEW = 'Matched circular ear radii, broad curved cheeks and centered nose. Face is balanced about x27; financial arrow is intentionally directional.'
