"""Independent 32px profile of paragraph-two-column.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'ae53c84e-ee3a-4727-8ba4-a655774e41c6'
SOURCE_PATH = 'pictographic-primitives/interface-essential/paragraph two column_ae53c84e-ee3a-4727-8ba4-a655774e41c6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ae53c84e-ee3a-4727-8ba4-a655774e41c6', 'pictographic-primitives/interface-essential/paragraph two column_ae53c84e-ee3a-4727-8ba4-a655774e41c6.svg'),)
PROFILE_SOURCE_KEYS = ('solo/paragraph-two-column',)
SOLO_SOURCE_ICON_IDS = ('paragraph-two-column',)
REFERENCE_EXPORT_SHA256 = '01902d2a701dd293a50bfcd1d8d25aea94b8ffa0eca1a4442fe275e3d970ccf9'

class Drawing(Sub32):
    icon_id = 'paragraph-two-column-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 16), (13, 16))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (20, 16), (30, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 5), (13, 5))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (20, 5), (30, 5))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 27), (13, 27))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (20, 27), (30, 27))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
