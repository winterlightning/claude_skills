"""Independent 32px profile of shuffle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '5d51dd05-eb69-498a-8a9c-a2c5b97155a3'
SOURCE_PATH = 'pictographic-primitives/interface-essential/shuffle_5d51dd05-eb69-498a-8a9c-a2c5b97155a3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5d51dd05-eb69-498a-8a9c-a2c5b97155a3', 'pictographic-primitives/interface-essential/shuffle_5d51dd05-eb69-498a-8a9c-a2c5b97155a3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/shuffle',)
SOLO_SOURCE_ICON_IDS = ('shuffle',)
REFERENCE_EXPORT_SHA256 = '4d4cda064f35bd92a8fa4554cd519de988943a959d495048a425bba869fa2ca0'

class Drawing(Sub32):
    icon_id = 'shuffle-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'interface-essential'
    categories = ('interface-essential', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (2, 25), ((9, 25), (11, 21), (16, 16)))
        self.add_bezier('p1-r1-2', (16, 16), ((21, 11), (23, 7), (30, 7)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_bezier('p2-r1-1', (2, 7), ((9, 7), (11, 11), (16, 16)))
        self.add_bezier('p2-r1-2', (16, 16), ((21, 21), (23, 25), (30, 25)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (25, 2), (30, 7))
        self.add_line('p3-r1-2', (30, 7), (25, 11))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (25, 21), (30, 25))
        self.add_line('p4-r1-2', (30, 25), (25, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-2')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-2')
        self.relate("connect", 'p1-r1-2', 'p3-r1-1')
        self.relate("connect", 'p1-r1-2', 'p3-r1-2')
        self.relate("connect", 'p2-r1-2', 'p4-r1-1')
        self.relate("connect", 'p2-r1-2', 'p4-r1-2')
