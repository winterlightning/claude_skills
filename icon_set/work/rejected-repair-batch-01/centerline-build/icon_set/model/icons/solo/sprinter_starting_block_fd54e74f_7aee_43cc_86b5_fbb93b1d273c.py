"""Sprinter starting block, authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='fd54e74f-7aee-43cc-86b5-fbb93b1d273c'
SOURCE_PATH='pictographic-primitives/sports/running ready starting block_fd54e74f-7aee-43cc-86b5-fbb93b1d273c.svg'
AUTHOR='gpt-6'

class SprinterStartingBlock(Solo48):
    icon_id='sprinter-starting-block'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/sports'
    aliases=()
    keywords=('sprinter', 'starting', 'block')
    def build(self) -> None:
        # HRECT_L centerline extremes (4, 8, 44, 40).
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x,y-r),(x,y+r),radius_x=r)
            self.add_arc(n+'-b',(x,y+r),(x,y-r),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def arc(n,a,b,r,ry=None,sweep=True):
            self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*pts):
            for i,(a,b) in enumerate(zip(pts,pts[1:]),1):self.add_line(f'{n}-{i}',a,b)
        self.add_polyline('leg',(24,8),(35,15),(39,20),(30,34),(23,40))
        self.add_polyline('shoe',(4,15),(11,21),(13,31),(9,37),(13,40),(23,40))
        self.relate('connect','shoe','leg')
        self.add_polyline('block',(23,40),(39,29),(44,40),closed=True)
        self.relate('connect','block','leg')
        self.relate('connect','block','shoe')
        self.add_line('ground',(4,40),(13,40))
        self.relate('connect','ground','shoe')
