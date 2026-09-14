"""Snowboard Jump, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='b8a4c620-274c-490b-adc6-1f6dfce51d92'
SOURCE_PATH='pictographic-primitives/sports/snowskating_b8a4c620-274c-490b-adc6-1f6dfce51d92.svg'
AUTHOR='gpt-6'

class SnowboardJump(Solo48):
    icon_id='snowboard-jump'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('snowboard', 'jump', 'board', 'snow', 'winter', 'athlete')
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
        circle('head',25,9,3)
        self.add_polyline('arms',(6,17),(23,23),(42,15))
        self.add_polyline('torso',(23,23),(19,28),(26,31),(24,37))
        self.relate('connect','arms','torso')
        self.add_polyline('rear-leg',(19,28),(12,35),(14,42))
        self.relate('connect','torso','rear-leg')
        self.add_polyline('board',(6,42),(14,42),(24,37),(40,29))
        self.relate('connect','board','torso')
        self.relate('connect','board','rear-leg')
