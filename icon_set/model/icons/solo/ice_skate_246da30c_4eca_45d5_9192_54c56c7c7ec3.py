"""Ice Skate Boot, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='246da30c-4eca-45d5-9192-54c56c7c7ec3'
SOURCE_PATH='pictographic-primitives/sports/skating shoes_246da30c-4eca-45d5-9192-54c56c7c7ec3.svg'
AUTHOR='gpt-6'

class IceSkate(Solo48):
    icon_id='ice-skate'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'sports'
    categories = ('sports', 'primitives')
    aliases=()
    keywords=('ice', 'skate', 'boot', 'blade', 'skating', 'winter')
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
        poly('upper',(6,12),(20,6),(20,19),(32,19))
        arc('toe',(32,19),(32,29),10,5)
        poly('sole',(32,29),(30,29),(14,29),(6,29),(6,12))
        self.add_contour('boot','upper-1','upper-2','upper-3','toe','sole-1','sole-2','sole-3','sole-4',closed=True)
        for x in (14,30):
            self.add_line(f'support-{x}',(x,29),(x,42))
            self.relate('connect',f'support-{x}','boot')
        self.add_polyline('blade',(6,42),(14,42),(30,42),(36,42))
        arc('blade-tip',(36,42),(42,36),6,sweep=False)
        self.relate('connect','blade','blade-tip')
        for x in (14,30):self.relate('connect',f'support-{x}','blade')
