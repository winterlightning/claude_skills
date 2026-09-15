'Sunglasses with sun.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81f3cdea-8b11-5ce2-be37-8b1a02812d9f'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-04/glasses sun_81f3cdea-8b11-5ce2-be37-8b1a02812d9f.svg'
AUTHOR = 'gpt-6'

class SunglassesWithSun(Solo48):
    icon_id = 'sunglasses-with-sun'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('sunglasses', 'sun', 'shades', 'summer', 'eyewear', 'glasses', 'holiday', 'beach')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_10_29 = (10, 29)
        p_17_29 = (17, 29)
        p_20_33 = (20, 33)
        p_20_38 = (20, 38)
        p_17_42 = (17, 42)
        p_10_42 = (10, 42)
        p_6_38 = (6, 38)
        p_6_33 = (6, 33)
        p_31_29 = (31, 29)
        p_38_29 = (38, 29)
        p_42_33 = (42, 33)
        p_42_38 = (42, 38)
        p_38_42 = (38, 42)
        p_31_42 = (31, 42)
        p_28_38 = (28, 38)
        p_28_33 = (28, 33)
        p_31_6 = (31, 6)
        p_31_7 = (31, 7)
        p_22_15 = (22, 15)
        p_23_15 = (23, 15)
        p_40_15 = (40, 15)
        p_31_15 = (31, 15)
        self.add_line('lens-left0', p_10_29, p_17_29)
        self.add_arc('lens-left1', p_17_29, p_20_33, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('lens-left2', p_20_33, p_20_38)
        self.add_arc('lens-left3', p_20_38, p_17_42, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('lens-left4', p_17_42, p_10_42)
        self.add_arc('lens-left5', p_10_42, p_6_38, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('lens-left6', p_6_38, p_6_33)
        self.add_arc('lens-left7', p_6_33, p_10_29, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('lens-right0', p_31_29, p_38_29)
        self.add_arc('lens-right1', p_38_29, p_42_33, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('lens-right2', p_42_33, p_42_38)
        self.add_arc('lens-right3', p_42_38, p_38_42, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('lens-right4', p_38_42, p_31_42)
        self.add_arc('lens-right5', p_31_42, p_28_38, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('lens-right6', p_28_38, p_28_33)
        self.add_arc('lens-right7', p_28_33, p_31_29, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('bridge', p_20_33, p_28_33)
        self.add_line('ray-top', p_31_6, p_31_7)
        self.add_line('ray-left', p_22_15, p_23_15)
        self.add_line('ray-right', p_40_15, p_40_15)
        self.add_line('sun', p_31_15, p_31_15)
        self.add_contour('lens-left', 'lens-left0', 'lens-left1', 'lens-left2', 'lens-left3', 'lens-left4', 'lens-left5', 'lens-left6', 'lens-left7', closed=True)
        self.add_contour('lens-right', 'lens-right0', 'lens-right1', 'lens-right2', 'lens-right3', 'lens-right4', 'lens-right5', 'lens-right6', 'lens-right7', closed=True)
        self.relate('connect', 'lens-left', 'bridge')
        self.relate('connect', 'lens-right', 'bridge')
