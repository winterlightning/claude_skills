"""Independent 32px profile of robot-99be828f.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '99be828f-ff32-44e9-a830-3f0a264491b1'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/robot_99be828f-ff32-44e9-a830-3f0a264491b1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('99be828f-ff32-44e9-a830-3f0a264491b1', 'pictographic-primitives/artificial-intelligence/robot_99be828f-ff32-44e9-a830-3f0a264491b1.svg'), ('a1bb0d4a-25ef-4c7a-beac-38a58444a803', 'pictographic-primitives/artificial-intelligence/robot_a1bb0d4a-25ef-4c7a-beac-38a58444a803.svg'), ('e46fb630-ba38-428c-8b2e-adf342a25e31', 'pictographic-primitives/artificial-intelligence/robot_e46fb630-ba38-428c-8b2e-adf342a25e31.svg'))
PROFILE_SOURCE_KEYS = ('solo/robot-99be828f', 'solo/robot-a1bb0d4a', 'solo/robot-e46fb630')
SOLO_SOURCE_ICON_IDS = ('robot-99be828f', 'robot-a1bb0d4a', 'robot-e46fb630')
REFERENCE_EXPORT_SHA256 = '6cf3da4ddb5230ef8edc8213cb1c057dc4a8f336e684b0dd05698c50dd060fb2'

class DrawingContainerSymbol(Sub32):
    icon_id = 'robot-99be828f-sub32-symbol'
    related_origin_icon_id = 'robot-99be828f-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/robot-99be828f-sub32'
    counterpart_icon_id = 'robot-99be828f-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'artificial-intelligence'
    categories = ('artificial-intelligence', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (16, 2), (16, 11))
        self.add_line('p1-r1-2', (16, 11), (6, 11))
        self.add_arc('p1-r1-3', (6, 11), (2, 14), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('p1-r1-4', (2, 14), (2, 26))
        self.add_arc('p1-r1-5', (2, 26), (6, 30), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('p1-r1-6', (6, 30), (26, 30))
        self.add_arc('p1-r1-7', (26, 30), (30, 26), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('p1-r1-8', (30, 26), (30, 14))
        self.add_arc('p1-r1-9', (30, 14), (26, 11), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('p1-r1-10', (26, 11), (16, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (11, 18), (11, 22))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (21, 18), (21, 22))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
