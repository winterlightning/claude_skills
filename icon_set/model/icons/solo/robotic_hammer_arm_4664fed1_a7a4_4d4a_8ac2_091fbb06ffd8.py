'Industrial Robotic Hammer Arm.\n\nSymbol plan: Robot hammer on an articulated arm above rounded base; simplify doubled arm rails to single structural strokes.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4664fed1-a7a4-4d4a-8ac2-091fbb06ffd8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/technology robot war hammer_4664fed1-a7a4-4d4a-8ac2-091fbb06ffd8.svg'
AUTHOR = 'gpt-6'

class RoboticHammerArm(Solo48):
    icon_id = 'robotic-hammer-arm'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('robotic', 'hammer', 'arm')

    def build(self):
        # Robot hammer on an articulated arm above rounded base; simplify doubled arm rails to single structural strokes.
        axis_x = 24
        p_6_37 = (6, 37)
        p_7_12 = (7, 12)
        p_11_32 = (11, 32)
        p_11_42 = (11, 42)
        p_16_17 = (16, 17)
        p_19_12 = (19, 12)
        p_25_32 = (25, 32)
        p_32_6 = (32, 6)
        p_32_12 = (32, 12)
        p_32_22 = (32, 22)
        p_37_32 = (2 * axis_x - p_11_32[0], p_11_32[1])
        p_37_42 = (2 * axis_x - p_11_42[0], p_11_42[1])
        p_42_6 = (42, 6)
        p_42_22 = (42, 22)
        p_42_37 = (2 * axis_x - p_6_37[0], p_6_37[1])
        self.add_line('base-1', p_11_32, p_37_32)
        self.add_arc('base-2', p_37_32, p_42_37, radius_x=5, radius_y=5, sweep=True)
        self.add_line('base-3', p_42_37, p_42_37)
        self.add_arc('base-4', p_42_37, p_37_42, radius_x=5, radius_y=5, sweep=True)
        self.add_line('base-5', p_37_42, p_11_42)
        self.add_arc('base-6', p_11_42, p_6_37, radius_x=5, radius_y=5, sweep=True)
        self.add_line('base-7', p_6_37, p_6_37)
        self.add_arc('base-8', p_6_37, p_11_32, radius_x=5, radius_y=5, sweep=True)
        self.add_contour('base', 'base-1', 'base-2', 'base-3', 'base-4', 'base-5', 'base-6', 'base-7', 'base-8', closed=True)
        self.add_arc('elbow-1', p_7_12, p_19_12, radius_x=6, radius_y=6, sweep=True)
        self.add_arc('elbow-2', p_19_12, p_7_12, radius_x=6, radius_y=6, sweep=True)
        self.add_contour('elbow', 'elbow-1', 'elbow-2', closed=True)
        self.add_line('lower-arm-1', p_16_17, p_25_32)
        self.add_contour('lower-arm', 'lower-arm-1', closed=False)
        self.relate("connect", 'lower-arm', 'elbow')
        self.relate("connect", 'lower-arm', 'base')
        self.add_line('upper-arm-1', p_19_12, p_32_12)
        self.add_contour('upper-arm', 'upper-arm-1', closed=False)
        self.relate("connect", 'upper-arm', 'elbow')
        self.add_line('hammer-1', p_32_6, p_42_6)
        self.add_line('hammer-2', p_42_6, p_42_22)
        self.add_line('hammer-3', p_42_22, p_32_22)
        self.add_line('hammer-4', p_32_22, p_32_6)
        self.add_contour('hammer', 'hammer-1', 'hammer-2', 'hammer-3', 'hammer-4', closed=True)
        self.relate("connect", 'upper-arm', 'hammer')
