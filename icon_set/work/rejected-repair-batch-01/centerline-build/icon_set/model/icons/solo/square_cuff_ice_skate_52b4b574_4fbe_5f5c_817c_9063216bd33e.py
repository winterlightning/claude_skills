"""Ice Skate Boot, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='52b4b574-4fbe-5f5c-817c-9063216bd33e'
SOURCE_PATH='pictographic-primitives/sports/skiing ice skates_52b4b574-4fbe-5f5c-817c-9063216bd33e.svg'
AUTHOR='gpt-6'

class SquareCuffIceSkate(Solo48):
    icon_id='square-cuff-ice-skate'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
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
        poly('upper',(6,6),(22,6),(22,18),(34,22))
        arc('toe',(34,22),(34,30),8,4)
        poly('sole',(34,30),(30,30),(14,30),(6,30),(6,6))
        self.add_contour('boot','upper-1','upper-2','upper-3','toe','sole-1','sole-2','sole-3','sole-4',closed=True)
        for x in (14,30):
            self.add_line(f'mount-{x}',(x,30),(x,42))
            self.relate('connect',f'mount-{x}','boot')
        self.add_polyline('blade',(6,42),(14,42),(30,42),(36,42))
        arc('tip',(36,42),(42,36),6,sweep=False)
        self.relate('connect','tip','blade')
        for x in (14,30):self.relate('connect',f'mount-{x}','blade')
