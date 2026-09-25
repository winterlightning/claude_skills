"""Electronic Processor Microchip.
Symbol plan: Twelve pins derived from three positions per edge, blank chip body. Lucide cpu: repeated edge pins and shared body junctions. SQUARE extremes (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a4171ac5-96ea-59a5-9263-48975b13a0af'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/electronics/microchip board_a4171ac5-96ea-59a5-9263-48975b13a0af.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'square-microchip-with-twelve-straight-pins'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "electronics"
    aliases = ()
    keywords = ('electronic', 'processor', 'microchip')

    def build(self):
        l,r,t,b=(12, 36, 12, 36)
        x0,x1,y0,y1=(6, 42, 6, 42)
        positions=(16,24,32)
        nodes=[(v,y) for v in positions for y in (t,b)]+[(x,v) for v in positions for x in (l,r)]
        self.add_polyline("body",(l,t),*( (v,t) for v in positions),(r,t),*((r,v) for v in positions),(r,b),*((v,b) for v in reversed(positions)),(l,b),*((l,v) for v in reversed(positions)),closed=True)
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
