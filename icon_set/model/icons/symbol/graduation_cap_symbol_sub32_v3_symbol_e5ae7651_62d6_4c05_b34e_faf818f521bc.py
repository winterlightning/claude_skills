"""Independent 32px profile of graduation-cap-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'e5ae7651-62d6-4c05-b34e-faf818f521bc'
SOURCE_PATH = 'pictographic-primitives/symbol/graduation cap_e5ae7651-62d6-4c05-b34e-faf818f521bc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e5ae7651-62d6-4c05-b34e-faf818f521bc', 'pictographic-primitives/symbol/graduation cap_e5ae7651-62d6-4c05-b34e-faf818f521bc.svg'), ('ac0c8839-9020-4a65-9a30-af5a45d63503', 'pictographic-primitives/accessories/batch-07/cap_ac0c8839-9020-4a65-9a30-af5a45d63503.svg'), ('5f6ee542-cdce-408a-b798-b60860e5b325', 'pictographic-primitives/accessories/batch-06/cap_5f6ee542-cdce-408a-b798-b60860e5b325.svg'))
PROFILE_SOURCE_KEYS = ('solo/graduation-cap-symbol', 'solo/academic-graduation-cap', 'solo/graduation-mortarboard')
SOLO_SOURCE_ICON_IDS = ('graduation-cap-symbol', 'academic-graduation-cap', 'graduation-mortarboard')
REFERENCE_EXPORT_SHA256 = '3db2ce90f5f70f0792c27acb4fbe21a247b788f59a72a50715d7930ff3bccb1b'

class DrawingVariant3ContainerSymbol(Sub32):
    icon_id = 'graduation-cap-symbol-sub32-v3-symbol'
    related_origin_icon_id = 'graduation-cap-symbol-sub32-v3'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/graduation-cap-symbol-sub32-v3'
    counterpart_icon_id = 'graduation-cap-symbol-sub32-v3'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_polyline('board', (2, 13), (16, 6), (30, 13), (16, 20), closed=True)
        self.add_line('right', (24, 16), (24, 21))
        self.add_bezier('br', (24, 21), ((24, 24), (20, 26), (16, 26)))
        self.add_bezier('bl', (16, 26), ((12, 26), (8, 24), (8, 21)))
        self.add_line('left', (8, 21), (8, 16))
        self.add_contour('band', 'right', 'br', 'bl', 'left')
        self.relate('connect', 'board', 'band')
