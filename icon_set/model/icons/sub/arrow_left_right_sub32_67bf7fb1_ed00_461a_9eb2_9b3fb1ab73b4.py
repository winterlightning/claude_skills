"""Independent 32px profile of arrow-left-right.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '67bf7fb1-ed00-461a-9eb2-9b3fb1ab73b4'
SOURCE_PATH = 'pictographic-primitives/symbol/arrows left right_67bf7fb1-ed00-461a-9eb2-9b3fb1ab73b4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('67bf7fb1-ed00-461a-9eb2-9b3fb1ab73b4', 'pictographic-primitives/symbol/arrows left right_67bf7fb1-ed00-461a-9eb2-9b3fb1ab73b4.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-left-right',)
SOLO_SOURCE_ICON_IDS = ('arrow-left-right',)
REFERENCE_EXPORT_SHA256 = 'e22dee4c20c77656e074453489d22ac2e44d62e6403cac79fe5624d88afcc050'

class Drawing(Sub32):
    icon_id = 'arrow-left-right-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (13, 5), (2, 16))
        self.add_line('p1-r1-2', (2, 16), (13, 27))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (19, 5), (30, 16))
        self.add_line('p2-r1-2', (30, 16), (19, 27))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (2, 16), (30, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p3-r1-1')
        self.relate("connect", 'p1-r1-2', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
