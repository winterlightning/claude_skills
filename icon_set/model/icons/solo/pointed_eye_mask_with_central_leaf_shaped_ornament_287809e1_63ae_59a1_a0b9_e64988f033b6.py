"""Decorative Masquerade Eye Mask.
Symbol plan: Pointed masquerade mask with matched eye holes and central plume. HRECT_L (4,8)-(44,40) gives the eye bowls enough width. No useful exact Lucide match. Mirrored radius12 bowls; reduce narrow leaf ornament to its central stroke and almond holes to small circles so the face remains clear at 48 pixels.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '287809e1-63ae-59a1-a0b9-e64988f033b6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/carnival mask_287809e1-63ae-59a1-a0b9-e64988f033b6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pointed-eye-mask-with-central-leaf-shaped-ornament'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "entertainment"
    aliases = ()
    keywords = ('decorative', 'masquerade', 'eye', 'mask')

    def build(self):
        self.add_line('plume',(24,8),(24,12))
        self.add_bezier('upper-left',(4,14),((12,20),(16,14),(24,24)))
        self.add_bezier('upper-right',(24,24),((32,14),(36,20),(44,14)))
        self.add_line('right-wall',(44,14),(44,28))
        self.add_arc('right-bowl',(44,28),(32,40),radius_x=12)
        self.add_bezier('nose-right',(32,40),((28,40),(26,36),(24,36)))
        self.add_bezier('nose-left',(24,36),((22,36),(20,40),(16,40)))
        self.add_arc('left-bowl',(16,40),(4,28),radius_x=12)
        self.add_line('left-wall',(4,28),(4,14))
        self.add_contour('mask','upper-left','upper-right','right-wall','right-bowl','nose-right','nose-left','left-bowl','left-wall',closed=True)
        for x in (15,33):self.circle(f'eye-{x}',x,29,2)

    def rounded(self, name, l, t, r, b, radius, nodes=()):
        # One radius owns all tangent corners; split straight walls at real joins.
        pts=[(l+radius,t),(r-radius,t),(r,t+radius),(r,b-radius),
             (r-radius,b),(l+radius,b),(l,b-radius),(l,t+radius)]
        members=[]
        for i,a in enumerate(pts):
            z=pts[(i+1)%8]; part=f"{name}-{i}"
            if i%2:
                self.add_arc(part,a,z,radius_x=radius)
                members.append(part)
            else:
                on=[p for p in nodes if p!=a and p!=z and
                    (z[0]-a[0])*(p[1]-a[1])==(z[1]-a[1])*(p[0]-a[0]) and
                    min(a[0],z[0])<=p[0]<=max(a[0],z[0]) and min(a[1],z[1])<=p[1]<=max(a[1],z[1])]
                on.sort(key=lambda p:(p[0]-a[0])**2+(p[1]-a[1])**2)
                path=[a,*on,z]
                for j,(v,w) in enumerate(zip(path,path[1:])):
                    if v==w: continue
                    member=f"{part}-{j}";self.add_line(member,v,w);members.append(member)
        self.add_contour(name,*members,closed=True)

    def circle(self,name,x,y,r):
        self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)
