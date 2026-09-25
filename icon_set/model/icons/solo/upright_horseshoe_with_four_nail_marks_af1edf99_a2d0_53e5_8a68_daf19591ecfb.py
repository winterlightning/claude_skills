"""Lucky Horseshoe Symbol.
Symbol plan: Broad upright horseshoe. VRECT_L (8,4)-(40,44) gives the U its upright proportions. Mirrored straight arms and concentric radius16/radius6 bottom arcs; no useful exact Lucide match. Omit four tiny nail marks and inward tip notches because the 10-unit bands cannot hold an interior stroke with the required clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'af1edf99-a2d0-53e5-8a68-daf19591ecfb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/casino lucky horseshoe_af1edf99-a2d0-53e5-8a68-daf19591ecfb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upright-horseshoe-with-four-nail-marks'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "entertainment"
    aliases = ()
    keywords = ('lucky', 'horseshoe', 'symbol')

    def build(self):
        self.add_polyline('left-tip',(8,28),(8,4),(18,4),(18,28))
        self.add_arc('inner',(18,28),(30,28),radius_x=6,sweep=False)
        self.add_polyline('right-tip',(30,28),(30,4),(40,4),(40,28))
        self.add_arc('outer',(40,28),(8,28),radius_x=16)
        self.contours.clear();self.add_contour('shoe',*[f'left-tip-{i}' for i in range(1,4)],'inner',*[f'right-tip-{i}' for i in range(1,4)],'outer',closed=True)

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
