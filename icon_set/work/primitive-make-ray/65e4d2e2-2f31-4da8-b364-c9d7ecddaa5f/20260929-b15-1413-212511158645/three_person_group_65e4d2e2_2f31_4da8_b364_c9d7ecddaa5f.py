"""Restore three outlined heads, a dominant rounded central bust, and distinct shoulder-and-side contours for both smaller people.
Symbol plan: Restore three outlined heads, a dominant rounded central bust, and distinct shoulder-and-side contours for both smaller people.
Construction reference: human_ref/user.svg: circular heads and smooth shoulders. Exact detached gaps are 4 visible units for all three heads.
Omissions: Small lower torso dividers omitted to preserve clear bodies.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='65e4d2e2-2f31-4da8-b364-c9d7ecddaa5f'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-fix-thuan/solo__three-person-group/20260929T142009Z-thuan-mac/reference/troop_65e4d2e2-2f31-4da8-b364-c9d7ecddaa5f.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='three-person-group'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=()

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def box(self,n,l,t,r,b,k=3):
        pts=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k)]
        ids=[]
        for i,a in enumerate(pts):
            z=pts[(i+1)%8]
            if a==z:continue
            q=n+str(i);ids.append(q)
            if i%2:self.add_arc(q,a,z,radius_x=k)
            else:self.add_line(q,a,z)
        self.add_contour(n,*ids,closed=True)

    def build(self):
        self.circle('center-head',24,14,6)
        for side,cx in [('left',7),('right',41)]:self.circle(side+'-head',cx,20,3)
        self.add_arc('center-shoulders',(16,36),(32,36),radius_x=8)
        self.add_line('center-left',(16,36),(16,40));self.add_line('center-right',(32,36),(32,40))
        for n in ['center-left','center-right']:self.relate('connect','center-shoulders',n)
        for n,sign in [('left',1),('right',-1)]:
            def p(x,y):return (24+sign*(x-24),y)
            self.add_line(n+'-top',p(8,31),p(7,31))
            self.add_arc(n+'-corner',p(7,31),p(4,34),radius_x=3,sweep=sign<0)
            self.add_polyline(n+'-side',p(4,34),p(4,40),p(8,40))
            self.add_contour(n+'-shoulder',n+'-top',n+'-corner')
            self.relate('connect',n+'-shoulder',n+'-side')
