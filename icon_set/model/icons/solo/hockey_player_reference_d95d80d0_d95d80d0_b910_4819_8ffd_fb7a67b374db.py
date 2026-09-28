'Ice Hockey Player.\n\nSymbol plan: Hockey pose with bent knees, stick and puck. Head r4 at (24,12); torso starts (24,24), exactly 4 ink units below head. Human full-body reference controls proportions.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd95d80d0-b910-4819-8ffd-fb7a67b374db'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/winter sport ice hockey_d95d80d0-b910-4819-8ffd-fb7a67b374db.svg'
AUTHOR = 'gpt-6'

class HockeyPlayerReferenceD95D80D0(Solo48):
    icon_id = 'hockey-player-reference-d95d80d0'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('hockey', 'player', 'reference', 'd95d80d0')

    def build(self):
        # Hockey pose with bent knees, stick and puck. Head r4 at (24,12); torso starts (24,24), exactly 4 ink units below head. Human full-body reference controls proportions.
        axis_x = 24
        p_4_40 = (4, 40)
        p_5_40 = (5, 40)
        p_14_40 = (14, 40)
        p_17_38 = (17, 38)
        p_18_26 = (18, 26)
        p_20_12 = (20, 12)
        p_24_24 = (24, 24)
        p_24_27 = (24, 27)
        p_24_35 = (24, 35)
        p_27_40 = (27, 40)
        p_28_12 = (2 * axis_x - p_20_12[0], p_20_12[1])
        p_29_27 = (29, 27)
        p_30_30 = (30, 30)
        p_37_34 = (37, 34)
        p_44_38 = (44, 38)
        self.add_arc('head-1', p_20_12, p_28_12, radius_x=4, radius_y=4, sweep=True)
        self.add_arc('head-2', p_28_12, p_20_12, radius_x=4, radius_y=4, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_bezier('torso-1', p_24_24, (p_24_27, p_29_27, p_30_30))
        self.add_contour('torso', 'torso-1', closed=False)
        self.add_line('front-leg-1', p_30_30, p_24_35)
        self.add_line('front-leg-2', p_24_35, p_27_40)
        self.add_contour('front-leg', 'front-leg-1', 'front-leg-2', closed=False)
        self.relate("connect", 'torso', 'front-leg')
        self.add_line('back-leg-1', p_30_30, p_37_34)
        self.add_line('back-leg-2', p_37_34, p_44_38)
        self.add_contour('back-leg', 'back-leg-1', 'back-leg-2', closed=False)
        self.relate("connect", 'torso', 'back-leg')
        self.add_line('arm-1', p_24_24, p_18_26)
        self.add_contour('arm', 'arm-1', closed=False)
        self.relate("connect", 'torso', 'arm')
        self.add_line('stick-1', p_18_26, p_17_38)
        self.add_line('stick-2', p_17_38, p_14_40)
        self.add_contour('stick', 'stick-1', 'stick-2', closed=False)
        self.relate("connect", 'arm', 'stick')
        self.add_line('puck-1', p_4_40, p_5_40)
        self.add_contour('puck', 'puck-1', closed=False)
        self.mark_human_figure("player", head="head", torso="torso-1", torso_junction="start")
