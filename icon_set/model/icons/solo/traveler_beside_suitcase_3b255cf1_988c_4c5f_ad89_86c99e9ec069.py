'Person with Suitcase.\n\nSymbol plan: Traveler stands beside a handled suitcase. Simple front-facing figure replaces the detailed profile; exact circular-head clearance.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3b255cf1-988c-4c5f-ad89-86c99e9ec069'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/foreigner_3b255cf1-988c-4c5f-ad89-86c99e9ec069.svg'
AUTHOR = 'gpt-6'

class TravelerBesideSuitcase(Solo48):
    icon_id = 'traveler-beside-suitcase'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('traveler', 'beside', 'suitcase')

    def build(self):
        # Traveler stands beside a handled suitcase. Simple front-facing figure replaces the detailed profile; exact circular-head clearance.
        axis_x = 24
        p_6_42 = (6, 42)
        p_7_11 = (7, 11)
        p_12_24 = (12, 24)
        p_12_34 = (12, 34)
        p_17_11 = (17, 11)
        p_18_42 = (18, 42)
        p_28_28 = (28, 28)
        p_28_40 = (28, 40)
        p_30_26 = (30, 26)
        p_30_42 = (2 * axis_x - p_18_42[0], p_18_42[1])
        p_31_18 = (31, 18)
        p_31_26 = (31, 26)
        p_39_18 = (39, 18)
        p_39_26 = (39, 26)
        p_40_26 = (40, 26)
        p_40_42 = (40, 42)
        p_42_28 = (42, 28)
        p_42_40 = (42, 40)
        self.add_arc('head-1', p_7_11, p_17_11, radius_x=5, radius_y=5, sweep=True)
        self.add_arc('head-2', p_17_11, p_7_11, radius_x=5, radius_y=5, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('torso-1', p_12_24, p_12_34)
        self.add_contour('torso', 'torso-1', closed=False)
        self.mark_human_figure("person", head="head", torso="torso-1", torso_junction="start")
        self.add_line('legs-1', p_6_42, p_12_34)
        self.add_line('legs-2', p_12_34, p_18_42)
        self.add_contour('legs', 'legs-1', 'legs-2', closed=False)
        self.relate("connect", 'legs', 'torso')
        self.add_line('case-1', p_30_26, p_31_26)
        self.add_line('case-1-join-1', p_31_26, p_39_26)
        self.add_line('case-1-join-2', p_39_26, p_40_26)
        self.add_arc('case-2', p_40_26, p_42_28, radius_x=2, radius_y=2, sweep=True)
        self.add_line('case-3', p_42_28, p_42_40)
        self.add_arc('case-4', p_42_40, p_40_42, radius_x=2, radius_y=2, sweep=True)
        self.add_line('case-5', p_40_42, p_30_42)
        self.add_arc('case-6', p_30_42, p_28_40, radius_x=2, radius_y=2, sweep=True)
        self.add_line('case-7', p_28_40, p_28_28)
        self.add_arc('case-8', p_28_28, p_30_26, radius_x=2, radius_y=2, sweep=True)
        self.add_contour('case', 'case-1', 'case-1-join-1', 'case-1-join-2', 'case-2', 'case-3', 'case-4', 'case-5', 'case-6', 'case-7', 'case-8', closed=True)
        self.add_line('handle-1', p_31_26, p_31_18)
        self.add_line('handle-2', p_31_18, p_39_18)
        self.add_line('handle-3', p_39_18, p_39_26)
        self.add_contour('handle', 'handle-1', 'handle-2', 'handle-3', closed=False)
        self.relate("connect", 'case', 'handle')
