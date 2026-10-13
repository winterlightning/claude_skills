"""Independent 32px profile of recycle-arrows.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '99131c40-2e10-4d8b-b928-083d50e252f1'
SOURCE_PATH = 'pictographic-primitives/symbol/recycle_99131c40-2e10-4d8b-b928-083d50e252f1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('99131c40-2e10-4d8b-b928-083d50e252f1', 'pictographic-primitives/symbol/recycle_99131c40-2e10-4d8b-b928-083d50e252f1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/recycle-arrows',)
SOLO_SOURCE_ICON_IDS = ('recycle-arrows',)
REFERENCE_EXPORT_SHA256 = '8a428a08d8c041eb7b73321d80ac107d59952bce2c68820096923efe2c6e7443'

class DrawingContainerSymbol(Sub32):
    icon_id = 'recycle-arrows-sub32-symbol'
    related_origin_icon_id = 'recycle-arrows-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/recycle-arrows-sub32'
    counterpart_icon_id = 'recycle-arrows-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Three arrows chasing around a triangle, 8-unit gaps at the corners, inward half arrowheads.
        self.add_line('shaft-0', (2, 20), (12, 2))
        self.add_line('head-0', (12, 2), (13, 7))
        self.relate('connect', 'shaft-0', 'head-0')
        self.add_line('shaft-1', (21, 2), (30, 18))
        self.add_line('head-1', (30, 18), (25, 16))
        self.relate('connect', 'shaft-1', 'head-1')
        self.add_line('shaft-2', (24, 30), (8, 30))
        self.add_line('head-2', (8, 30), (12, 27))
        self.relate('connect', 'shaft-2', 'head-2')
