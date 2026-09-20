'Hot Dog with Mustard.\n\nSymbol plan: Broad bun, protruding sausage and shallow condiment wave; shared endpoints join bun and sausage.\nKeyshape: HRECT_M; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '66284022-0b49-42b4-88a5-98ecbc75d225'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/hot dog_66284022-0b49-42b4-88a5-98ecbc75d225.svg'
AUTHOR = 'gpt-6'

class HotDogWithWavyCondiment(Solo48):
    icon_id = 'hot-dog-with-wavy-condiment'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('hot', 'dog', 'with', 'wavy', 'condiment')

    def build(self):
        # Broad bun, protruding sausage and shallow condiment wave; shared endpoints join bun and sausage.
        axis_x = 24
        p_4_22 = (4, 22)
        p_4_27 = (4, 27)
        p_4_35 = (4, 35)
        p_6_18 = (6, 18)
        p_10_10 = (10, 10)
        p_10_18 = (10, 18)
        p_13_38 = (13, 38)
        p_15_10 = (15, 10)
        p_17_29 = (17, 29)
        p_19_27 = (19, 27)
        p_20_20 = (20, 20)
        p_21_27 = (21, 27)
        p_24_10 = (24, 10)
        p_24_29 = (24, 29)
        p_24_38 = (24, 38)
        p_27_27 = (2 * axis_x - p_21_27[0], p_21_27[1])
        p_28_20 = (2 * axis_x - p_20_20[0], p_20_20[1])
        p_29_27 = (2 * axis_x - p_19_27[0], p_19_27[1])
        p_31_29 = (2 * axis_x - p_17_29[0], p_17_29[1])
        p_33_10 = (2 * axis_x - p_15_10[0], p_15_10[1])
        p_35_38 = (2 * axis_x - p_13_38[0], p_13_38[1])
        p_38_10 = (2 * axis_x - p_10_10[0], p_10_10[1])
        p_38_18 = (2 * axis_x - p_10_18[0], p_10_18[1])
        p_42_18 = (2 * axis_x - p_6_18[0], p_6_18[1])
        p_44_22 = (2 * axis_x - p_4_22[0], p_4_22[1])
        p_44_27 = (2 * axis_x - p_4_27[0], p_4_27[1])
        p_44_35 = (2 * axis_x - p_4_35[0], p_4_35[1])
        self.add_bezier('bun-1', p_10_18, (p_6_18, p_4_22, p_4_27))
        self.add_bezier('bun-2', p_4_27, (p_4_35, p_13_38, p_24_38))
        self.add_bezier('bun-3', p_24_38, (p_35_38, p_44_35, p_44_27))
        self.add_bezier('bun-4', p_44_27, (p_44_22, p_42_18, p_38_18))
        self.add_bezier('bun-5', p_38_18, (p_28_20, p_20_20, p_10_18))
        self.add_contour('bun', 'bun-1', 'bun-2', 'bun-3', 'bun-4', 'bun-5', closed=True)
        self.add_bezier('sausage-1', p_10_18, (p_10_10, p_15_10, p_24_10))
        self.add_bezier('sausage-2', p_24_10, (p_33_10, p_38_10, p_38_18))
        self.add_contour('sausage', 'sausage-1', 'sausage-2', closed=False)
        self.relate("connect", 'bun', 'sausage')
        self.add_bezier('condiment-1', p_17_29, (p_19_27, p_21_27, p_24_29))
        self.add_bezier('condiment-2', p_24_29, (p_27_27, p_29_27, p_31_29))
        self.add_contour('condiment', 'condiment-1', 'condiment-2', closed=False)
