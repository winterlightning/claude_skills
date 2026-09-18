"""Independent 32px profile of triangle-design.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'b4208180-348f-4efd-9c97-aa942b6924da'
SOURCE_PATH = 'pictographic-primitives/design/triangle_b4208180-348f-4efd-9c97-aa942b6924da.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b4208180-348f-4efd-9c97-aa942b6924da', 'pictographic-primitives/design/triangle_b4208180-348f-4efd-9c97-aa942b6924da.svg'),)
PROFILE_SOURCE_KEYS = ('solo/triangle-design',)
SOLO_SOURCE_ICON_IDS = ('triangle-design',)
REFERENCE_EXPORT_SHA256 = '6220560cf44654344678e49f637a322e41a26373ee3f3262a30d5b9f7a13c0e8'

class Drawing(Sub32):
    icon_id = 'triangle-design-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'design'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 27), (16, 5))
        self.add_line('p1-r1-2', (16, 5), (2, 27))
        self.add_line('p1-r1-3', (2, 27), (30, 27))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
