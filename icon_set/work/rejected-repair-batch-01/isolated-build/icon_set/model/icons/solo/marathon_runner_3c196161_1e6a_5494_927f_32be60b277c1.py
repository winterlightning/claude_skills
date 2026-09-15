"""Running Athlete, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='3c196161-1e6a-5494-927f-32be60b277c1'
SOURCE_PATH='pictographic-primitives/sports/sport marathon_3c196161-1e6a-5494-927f-32be60b277c1.svg'
AUTHOR='gpt-6'

class MarathonRunner(Solo48):
    icon_id='marathon-runner'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('running', 'runner', 'marathon', 'athlete', 'fitness', 'sport')
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
        self.add_polyline('arms',(6,26),(14,20),(23,22),(35,24),(42,18))
        self.add_line('torso',(23,22),(19,31))
        self.add_polyline('rear-leg',(19,31),(12,37),(6,37))
        self.add_polyline('front-leg',(19,31),(29,35),(30,42))
        for x,y in [('arms','torso'),('torso','rear-leg'),('torso','front-leg'),('rear-leg','front-leg')]:self.relate('connect',x,y)
