"""Independent 32px profile of hierarchy-circle-leaves.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'f540eba4-5f02-4b15-ab87-852a4076e2c9'
SOURCE_PATH = 'pictographic-primitives/programing/hierarchy_f540eba4-5f02-4b15-ab87-852a4076e2c9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f540eba4-5f02-4b15-ab87-852a4076e2c9', 'pictographic-primitives/programing/hierarchy_f540eba4-5f02-4b15-ab87-852a4076e2c9.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hierarchy-circle-leaves',)
SOLO_SOURCE_ICON_IDS = ('hierarchy-circle-leaves',)
REFERENCE_EXPORT_SHA256 = '422d84c25ff1bd4c6142b6667dbf3634fef2ece6d3334d62e375e856b66df33a'

class DrawingContainerSymbol(Sub32):
    icon_id = 'hierarchy-circle-leaves-sub32-symbol'
    related_origin_icon_id = 'hierarchy-circle-leaves-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/hierarchy-circle-leaves-sub32'
    counterpart_icon_id = 'hierarchy-circle-leaves-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'programing'
    categories = ('programing', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Hierarchy: a box on top branching down to two circles.
        self.add_polyline('top', (12, 2), (20, 2), (20, 10), (12, 10), closed=True)
        self.add_polyline('branch', (6, 22), (16, 10), (26, 22))
        self.add_arc('leaf-l-1', (2, 26), (10, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('leaf-l-2', (10, 26), (2, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('leaf-l', 'leaf-l-1', 'leaf-l-2', closed=True)
        self.add_arc('leaf-r-1', (22, 26), (30, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('leaf-r-2', (30, 26), (22, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('leaf-r', 'leaf-r-1', 'leaf-r-2', closed=True)
        self.relate('connect', 'top', 'branch')
        self.relate('connect', 'branch', 'leaf-l')
        self.relate('connect', 'branch', 'leaf-r')
