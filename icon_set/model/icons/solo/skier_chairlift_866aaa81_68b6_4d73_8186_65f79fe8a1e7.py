"""Skier on Chairlift, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='866aaa81-68b6-4d73-8186-65f79fe8a1e7'
SOURCE_PATH='pictographic-primitives/sports/skiing cable car_866aaa81-68b6-4d73-8186-65f79fe8a1e7.svg'
AUTHOR='gpt-6'

class SkierChairlift(Solo48):
    icon_id='skier-chairlift'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('ski', 'chairlift', 'skier', 'lift', 'snow', 'winter')
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
        circle('head',17,9,3)
        self.add_polyline('rider',(12,21),(14,32),(29,32),(33,38))
        self.add_polyline('arm',(12,21),(23,23),(32,23))
        self.relate('connect','rider','arm')
        self.add_polyline('suspension',(32,6),(32,16),(32,23))
        self.relate('connect','arm','suspension')
        self.add_line('seat',(6,32),(14,32))
        self.relate('connect','seat','rider')
        self.add_polyline('ski',(12,42),(33,38),(42,35))
        self.relate('connect','rider','ski')
