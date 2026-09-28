"""Inline skate, authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='a010f79f-3ca0-5f51-8cbf-bd0c35154343'
SOURCE_PATH='pictographic-primitives/sports/rollerblades_a010f79f-3ca0-5f51-8cbf-bd0c35154343.svg'
AUTHOR='gpt-6'

class InlineSkate(Solo48):
    icon_id='inline-skate'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases=()
    keywords=('inline', 'skate')
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
        poly('boot-upper',(8,6),(22,6),(22,19),(34,19))
        arc('toe',(34,19),(34,27),8,4)
        self.add_line('sole',(34,27),(14,27))
        arc('heel',(14,27),(6,19),8)
        self.add_line('back',(6,19),(8,6))
        self.add_contour('boot','boot-upper-1','boot-upper-2','boot-upper-3','toe','sole','heel','back',closed=True)
        for x in (9,24,39):circle(f'wheel-{x}',x,39,3)
