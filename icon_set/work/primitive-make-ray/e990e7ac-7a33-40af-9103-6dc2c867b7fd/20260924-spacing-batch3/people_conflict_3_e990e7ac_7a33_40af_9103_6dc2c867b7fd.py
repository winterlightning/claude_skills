from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='e990e7ac-7a33-40af-9103-6dc2c867b7fd'
SOURCE_PATH='pictographic-primitives/_uncategorized_30/people conflict 3_e990e7ac-7a33-40af-9103-6dc2c867b7fd.svg'
AUTHOR='gpt-6'
PLAN='Two inward-facing human profiles beneath a conflict burst. Mirrored connected head/neck profiles; no detached-head gap applies. Broadened neck opening clears internal-spacing check.'
CONSTRUCTION_REFERENCE='human_ref/user.svg round cranium; source opposing profiles, no useful exact Lucide match'
class Drawing(Solo48):
    icon_id='people-conflict-3'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('people', 'conflict', '3')
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
        # Opposed profiles mirror about x=24; coherent head/neck outlines.
        for n,flip in [('left',False),('right',True)]:
            def p(x,y):return (48-x,y) if flip else (x,y)
            self.add_arc(n+'-skull',p(6,30),p(18,30),radius_x=6,sweep=not flip)
            self.add_polyline(n+'-face',p(18,30),p(20,34),p(16,34),p(14,42))
            self.add_polyline(n+'-back',p(6,30),p(6,42))
            self.relate('connect',n+'-skull',n+'-face');self.relate('connect',n+'-skull',n+'-back')
        self.add_polyline('burst',(14,14),(14,8),(20,11),(24,6),(28,11),(34,8),(34,14))

FINAL_OMISSIONS = 'Remove small mouth/jaw stair steps.'
VISUAL_REVIEW = 'Mirrored connected head/neck profiles; no detached-head gap applies. Broadened neck opening clears internal-spacing check.'
