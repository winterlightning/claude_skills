'Jacks Game Piece.\n\nSymbol plan: Four diagonally mirrored rounded arms around a central body; no artificial center hole.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '026be293-cfdd-4dca-a93d-8e4c6dfddfdc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/jack_026be293-cfdd-4dca-a93d-8e4c6dfddfdc.svg'
AUTHOR = 'gpt-6'

class FourArmedJacksPiece(Solo48):
    icon_id = 'four-armed-jacks-piece'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('four', 'armed', 'jacks', 'piece')

    def build(self):
        # Four diagonally mirrored rounded arms around a central body; no artificial center hole.
        axis_x = 24
        p_6_8 = (6, 8)
        p_6_10 = (6, 10)
        p_6_11 = (6, 11)
        p_6_12 = (6, 12)
        p_6_36 = (6, 36)
        p_6_37 = (6, 37)
        p_6_38 = (6, 38)
        p_6_40 = (6, 40)
        p_7_13 = (7, 13)
        p_7_35 = (7, 35)
        p_8_6 = (8, 6)
        p_8_42 = (8, 42)
        p_10_6 = (10, 6)
        p_10_42 = (10, 42)
        p_11_6 = (11, 6)
        p_11_42 = (11, 42)
        p_12_6 = (12, 6)
        p_12_42 = (12, 42)
        p_13_7 = (13, 7)
        p_13_41 = (13, 41)
        p_16_22 = (16, 22)
        p_16_26 = (16, 26)
        p_22_16 = (22, 16)
        p_22_32 = (22, 32)
        p_26_16 = (2 * axis_x - p_22_16[0], p_22_16[1])
        p_26_32 = (2 * axis_x - p_22_32[0], p_22_32[1])
        p_32_22 = (2 * axis_x - p_16_22[0], p_16_22[1])
        p_32_26 = (2 * axis_x - p_16_26[0], p_16_26[1])
        p_35_7 = (2 * axis_x - p_13_7[0], p_13_7[1])
        p_35_41 = (2 * axis_x - p_13_41[0], p_13_41[1])
        p_36_6 = (2 * axis_x - p_12_6[0], p_12_6[1])
        p_36_42 = (2 * axis_x - p_12_42[0], p_12_42[1])
        p_37_6 = (2 * axis_x - p_11_6[0], p_11_6[1])
        p_37_42 = (2 * axis_x - p_11_42[0], p_11_42[1])
        p_38_6 = (2 * axis_x - p_10_6[0], p_10_6[1])
        p_38_42 = (2 * axis_x - p_10_42[0], p_10_42[1])
        p_40_6 = (2 * axis_x - p_8_6[0], p_8_6[1])
        p_40_42 = (2 * axis_x - p_8_42[0], p_8_42[1])
        p_41_13 = (2 * axis_x - p_7_13[0], p_7_13[1])
        p_41_35 = (2 * axis_x - p_7_35[0], p_7_35[1])
        p_42_8 = (2 * axis_x - p_6_8[0], p_6_8[1])
        p_42_10 = (2 * axis_x - p_6_10[0], p_6_10[1])
        p_42_11 = (2 * axis_x - p_6_11[0], p_6_11[1])
        p_42_12 = (2 * axis_x - p_6_12[0], p_6_12[1])
        p_42_36 = (2 * axis_x - p_6_36[0], p_6_36[1])
        p_42_37 = (2 * axis_x - p_6_37[0], p_6_37[1])
        p_42_38 = (2 * axis_x - p_6_38[0], p_6_38[1])
        p_42_40 = (2 * axis_x - p_6_40[0], p_6_40[1])
        self.add_line('jack-1', p_16_22, p_7_13)
        self.add_bezier('jack-2', p_7_13, (p_6_12, p_6_11, p_6_10))
        self.add_bezier('jack-3', p_6_10, (p_6_8, p_8_6, p_10_6))
        self.add_bezier('jack-4', p_10_6, (p_11_6, p_12_6, p_13_7))
        self.add_line('jack-5', p_13_7, p_22_16)
        self.add_line('jack-6', p_22_16, p_26_16)
        self.add_line('jack-7', p_26_16, p_35_7)
        self.add_bezier('jack-8', p_35_7, (p_36_6, p_37_6, p_38_6))
        self.add_bezier('jack-9', p_38_6, (p_40_6, p_42_8, p_42_10))
        self.add_bezier('jack-10', p_42_10, (p_42_11, p_42_12, p_41_13))
        self.add_line('jack-11', p_41_13, p_32_22)
        self.add_line('jack-12', p_32_22, p_32_26)
        self.add_line('jack-13', p_32_26, p_41_35)
        self.add_bezier('jack-14', p_41_35, (p_42_36, p_42_37, p_42_38))
        self.add_bezier('jack-15', p_42_38, (p_42_40, p_40_42, p_38_42))
        self.add_bezier('jack-16', p_38_42, (p_37_42, p_36_42, p_35_41))
        self.add_line('jack-17', p_35_41, p_26_32)
        self.add_line('jack-18', p_26_32, p_22_32)
        self.add_line('jack-19', p_22_32, p_13_41)
        self.add_bezier('jack-20', p_13_41, (p_12_42, p_11_42, p_10_42))
        self.add_bezier('jack-21', p_10_42, (p_8_42, p_6_40, p_6_38))
        self.add_bezier('jack-22', p_6_38, (p_6_37, p_6_36, p_7_35))
        self.add_line('jack-23', p_7_35, p_16_26)
        self.add_line('jack-24', p_16_26, p_16_22)
        self.add_contour('jack', 'jack-1', 'jack-2', 'jack-3', 'jack-4', 'jack-5', 'jack-6', 'jack-7', 'jack-8', 'jack-9', 'jack-10', 'jack-11', 'jack-12', 'jack-13', 'jack-14', 'jack-15', 'jack-16', 'jack-17', 'jack-18', 'jack-19', 'jack-20', 'jack-21', 'jack-22', 'jack-23', 'jack-24', closed=True)
