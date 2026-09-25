"""Sprinter, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='75e49329-7c83-5e90-acf4-a0bb56f6af09'
SOURCE_PATH='pictographic-primitives/sports/sprinting running_75e49329-7c83-5e90-acf4-a0bb56f6af09.svg'
AUTHOR='gpt-6'

class Sprinter(Solo48):
    icon_id='sprinter'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    aliases=()
    keywords=('sprint', 'runner', 'running', 'athlete', 'speed', 'sport')
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
        def wave(n,y):
            for i,x in enumerate((6,18,30)):
                arc(f'{n}-{i}',(x,y),(x+12,y),6,2,sweep=i%2==0)
            self.add_contour(n,*[f'{n}-{i}' for i in range(3)])
        axis=24
        def mirror(p):return (2*axis-p[0],p[1])
        circle('head',20,9,3)
        self.add_polyline('arms',(6,17),(13,24),(25,20),(32,18),(37,24))
        self.add_polyline('body',(25,20),(29,30),(36,38),(42,40))
        self.add_polyline('front-leg',(29,30),(17,33),(23,42))
        self.relate('connect','body','arms')
        self.relate('connect','body','front-leg')
