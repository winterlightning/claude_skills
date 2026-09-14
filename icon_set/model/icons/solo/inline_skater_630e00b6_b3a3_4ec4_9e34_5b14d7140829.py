"""Inline skater, authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='630e00b6-b3a3-4ec4-9e34-5b14d7140829'
SOURCE_PATH='pictographic-primitives/sports/rollerblades person_630e00b6-b3a3-4ec4-9e34-5b14d7140829.svg'
AUTHOR='gpt-6'

class InlineSkater(Solo48):
    icon_id='inline-skater'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('inline', 'skater')
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
        circle('head',34,9,3)
        self.add_polyline('arms',(13,19),(25,19),(33,25),(42,25))
        self.add_polyline('torso',(25,19),(21,27),(30,30),(28,34))
        self.relate('connect','arms','torso')
        self.add_polyline('back-leg',(21,27),(13,29),(6,26))
        self.relate('connect','back-leg','torso')
        self.add_line('skate-front',(25,34),(33,34))
        self.relate('connect','torso','skate-front')
        for x in (25,33):self.add_dot(f'wheel-front-{x}',(x,42))
        self.add_dot('wheel-rear-a',(6,35))
        self.add_dot('wheel-rear-b',(14,39))
