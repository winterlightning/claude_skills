"""Reclining person on a curved sled. Lucide accessibility informs articulated strokes and detached head; raised legs and leaning arm retain the source pose.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd6bf82b5-b45d-4650-80db-680bfbec97fe'
SOURCE_PATH = 'pictographic-primitives/symbol/snow slide_d6bf82b5-b45d-4650-80db-680bfbec97fe.svg'
AUTHOR = 'gpt-6'


class SleddingPerson(Solo48):
    icon_id = 'sledding-person'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('sledding', 'toboggan', 'luge', 'winter', 'snow', 'slide', 'sport', 'sled')

    def build(self) -> None:
        cx,cy,r=37,18,5

        self.add_arc('head-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc('head-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour('head','head-top','head-bottom',closed=True)

        self.add_polyline('body',(12,6),(15,16),(24,24))
        self.add_line('arm',(22,10),(24,24))
        self.relate('connect','body','arm')
        self.add_line('sled-run',(6,26),(28,40))
        self.add_arc('sled-curve',(28,40),(42,40),radius_x=7,radius_y=2,sweep=False)
        self.add_contour('sled','sled-run','sled-curve')
