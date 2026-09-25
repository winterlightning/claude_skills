"""Racer raised arms, authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='ccdd0a46-c667-4e7a-8d4d-7666a4ba3ccd'
SOURCE_PATH='pictographic-primitives/sports/race_ccdd0a46-c667-4e7a-8d4d-7666a4ba3ccd.svg'
AUTHOR='gpt-6'

class RacerRaisedArms(Solo48):
    icon_id='racer-raised-arms'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    aliases=()
    keywords=('racer', 'raised', 'arms')
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
        circle('head',24,10,4)
        self.add_polyline('arms',(6,6),(11,20),(24,25),(37,20),(42,6))
        self.add_line('body',(24,25),(24,32))
        self.relate('connect','arms','body')
        self.add_polyline('legs',(16,42),(24,32),(32,42))
        self.relate('connect','body','legs')
        self.add_line('bike-left',(6,42),(8,31))
        self.add_line('bike-right',(42,42),(40,31))
