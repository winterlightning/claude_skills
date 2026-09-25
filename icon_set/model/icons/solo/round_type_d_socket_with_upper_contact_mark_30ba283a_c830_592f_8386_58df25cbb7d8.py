"""Type D Power Socket.
Symbol plan: Type D circular face, lower round contacts and centered upper upright contact. CIRCLE radius20 at (24,24), matching round face. Shared circle construction; preserve all identity features.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30ba283a-c830-592f-8386-58df25cbb7d8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/power outlet type d_30ba283a-c830-592f-8386-58df25cbb7d8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-type-d-socket-with-upper-contact-mark'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "electronics"
    aliases = ()
    keywords = ('type', 'd', 'power', 'socket')

    def build(self):
        self.circle('face',24,24,20)
        for x in (16,32):self.circle(f'contact-{x}',x,28,2)
        self.add_line('upper-contact',(24,14),(24,18))

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
