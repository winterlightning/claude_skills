# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of recycle-arrows.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '99131c40-2e10-4d8b-b928-083d50e252f1'
SOURCE_PATH = 'pictographic-primitives/symbol/recycle_99131c40-2e10-4d8b-b928-083d50e252f1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('99131c40-2e10-4d8b-b928-083d50e252f1', 'pictographic-primitives/symbol/recycle_99131c40-2e10-4d8b-b928-083d50e252f1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/recycle-arrows',)
SOLO_SOURCE_ICON_IDS = ('recycle-arrows',)
REFERENCE_EXPORT_SHA256 = '8a428a08d8c041eb7b73321d80ac107d59952bce2c68820096923efe2c6e7443'

class DrawingContainerSymbol(Sub32):
    icon_id = 'recycle-arrows-sub32-symbol'
    variant_of = 'recycle-arrows-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/recycle-arrows-sub32'
    counterpart_icon_id = 'recycle-arrows-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (11, 7), (21, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (21, 7), (25, 14))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (19, 13), (25, 14))
        self.add_line('p2-r1-2', (25, 14), (27, 8))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (30, 19), (30, 21))
        self.add_arc('p3-r1-2', (30, 21), (25, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p3-r1-3', (25, 25), (16, 25))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (21, 21), (16, 25))
        self.add_line('p4-r1-2', (16, 25), (21, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (9, 25), (7, 25))
        self.add_arc('p5-r1-2', (7, 25), (2, 21), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p5-r1-3', (2, 21), (7, 13))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', closed=False)
        self.add_line('p6-r1-1', (2, 14), (7, 13))
        self.add_line('p6-r1-2', (7, 13), (8, 19))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-2')
        self.relate('connect', 'p3-r1-3', 'p4-r1-1')
        self.relate('connect', 'p3-r1-3', 'p4-r1-2')
        self.relate('connect', 'p5-r1-3', 'p6-r1-1')
        self.relate('connect', 'p5-r1-3', 'p6-r1-2')
