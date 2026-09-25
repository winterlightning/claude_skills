"""Electronic Diode Component.
Symbol plan: Diagonal axial diode with lower-left polarity band; intentional directional diagonal. SQUARE extremes (6,6)-(42,42). No useful Lucide subject match; coherent capsule and shared terminals.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'df3cec3b-cd40-4110-be54-9f249b9ee747'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/crystal diode_df3cec3b-cd40-4110-be54-9f249b9ee747.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diagonal-axial-diode-with-polarity-band'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "electronics"
    aliases = ()
    keywords = ('electronic', 'diode', 'component')

    def build(self):
        # Diagonal package owns side-band and lead nodes, all exact integer points.
        self.add_polyline('body',(12,28),(18,22),(28,12),(32,16),(36,20),(26,30),(20,36),(16,32),closed=True)
        self.add_line('lower-lead',(6,42),(16,32))
        self.add_line('upper-lead',(32,16),(42,6))
        self.add_line('band',(18,22),(26,30))
        for part in ('lower-lead','upper-lead','band'):self.relate('connect',part,'body')

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
