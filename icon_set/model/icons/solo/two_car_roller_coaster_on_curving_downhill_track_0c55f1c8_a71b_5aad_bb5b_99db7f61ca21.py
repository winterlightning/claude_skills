"""Roller Coaster Theme Park Ride.
Symbol plan: Two coupled coaster cars descend a curved supported track. SQUARE (6,6)-(42,42) spans cars and structure. Lucide roller-coaster informs coherent curved track and vertical supports. Shared rail attachment nodes. Omit wheels and rightmost support/base extension; descent is intentionally directional.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0c55f1c8-a71b-5aad-bb5b-99db7f61ca21'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/amusement park rollercoaster_0c55f1c8-a71b-5aad-bb5b-99db7f61ca21.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-car-roller-coaster-on-curving-downhill-track'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "entertainment"
    aliases = ()
    keywords = ('roller', 'coaster', 'theme', 'park', 'ride')

    def build(self):
        self.add_polyline('train',(10,16),(10,6),(18,6),(18,16),(22,20),(28,12),(36,18),(30,26))
        self.add_polyline('upper-left',(6,16),(10,16),(18,16),(22,20),(30,26))
        self.add_bezier('upper-right',(30,26),((34,29),(38,30),(42,30)))
        self.relate('connect','train','upper-left');self.relate('connect','upper-left','upper-right');self.relate('connect','train','upper-right')
        self.add_bezier('lower-left',(6,26),((12,26),(14,28),(20,30)))
        self.add_bezier('lower-right',(20,30),((28,34),(34,40),(42,40)))
        self.add_contour('lower-rail','lower-left','lower-right')
        self.add_polyline('supports',(6,26),(6,42),(20,42),(20,30));self.relate('connect','supports','lower-rail')

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
