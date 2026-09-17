"""Electronic Circuit Fuse Component.
Symbol plan: Axial fuse with symmetric broad endcaps and narrow tube. HRECT_M extremes (4,10)-(44,38). Lucide plug: rounded housing and attached leads.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '19059222-8a90-50b8-a216-cc1d758bf898'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/electronics fuse_19059222-8a90-50b8-a216-cc1d758bf898.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'horizontal-axial-fuse-with-rounded-end-caps'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/electronics"
    aliases = ()
    keywords = ('electronic', 'circuit', 'fuse', 'component')

    def build(self):
        for side,l,r,seam in [('left',8,16,16),('right',32,40,32)]:
         self.rounded(side,l,10,r,38,2,nodes=((l,24),(r,24),(seam,18),(seam,30)))
         self.add_line(side+'-wire',(l if side=='left' else r,24),(4 if side=='left' else 44,24))
         self.relate('connect',side+'-wire',side)
        for y in (18,30):
         self.add_line(f'tube-{y}',(16,y),(32,y))
         for side in ('left','right'):self.relate('connect',f'tube-{y}',side)

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
