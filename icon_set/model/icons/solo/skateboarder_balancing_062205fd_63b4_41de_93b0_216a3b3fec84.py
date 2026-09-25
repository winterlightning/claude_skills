"""Skateboarder Balancing, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='062205fd-63b4-41de-93b0-216a3b3fec84'
SOURCE_PATH='pictographic-primitives/sports/skateboard person_062205fd-63b4-41de-93b0-216a3b3fec84.svg'
AUTHOR='gpt-6'

class SkateboarderBalancing(Solo48):
    icon_id='skateboarder-balancing'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases=()
    keywords=('skateboard', 'rider', 'skating', 'balance', 'athlete', 'sport')
    def build(self) -> None:
        # VRECT_L centerline extremes (8, 4, 40, 44) from current SOLO48 contract.
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(n+'-b',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def arc(n,a,b,r,ry=None,sweep=True):
            self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*pts):
            for i,(a,b) in enumerate(zip(pts,pts[1:]),1):self.add_line(f'{n}-{i}',a,b)
        axis=24
        def mirror(p):return (2*axis-p[0],p[1])
        circle('head',28,7,3)
        self.add_polyline('arms',(8,19),(25,19),(40,19))
        self.add_line('torso',(25,19),(21,27))
        self.relate('connect','arms','torso')
        self.add_polyline('front-leg',(21,27),(32,27),(28,36))
        self.relate('connect','torso','front-leg')
        self.add_polyline('back-leg',(21,27),(15,33),(8,33))
        self.relate('connect','torso','back-leg')
        self.relate('connect','front-leg','back-leg')
        self.add_polyline('deck',(20,36),(28,36),(38,36))
        self.relate('connect','deck','front-leg')
        for x in (23,35):self.add_dot(f'wheel-{x}',(x,44))
