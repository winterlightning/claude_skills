"""Running Athlete, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='308599f6-0b87-5e57-8523-c30eb5dd4e7a'
SOURCE_PATH='pictographic-primitives/sports/sport runner_308599f6-0b87-5e57-8523-c30eb5dd4e7a.svg'
AUTHOR='gpt-6'

class RunningAthlete(Solo48):
    icon_id='running-athlete'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('running', 'runner', 'athlete', 'fitness', 'stride', 'sport')
    def build(self) -> None:
        # SQUARE centerline extremes (6, 6, 42, 42) from current SOLO48 contract.
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
        circle('head',26,9,3)
        self.add_polyline('arms',(6,27),(12,19),(23,22),(36,22),(42,12))
        self.add_line('torso',(23,22),(20,32))
        self.add_polyline('rear-leg',(20,32),(12,38),(6,38))
        self.add_polyline('front-leg',(20,32),(28,36),(28,42))
        for x,y in [('arms','torso'),('torso','rear-leg'),('torso','front-leg'),('rear-leg','front-leg')]:self.relate('connect',x,y)
