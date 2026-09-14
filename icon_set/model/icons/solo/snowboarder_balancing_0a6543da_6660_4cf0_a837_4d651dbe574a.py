"""Snowboarder Balancing, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='0a6543da-6660-4cf0-a837-4d651dbe574a'
SOURCE_PATH='pictographic-primitives/sports/skiing board slide_0a6543da-6660-4cf0-a837-4d651dbe574a.svg'
AUTHOR='gpt-6'

class SnowboarderBalancing(Solo48):
    icon_id='snowboarder-balancing'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('snowboard', 'rider', 'snow', 'winter', 'balance', 'sport')
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
        circle('head',28,9,3)
        self.add_polyline('arms',(6,6),(11,17),(24,22),(40,30))
        self.add_line('torso',(24,22),(19,29))
        self.relate('connect','torso','arms')
        self.add_polyline('leg-left',(19,29),(12,31),(12,36))
        self.add_polyline('leg-right',(19,29),(30,32),(30,40))
        self.relate('connect','torso','leg-left')
        self.relate('connect','torso','leg-right')
        self.relate('connect','leg-left','leg-right')
        self.add_polyline('board',(6,32),(8,35),(12,36),(30,40),(38,42),(42,37))
        self.relate('connect','board','leg-left')
        self.relate('connect','board','leg-right')
