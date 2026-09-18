"""Independent 32px profile of arrow-dot-left.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '2ebf9acc-12df-4295-afb7-797830fc7f91'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow dot left_2ebf9acc-12df-4295-afb7-797830fc7f91.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2ebf9acc-12df-4295-afb7-797830fc7f91', 'pictographic-primitives/arrows/arrow dot left_2ebf9acc-12df-4295-afb7-797830fc7f91.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-dot-left',)
SOLO_SOURCE_ICON_IDS = ('arrow-dot-left',)
REFERENCE_EXPORT_SHA256 = 'bb53b6be13aba2b731adf2346e20696c0e42dc7ad0ad45ccccbf2b5829c9ce1f'

class Drawing(Sub32):
    icon_id = 'arrow-dot-left-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'arrows'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (13, 5), (2, 16))
        self.add_line('p1-r1-2', (2, 16), (13, 27))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (13, 16), (2, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (30, 16), (27, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (22, 16), (19, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
