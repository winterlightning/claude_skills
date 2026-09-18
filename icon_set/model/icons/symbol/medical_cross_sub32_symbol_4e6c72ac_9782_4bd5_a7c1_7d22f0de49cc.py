"""Independent 32px profile of medical-cross.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '4e6c72ac-9782-4bd5-a7c1-7d22f0de49cc'
SOURCE_PATH = 'pictographic-primitives/health/medical cross_4e6c72ac-9782-4bd5-a7c1-7d22f0de49cc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4e6c72ac-9782-4bd5-a7c1-7d22f0de49cc', 'pictographic-primitives/health/medical cross_4e6c72ac-9782-4bd5-a7c1-7d22f0de49cc.svg'),)
PROFILE_SOURCE_KEYS = ('solo/medical-cross',)
SOLO_SOURCE_ICON_IDS = ('medical-cross',)
REFERENCE_EXPORT_SHA256 = '267c8c921a2432b95229f741523e5ca83b9eb18ed40dcf09d1122be401f343d6'

class DrawingContainerSymbol(Sub32):
    icon_id = 'medical-cross-sub32-symbol'
    related_origin_icon_id = 'medical-cross-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/medical-cross-sub32'
    counterpart_icon_id = 'medical-cross-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'health'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (11, 2), (21, 2))
        self.add_line('p1-r1-2', (21, 2), (21, 11))
        self.add_line('p1-r1-3', (21, 11), (30, 11))
        self.add_line('p1-r1-4', (30, 11), (30, 21))
        self.add_line('p1-r1-5', (30, 21), (21, 21))
        self.add_line('p1-r1-6', (21, 21), (21, 30))
        self.add_line('p1-r1-7', (21, 30), (11, 30))
        self.add_line('p1-r1-8', (11, 30), (11, 21))
        self.add_line('p1-r1-9', (11, 21), (2, 21))
        self.add_line('p1-r1-10', (2, 21), (2, 11))
        self.add_line('p1-r1-11', (2, 11), (11, 11))
        self.add_line('p1-r1-12', (11, 11), (11, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
