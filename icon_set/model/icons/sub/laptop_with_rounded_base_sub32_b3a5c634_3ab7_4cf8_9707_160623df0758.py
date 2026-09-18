"""Independent 32px profile of laptop-with-rounded-base.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'b3a5c634-3ab7-4cf8-9707-160623df0758'
SOURCE_PATH = 'pictographic-primitives/computers/batch-03/laptop_b3a5c634-3ab7-4cf8-9707-160623df0758.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b3a5c634-3ab7-4cf8-9707-160623df0758', 'pictographic-primitives/computers/batch-03/laptop_b3a5c634-3ab7-4cf8-9707-160623df0758.svg'), ('f99926f6-12c0-4ba6-aff3-e7bf08c23a81', 'pictographic-primitives/computers/batch-03/laptop_f99926f6-12c0-4ba6-aff3-e7bf08c23a81.svg'))
PROFILE_SOURCE_KEYS = ('solo/laptop-with-rounded-base',)
SOLO_SOURCE_ICON_IDS = ('laptop-with-rounded-base',)
REFERENCE_EXPORT_SHA256 = '075b9a342b75464a6f337a52bb11e757968334c1b3fc02351d60afa626ae1999'

class Drawing(Sub32):
    icon_id = 'laptop-with-rounded-base-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/device'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (3, 21), (3, 8))
        self.add_arc('p1-r1-2', (3, 8), (7, 5), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (7, 5), (25, 5))
        self.add_arc('p1-r1-4', (25, 5), (29, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (29, 8), (29, 21))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (2, 21), (3, 21))
        self.add_line('p2-r1-2', (3, 21), (29, 21))
        self.add_line('p2-r1-3', (29, 21), (30, 21))
        self.add_line('p2-r1-4', (30, 21), (30, 22))
        self.add_arc('p2-r1-5', (30, 22), (26, 27), radius_x=4, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p2-r1-6', (26, 27), (6, 27))
        self.add_arc('p2-r1-7', (6, 27), (2, 22), radius_x=4, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p2-r1-8', (2, 22), (2, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-2')
        self.relate("connect", 'p1-r1-5', 'p2-r1-2')
        self.relate("connect", 'p1-r1-5', 'p2-r1-3')
