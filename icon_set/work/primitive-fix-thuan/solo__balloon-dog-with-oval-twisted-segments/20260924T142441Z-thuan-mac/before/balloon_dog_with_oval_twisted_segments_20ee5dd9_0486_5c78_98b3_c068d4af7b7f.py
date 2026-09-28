"""Balloon Animal Dog.
Symbol plan: Left-facing balloon dog, connected inflated lobes and twist seams. HRECT_L (4,8)-(44,40) fits ear, muzzle, tail and two legs. No useful exact Lucide match. Shared radius4 rounds every balloon end; body/neck enlarged to avoid point-kissing loops.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '20ee5dd9-0486-5c78-98b3-c068d4af7b7f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/amusement park balloon_20ee5dd9-0486-5c78-98b3-c068d4af7b7f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'balloon-dog-with-oval-twisted-segments'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('balloon', 'animal', 'dog')

    def build(self):
        # A continuous inflated silhouette, with shared seams instead of touching loops.
        self.add_arc('ear-top',(14,12),(22,12),radius_x=4)
        self.add_polyline('neck-right',(22,12),(22,16),(22,20),(24,24))
        self.add_bezier('back',(24,24),((28,22),(30,22),(34,24)))
        self.add_bezier('tail-up',(34,24),((34,20),(36,18),(38,16)),((42,12),(44,12),(44,16)))
        self.add_bezier('tail-down',(44,16),((44,22),(42,24),(42,28)))
        self.add_bezier('rear-leg',(42,28),((44,30),(44,34),(44,36)))
        self.add_arc('rear-foot',(44,36),(36,36),radius_x=4)
        self.add_line('rear-inner',(36,36),(34,32))
        self.add_bezier('belly',(34,32),((30,34),(28,34),(24,32)))
        self.add_line('front-inner',(24,32),(24,36))
        self.add_arc('front-foot',(24,36),(16,36),radius_x=4)
        self.add_polyline('neck-left',(16,36),(16,24),(14,24),(8,24))
        self.add_arc('muzzle',(8,24),(8,16),radius_x=4)
        self.add_polyline('ear-left',(8,16),(14,16),(14,12))
        self.contours.clear()
        self.add_contour('silhouette','ear-top',*[f'neck-right-{i}' for i in range(1,4)],'back','tail-up','tail-down','rear-leg','rear-foot','rear-inner','belly','front-inner','front-foot',*[f'neck-left-{i}' for i in range(1,4)],'muzzle','ear-left-1','ear-left-2',closed=True)
        for name,a,z in [('muzzle-twist',(14,16),(14,24)),('neck-twist',(16,24),(24,24)),('front-twist',(24,24),(24,32)),('rear-twist',(34,24),(34,32)),('tail-twist',(34,24),(42,28))]:
         self.add_line(name,a,z);self.relate('connect',name,'silhouette')
        self.relate('connect','neck-twist','front-twist');self.relate('connect','rear-twist','tail-twist')

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
