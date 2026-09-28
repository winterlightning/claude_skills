'Person Lifting Dumbbell.\n\nSymbol plan: Person raises a dumbbell with equal weights either side of a vertical grip. Eight-unit horizontal separation keeps both weight ends distinct from the arm.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '17bb5f28-c6de-4e45-8379-d4c98addac37'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/exercise_17bb5f28-c6de-4e45-8379-d4c98addac37.svg'
AUTHOR = 'gpt-6'

class PersonRaisingDumbbell(Solo48):
    icon_id = 'person-raising-dumbbell'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('person', 'raising', 'dumbbell')

    def build(self):
        # Person raises a dumbbell with equal weights either side of a vertical grip. Eight-unit horizontal separation keeps both weight ends distinct from the arm.
        axis_x = 24
        p_6_31 = (6, 31)
        p_6_42 = (6, 42)
        p_8_11 = (8, 11)
        p_13_24 = (13, 24)
        p_13_34 = (13, 34)
        p_18_11 = (18, 11)
        p_24_30 = (24, 30)
        p_26_12 = (26, 12)
        p_26_16 = (26, 16)
        p_26_20 = (26, 20)
        p_27_42 = (27, 42)
        p_34_16 = (34, 16)
        p_34_30 = (34, 30)
        p_42_12 = (42, 12)
        p_42_16 = (42, 16)
        p_42_20 = (42, 20)
        self.add_arc('head-1', p_8_11, p_18_11, radius_x=5, radius_y=5, sweep=True)
        self.add_arc('head-2', p_18_11, p_8_11, radius_x=5, radius_y=5, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('torso-1', p_13_24, p_13_34)
        self.add_contour('torso', 'torso-1', closed=False)
        self.mark_human_figure("person", head="head", torso="torso-1", torso_junction="start")
        self.add_line('legs-1', p_6_42, p_13_34)
        self.add_line('legs-2', p_13_34, p_27_42)
        self.add_contour('legs', 'legs-1', 'legs-2', closed=False)
        self.relate("connect", 'legs', 'torso')
        self.add_line('arms-1', p_6_31, p_13_24)
        self.add_line('arms-2', p_13_24, p_24_30)
        self.add_line('arms-3', p_24_30, p_34_30)
        self.add_line('arms-4', p_34_30, p_34_16)
        self.add_contour('arms', 'arms-1', 'arms-2', 'arms-3', 'arms-4', closed=False)
        self.relate("connect", 'arms', 'torso')
        self.add_line('bar-1', p_26_16, p_34_16)
        self.add_line('bar-1-join-1', p_34_16, p_42_16)
        self.add_contour('bar', 'bar-1', 'bar-1-join-1', closed=False)
        self.add_line('weight-l-1', p_26_12, p_26_16)
        self.add_line('weight-l-1-join-1', p_26_16, p_26_20)
        self.add_contour('weight-l', 'weight-l-1', 'weight-l-1-join-1', closed=False)
        self.add_line('weight-r-1', p_42_12, p_42_16)
        self.add_line('weight-r-1-join-1', p_42_16, p_42_20)
        self.add_contour('weight-r', 'weight-r-1', 'weight-r-1-join-1', closed=False)
        self.relate("connect", 'bar', 'weight-l')
        self.relate("connect", 'bar', 'weight-r')
        self.relate("connect", 'arms', 'bar')
