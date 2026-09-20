# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of liras.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '986af714-6fb8-449a-ad31-d5271f278137'
SOURCE_PATH = 'pictographic-primitives/money/liras_986af714-6fb8-449a-ad31-d5271f278137.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('986af714-6fb8-449a-ad31-d5271f278137', 'pictographic-primitives/money/liras_986af714-6fb8-449a-ad31-d5271f278137.svg'),)
PROFILE_SOURCE_KEYS = ('solo/liras',)
SOLO_SOURCE_ICON_IDS = ('liras',)
REFERENCE_EXPORT_SHA256 = 'e40bd69750f4eb3147f9a383eb2bc20ab3339d4b8dabc691afe542e24fafce2a'

class DrawingContainerSymbol(Sub32):
    icon_id = 'liras-sub32-symbol'
    variant_of = 'liras-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/liras-sub32'
    counterpart_icon_id = 'liras-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'money'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (27, 8), ((27, 4), (24, 2), (20, 2)))
        self.add_bezier('p1-r1-2', (20, 2), ((15, 2), (12, 4), (12, 8)))
        self.add_line('p1-r1-3', (12, 8), (12, 23))
        self.add_arc('p1-r1-4', (12, 23), (5, 30), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (5, 30), (27, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (6, 13), (20, 13))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (6, 22), (20, 22))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-4', 'p2-r1-1')
