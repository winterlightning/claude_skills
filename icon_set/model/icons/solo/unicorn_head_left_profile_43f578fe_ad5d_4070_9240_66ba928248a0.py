'Mythical Unicorn Head Profile.\n\nSymbol plan: Left-facing unicorn with long muzzle, tall ear, upper-left horn and sweeping back of neck. Simplify horn to one tapered-looking stroke.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '43f578fe-ad5d-4070-9240-66ba928248a0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/alicorn_43f578fe-ad5d-4070-9240-66ba928248a0.svg'
AUTHOR = 'gpt-6'

class UnicornHeadLeftProfile(Solo48):
    icon_id = 'unicorn-head-left-profile'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('unicorn', 'head', 'left', 'profile')

    def build(self):
        # Left-facing unicorn with long muzzle, tall ear, upper-left horn and sweeping back of neck. Simplify horn to one tapered-looking stroke.
        axis_x = 24
        p_8_4 = (8, 4)
        p_8_22 = (8, 22)
        p_8_26 = (8, 26)
        p_8_32 = (8, 32)
        p_15_18 = (15, 18)
        p_17_16 = (17, 16)
        p_18_31 = (18, 31)
        p_21_4 = (21, 4)
        p_21_12 = (21, 12)
        p_21_44 = (21, 44)
        p_23_26 = (23, 26)
        p_25_28 = (25, 28)
        p_25_35 = (25, 35)
        p_27_4 = (2 * axis_x - p_21_4[0], p_21_4[1])
        p_27_11 = (27, 11)
        p_28_12 = (28, 12)
        p_38_13 = (38, 13)
        p_40_30 = (40, 30)
        p_40_44 = (40, 44)
        self.add_bezier('head-1', p_21_44, (p_25_35, p_25_28, p_23_26))
        self.add_bezier('head-2', p_23_26, (p_18_31, p_8_32, p_8_26))
        self.add_bezier('head-3', p_8_26, (p_8_22, p_15_18, p_21_12))
        self.add_line('head-4', p_21_12, p_21_4)
        self.add_bezier('head-5', p_21_4, (p_27_4, p_27_11, p_28_12))
        self.add_bezier('head-6', p_28_12, (p_38_13, p_40_30, p_40_44))
        self.add_contour('head', 'head-1', 'head-2', 'head-3', 'head-4', 'head-5', 'head-6', closed=False)
        self.add_line('horn-1', p_17_16, p_8_4)
        self.add_contour('horn', 'horn-1', closed=False)
        self.relate("connect", 'head', 'horn')
