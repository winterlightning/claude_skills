'Person Fixing Ceiling Lamp.\n\nSymbol plan: Person reaches up to a pendant lamp. The reaching hand meets the shade; body uses the exact detached head gap.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6f4ee788-e4fb-4264-83ea-ab395e4598e7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/home improvement 9_6f4ee788-e4fb-4264-83ea-ab395e4598e7.svg'
AUTHOR = 'gpt-6'

class PersonReachingTowardHangingLamp(Solo48):
    icon_id = 'person-reaching-toward-hanging-lamp'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('person', 'reaching', 'toward', 'hanging', 'lamp')

    def build(self):
        # Person reaches up to a pendant lamp. The reaching hand meets the shade; body uses the exact detached head gap.
        axis_x = 24
        p_8_30 = (8, 30)
        p_8_44 = (8, 44)
        p_9_9 = (9, 9)
        p_14_22 = (14, 22)
        p_14_32 = (14, 32)
        p_19_9 = (19, 9)
        p_24_44 = (24, 44)
        p_27_22 = (27, 22)
        p_28_12 = (28, 12)
        p_30_12 = (30, 12)
        p_34_4 = (34, 4)
        p_34_6 = (34, 6)
        p_40_12 = (40, 12)
        self.add_arc('head-1', p_9_9, p_19_9, radius_x=5, radius_y=5, sweep=True)
        self.add_arc('head-2', p_19_9, p_9_9, radius_x=5, radius_y=5, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('torso-1', p_14_22, p_14_32)
        self.add_contour('torso', 'torso-1', closed=False)
        self.mark_human_figure("person", head="head", torso="torso-1", torso_junction="start")
        self.add_line('legs-1', p_8_44, p_14_32)
        self.add_line('legs-2', p_14_32, p_24_44)
        self.add_contour('legs', 'legs-1', 'legs-2', closed=False)
        self.relate("connect", 'legs', 'torso')
        self.add_line('arms-1', p_8_30, p_14_22)
        self.add_line('arms-2', p_14_22, p_27_22)
        self.add_line('arms-3', p_27_22, p_30_12)
        self.add_contour('arms', 'arms-1', 'arms-2', 'arms-3', closed=False)
        self.relate("connect", 'arms', 'torso')
        self.add_arc('lamp-1', p_28_12, p_40_12, radius_x=6, radius_y=6, sweep=True)
        self.add_line('lamp-2', p_40_12, p_30_12)
        self.add_line('lamp-3', p_30_12, p_28_12)
        self.add_contour('lamp', 'lamp-1', 'lamp-2', 'lamp-3', closed=True)
        self.add_line('cord-1', p_34_4, p_34_6)
        self.add_contour('cord', 'cord-1', closed=False)
        self.relate("connect", 'lamp', 'cord')
        self.relate("connect", 'arms', 'lamp')
