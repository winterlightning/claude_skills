"""A blank baby portrait with curled hair, ear bumps and broad shoulders; Lucide baby informs the continuous face contour."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '454b702c-a035-5fa0-a3ec-ac065587fca8'
SOURCE_PATH = 'pictographic-primitives/babies/baby_454b702c-a035-5fa0-a3ec-ac065587fca8.svg'
AUTHOR = 'gpt-6'


class BabyHead(Solo48):
    icon_id = 'baby-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/babies"
    aliases = ()
    keywords = ('baby', 'head', 'infant', 'nursery')

    def build(self) -> None:
        # Centerline extremes: (2,2)-(46,46).
        self.add_arc('crown-left', (10, 17), (24, 6), radius_x=14, radius_y=11, sweep=True, large_arc=False)
        self.add_arc('curl-up', (24, 6), (32, 6), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('curl-down', (32, 6), (24, 14), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('crown-right', (31, 10), (38, 17), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('upper-cheek-right', (38, 17), (40, 23), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('ear-right', (40, 23), (40, 29), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('jaw-right', (40,29), (36,36), radius_x=16, radius_y=11)
        self.add_arc('jaw-bottom', (36,36), (12,36), radius_x=12, radius_y=4)
        self.add_arc('jaw-left', (12,36), (8,29), radius_x=16, radius_y=11)
        self.add_arc('ear-left', (8, 29), (8, 23), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('upper-cheek-left', (8, 23), (10, 17), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_contour('face', 'crown-right', 'upper-cheek-right', 'ear-right', 'jaw-right', 'jaw-bottom', 'jaw-left', 'ear-left', 'upper-cheek-left', 'crown-left', 'curl-up', 'curl-down', closed=False)
        self.add_arc('shoulder-left', (12, 36), (2, 46), radius_x=10, radius_y=10, sweep=False, large_arc=False)
        self.add_arc('shoulder-right', (46, 46), (36, 36), radius_x=10, radius_y=10, sweep=False, large_arc=False)
        self.relate("connect", 'face', 'shoulder-left')
        self.relate("connect", 'face', 'shoulder-right')
