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
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Warning triangle: the ! stem hangs from the apex (a shared joint), its dot 4 units clear of every side.
        self.add_polyline('triangle', (16, 2), (30, 30), (2, 30), closed=True)
        self.add_line('stem', (16, 2), (16, 14))
        self.add_line('dot', (16, 22), (16, 22))
        self.relate('connect', 'triangle', 'stem')
