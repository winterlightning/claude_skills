'Loaf of Bread.\n\nSymbol plan: Wide domed loaf with two well-spaced scores; reduce three cuts to two.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e29d9ec2-8f36-47bd-baba-22a35e21d40e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/loaf_e29d9ec2-8f36-47bd-baba-22a35e21d40e.svg'
AUTHOR = 'gpt-6'

class ScoredBreadLoaf(Solo48):
    icon_id = 'scored-bread-loaf'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('scored', 'bread', 'loaf')

    def build(self):
        # Wide domed loaf with two well-spaced scores; reduce three cuts to two.
        axis_x = 24
        p_4_15 = (4, 15)
        p_4_30 = (4, 30)
        p_4_34 = (4, 34)
        p_10_40 = (10, 40)
        p_11_8 = (11, 8)
        p_19_9 = (19, 9)
        p_19_21 = (19, 21)
        p_24_8 = (24, 8)
        p_29_9 = (2 * axis_x - p_19_9[0], p_19_9[1])
        p_29_21 = (2 * axis_x - p_19_21[0], p_19_21[1])
        p_37_8 = (2 * axis_x - p_11_8[0], p_11_8[1])
        p_38_40 = (2 * axis_x - p_10_40[0], p_10_40[1])
        p_44_15 = (2 * axis_x - p_4_15[0], p_4_15[1])
        p_44_30 = (2 * axis_x - p_4_30[0], p_4_30[1])
        p_44_34 = (2 * axis_x - p_4_34[0], p_4_34[1])
        self.add_bezier('loaf-1', p_4_30, (p_4_15, p_11_8, p_24_8))
        self.add_bezier('loaf-2', p_24_8, (p_37_8, p_44_15, p_44_30))
        self.add_line('loaf-3', p_44_30, p_44_34)
        self.add_arc('loaf-4', p_44_34, p_38_40, radius_x=6, radius_y=6, sweep=True)
        self.add_line('loaf-5', p_38_40, p_10_40)
        self.add_arc('loaf-6', p_10_40, p_4_34, radius_x=6, radius_y=6, sweep=True)
        self.add_line('loaf-7', p_4_34, p_4_30)
        self.add_contour('loaf', 'loaf-1', 'loaf-2', 'loaf-3', 'loaf-4', 'loaf-5', 'loaf-6', 'loaf-7', closed=True)
        self.add_line('score-19-1', p_19_9, p_19_21)
        self.add_contour('score-19', 'score-19-1', closed=False)
        self.relate("connect", 'loaf', 'score-19')
        self.add_line('score-29-1', p_29_9, p_29_21)
        self.add_contour('score-29', 'score-29-1', closed=False)
        self.relate("connect", 'loaf', 'score-29')
