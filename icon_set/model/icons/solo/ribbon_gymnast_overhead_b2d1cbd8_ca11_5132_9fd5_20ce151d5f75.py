"""Ribbon gymnast overhead, authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='b2d1cbd8-ca11-5132-9fd5-20ce151d5f75'
SOURCE_PATH='pictographic-primitives/sports/rhythmic ribbon_b2d1cbd8-ca11-5132-9fd5-20ce151d5f75.svg'
AUTHOR='gpt-6'

class RibbonGymnastOverhead(Solo48):
    icon_id='ribbon-gymnast-overhead'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases=()
    keywords=('ribbon', 'gymnast', 'overhead')
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
        circle('head',25,18,3)
        self.add_polyline('body',(24,30),(29,32),(24,42))
        self.add_polyline('arms',(16,30),(24,30),(38,28))
        self.relate('connect','arms','body')
        self.add_polyline('leg-raised',(29,32),(35,36),(40,32))
        self.relate('connect','body','leg-raised')
        arc('ribbon-top',(6,18),(42,18),18,12)
        self.add_line('ribbon-wand',(38,28),(42,18))
        self.relate('connect','ribbon-wand','arms')
        self.relate('connect','ribbon-wand','ribbon-top')
        arc('ribbon-curl',(6,18),(12,18),3,3,sweep=False)
        self.relate('connect','ribbon-curl','ribbon-top')
