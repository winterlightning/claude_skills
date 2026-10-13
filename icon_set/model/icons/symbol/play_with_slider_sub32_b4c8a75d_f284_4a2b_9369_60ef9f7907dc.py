"""Independent 32px profile of play-with-slider.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'b4c8a75d-f284-4a2b-9369-60ef9f7907dc'
SOURCE_PATH = 'pictographic-primitives/symbol/play with slider_b4c8a75d-f284-4a2b-9369-60ef9f7907dc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b4c8a75d-f284-4a2b-9369-60ef9f7907dc', 'pictographic-primitives/symbol/play with slider_b4c8a75d-f284-4a2b-9369-60ef9f7907dc.svg'),)
PROFILE_SOURCE_KEYS = ('solo/play-with-slider',)
SOLO_SOURCE_ICON_IDS = ('play-with-slider',)
REFERENCE_EXPORT_SHA256 = '0c123b3d7c381f272c340168bda0515c3d5d4a29a179f9283c6d62b75bf88844'

class Drawing(Sub32):
    icon_id = 'play-with-slider-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (21, 25), (21, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 28), (30, 28))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (25, 12), (9, 2))
        self.add_line('p3-r1-2', (9, 2), (9, 21))
        self.add_line('p3-r1-3', (9, 21), (25, 12))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
