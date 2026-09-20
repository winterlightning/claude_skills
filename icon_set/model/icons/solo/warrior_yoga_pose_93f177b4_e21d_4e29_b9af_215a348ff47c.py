'Person in Yoga Warrior Pose.\n\nSymbol plan: Warrior pose with extended arms, bent left knee and straight right leg. Exact 4-unit head gap.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '93f177b4-e21d-4e29-b9af-215a348ff47c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/yoga_93f177b4-e21d-4e29-b9af-215a348ff47c.svg'
AUTHOR = 'gpt-6'

class WarriorYogaPose(Solo48):
    icon_id = 'warrior-yoga-pose'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('warrior', 'yoga', 'pose')

    def build(self):
        # Warrior pose with extended arms, bent left knee and straight right leg. Exact 4-unit head gap.
        axis_x = 24
        p_4_26 = (4, 26)
        p_8_35 = (8, 35)
        p_8_40 = (8, 40)
        p_19_13 = (19, 13)
        p_24_26 = (24, 26)
        p_24_35 = (24, 35)
        p_29_13 = (2 * axis_x - p_19_13[0], p_19_13[1])
        p_42_40 = (42, 40)
        p_44_26 = (2 * axis_x - p_4_26[0], p_4_26[1])
        self.add_arc('head-1', p_19_13, p_29_13, radius_x=5, radius_y=5, sweep=True)
        self.add_arc('head-2', p_29_13, p_19_13, radius_x=5, radius_y=5, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('torso-1', p_24_26, p_24_35)
        self.add_contour('torso', 'torso-1', closed=False)
        self.mark_human_figure("person", head="head", torso="torso-1", torso_junction="start")
        self.add_line('arms-1', p_4_26, p_24_26)
        self.add_line('arms-1-join-1', p_24_26, p_44_26)
        self.add_contour('arms', 'arms-1', 'arms-1-join-1', closed=False)
        self.relate("connect", 'arms', 'torso')
        self.add_line('legs-1', p_8_40, p_8_35)
        self.add_line('legs-2', p_8_35, p_24_35)
        self.add_line('legs-3', p_24_35, p_42_40)
        self.add_contour('legs', 'legs-1', 'legs-2', 'legs-3', closed=False)
        self.relate("connect", 'legs', 'torso')
