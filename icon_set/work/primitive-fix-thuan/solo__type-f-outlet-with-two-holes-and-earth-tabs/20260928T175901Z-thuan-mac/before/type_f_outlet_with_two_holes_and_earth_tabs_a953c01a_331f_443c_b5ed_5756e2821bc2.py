"""Type F Electrical Power Outlet.
Symbol plan: Type F recess with two contacts and inward earth tabs. CIRCLE radius20 about (24,24). Drop secondary plate; split circle at cardinal attachment nodes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a953c01a-331f-443c-b5ed-5756e2821bc2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/power outlet type f_a953c01a-331f-443c-b5ed-5756e2821bc2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'type-f-outlet-with-two-holes-and-earth-tabs'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "electronics"
    categories = ("electronics", "primitives")
    aliases = ()
    keywords = ('type', 'f', 'electrical', 'power', 'outlet')

    def build(self):
        points=[(24,4),(44,24),(24,44),(4,24)]
        for i,p in enumerate(points):self.add_arc(f'rim-{i}',p,points[(i+1)%4],radius_x=20)
        self.add_contour('recess',*[f'rim-{i}' for i in range(4)],closed=True)
        for y,end in ((4,12),(44,36)):
         self.add_line(f'earth-{y}',(24,y),(24,end));self.relate('connect',f'earth-{y}','recess')
        for x in (16,32):self.circle(f'contact-{x}',x,24,2)

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
