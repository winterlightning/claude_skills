'Jasmine Flower with Stem and Leaves.\n\nSymbol plan: Five-petaled jasmine flower and two leaves on stem; omit tiny center ring to avoid trapped pockets.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: flower-2.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cedead88-3fef-43fc-9cca-93bae27399b5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/jasmine_cedead88-3fef-43fc-9cca-93bae27399b5.svg'
AUTHOR = 'gpt-6'

class FivePetalFlowerOnStem(Solo48):
    icon_id = 'five-petal-flower-on-stem'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('five', 'petal', 'flower', 'on', 'stem')

    def build(self):
        # Five-petaled jasmine flower and two leaves on stem; omit tiny center ring to avoid trapped pockets.
        axis_x = 24
        p_5_14 = (5, 14)
        p_7_23 = (7, 23)
        p_8_38 = (8, 38)
        p_12_29 = (12, 29)
        p_12_38 = (12, 38)
        p_15_12 = (15, 12)
        p_16_6 = (16, 6)
        p_17_22 = (17, 22)
        p_18_40 = (18, 40)
        p_20_4 = (20, 4)
        p_20_33 = (20, 33)
        p_24_4 = (24, 4)
        p_24_26 = (24, 26)
        p_24_44 = (24, 44)
        p_26_32 = (26, 32)
        p_29_10 = (29, 10)
        p_29_12 = (29, 12)
        p_29_22 = (29, 22)
        p_30_7 = (30, 7)
        p_30_40 = (2 * axis_x - p_18_40[0], p_18_40[1])
        p_31_22 = (2 * axis_x - p_17_22[0], p_17_22[1])
        p_33_31 = (33, 31)
        p_35_23 = (35, 23)
        p_36_20 = (36, 20)
        p_36_38 = (2 * axis_x - p_12_38[0], p_12_38[1])
        p_38_8 = (38, 8)
        p_40_38 = (2 * axis_x - p_8_38[0], p_8_38[1])
        p_41_13 = (41, 13)
        self.add_bezier('flower-1', p_24_4, (p_30_7, p_29_10, p_29_12))
        self.add_bezier('flower-2', p_29_12, (p_38_8, p_41_13, p_36_20))
        self.add_bezier('flower-3', p_36_20, (p_35_23, p_31_22, p_29_22))
        self.add_bezier('flower-4', p_29_22, (p_33_31, p_26_32, p_24_26))
        self.add_bezier('flower-5', p_24_26, (p_20_33, p_12_29, p_17_22))
        self.add_bezier('flower-6', p_17_22, (p_7_23, p_5_14, p_15_12))
        self.add_bezier('flower-7', p_15_12, (p_16_6, p_20_4, p_24_4))
        self.add_contour('flower', 'flower-1', 'flower-2', 'flower-3', 'flower-4', 'flower-5', 'flower-6', 'flower-7', closed=True)
        self.add_line('stem-1', p_24_26, p_24_44)
        self.add_contour('stem', 'stem-1', closed=False)
        self.relate("connect", 'stem', 'flower')
        self.add_bezier('leaves-1', p_8_38, (p_12_38, p_18_40, p_24_44))
        self.add_bezier('leaves-2', p_24_44, (p_30_40, p_36_38, p_40_38))
        self.add_contour('leaves', 'leaves-1', 'leaves-2', closed=False)
        self.relate("connect", 'stem', 'leaves')
