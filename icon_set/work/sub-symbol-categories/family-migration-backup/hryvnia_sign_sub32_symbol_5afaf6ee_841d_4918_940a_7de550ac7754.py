# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of hryvnia-sign.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '5afaf6ee-841d-4918-940a-7de550ac7754'
SOURCE_PATH = 'pictographic-primitives/symbol/hryvnia sign_5afaf6ee-841d-4918-940a-7de550ac7754.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5afaf6ee-841d-4918-940a-7de550ac7754', 'pictographic-primitives/symbol/hryvnia sign_5afaf6ee-841d-4918-940a-7de550ac7754.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hryvnia-sign',)
SOLO_SOURCE_ICON_IDS = ('hryvnia-sign',)
REFERENCE_EXPORT_SHA256 = 'b9e1434df29b434468c4b6ea403b86c765d4f5b0fa3c6b4c140ac39778b8f14c'

class DrawingContainerSymbol(Sub32):
    icon_id = 'hryvnia-sign-sub32-symbol'
    variant_of = 'hryvnia-sign-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/hryvnia-sign-sub32'
    counterpart_icon_id = 'hryvnia-sign-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (9, 2), (17, 2))
        self.add_arc('p1-r1-2', (17, 2), (17, 13), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-3', (17, 13), (15, 19))
        self.add_arc('p1-r1-4', (15, 19), (15, 30), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('p1-r1-5', (15, 30), (23, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (5, 13), (17, 13))
        self.add_line('p2-r1-2', (17, 13), (27, 13))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (5, 19), (15, 19))
        self.add_line('p3-r1-2', (15, 19), (27, 19))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p2-r1-1')
        self.relate('connect', 'p1-r1-3', 'p2-r1-2')
        self.relate('connect', 'p1-r1-3', 'p3-r1-1')
        self.relate('connect', 'p1-r1-3', 'p3-r1-2')
        self.relate('connect', 'p1-r1-4', 'p3-r1-1')
        self.relate('connect', 'p1-r1-4', 'p3-r1-2')
