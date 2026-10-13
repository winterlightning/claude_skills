"""Independent 32px profile of first-aid-medical-case.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '1f12e0e9-892e-4d3d-ab45-7a2a22a30f92'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/medical kit_1f12e0e9-892e-4d3d-ab45-7a2a22a30f92.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1f12e0e9-892e-4d3d-ab45-7a2a22a30f92', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/medical kit_1f12e0e9-892e-4d3d-ab45-7a2a22a30f92.svg'), ('41bb0b4b-dc69-42d5-bf22-17d0a68fea2b', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/medical kit 1_41bb0b4b-dc69-42d5-bf22-17d0a68fea2b.svg'))
PROFILE_SOURCE_KEYS = ('solo/first-aid-medical-case', 'solo/emergency-medical-first-aid-kit')
SOLO_SOURCE_ICON_IDS = ('first-aid-medical-case', 'emergency-medical-first-aid-kit')
REFERENCE_EXPORT_SHA256 = '52c1a511ad3015b76444f7acd543b8d84e05538e9e6297433748b71165d087ce'

class DrawingContainerSymbol(Sub32):
    icon_id = 'first-aid-medical-case-sub32-symbol'
    related_origin_icon_id = 'first-aid-medical-case-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/first-aid-medical-case-sub32'
    counterpart_icon_id = 'first-aid-medical-case-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 8), (10, 8))
        self.add_line('p1-r1-2', (10, 8), (22, 8))
        self.add_line('p1-r1-3', (22, 8), (27, 8))
        self.add_arc('p1-r1-4', (27, 8), (30, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-5', (30, 11), (30, 27))
        self.add_arc('p1-r1-6', (30, 27), (27, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-7', (27, 30), (22, 30))
        self.add_line('p1-r1-8', (22, 30), (10, 30))
        self.add_line('p1-r1-9', (10, 30), (5, 30))
        self.add_arc('p1-r1-10', (5, 30), (2, 27), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p1-r1-11', (2, 27), (2, 11))
        self.add_arc('p1-r1-12', (2, 11), (5, 8), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', 'p1-r1-11', 'p1-r1-12', closed=False)
        self.add_line('p2-r1-1', (10, 8), (10, 5))
        self.add_arc('p2-r1-2', (10, 5), (13, 2), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-3', (13, 2), (19, 2))
        self.add_arc('p2-r1-4', (19, 2), (22, 5), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('p2-r1-5', (22, 5), (22, 8))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (11, 19), (16, 19))
        self.add_line('p3-r1-2', (16, 19), (21, 19))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (16, 15), (16, 19))
        self.add_line('p4-r1-2', (16, 19), (16, 23))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-5')
        self.relate('connect', 'p1-r1-3', 'p2-r1-5')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-2')
        self.relate('connect', 'p3-r1-2', 'p4-r1-1')
        self.relate('connect', 'p3-r1-2', 'p4-r1-2')
