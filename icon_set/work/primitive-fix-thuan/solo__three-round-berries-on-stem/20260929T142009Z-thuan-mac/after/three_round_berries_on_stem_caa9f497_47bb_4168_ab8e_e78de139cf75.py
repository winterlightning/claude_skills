"""Restore three equally round berries with a complete foreground fruit and joined rear arcs, plus a separate pointed leaf and branching stem.
Symbol plan: Restore three equally round berries with a complete foreground fruit and joined rear arcs, plus a separate pointed leaf and branching stem.
Construction reference: No useful exact Lucide match; source defines three round fruits and shared leaf/stem hierarchy.
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
        self.circle('front',24,36,8)
        self.add_arc('left-upper',(24,28),(8,28),radius_x=8,sweep=False)
        self.add_arc('left-lower',(8,28),(16,36),radius_x=8,sweep=False)
        self.add_contour('left','left-upper','left-lower')
        self.add_arc('right-upper',(40,28),(24,28),radius_x=8,sweep=False)
        self.add_arc('right-lower',(32,36),(40,28),radius_x=8,sweep=False)
        self.add_contour('right','right-lower','right-upper')
        for a,b in [('front','left'),('front','right'),('left','right')]:self.relate('connect',a,b)
        self.add_polyline('stem',(24,28),(24,12),(32,4))
        for n in ('front','left','right'):self.relate('connect','stem',n)
        self.add_bezier('leaf-upper',(8,4),((16,4),(24,4),(24,12)))
        self.add_bezier('leaf-lower',(24,12),((16,12),(8,12),(8,4)))
        self.add_contour('leaf','leaf-upper','leaf-lower',closed=True);self.relate('connect','leaf','stem')
