"""Ribbon gymnast circle, authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='f8bb3c70-137a-40bf-96f2-7de841464ca6'
SOURCE_PATH='pictographic-primitives/sports/ribbon person_f8bb3c70-137a-40bf-96f2-7de841464ca6.svg'
AUTHOR='gpt-6'

class RibbonGymnastCircle(Solo48):
    icon_id='ribbon-gymnast-circle'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('ribbon', 'gymnast', 'circle')
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
        circle('head',24,18,3)
        self.add_polyline('arms',(6,24),(12,28),(24,30),(34,35))
        self.add_line('torso',(24,30),(24,34))
        self.relate('connect','arms','torso')
        self.add_polyline('legs',(18,42),(24,34),(34,42))
        self.relate('connect','torso','legs')
        arc('ribbon-top',(6,24),(42,24),18,18)
        self.add_line('wand',(34,35),(42,24))
        self.relate('connect','wand','arms')
        self.relate('connect','wand','ribbon-top')
        self.relate('connect','arms','ribbon-top')
