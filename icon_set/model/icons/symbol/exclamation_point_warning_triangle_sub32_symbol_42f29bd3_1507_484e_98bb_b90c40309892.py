"""Independent 32px profile of exclamation-point-warning-triangle-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '42f29bd3-1507-484e-98bb-b90c40309892'
SOURCE_PATH = 'icon_set/dist/gallery/combination-originals/42f29bd3-1507-484e-98bb-b90c40309892.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('42f29bd3-1507-484e-98bb-b90c40309892', 'icon_set/dist/gallery/combination-originals/42f29bd3-1507-484e-98bb-b90c40309892.svg'),)
PROFILE_SOURCE_KEYS = ('solo/exclamation-point-warning-triangle-solo',)
SOLO_SOURCE_ICON_IDS = ('exclamation-point-warning-triangle-solo',)
REFERENCE_EXPORT_SHA256 = '4527c73c3453bc70aa7b4e7dbbe251d34863d0f19f843b79cde5579688fe0c47'

class DrawingContainerSymbol(Sub32):
    icon_id = 'exclamation-point-warning-triangle-sub32-symbol'
    related_origin_icon_id = 'exclamation-point-warning-triangle-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/exclamation-point-warning-triangle-sub32'
    counterpart_icon_id = 'exclamation-point-warning-triangle-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (27, 30))
        self.add_line('p1-r1-2', (27, 30), (5, 30))
        self.add_line('p1-r1-3', (5, 30), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (16, 17), (16, 19))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 24), (16, 24))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
