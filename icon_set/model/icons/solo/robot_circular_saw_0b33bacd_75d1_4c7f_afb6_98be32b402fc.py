'Industrial Gear on Robotic Base.\n\nSymbol plan: Toothed saw with central circular hub above rounded robot base; broad teeth preserve industrial cutting identity.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0b33bacd-75d1-4c7f-afb6-98be32b402fc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/technology robot war saw_0b33bacd-75d1-4c7f-afb6-98be32b402fc.svg'
AUTHOR = 'gpt-6'

class RobotCircularSaw(Solo48):
    icon_id = 'robot-circular-saw'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('robot', 'circular', 'saw')

    def build(self):
        # Toothed saw with central circular hub above rounded robot base; broad teeth preserve industrial cutting identity.
        axis_x = 24
        p_6_37 = (6, 37)
        p_8_19 = (8, 19)
        p_11_12 = (11, 12)
        p_11_32 = (11, 32)
        p_11_42 = (11, 42)
        p_12_23 = (12, 23)
        p_15_12 = (15, 12)
        p_20_6 = (20, 6)
        p_22_18 = (22, 18)
        p_26_18 = (2 * axis_x - p_22_18[0], p_22_18[1])
        p_28_6 = (2 * axis_x - p_20_6[0], p_20_6[1])
        p_33_12 = (2 * axis_x - p_15_12[0], p_15_12[1])
        p_36_23 = (2 * axis_x - p_12_23[0], p_12_23[1])
        p_37_12 = (2 * axis_x - p_11_12[0], p_11_12[1])
        p_37_32 = (2 * axis_x - p_11_32[0], p_11_32[1])
        p_37_42 = (2 * axis_x - p_11_42[0], p_11_42[1])
        p_40_19 = (2 * axis_x - p_8_19[0], p_8_19[1])
        p_42_37 = (2 * axis_x - p_6_37[0], p_6_37[1])
        self.add_line('saw-1', p_12_23, p_8_19)
        self.add_line('saw-2', p_8_19, p_11_12)
        self.add_line('saw-3', p_11_12, p_15_12)
        self.add_line('saw-4', p_15_12, p_20_6)
        self.add_line('saw-5', p_20_6, p_28_6)
        self.add_line('saw-6', p_28_6, p_33_12)
        self.add_line('saw-7', p_33_12, p_37_12)
        self.add_line('saw-8', p_37_12, p_40_19)
        self.add_line('saw-9', p_40_19, p_36_23)
        self.add_contour('saw', 'saw-1', 'saw-2', 'saw-3', 'saw-4', 'saw-5', 'saw-6', 'saw-7', 'saw-8', 'saw-9', closed=False)
        self.add_arc('hub-1', p_22_18, p_26_18, radius_x=2, radius_y=2, sweep=True)
        self.add_arc('hub-2', p_26_18, p_22_18, radius_x=2, radius_y=2, sweep=True)
        self.add_contour('hub', 'hub-1', 'hub-2', closed=True)
        self.add_line('base-1', p_11_32, p_37_32)
        self.add_arc('base-2', p_37_32, p_42_37, radius_x=5, radius_y=5, sweep=True)
        self.add_line('base-3', p_42_37, p_42_37)
        self.add_arc('base-4', p_42_37, p_37_42, radius_x=5, radius_y=5, sweep=True)
        self.add_line('base-5', p_37_42, p_11_42)
        self.add_arc('base-6', p_11_42, p_6_37, radius_x=5, radius_y=5, sweep=True)
        self.add_line('base-7', p_6_37, p_6_37)
        self.add_arc('base-8', p_6_37, p_11_32, radius_x=5, radius_y=5, sweep=True)
        self.add_contour('base', 'base-1', 'base-2', 'base-3', 'base-4', 'base-5', 'base-6', 'base-7', 'base-8', closed=True)
