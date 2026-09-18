"""Independent 32px profile of pen-diagonal.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'eaffe809-493c-4509-b0a8-2553b0147b83'
SOURCE_PATH = 'pictographic-primitives/symbol/pen_eaffe809-493c-4509-b0a8-2553b0147b83.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('eaffe809-493c-4509-b0a8-2553b0147b83', 'pictographic-primitives/symbol/pen_eaffe809-493c-4509-b0a8-2553b0147b83.svg'),)
PROFILE_SOURCE_KEYS = ('solo/pen-diagonal',)
SOLO_SOURCE_ICON_IDS = ('pen-diagonal',)
REFERENCE_EXPORT_SHA256 = 'cbffcea77879c84f94f12b843c037a08e9c443413f70a6097923778df139d800'

class Drawing(Sub32):
    icon_id = 'pen-diagonal-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (5, 22))
        self.add_line('p1-r1-2', (5, 22), (21, 7))
        self.add_line('p1-r1-3', (21, 7), (24, 4))
        self.add_line('p1-r1-4', (24, 4), (30, 10))
        self.add_line('p1-r1-5', (30, 10), (11, 28))
        self.add_line('p1-r1-6', (11, 28), (2, 30))
        self.add_line('p1-r1-7', (2, 30), (2, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_arc('p2-r1-1', (21, 7), (11, 7), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('p2-r1-2', (11, 7), (5, 13))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
