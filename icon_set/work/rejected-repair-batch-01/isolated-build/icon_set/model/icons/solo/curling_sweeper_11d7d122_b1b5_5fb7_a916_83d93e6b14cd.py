"""Curling Sweeper, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='11d7d122-b1b5-5fb7-a916-83d93e6b14cd'
SOURCE_PATH='pictographic-primitives/sports/sport curling_11d7d122-b1b5-5fb7-a916-83d93e6b14cd.svg'
AUTHOR='gpt-6'

class CurlingSweeper(Solo48):
    icon_id='curling-sweeper'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('curling', 'sweeper', 'broom', 'athlete', 'ice', 'sport')
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
        circle('head',23,9,3)
        self.add_line('torso',(25,20),(24,28))
        self.add_line('arm',(25,20),(15,25))
        self.add_line('broom-shaft',(15,25),(11,34))
        arc('broom-a',(11,34),(11,42),5,4)
        arc('broom-b',(11,42),(11,34),5,4)
        self.add_contour('broom','broom-a','broom-b',closed=True)
        self.add_polyline('front-leg',(24,28),(30,35),(27,42))
        self.add_line('rear-leg',(24,28),(42,40))
        for x,y in [('torso','arm'),('arm','broom-shaft'),('broom','broom-shaft'),('torso','front-leg'),('torso','rear-leg'),('front-leg','rear-leg')]:self.relate('connect',x,y)
