"""Person in Spotlight.
Symbol plan: Standing person framed by two overhead lamps and slanted beams. VRECT_L (8,4)-(40,44) suits tall beams. human_ref/full_body_ref.png: radius4 head (24,22), torso at (24,34), exactly8 centerline/4 ink gap. No useful exact Lucide match. Mirrored lamps and pose; omit collar and simplify fixtures to rounded squares.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e4f80d5-c808-5baf-ac53-d434f977c74e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/movie celebrity_8e4f80d5-c808-5baf-ac53-d434f977c74e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-person-between-two-overhead-spotlights'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "entertainment"
    aliases = ()
    keywords = ('person', 'in', 'spotlight')

    def build(self):
        for n,l,r in [('left',8,16),('right',32,40)]:
         cx=(l+r)//2;self.rounded(n+'-lamp',l,4,r,12,2,nodes=((cx,12),))
         self.add_line(n+'-beam',(cx,12),(l if n=='left' else r,44));self.relate('connect',n+'-beam',n+'-lamp')
        self.circle('head',24,22,4)
        self.add_polyline('arms',(18,34),(24,34),(30,34))
        self.add_line('torso',(24,34),(24,38));self.relate('connect','torso','arms')
        self.add_polyline('legs',(18,44),(24,38),(30,44));self.relate('connect','legs','torso')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

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
