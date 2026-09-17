"""Amusement Park Carousel Horse.
Symbol plan: Carousel horse below triangular canopy, mounted on a pole offset two units left for muzzle clearance. VRECT_L (8,4)-(40,44) gives vertical room. No useful Lucide horse match. Reduce legs to bent strokes and omit eye; retain head, muzzle, tail and canopy.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b951d0e4-79bf-546b-b5b2-2b4ef11ec445'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/amusement park merry go round toys_b951d0e4-79bf-546b-b5b2-2b4ef11ec445.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'carousel-horse-on-pole-beneath-triangular-canopy'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('amusement', 'park', 'carousel', 'horse')

    def build(self):
        self.add_polyline('canopy',(8,14),(24,4),(40,14),(22,14),closed=True)
        self.add_polyline('back-neck',(14,28),(22,28),(30,28),(30,22),(34,22))
        self.add_arc('muzzle-curve',(34,22),(40,28),radius_x=6)
        self.add_polyline('chest-belly',(40,28),(40,32),(36,32),(34,36),(22,36),(18,36),(12,36),(12,32),(14,28))
        self.contours=[c for c in self.contours if c.contour_id not in ('back-neck','chest-belly')]
        self.add_contour('horse',*[f'back-neck-{i}' for i in range(1,5)],'muzzle-curve',*[f'chest-belly-{i}' for i in range(1,9)],closed=True)
        self.add_polyline('rear-leg',(12,36),(8,42),(12,44));self.relate('connect','rear-leg','horse')
        self.add_polyline('front-leg',(34,36),(38,44));self.relate('connect','front-leg','horse')
        self.add_line('tail',(14,28),(8,24));self.relate('connect','tail','horse')
        self.add_line('pole-top',(22,14),(22,28));self.relate('connect','pole-top','canopy');self.relate('connect','pole-top','horse')
        self.add_line('pole-bottom',(22,36),(22,44));self.relate('connect','pole-bottom','horse')

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
