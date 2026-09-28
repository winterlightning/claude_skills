"""Ribbon gymnast overhead, authored on SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='b2d1cbd8-ca11-5132-9fd5-20ce151d5f75'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ribbon-gymnast-overhead/20260927T155415Z-thuan-mac-1/reference/rhythmic ribbon_b2d1cbd8-ca11-5132-9fd5-20ce151d5f75.svg'
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
        circle('head',24,19,3)
        self.add_line('torso',(24,30),(26,34))
        self.mark_human_figure('gymnast',head='head',torso='torso',torso_junction='start')
        self.add_polyline('arms',(14,30),(24,30),(34,30),(40,22))
        self.relate('connect','arms','torso')
        self.add_polyline('leg-raised',(26,34),(17,39),(12,37))
        self.add_line('leg-down',(26,34),(30,42))
        self.relate('connect','torso','leg-raised')
        self.relate('connect','torso','leg-down')
        self.relate('connect','leg-raised','leg-down')
        arc('ribbon-top',(6,18),(42,18),18,12)
        self.add_line('ribbon-wand',(40,22),(42,18))
        self.relate('connect','ribbon-wand','arms')
        self.relate('connect','ribbon-wand','ribbon-top')
        arc('ribbon-curl',(6,18),(12,18),3,3,sweep=False)
        self.relate('connect','ribbon-curl','ribbon-top')
