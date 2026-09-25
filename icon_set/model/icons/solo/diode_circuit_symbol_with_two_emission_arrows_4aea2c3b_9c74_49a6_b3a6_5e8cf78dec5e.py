"""Light Emitting Diode Circuit Symbol.
Symbol plan: LED circuit diode and two emission arrows, intrinsic circuit notation. SQUARE extremes (6,6)-(42,42). No useful Lucide subject match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4aea2c3b-9c74-49a6-b3a6-5e8cf78dec5e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/light emitting diode_4aea2c3b-9c74-49a6-b3a6-5e8cf78dec5e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diode-circuit-symbol-with-two-emission-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "electronics"
    aliases = ()
    keywords = ('light', 'emitting', 'diode', 'circuit', 'symbol')

    def build(self):
        self.add_polyline('triangle',(14,22),(32,32),(14,42),(14,32),closed=True)
        self.add_line('input',(6,32),(14,32));self.relate('connect','input','triangle')
        self.add_polyline('bar',(32,22),(32,32),(32,42));self.relate('connect','bar','triangle')
        self.add_line('output',(32,32),(42,32));self.relate('connect','output','bar');self.relate('connect','output','triangle')
        for i,(x,y) in enumerate(((18,6),(34,6))):
         self.add_polyline(f'arrow-{i}',(x-6,y+6),(x,y),(x-6,y))
         self.add_line(f'arrow-tip-{i}',(x,y),(x,y+6));self.relate('connect',f'arrow-{i}',f'arrow-tip-{i}')

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
