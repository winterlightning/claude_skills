'Industrial Robotic Arm with Box.\n\nSymbol plan: Industrial arm with round elbow, open gripper and separate box; omit doubled arm edges to provide claw clearance.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f5f94845-109c-419b-b80e-b9dfc0c95900'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__robotic-gripper-above-box/20260927T171905Z-thuan-mac-1/reference/factory robot arm box_f5f94845-109c-419b-b80e-b9dfc0c95900.svg'
AUTHOR = 'gpt-6'

class RoboticGripperAboveBox(Solo48):
    icon_id = 'robotic-gripper-above-box'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('robotic', 'gripper', 'above', 'box')

    def build(self):
        # Industrial arm with round elbow, open gripper and separate box; omit doubled arm edges to provide claw clearance.
        axis_x = 24
        p_6_42 = (6, 42)
        p_8_12 = (8, 12)
        p_10_34 = (10, 34)
        p_14_18 = (14, 18)
        p_14_34 = (14, 34)
        p_18_42 = (18, 42)
        p_20_12 = (20, 12)
        p_29_34 = (29, 34)
        p_29_42 = (29, 42)
        p_31_21 = (31, 21)
        p_31_25 = (31, 25)
        p_37_12 = (37, 12)
        p_37_21 = (37, 21)
        p_42_21 = (42, 21)
        p_42_25 = (42, 25)
        p_42_34 = (42, 34)
        p_42_42 = (2 * axis_x - p_6_42[0], p_6_42[1])
        self.add_arc('elbow-1', p_8_12, p_20_12, radius_x=6, radius_y=6, sweep=True)
        self.add_arc('elbow-2', p_20_12, p_8_12, radius_x=6, radius_y=6, sweep=True)
        self.add_contour('elbow', 'elbow-1', 'elbow-2', closed=True)
        self.add_line('base-1', p_6_42, p_10_34)
        self.add_line('base-2', p_10_34, p_14_34)
        self.add_line('base-3', p_14_34, p_18_42)
        self.add_line('base-4', p_18_42, p_6_42)
        self.add_contour('base', 'base-1', 'base-2', 'base-3', 'base-4', closed=True)
        self.add_line('upright-1', p_14_18, p_14_34)
        self.add_contour('upright', 'upright-1', closed=False)
        self.relate("connect", 'upright', 'elbow')
        self.relate("connect", 'upright', 'base')
        self.add_line('arm-1', p_20_12, p_37_12)
        self.add_line('arm-2', p_37_12, (37,20))
        self.add_contour('arm', 'arm-1', 'arm-2', closed=False)
        self.relate("connect", 'elbow', 'arm')
        self.add_arc('gripper-left',(30,26),(30,20),radius_x=3,sweep=True)
        self.add_line('gripper-top-left',(30,20),(37,20))
        self.add_line('gripper-top-right',(37,20),(39,20))
        self.add_arc('gripper-right',(39,20),(39,26),radius_x=3,sweep=True)
        self.add_contour('gripper','gripper-left','gripper-top-left',
                         'gripper-top-right','gripper-right',closed=False)
        self.relate("connect", 'arm', 'gripper')
        self.add_line('box-1', p_29_34, p_42_34)
        self.add_line('box-2', p_42_34, p_42_42)
        self.add_line('box-3', p_42_42, p_29_42)
        self.add_line('box-4', p_29_42, p_29_34)
        self.add_contour('box', 'box-1', 'box-2', 'box-3', 'box-4', closed=True)
