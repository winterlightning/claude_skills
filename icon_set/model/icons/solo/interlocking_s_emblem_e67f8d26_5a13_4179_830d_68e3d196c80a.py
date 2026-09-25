'Interlocking Stylized S Shape.\n\nSymbol plan: Two opposing diagonal ribbon runs with open ends retain the interlocking S emblem; preserve distinct ribbons and broaden their spacing.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e67f8d26-5a13-4179-830d-68e3d196c80a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/squarespace logo_e67f8d26-5a13-4179-830d-68e3d196c80a.svg'
AUTHOR = 'gpt-6'

class InterlockingSEmblem(Solo48):
    icon_id = 'interlocking-s-emblem'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('interlocking', 's', 'emblem')

    def build(self):
        # Two opposing diagonal ribbon runs with open ends retain the interlocking S emblem; preserve distinct ribbons and broaden their spacing.
        axis_x = 24
        p_6_24 = (6, 24)
        p_6_27 = (6, 27)
        p_6_30 = (6, 30)
        p_7_23 = (7, 23)
        p_9_21 = (9, 21)
        p_9_32 = (9, 32)
        p_12_32 = (12, 32)
        p_15_32 = (15, 32)
        p_16_42 = (16, 42)
        p_17_29 = (17, 29)
        p_20_26 = (20, 26)
        p_24_6 = (24, 6)
        p_31_42 = (31, 42)
        p_34_12 = (34, 12)
        p_34_24 = (34, 24)
        p_38_20 = (38, 20)
        p_38_35 = (38, 35)
        p_40_33 = (40, 33)
        p_42_23 = (42, 23)
        p_42_28 = (42, 28)
        p_42_31 = (42, 31)
        self.add_line('upper-ribbon-1', p_24_6, p_9_21)
        self.add_bezier('upper-ribbon-2', p_9_21, (p_7_23, p_6_24, p_6_27))
        self.add_bezier('upper-ribbon-3', p_6_27, (p_6_30, p_9_32, p_12_32))
        self.add_bezier('upper-ribbon-4', p_12_32, (p_15_32, p_17_29, p_20_26))
        self.add_line('upper-ribbon-5', p_20_26, p_34_12)
        self.add_contour('upper-ribbon', 'upper-ribbon-1', 'upper-ribbon-2', 'upper-ribbon-3', 'upper-ribbon-4', 'upper-ribbon-5', closed=False)
        self.add_line('lower-ribbon-1', p_16_42, p_34_24)
        self.add_bezier('lower-ribbon-2', p_34_24, (p_38_20, p_42_23, p_42_28))
        self.add_bezier('lower-ribbon-3', p_42_28, (p_42_31, p_40_33, p_38_35))
        self.add_line('lower-ribbon-4', p_38_35, p_31_42)
        self.add_contour('lower-ribbon', 'lower-ribbon-1', 'lower-ribbon-2', 'lower-ribbon-3', 'lower-ribbon-4', closed=False)
