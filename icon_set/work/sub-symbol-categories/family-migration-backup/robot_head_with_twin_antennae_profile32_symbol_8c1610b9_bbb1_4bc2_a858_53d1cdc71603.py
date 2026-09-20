# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of robot-head-with-twin-antennae.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '8c1610b9-bbb1-4bc2-a858-53d1cdc71603'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/robot_8c1610b9-bbb1-4bc2-a858-53d1cdc71603.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8c1610b9-bbb1-4bc2-a858-53d1cdc71603', 'pictographic-primitives/artificial-intelligence/robot_8c1610b9-bbb1-4bc2-a858-53d1cdc71603.svg'), ('dbe0f105-1e06-44cc-8dc4-597b67509f96', 'pictographic-primitives/artificial-intelligence/robot_dbe0f105-1e06-44cc-8dc4-597b67509f96.svg'))
PROFILE_SOURCE_KEYS = ('solo/robot-head-with-twin-antennae',)
SOLO_SOURCE_ICON_IDS = ('robot-head-with-twin-antennae',)
REFERENCE_EXPORT_SHA256 = 'ce108c0cd1772282d247a3402b950e8534ea7698f4038665dd4c7d6f6776242e'

class DrawingContainerSymbol(Sub32):
    icon_id = 'robot-head-with-twin-antennae-profile32-symbol'
    variant_of = 'robot-head-with-twin-antennae-profile32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/robot-head-with-twin-antennae-profile32'
    counterpart_icon_id = 'robot-head-with-twin-antennae-profile32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'artificial-intelligence'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 11), (10, 11))
        self.add_line('p1-r1-2', (10, 11), (22, 11))
        self.add_line('p1-r1-3', (22, 11), (30, 11))
        self.add_line('p1-r1-4', (30, 11), (30, 19))
        self.add_arc('p1-r1-5', (30, 19), (19, 30), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (19, 30), (13, 30))
        self.add_arc('p1-r1-7', (13, 30), (2, 19), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (2, 19), (2, 11))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_line('p2-r1-1', (10, 2), (10, 11))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (10, 18), (10, 21))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (22, 2), (22, 11))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (22, 18), (22, 21))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p4-r1-1')
        self.relate('connect', 'p1-r1-3', 'p4-r1-1')
