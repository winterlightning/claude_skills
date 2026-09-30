"""Restore three round berries with a larger foreground fruit, a single stem and a pointed leaf.
Symbol plan: Restore three round berries with a larger foreground fruit, a single stem and a pointed leaf.
Construction reference: No useful exact Lucide match; source defines three round fruits and the shared leaf/stem hierarchy.
Omissions: None
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='caa9f497-47bb-4168-ab8e-e78de139cf75'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-fix-thuan/solo__three-round-berries-on-stem/20260929T142009Z-thuan-mac/reference/cranberry_caa9f497-47bb-4168-ab8e-e78de139cf75.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='three-round-berries-on-stem'
    keyshape=Keyshape.VRECT_L
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
        # Three round fruits: foreground circle occludes the paired rear fruit contours.
        self.circle('front',24,35,9)
        self.add_arc('left-fruit',(24,26),(8,26),radius_x=8)
        self.add_arc('left-lower',(8,26),(16,34),radius_x=8)
        self.add_contour('left','left-fruit','left-lower')
        self.add_arc('right-fruit',(40,26),(24,26),radius_x=8)
        self.add_arc('right-lower',(32,34),(40,26),radius_x=8)
        self.add_contour('right','right-lower','right-fruit')
        self.relate('connect','front','left');self.relate('connect','front','right');self.relate('connect','left','right')
        self.add_polyline('stem',(24,26),(24,14),(32,6))
        self.relate('connect','stem','left');self.relate('connect','stem','right');self.relate('connect','stem','front')
        self.add_arc('leaf-upper',(8,4),(24,14),radius_x=16,radius_y=10)
        self.add_arc('leaf-lower',(24,14),(8,4),radius_x=16,radius_y=10)
        self.add_contour('leaf','leaf-upper','leaf-lower',closed=True);self.relate('connect','leaf','stem')
