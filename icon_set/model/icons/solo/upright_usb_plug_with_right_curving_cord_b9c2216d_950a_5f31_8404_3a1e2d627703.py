"""USB Plug Connector Cable.
Symbol plan: USB plug and right-curving cord. VRECT_L (8,4)-(40,44) suits upright housing and cable. Lucide plug/cable: attached tip and tangent rounded base/cord. Rightward tail is intentional.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b9c2216d-950a-5f31-8404-3a1e2d627703'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/usb cable_b9c2216d-950a-5f31-8404-3a1e2d627703.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upright-usb-plug-with-right-curving-cord'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "electronics"
    aliases = ()
    keywords = ('usb', 'plug', 'connector', 'cable')

    def build(self):
        self.add_polyline('housing-top',(8,20),(8,14),(12,14),(28,14),(32,14),(32,20))
        self.add_arc('base-right',(32,20),(20,32),radius_x=12)
        self.add_arc('base-left',(20,32),(8,20),radius_x=12)
        self.contours.clear()
        self.add_contour('housing',*[f'housing-top-{i}' for i in range(1,6)],'base-right','base-left',closed=True)
        self.add_polyline('tip',(12,14),(12,4),(28,4),(28,14));self.relate('connect','tip','housing')
        self.add_line('cord-start',(20,32),(20,36))
        self.add_arc('cord-bend',(20,36),(28,44),radius_x=8,sweep=False)
        self.add_line('cord-end',(28,44),(40,44));self.add_contour('cord','cord-start','cord-bend','cord-end')
        self.relate('connect','cord','housing')

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
