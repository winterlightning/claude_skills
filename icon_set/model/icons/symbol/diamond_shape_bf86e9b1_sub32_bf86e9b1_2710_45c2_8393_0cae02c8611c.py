"""Independent 32px profile of diamond-shape-bf86e9b1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'bf86e9b1-2710-45c2-8393-0cae02c8611c'
SOURCE_PATH = 'pictographic-primitives/design/diamond shape_bf86e9b1-2710-45c2-8393-0cae02c8611c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bf86e9b1-2710-45c2-8393-0cae02c8611c', 'pictographic-primitives/design/diamond shape_bf86e9b1-2710-45c2-8393-0cae02c8611c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/diamond-shape-bf86e9b1',)
SOLO_SOURCE_ICON_IDS = ('diamond-shape-bf86e9b1',)
REFERENCE_EXPORT_SHA256 = '75033c07866ee62642e2fcd438bb568e6b4d232642fd1e879f11a31ecf68e40b'

class Drawing(Sub32):
    icon_id = 'diamond-shape-bf86e9b1-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'design'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (2, 16))
        self.add_line('p1-r1-2', (2, 16), (16, 30))
        self.add_line('p1-r1-3', (16, 30), (30, 16))
        self.add_line('p1-r1-4', (30, 16), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
