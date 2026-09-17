"""Ring Toss Game.
Symbol plan: Ring toss with raised ring around peg and incoming motion. SQUARE (6,6)-(42,42) spans base and flight arc. No useful exact Lucide match. Shared rim nodes show peg occlusion. Reduce three motion strokes to one and oval base to a baseline for clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ad81a96-997b-4bb3-a30a-af2bd535e7fe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/ting toss_4ad81a96-997b-4bb3-a30a-af2bd535e7fe.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ring-toss-with-flying-ring-and-motion-arcs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('ring', 'toss', 'game')

    def build(self):
        self.add_bezier('ring-left',(18,20),((10,20),(6,22),(6,26)),((6,30),(10,32),(18,32)))
        self.add_bezier('ring-right',(18,32),((26,32),(30,30),(30,26)),((30,22),(26,20),(18,20)))
        self.add_contour('ring','ring-left','ring-right',closed=True)
        self.add_line('peg-top',(18,12),(18,20));self.relate('connect','peg-top','ring')
        self.add_line('peg-bottom',(18,32),(18,42));self.relate('connect','peg-bottom','ring')
        self.add_polyline('base',(6,42),(18,42),(30,42));self.relate('connect','base','peg-bottom')
        self.add_bezier('flight',(42,6),((36,6),(32,10),(30,14)))

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
