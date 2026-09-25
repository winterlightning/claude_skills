'Pair of Underwear Briefs.\n\nSymbol plan: Mirrored briefs with two deep curved leg openings and a broad waistband. Shared side and crotch nodes keep opening attachments exact.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9d6a1c68-dc6b-43db-bb6a-c1ddc234f2ab'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/knickers_9d6a1c68-dc6b-43db-bb6a-c1ddc234f2ab.svg'
AUTHOR = 'gpt-6'

class Knickers(Solo48):
    icon_id = 'knickers'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('knickers',)

    def build(self):
        # Mirrored briefs with two deep curved leg openings and a broad waistband. Shared side and crotch nodes keep opening attachments exact.
        axis_x = 24
        p_4_8 = (4, 8)
        p_4_12 = (4, 12)
        p_5_16 = (5, 16)
        p_5_19 = (5, 19)
        p_6_26 = (6, 26)
        p_13_32 = (13, 32)
        p_14_19 = (14, 19)
        p_20_28 = (20, 28)
        p_20_40 = (20, 40)
        p_28_28 = (2 * axis_x - p_20_28[0], p_20_28[1])
        p_28_40 = (2 * axis_x - p_20_40[0], p_20_40[1])
        p_34_19 = (2 * axis_x - p_14_19[0], p_14_19[1])
        p_35_32 = (2 * axis_x - p_13_32[0], p_13_32[1])
        p_42_26 = (2 * axis_x - p_6_26[0], p_6_26[1])
        p_43_16 = (2 * axis_x - p_5_16[0], p_5_16[1])
        p_43_19 = (2 * axis_x - p_5_19[0], p_5_19[1])
        p_44_8 = (2 * axis_x - p_4_8[0], p_4_8[1])
        p_44_12 = (2 * axis_x - p_4_12[0], p_4_12[1])
        self.add_line('outline-1', p_4_8, p_44_8)
        self.add_bezier('outline-2', p_44_8, (p_44_12, p_43_16, p_43_19))
        self.add_bezier('outline-3', p_43_19, (p_42_26, p_35_32, p_28_40))
        self.add_line('outline-4', p_28_40, p_20_40)
        self.add_bezier('outline-5', p_20_40, (p_13_32, p_6_26, p_5_19))
        self.add_bezier('outline-6', p_5_19, (p_5_16, p_4_12, p_4_8))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', closed=True)
        self.add_bezier('left-opening-1', p_5_19, (p_14_19, p_20_28, p_20_40))
        self.add_contour('left-opening', 'left-opening-1', closed=False)
        self.add_bezier('right-opening-1', p_43_19, (p_34_19, p_28_28, p_28_40))
        self.add_contour('right-opening', 'right-opening-1', closed=False)
        self.relate("connect", 'outline', 'left-opening')
        self.relate("connect", 'outline', 'right-opening')
