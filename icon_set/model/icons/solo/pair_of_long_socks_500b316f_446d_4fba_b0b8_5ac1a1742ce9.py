'Pair of Socks.\n\nSymbol plan: Pair of long socks with outward toes and short cuff seams; equal-width shafts mirrored about center.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '500b316f-446d-4fba-b0b8-5ac1a1742ce9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hosiery_500b316f-446d-4fba-b0b8-5ac1a1742ce9.svg'
AUTHOR = 'gpt-6'

class PairOfLongSocks(Solo48):
    icon_id = 'pair-of-long-socks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('pair', 'of', 'long', 'socks')

    def build(self):
        # Pair of long socks with outward toes and short cuff seams; equal-width shafts mirrored about center.
        axis_x = 24
        p_4_42 = (4, 42)
        p_6_35 = (6, 35)
        p_8_31 = (8, 31)
        p_10_6 = (10, 6)
        p_10_14 = (10, 14)
        p_10_27 = (10, 27)
        p_10_42 = (10, 42)
        p_15_42 = (15, 42)
        p_20_6 = (20, 6)
        p_20_14 = (20, 14)
        p_20_28 = (20, 28)
        p_20_35 = (20, 35)
        p_28_6 = (2 * axis_x - p_20_6[0], p_20_6[1])
        p_28_14 = (2 * axis_x - p_20_14[0], p_20_14[1])
        p_28_28 = (2 * axis_x - p_20_28[0], p_20_28[1])
        p_28_35 = (2 * axis_x - p_20_35[0], p_20_35[1])
        p_33_42 = (2 * axis_x - p_15_42[0], p_15_42[1])
        p_38_6 = (2 * axis_x - p_10_6[0], p_10_6[1])
        p_38_14 = (2 * axis_x - p_10_14[0], p_10_14[1])
        p_38_27 = (2 * axis_x - p_10_27[0], p_10_27[1])
        p_38_42 = (2 * axis_x - p_10_42[0], p_10_42[1])
        p_40_31 = (2 * axis_x - p_8_31[0], p_8_31[1])
        p_42_35 = (2 * axis_x - p_6_35[0], p_6_35[1])
        p_44_42 = (2 * axis_x - p_4_42[0], p_4_42[1])
        self.add_line('left-sock-1', p_10_6, p_20_6)
        self.add_line('left-sock-2', p_20_6, p_20_28)
        self.add_bezier('left-sock-3', p_20_28, (p_20_35, p_15_42, p_10_42))
        self.add_bezier('left-sock-4', p_10_42, (p_4_42, p_6_35, p_8_31))
        self.add_line('left-sock-5', p_8_31, p_10_27)
        self.add_line('left-sock-6', p_10_27, p_10_6)
        self.add_contour('left-sock', 'left-sock-1', 'left-sock-2', 'left-sock-3', 'left-sock-4', 'left-sock-5', 'left-sock-6', closed=True)
        self.add_line('left-sock-cuff-1', p_10_14, p_20_14)
        self.add_contour('left-sock-cuff', 'left-sock-cuff-1', closed=False)
        self.relate("connect", 'left-sock', 'left-sock-cuff')
        self.add_line('right-sock-1', p_38_6, p_28_6)
        self.add_line('right-sock-2', p_28_6, p_28_28)
        self.add_bezier('right-sock-3', p_28_28, (p_28_35, p_33_42, p_38_42))
        self.add_bezier('right-sock-4', p_38_42, (p_44_42, p_42_35, p_40_31))
        self.add_line('right-sock-5', p_40_31, p_38_27)
        self.add_line('right-sock-6', p_38_27, p_38_6)
        self.add_contour('right-sock', 'right-sock-1', 'right-sock-2', 'right-sock-3', 'right-sock-4', 'right-sock-5', 'right-sock-6', closed=True)
        self.add_line('right-sock-cuff-1', p_38_14, p_28_14)
        self.add_contour('right-sock-cuff', 'right-sock-cuff-1', closed=False)
        self.relate("connect", 'right-sock', 'right-sock-cuff')
