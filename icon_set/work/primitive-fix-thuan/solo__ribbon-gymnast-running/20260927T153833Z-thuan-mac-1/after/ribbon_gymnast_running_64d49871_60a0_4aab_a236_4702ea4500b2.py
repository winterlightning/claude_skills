"""Fresh revision of ribbon-gymnast-running.

Original and rejected SVG compared before drawing. The runner had stiff limbs and a detached squiggle; reposed the bent legs and connected the ribbon gesture.
"""
"""Ribbon gymnast running, authored on SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='64d49871-60a0-4aab-a236-4702ea4500b2'
SOURCE_PATH='pictographic-primitives/sports/ribbon person_64d49871-60a0-4aab-a236-4702ea4500b2.svg'
AUTHOR='gpt-6'

class RibbonGymnastRunning(Solo48):
    icon_id='ribbon-gymnast-running'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases=()
    keywords=('ribbon', 'gymnast', 'running')
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
        circle('head',30,9,3)
        self.add_polyline('arms',(14,24),(24,19),(32,24),(42,18))
        self.add_line('body',(24,19),(19,30))
        self.relate('connect','arms','body')
        self.add_polyline('front-leg',(19,30),(30,32),(36,42))
        self.add_polyline('back-leg',(19,30),(12,38),(6,34))
        self.relate('connect','body','front-leg')
        self.relate('connect','body','back-leg')
        self.relate('connect','front-leg','back-leg')
        arc('ribbon-a',(6,6),(12,12),6,sweep=False)
        arc('ribbon-b',(12,12),(18,6),6,sweep=True)
        self.add_contour('ribbon','ribbon-a','ribbon-b')
