"""Racing cyclist, authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='1cb7d2ba-c91a-4cd1-bd29-7ebbabf08914'
SOURCE_PATH='pictographic-primitives/sports/race_1cb7d2ba-c91a-4cd1-bd29-7ebbabf08914.svg'
AUTHOR='gpt-6'

class RacingCyclist(Solo48):
    icon_id='racing-cyclist'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('racing', 'cyclist')
    def build(self) -> None:
        # SQUARE centerline extremes (6, 6, 42, 42).
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(n+'-b',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def arc(n,a,b,r,ry=None,sweep=True):
            self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*pts):
            for i,(a,b) in enumerate(zip(pts,pts[1:]),1):self.add_line(f'{n}-{i}',a,b)
        circle('head',32,9,3)
        circle('wheel-rear',12,36,6)
        circle('wheel-front',36,36,6)
        self.add_polyline('rider',(25,18),(18,24),(25,29),(21,38))
        self.add_polyline('arms',(25,18),(30,24),(37,24))
        self.relate('connect','rider','arms')
        self.add_line('fork',(31,24),(36,36))
        self.relate('connect','fork','arms')
        self.relate('connect','fork','wheel-front')
        self.add_line('frame',(12,36),(18,24))
        self.relate('connect','frame','wheel-rear')
        self.relate('connect','frame','rider')
