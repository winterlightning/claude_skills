"""Independent 32px profile of sailboat-triangle-sail.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '6920feca-ba55-4c5c-8e6c-032c49ca2982'
SOURCE_PATH = 'pictographic-primitives/outdoors/sailing boat_6920feca-ba55-4c5c-8e6c-032c49ca2982.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6920feca-ba55-4c5c-8e6c-032c49ca2982', 'pictographic-primitives/outdoors/sailing boat_6920feca-ba55-4c5c-8e6c-032c49ca2982.svg'),)
PROFILE_SOURCE_KEYS = ('solo/sailboat-triangle-sail',)
SOLO_SOURCE_ICON_IDS = ('sailboat-triangle-sail',)
REFERENCE_EXPORT_SHA256 = 'f850253c460aa222eaddc613f2f9789730c2299eb7dd03edc4e7ecb23b8fb31b'

class Drawing(Sub32):
    icon_id = 'sailboat-triangle-sail-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'outdoors'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 16), (16, 5))
        self.add_line('p1-r1-2', (16, 5), (24, 16))
        self.add_line('p1-r1-3', (24, 16), (8, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (2, 22), (30, 22))
        self.add_line('p2-r1-2', (30, 22), (24, 27))
        self.add_line('p2-r1-3', (24, 27), (8, 27))
        self.add_line('p2-r1-4', (8, 27), (2, 22))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
