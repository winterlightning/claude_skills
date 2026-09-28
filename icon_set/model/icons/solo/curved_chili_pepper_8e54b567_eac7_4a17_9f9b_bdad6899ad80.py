'Hot Chili Pepper.\n\nSymbol plan: Curved tapered pepper with upper-right stem; asymmetric outline follows the reference.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e54b567-eac7-4a17-9f9b-bdad6899ad80'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/jalapen_8e54b567-eac7-4a17-9f9b-bdad6899ad80.svg'
AUTHOR = 'gpt-6'

class CurvedChiliPepper(Solo48):
    icon_id = 'curved-chili-pepper'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('curved', 'chili', 'pepper')

    def build(self):
        # Curved tapered pepper with upper-right stem; asymmetric outline follows the reference.
        axis_x = 24
        p_8_39 = (8, 39)
        p_8_41 = (8, 41)
        p_8_43 = (8, 43)
        p_9_39 = (9, 39)
        p_9_44 = (9, 44)
        p_10_38 = (10, 38)
        p_12_44 = (12, 44)
        p_17_19 = (17, 19)
        p_20_30 = (20, 30)
        p_21_44 = (21, 44)
        p_23_15 = (23, 15)
        p_30_8 = (30, 8)
        p_30_13 = (30, 13)
        p_31_9 = (31, 9)
        p_34_4 = (34, 4)
        p_36_36 = (36, 36)
        p_38_15 = (38, 15)
        p_38_24 = (38, 24)
        p_40_4 = (40, 4)
        self.add_bezier('pepper-1', p_23_15, (p_31_9, p_38_15, p_38_24))
        self.add_bezier('pepper-2', p_38_24, (p_36_36, p_21_44, p_12_44))
        self.add_bezier('pepper-3', p_12_44, (p_9_44, p_8_43, p_8_41))
        self.add_bezier('pepper-4', p_8_41, (p_8_39, p_9_39, p_10_38))
        self.add_bezier('pepper-5', p_10_38, (p_20_30, p_17_19, p_23_15))
        self.add_contour('pepper', 'pepper-1', 'pepper-2', 'pepper-3', 'pepper-4', 'pepper-5', closed=True)
        self.add_bezier('stem-1', p_30_13, (p_30_8, p_34_4, p_40_4))
        self.add_contour('stem', 'stem-1', closed=False)
        self.relate("connect", 'pepper', 'stem')
