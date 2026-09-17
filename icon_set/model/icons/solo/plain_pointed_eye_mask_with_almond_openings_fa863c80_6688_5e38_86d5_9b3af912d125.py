"""Masquerade Eye Mask.
Symbol plan: Plain masquerade mask with paired openings. HRECT_L (4,8)-(44,40) provides broad eye bowls. No useful exact Lucide mask match. Mirror upper curves and radius12 lower bowls; simplify almond holes to round holes to preserve clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa863c80-6688-5e38-86d5-9b3af912d125'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/carnival mask_fa863c80-6688-5e38-86d5-9b3af912d125.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'plain-pointed-eye-mask-with-almond-openings'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('masquerade', 'eye', 'mask')

    def build(self):
        self.add_bezier('upper-left',(4,8),((12,14),(16,8),(24,18)))
        self.add_bezier('upper-right',(24,18),((32,8),(36,14),(44,8)))
        self.add_line('right-wall',(44,8),(44,28));self.add_arc('right-bowl',(44,28),(32,40),radius_x=12)
        self.add_bezier('nose-right',(32,40),((28,40),(26,37),(24,37)))
        self.add_bezier('nose-left',(24,37),((22,37),(20,40),(16,40)))
        self.add_arc('left-bowl',(16,40),(4,28),radius_x=12);self.add_line('left-wall',(4,28),(4,8))
        self.add_contour('mask','upper-left','upper-right','right-wall','right-bowl','nose-right','nose-left','left-bowl','left-wall',closed=True)
        for x in (16,32):self.circle(f'eye-{x}',x,28,3)

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
