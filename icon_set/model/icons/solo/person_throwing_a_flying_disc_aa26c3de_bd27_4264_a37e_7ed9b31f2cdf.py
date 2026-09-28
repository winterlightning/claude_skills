'Person Throwing a Frisbee.\n\nSymbol plan: Throwing figure reaches right toward an airborne disc; omit motion trail and second arm. Exact head gap at torso neck.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa26c3de-bd27-4264-a37e-7ed9b31f2cdf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/flung_aa26c3de-bd27-4264-a37e-7ed9b31f2cdf.svg'
AUTHOR = 'gpt-6'

class PersonThrowingAFlyingDisc(Solo48):
    icon_id = 'person-throwing-a-flying-disc'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('person', 'throwing', 'a', 'flying', 'disc')

    def build(self):
        # Throwing figure reaches right toward an airborne disc; omit motion trail and second arm. Exact head gap at torso neck.
        axis_x = 24
        p_6_42 = (6, 42)
        p_9_11 = (9, 11)
        p_14_24 = (14, 24)
        p_14_32 = (14, 32)
        p_19_11 = (19, 11)
        p_24_24 = (24, 24)
        p_25_42 = (25, 42)
        p_29_22 = (29, 22)
        p_30_6 = (30, 6)
        p_30_14 = (30, 14)
        p_34_6 = (34, 6)
        p_34_14 = (34, 14)
        p_38_6 = (38, 6)
        p_38_14 = (38, 14)
        p_42_7 = (42, 7)
        p_42_10 = (42, 10)
        p_42_13 = (42, 13)
        self.add_arc('head-1', p_9_11, p_19_11, radius_x=5, radius_y=5, sweep=True)
        self.add_arc('head-2', p_19_11, p_9_11, radius_x=5, radius_y=5, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('torso-1', p_14_24, p_14_32)
        self.add_contour('torso', 'torso-1', closed=False)
        self.mark_human_figure("person", head="head", torso="torso-1", torso_junction="start")
        self.add_line('legs-1', p_6_42, p_14_32)
        self.add_line('legs-2', p_14_32, p_25_42)
        self.add_contour('legs', 'legs-1', 'legs-2', closed=False)
        self.relate("connect", 'legs', 'torso')
        self.add_line('arms-1', p_14_24, p_24_24)
        self.add_line('arms-2', p_24_24, p_29_22)
        self.add_contour('arms', 'arms-1', 'arms-2', closed=False)
        self.relate("connect", 'arms', 'torso')
        self.add_bezier('disc-1', p_34_6, (p_38_6, p_42_7, p_42_10))
        self.add_bezier('disc-2', p_42_10, (p_42_13, p_38_14, p_34_14))
        self.add_bezier('disc-3', p_34_14, (p_30_14, p_30_6, p_34_6))
        self.add_contour('disc', 'disc-1', 'disc-2', 'disc-3', closed=True)
