"""Treadmill Runner, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='3c5c4a6e-1312-467a-bde1-c8156f8fa37c'
SOURCE_PATH='pictographic-primitives/sports/sport runninng treadmill_3c5c4a6e-1312-467a-bde1-c8156f8fa37c.svg'
AUTHOR='gpt-6'

class TreadmillRunner(Solo48):
    icon_id='treadmill-runner'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('treadmill', 'runner', 'running', 'fitness', 'exercise', 'machine')
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
        circle('head',22,9,3)
        self.add_line('torso',(16,19),(14,29))
        self.add_polyline('arms',(10,24),(16,19),(24,25),(26,23))
        self.add_polyline('front-leg',(14,29),(24,34),(23,42))
        self.add_line('rear-leg',(14,29),(8,42))
        self.add_polyline('belt',(6,42),(8,42),(23,42),(42,42))
        self.add_line('stem',(39,17),(42,42))
        self.add_polyline('console',(34,17),(39,17),(42,12))
        for x,y in [('torso','arms'),('torso','front-leg'),('torso','rear-leg'),('front-leg','rear-leg'),('front-leg','belt'),('rear-leg','belt'),('stem','belt'),('stem','console')]:self.relate('connect',x,y)
