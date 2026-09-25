"""Pigeon Carrying An Envelope.
Symbol plan: Right-facing pigeon carrying a letter, one natural subject. HRECT_L (4,8)-(44,40) spans wing, tail and envelope. Lucide bird: smooth raised head and swept silhouette. Omit eye and feather subdivisions to retain letter space.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd570b3c7-a434-5f91-872a-6af799463d20'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/emails/envelope pigeon_d570b3c7-a434-5f91-872a-6af799463d20.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'right-facing-pigeon-carrying-front-envelope'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "emails"
    aliases = ()
    keywords = ('pigeon', 'carrying', 'an', 'envelope')

    def build(self):
        self.add_bezier('back',(4,16),((10,19),(14,22),(18,22)),((25,22),(22,8),(32,8)))
        self.add_arc('head',(32,8),(38,14),radius_x=6)
        self.add_polyline('beak-neck',(38,14),(44,16),(36,18),(36,26))
        self.add_bezier('belly',(22,36),((20,36),(18,36),(16,36)))
        self.add_polyline('tail',(16,36),(8,40),(4,32),(12,28))
        self.add_bezier('wing',(12,28),((6,28),(4,22),(4,16)))
        self.add_contour('upper','back','head',*[f'beak-neck-{i}' for i in range(1,4)])
        self.contours=[c for c in self.contours if c.contour_id not in ('beak-neck','tail')]
        self.add_contour('lower','belly',*[f'tail-{i}' for i in range(1,4)],'wing')
        self.relate('connect','upper','lower')
        self.add_polyline('letter',(22,26),(36,26),(44,26),(44,40),(22,40),(22,36),closed=True)
        self.add_polyline('flap',(22,26),(33,34),(44,26));self.relate('connect','flap','letter')
        self.relate('connect','letter','upper');self.relate('connect','letter','lower')

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
