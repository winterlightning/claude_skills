"""Electronic Microchip Processor.
Symbol plan: Twelve pins derived from three positions per edge, blank chip body. Lucide cpu: repeated edge pins and shared body junctions. VRECT_L extremes (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e1b60aee-63d4-4ea4-b4a7-720974c502f6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/integrated circuit_e1b60aee-63d4-4ea4-b4a7-720974c502f6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tall-rounded-microchip-with-twelve-pins'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/electronics"
    aliases = ()
    keywords = ('electronic', 'microchip', 'processor')

    def build(self):
        l,r,t,b=(12, 36, 10, 38)
        x0,x1,y0,y1=(8, 40, 4, 44)
        positions=(16,24,32)
        nodes=[(v,y) for v in positions for y in (t,b)]+[(x,v) for v in positions for x in (l,r)]
        self.rounded("body",l,t,r,b,3,nodes)
        for v in positions:
         for name,a,z in [('top',(v,t),(v,y0)),('bottom',(v,b),(v,y1)),('left',(l,v),(x0,v)),('right',(r,v),(x1,v))]:
          part=f'pin-{name}-{v}';self.add_line(part,a,z);self.relate('connect',part,'body')

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
