"""Independent 32px profile of snowflake-holidays.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '34931aa4-2ff2-4490-a0da-404a030fd356'
SOURCE_PATH = 'pictographic-primitives/holidays/snowflake_34931aa4-2ff2-4490-a0da-404a030fd356.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('34931aa4-2ff2-4490-a0da-404a030fd356', 'pictographic-primitives/holidays/snowflake_34931aa4-2ff2-4490-a0da-404a030fd356.svg'),)
PROFILE_SOURCE_KEYS = ('solo/snowflake-holidays',)
SOLO_SOURCE_ICON_IDS = ('snowflake-holidays',)
REFERENCE_EXPORT_SHA256 = '47724b202bb6ad0617ec783d8734dc850c6c8f0bdf883c065e9f225fb20e6ad5'

class Drawing(Sub32):
    icon_id = 'snowflake-holidays-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'holidays'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (16, 8))
        self.add_line('p1-r1-2', (16, 8), (16, 16))
        self.add_line('p1-r1-3', (16, 16), (16, 24))
        self.add_line('p1-r1-4', (16, 24), (16, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (2, 8), (8, 12))
        self.add_line('p2-r1-2', (8, 12), (16, 16))
        self.add_line('p2-r1-3', (16, 16), (24, 20))
        self.add_line('p2-r1-4', (24, 20), (30, 24))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (2, 24), (8, 20))
        self.add_line('p3-r1-2', (8, 20), (16, 16))
        self.add_line('p3-r1-3', (16, 16), (24, 12))
        self.add_line('p3-r1-4', (24, 12), (30, 8))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (11, 4), (16, 8))
        self.add_line('p4-r1-2', (16, 8), (21, 4))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (11, 28), (16, 24))
        self.add_line('p5-r1-2', (16, 24), (21, 28))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p6-r1-1', (8, 6), (8, 12))
        self.add_line('p6-r1-2', (8, 12), (2, 14))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.add_line('p7-r1-1', (24, 26), (24, 20))
        self.add_line('p7-r1-2', (24, 20), (30, 18))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', closed=False)
        self.add_line('p8-r1-1', (2, 18), (8, 20))
        self.add_line('p8-r1-2', (8, 20), (8, 26))
        self.add_contour('path-8-1', 'p8-r1-1', 'p8-r1-2', closed=False)
        self.add_line('p9-r1-1', (30, 14), (24, 12))
        self.add_line('p9-r1-2', (24, 12), (24, 6))
        self.add_contour('path-9-1', 'p9-r1-1', 'p9-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p4-r1-1')
        self.relate("connect", 'p1-r1-1', 'p4-r1-2')
        self.relate("connect", 'p1-r1-2', 'p2-r1-2')
        self.relate("connect", 'p1-r1-2', 'p2-r1-3')
        self.relate("connect", 'p1-r1-2', 'p3-r1-2')
        self.relate("connect", 'p1-r1-2', 'p3-r1-3')
        self.relate("connect", 'p1-r1-2', 'p4-r1-1')
        self.relate("connect", 'p1-r1-2', 'p4-r1-2')
        self.relate("connect", 'p1-r1-3', 'p2-r1-2')
        self.relate("connect", 'p1-r1-3', 'p2-r1-3')
        self.relate("connect", 'p1-r1-3', 'p3-r1-2')
        self.relate("connect", 'p1-r1-3', 'p3-r1-3')
        self.relate("connect", 'p1-r1-3', 'p5-r1-1')
        self.relate("connect", 'p1-r1-3', 'p5-r1-2')
        self.relate("connect", 'p1-r1-4', 'p5-r1-1')
        self.relate("connect", 'p1-r1-4', 'p5-r1-2')
        self.relate("connect", 'p2-r1-1', 'p6-r1-1')
        self.relate("connect", 'p2-r1-1', 'p6-r1-2')
        self.relate("connect", 'p2-r1-2', 'p3-r1-2')
        self.relate("connect", 'p2-r1-2', 'p3-r1-3')
        self.relate("connect", 'p2-r1-2', 'p6-r1-1')
        self.relate("connect", 'p2-r1-2', 'p6-r1-2')
        self.relate("connect", 'p2-r1-3', 'p3-r1-2')
        self.relate("connect", 'p2-r1-3', 'p3-r1-3')
        self.relate("connect", 'p2-r1-3', 'p7-r1-1')
        self.relate("connect", 'p2-r1-3', 'p7-r1-2')
        self.relate("connect", 'p2-r1-4', 'p7-r1-1')
        self.relate("connect", 'p2-r1-4', 'p7-r1-2')
        self.relate("connect", 'p3-r1-1', 'p8-r1-1')
        self.relate("connect", 'p3-r1-1', 'p8-r1-2')
        self.relate("connect", 'p3-r1-2', 'p8-r1-1')
        self.relate("connect", 'p3-r1-2', 'p8-r1-2')
        self.relate("connect", 'p3-r1-3', 'p9-r1-1')
        self.relate("connect", 'p3-r1-3', 'p9-r1-2')
        self.relate("connect", 'p3-r1-4', 'p9-r1-1')
        self.relate("connect", 'p3-r1-4', 'p9-r1-2')
