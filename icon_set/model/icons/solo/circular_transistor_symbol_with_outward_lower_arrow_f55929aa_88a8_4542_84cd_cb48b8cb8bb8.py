"""NPN Bipolar Junction Transistor Symbol.
Symbol plan: NPN transistor with outward emitter arrow and circular boundary. CIRCLE radius20 about (24,24). Intentional right-facing branches. No useful Lucide subject match.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f55929aa-88a8-4542-84cd-cb48b8cb8bb8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/npn bipolar transistor_f55929aa-88a8-4542-84cd-cb48b8cb8bb8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circular-transistor-symbol-with-outward-lower-arrow'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "electronics"
    categories = ("electronics", "primitives")
    aliases = ()
    keywords = ('npn', 'bipolar', 'junction', 'transistor', 'symbol')

    def build(self):
        self.circle('boundary',24,24,20)
        self.add_polyline('base',(18,14),(18,24),(18,34))
        self.add_line('input',(4,24),(18,24));self.relate('connect','input','boundary');self.relate('connect','input','base')
        self.add_line('collector',(18,24),(34,14));self.relate('connect','collector','base')
        self.add_line('emitter',(18,24),(34,34));self.relate('connect','emitter','base');self.relate('connect','emitter','collector')
        self.add_polyline('arrow',(26,34),(34,34),(34,26));self.relate('connect','arrow','emitter')

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
