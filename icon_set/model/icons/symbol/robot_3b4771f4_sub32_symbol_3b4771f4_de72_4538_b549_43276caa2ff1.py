"""Independent 32px profile of robot-3b4771f4.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '3b4771f4-de72-4538-b549-43276caa2ff1'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/robot_3b4771f4-de72-4538-b549-43276caa2ff1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3b4771f4-de72-4538-b549-43276caa2ff1', 'pictographic-primitives/artificial-intelligence/robot_3b4771f4-de72-4538-b549-43276caa2ff1.svg'), ('233b4b91-c66d-47bb-8540-9a5b8f63230e', 'pictographic-primitives/artificial-intelligence/robot_233b4b91-c66d-47bb-8540-9a5b8f63230e.svg'))
PROFILE_SOURCE_KEYS = ('solo/robot-3b4771f4', 'solo/robot-artificial-intelligence')
SOLO_SOURCE_ICON_IDS = ('robot-3b4771f4', 'robot-artificial-intelligence')
REFERENCE_EXPORT_SHA256 = 'e8045c3d77e1b5a76dd3c471742c92d3976285f48fc3a2b95d7f608881c1f4fa'

class DrawingContainerSymbol(Sub32):
    icon_id = 'robot-3b4771f4-sub32-symbol'
    related_origin_icon_id = 'robot-3b4771f4-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/robot-3b4771f4-sub32'
    counterpart_icon_id = 'robot-3b4771f4-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'artificial-intelligence'
    categories = ('artificial-intelligence', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (10, 2), (10, 10))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (22, 2), (22, 10))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (10, 10), (5, 15), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('p3-r1-2', (5, 15), (5, 23))
        self.add_arc('p3-r1-3', (5, 23), (10, 30), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('p3-r1-4', (10, 30), (22, 30))
        self.add_arc('p3-r1-5', (22, 30), (27, 24), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('p3-r1-6', (27, 24), (27, 14))
        self.add_arc('p3-r1-7', (27, 14), (22, 10), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', closed=False)
        self.add_line('p4-r1-1', (10, 10), (22, 10))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (12, 19), (12, 22))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (20, 19), (20, 22))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-7')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-7', 'p4-r1-1')
