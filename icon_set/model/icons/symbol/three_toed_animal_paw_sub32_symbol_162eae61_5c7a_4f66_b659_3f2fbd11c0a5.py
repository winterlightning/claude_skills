"""Independent 32px profile of three-toed-animal-paw.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '162eae61-5c7a-4f66-b659-3f2fbd11c0a5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/paw print_162eae61-5c7a-4f66-b659-3f2fbd11c0a5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('162eae61-5c7a-4f66-b659-3f2fbd11c0a5', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/paw print_162eae61-5c7a-4f66-b659-3f2fbd11c0a5.svg'),)
PROFILE_SOURCE_KEYS = ('solo/three-toed-animal-paw',)
SOLO_SOURCE_ICON_IDS = ('three-toed-animal-paw',)
REFERENCE_EXPORT_SHA256 = '97e14db0f190787388dc6913bc426cf24f0f12f95de4197689b028c24eabf262'

class DrawingContainerSymbol(Sub32):
    icon_id = 'three-toed-animal-paw-sub32-symbol'
    related_origin_icon_id = 'three-toed-animal-paw-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/three-toed-animal-paw-sub32'
    counterpart_icon_id = 'three-toed-animal-paw-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (14, 4), (16, 2), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (16, 2), (18, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (18, 4), (16, 6), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p1-r1-4', (16, 6), (14, 4), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=True)
        self.add_arc('p2-r1-1', (2, 14), (4, 12), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p2-r1-2', (4, 12), (6, 14), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p2-r1-3', (6, 14), (4, 16), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p2-r1-4', (4, 16), (2, 14), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=True)
        self.add_arc('p3-r1-1', (26, 14), (28, 12), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (28, 12), (30, 14), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p3-r1-3', (30, 14), (28, 16), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('p3-r1-4', (28, 16), (26, 14), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=True)
        self.add_bezier('p4-r1-1', (16, 20), ((13, 20), (13, 23), (10, 25)))
        self.add_bezier('p4-r1-2', (10, 25), ((7, 26), (6, 27), (6, 28)))
        self.add_bezier('p4-r1-3', (6, 28), ((6, 30), (11, 30), (16, 30)))
        self.add_bezier('p4-r1-4', (16, 30), ((16, 30), (16, 30), (16, 30)))
        self.add_bezier('p4-r1-5', (16, 30), ((21, 30), (26, 30), (26, 28)))
        self.add_bezier('p4-r1-6', (26, 28), ((26, 27), (25, 26), (22, 25)))
        self.add_bezier('p4-r1-7', (22, 25), ((19, 23), (19, 20), (16, 20)))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', 'p4-r1-7', closed=False)
