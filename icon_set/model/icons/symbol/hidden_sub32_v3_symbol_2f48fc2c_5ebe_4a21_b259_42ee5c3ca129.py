"""Independent 32px profile of hidden.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '2f48fc2c-5ebe-4a21-b259-42ee5c3ca129'
SOURCE_PATH = 'pictographic-primitives/symbol/hidden_2f48fc2c-5ebe-4a21-b259-42ee5c3ca129.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2f48fc2c-5ebe-4a21-b259-42ee5c3ca129', 'pictographic-primitives/symbol/hidden_2f48fc2c-5ebe-4a21-b259-42ee5c3ca129.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hidden',)
SOLO_SOURCE_ICON_IDS = ('hidden',)
REFERENCE_EXPORT_SHA256 = '887e49d709ee5b7b152870a6bfa100d7d2263b4d65ff8450edfa3a8fea9c5cbf'

class DrawingVariant3ContainerSymbol(Sub32):
    icon_id = 'hidden-sub32-v3-symbol'
    related_origin_icon_id = 'hidden-sub32-v3'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/hidden-sub32-v3'
    counterpart_icon_id = 'hidden-sub32-v3'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('ul', (2, 16), ((4, 12), (6, 10), (8, 8)))
        self.add_bezier('ut', (8, 8), ((10, 6), (13, 6), (16, 6)))
        self.add_bezier('rt', (16, 6), ((19, 6), (22, 6), (24, 8)))
        self.add_bezier('ur', (24, 8), ((26, 10), (28, 12), (30, 16)))
        self.add_bezier('lr', (30, 16), ((28, 20), (26, 22), (24, 24)))
        self.add_bezier('lb', (24, 24), ((22, 26), (19, 26), (16, 26)))
        self.add_bezier('bl', (16, 26), ((13, 26), (10, 26), (8, 24)))
        self.add_bezier('ll', (8, 24), ((6, 22), (4, 20), (2, 16)))
        self.add_contour('eye', 'ul', 'ut', 'rt', 'ur', 'lr', 'lb', 'bl', 'll', closed=True)
        self.add_line('slash', (8, 8), (24, 24))
        self.relate('connect', 'eye', 'slash')
