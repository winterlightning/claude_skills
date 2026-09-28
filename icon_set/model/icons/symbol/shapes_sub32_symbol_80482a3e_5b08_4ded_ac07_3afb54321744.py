"""Independent 32px profile of shapes.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '80482a3e-5b08-4ded-ac07-3afb54321744'
SOURCE_PATH = 'pictographic-primitives/design/shapes_80482a3e-5b08-4ded-ac07-3afb54321744.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('80482a3e-5b08-4ded-ac07-3afb54321744', 'pictographic-primitives/design/shapes_80482a3e-5b08-4ded-ac07-3afb54321744.svg'), ('e7bf48a0-7fdc-49bf-add4-fd6807a17ab3', 'pictographic-primitives/design/shapes_e7bf48a0-7fdc-49bf-add4-fd6807a17ab3.svg'))
PROFILE_SOURCE_KEYS = ('solo/shapes', 'solo/shapes-design')
SOLO_SOURCE_ICON_IDS = ('shapes', 'shapes-design')
REFERENCE_EXPORT_SHA256 = '1f4c5a249440d3b60fc4a72e220904ed0ea8f2a5cfb5ab3a8d697b5be2d4f079'

class DrawingContainerSymbol(Sub32):
    icon_id = 'shapes-sub32-symbol'
    related_origin_icon_id = 'shapes-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/shapes-sub32'
    counterpart_icon_id = 'shapes-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'design'
    categories = ('design', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (12, 12), (22, 12))
        self.add_line('p1-r1-2', (22, 12), (30, 12))
        self.add_line('p1-r1-3', (30, 12), (30, 30))
        self.add_line('p1-r1-4', (30, 30), (12, 30))
        self.add_line('p1-r1-5', (12, 30), (12, 22))
        self.add_line('p1-r1-6', (12, 22), (12, 12))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_arc('p2-r1-1', (22, 12), (12, 2), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('p2-r1-2', (12, 2), (2, 12), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('p2-r1-3', (2, 12), (12, 22), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-5', 'p2-r1-3')
        self.relate('connect', 'p1-r1-6', 'p2-r1-3')
