"""Robot head with twin antennae, independently laid out for SUB32.
Two antennas, flat top, bowl-shaped lower corners, two short vertical eyes.
SQUARE ink (0,0)-(32,32), centerline (2,2)-(30,30).
Lucide bot informs the joined head contour and paired eye strokes.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '8c1610b9-bbb1-4bc2-a858-53d1cdc71603'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/robot_8c1610b9-bbb1-4bc2-a858-53d1cdc71603.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8c1610b9-bbb1-4bc2-a858-53d1cdc71603', 'pictographic-primitives/artificial-intelligence/robot_8c1610b9-bbb1-4bc2-a858-53d1cdc71603.svg'), ('dbe0f105-1e06-44cc-8dc4-597b67509f96', 'pictographic-primitives/artificial-intelligence/robot_dbe0f105-1e06-44cc-8dc4-597b67509f96.svg'))
SOLO_SOURCE_ICON_ID = 'robot-head-with-twin-antennae'

class RobotHeadSub32ContainerSymbol(Sub32):
    icon_id = 'robot-head-with-twin-antennae-sub32-symbol'
    related_origin_icon_id = 'robot-head-with-twin-antennae-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/robot-head-with-twin-antennae-sub32'
    counterpart_icon_id = 'robot-head-with-twin-antennae-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    categories = ('artificial-intelligence', 'primitives')

    def build(self):
        nodes = [(2, 10), (10, 10), (22, 10), (30, 10), (30, 20)]
        for i, (a, b) in enumerate(zip(nodes, nodes[1:]), 1):
            self.add_line(f'top-{i}', a, b)
        self.add_arc('lower-right', (30, 20), (20, 30), radius_x=10)
        self.add_line('base', (20, 30), (12, 30))
        self.add_arc('lower-left', (12, 30), (2, 20), radius_x=10)
        self.add_line('left', (2, 20), (2, 10))
        self.add_contour('head', 'top-1', 'top-2', 'top-3', 'top-4', 'lower-right', 'base', 'lower-left', 'left', closed=True)
        for i, x in enumerate((10, 22)):
            self.add_line(f'antenna-{i}', (x, 2), (x, 10))
            self.relate('connect', f'antenna-{i}', 'head')
            self.add_line(f'eye-{i}', (x, 18), (x, 20))
