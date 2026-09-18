"""Independent 32px profile of shark-fin.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '32524ca1-aaf5-42f1-a415-bf402a062588'
SOURCE_PATH = 'pictographic-primitives/symbol/shark tail_32524ca1-aaf5-42f1-a415-bf402a062588.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('32524ca1-aaf5-42f1-a415-bf402a062588', 'pictographic-primitives/symbol/shark tail_32524ca1-aaf5-42f1-a415-bf402a062588.svg'),)
PROFILE_SOURCE_KEYS = ('solo/shark-fin',)
SOLO_SOURCE_ICON_IDS = ('shark-fin',)
REFERENCE_EXPORT_SHA256 = 'a857c54f327c5627c9825ed3b886540add1cc93234e4c9d1a137a3d496e200b4'

class Drawing(Sub32):
    icon_id = 'shark-fin-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (3, 17), ((7, 10), (13, 5), (20, 5)))
        self.add_bezier('p1-r1-2', (20, 5), ((20, 11), (24, 15), (30, 17)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (2, 24), (16, 24), radius_x=7, radius_y=3, large_arc=False, sweep=False)
        self.add_arc('p2-r1-2', (16, 24), (30, 24), radius_x=7, radius_y=3, large_arc=False, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
