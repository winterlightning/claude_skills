"""Independent 32px profile of circles-three-trefoil.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '35f09f7d-689b-4b3c-944a-4e852904bb48'
SOURCE_PATH = 'pictographic-primitives/symbol/three circles_35f09f7d-689b-4b3c-944a-4e852904bb48.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('35f09f7d-689b-4b3c-944a-4e852904bb48', 'pictographic-primitives/symbol/three circles_35f09f7d-689b-4b3c-944a-4e852904bb48.svg'),)
PROFILE_SOURCE_KEYS = ('solo/circles-three-trefoil',)
SOLO_SOURCE_ICON_IDS = ('circles-three-trefoil',)
REFERENCE_EXPORT_SHA256 = '9dfca71b04c9158a59f2cd57ae4fb855ac7a8074d06ab21738e1722f604ad89a'

class DrawingContainerSymbol(Sub32):
    icon_id = 'circles-three-trefoil-sub32-symbol'
    related_origin_icon_id = 'circles-three-trefoil-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/circles-three-trefoil-sub32'
    counterpart_icon_id = 'circles-three-trefoil-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Trefoil of three circles in a triangle, each 4 units clear of the others (overlapping circles always leave slivers).
        self.add_arc('c1-1', (11, 7), (21, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('c1-2', (21, 7), (11, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('top', 'c1-1', 'c1-2', closed=True)
        self.add_arc('c2-1', (2, 25), (12, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('c2-2', (12, 25), (2, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('left', 'c2-1', 'c2-2', closed=True)
        self.add_arc('c3-1', (20, 25), (30, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('c3-2', (30, 25), (20, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('right', 'c3-1', 'c3-2', closed=True)
