"""Crouching snowboarder on a sloping board. Lucide accessibility informs articulated figure strokes. Raised arm, bent knees and board retained; no clothing detail added.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6bd421c1-b45f-42f7-bc55-f1a7d00409df'
SOURCE_PATH = 'pictographic-primitives/symbol/skiing_6bd421c1-b45f-42f7-bc55-f1a7d00409df.svg'
AUTHOR = 'gpt-6'


class Snowboarding(Solo48):
    icon_id = 'snowboarding'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('snowboarding', 'snowboard', 'winter', 'sport', 'snow', 'mountain', 'ride', 'extreme')

    def build(self) -> None:
        cx,cy,r=38,16,4

        self.add_arc('head-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc('head-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour('head','head-top','head-bottom',closed=True)

        self.add_polyline('leg-left',(26,22),(18,18),(12,34))
        self.add_polyline('leg-right',(26,22),(20,28),(26,32),(24,38))
        self.add_line('arm-raised',(22,6),(26,22))
        self.add_line('arm-front',(26,22),(32,29))
        parts=['leg-left','leg-right','arm-raised','arm-front']
        for i,a in enumerate(parts):
            for b in parts[i+1:]:self.relate('connect',a,b)
        self.add_polyline('board-run',(6,32),(12,34),(24,38),(30,40))
        self.add_arc('board-tip',(30,40),(42,40),radius_x=6,radius_y=2,sweep=False)
        self.relate('connect','board-run','board-tip')
        for part in ('leg-left','leg-right'):self.relate('connect',part,'board-run')
