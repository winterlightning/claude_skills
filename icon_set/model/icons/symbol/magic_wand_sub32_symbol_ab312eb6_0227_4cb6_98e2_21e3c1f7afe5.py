"""Independent 32px profile of magic-wand.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'ab312eb6-0227-4cb6-98e2-21e3c1f7afe5'
SOURCE_PATH = 'pictographic-primitives/design/magic wand_ab312eb6-0227-4cb6-98e2-21e3c1f7afe5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ab312eb6-0227-4cb6-98e2-21e3c1f7afe5', 'pictographic-primitives/design/magic wand_ab312eb6-0227-4cb6-98e2-21e3c1f7afe5.svg'),)
PROFILE_SOURCE_KEYS = ('solo/magic-wand',)
SOLO_SOURCE_ICON_IDS = ('magic-wand',)
REFERENCE_EXPORT_SHA256 = 'ee265d49bd247358be2a0adf22b122d777fa833e284d8e776b723f504fbca8dc'

class DrawingContainerSymbol(Sub32):
    icon_id = 'magic-wand-sub32-symbol'
    related_origin_icon_id = 'magic-wand-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/magic-wand-sub32'
    counterpart_icon_id = 'magic-wand-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'design'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (21, 2), (24, 8))
        self.add_line('p1-r1-2', (24, 8), (30, 8))
        self.add_line('p1-r1-3', (30, 8), (25, 13))
        self.add_line('p1-r1-4', (25, 13), (27, 21))
        self.add_line('p1-r1-5', (27, 21), (21, 16))
        self.add_line('p1-r1-6', (21, 16), (14, 21))
        self.add_line('p1-r1-7', (14, 21), (16, 13))
        self.add_line('p1-r1-8', (16, 13), (11, 8))
        self.add_line('p1-r1-9', (11, 8), (18, 8))
        self.add_line('p1-r1-10', (18, 8), (21, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (2, 30), (14, 21))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
        self.relate('connect', 'p1-r1-7', 'p2-r1-1')
