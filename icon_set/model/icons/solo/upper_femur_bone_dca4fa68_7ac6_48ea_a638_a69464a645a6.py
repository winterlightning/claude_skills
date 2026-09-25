'Human Hip Bone.\n\nSymbol plan: Offset ball at upper right, smaller left projection and open shaft; smooth asymmetric silhouette.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dca4fa68-7ac6-48ea-a638-a69464a645a6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hip_dca4fa68-7ac6-48ea-a638-a69464a645a6.svg'
AUTHOR = 'gpt-6'

class UpperFemurBone(Solo48):
    icon_id = 'upper-femur-bone'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('upper', 'femur', 'bone')

    def build(self):
        # Offset ball at upper right, smaller left projection and open shaft; smooth asymmetric silhouette.
        axis_x = 24
        p_8_20 = (8, 20)
        p_8_26 = (8, 26)
        p_8_31 = (8, 31)
        p_15_20 = (15, 20)
        p_16_31 = (16, 31)
        p_16_36 = (16, 36)
        p_16_44 = (16, 44)
        p_18_25 = (18, 25)
        p_20_12 = (20, 12)
        p_21_4 = (21, 4)
        p_22_30 = (22, 30)
        p_25_19 = (25, 19)
        p_28_23 = (28, 23)
        p_30_4 = (30, 4)
        p_36_4 = (36, 4)
        p_36_30 = (36, 30)
        p_36_36 = (36, 36)
        p_36_44 = (36, 44)
        p_40_8 = (40, 8)
        p_40_14 = (40, 14)
        p_40_24 = (40, 24)
        self.add_line('bone-1', p_16_44, p_16_36)
        self.add_bezier('bone-2', p_16_36, (p_16_31, p_8_31, p_8_26))
        self.add_bezier('bone-3', p_8_26, (p_8_20, p_15_20, p_18_25))
        self.add_bezier('bone-4', p_18_25, (p_22_30, p_28_23, p_25_19))
        self.add_bezier('bone-5', p_25_19, (p_20_12, p_21_4, p_30_4))
        self.add_bezier('bone-6', p_30_4, (p_36_4, p_40_8, p_40_14))
        self.add_bezier('bone-7', p_40_14, (p_40_24, p_36_30, p_36_36))
        self.add_line('bone-8', p_36_36, p_36_44)
        self.add_contour('bone', 'bone-1', 'bone-2', 'bone-3', 'bone-4', 'bone-5', 'bone-6', 'bone-7', 'bone-8', closed=False)
