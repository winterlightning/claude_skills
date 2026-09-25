'Person Holding a Balloon.\n\nSymbol plan: Figure holding a balloon string; oval balloon and circular head remain separate. Omit the second arm to avoid crowding.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e35d23a2-caaa-44fe-b722-3d1dffe53b5e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hold balloon_e35d23a2-caaa-44fe-b722-3d1dffe53b5e.svg'
AUTHOR = 'gpt-6'

class PersonHoldingBalloonString(Solo48):
    icon_id = 'person-holding-balloon-string'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('person', 'holding', 'balloon', 'string')

    def build(self):
        # Figure holding a balloon string; oval balloon and circular head remain separate. Omit the second arm to avoid crowding.
        axis_x = 24
        p_8_15 = (8, 15)
        p_8_44 = (8, 44)
        p_13_28 = (13, 28)
        p_13_34 = (13, 34)
        p_18_15 = (18, 15)
        p_19_44 = (19, 44)
        p_21_32 = (21, 32)
        p_26_7 = (26, 7)
        p_26_11 = (26, 11)
        p_26_16 = (26, 16)
        p_29_4 = (29, 4)
        p_30_21 = (30, 21)
        p_33_4 = (33, 4)
        p_33_23 = (33, 23)
        p_33_32 = (33, 32)
        p_36_21 = (36, 21)
        p_37_4 = (37, 4)
        p_40_7 = (40, 7)
        p_40_11 = (40, 11)
        p_40_16 = (40, 16)
        self.add_arc('head-1', p_8_15, p_18_15, radius_x=5, radius_y=5, sweep=True)
        self.add_arc('head-2', p_18_15, p_8_15, radius_x=5, radius_y=5, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('torso-1', p_13_28, p_13_34)
        self.add_contour('torso', 'torso-1', closed=False)
        self.mark_human_figure("person", head="head", torso="torso-1", torso_junction="start")
        self.add_line('legs-1', p_8_44, p_13_34)
        self.add_line('legs-2', p_13_34, p_19_44)
        self.add_contour('legs', 'legs-1', 'legs-2', closed=False)
        self.relate("connect", 'legs', 'torso')
        self.add_line('arm-1', p_13_28, p_21_32)
        self.add_line('arm-2', p_21_32, p_33_32)
        self.add_contour('arm', 'arm-1', 'arm-2', closed=False)
        self.relate("connect", 'arm', 'torso')
        self.add_bezier('balloon-1', p_33_4, (p_37_4, p_40_7, p_40_11))
        self.add_bezier('balloon-2', p_40_11, (p_40_16, p_36_21, p_33_23))
        self.add_bezier('balloon-3', p_33_23, (p_30_21, p_26_16, p_26_11))
        self.add_bezier('balloon-4', p_26_11, (p_26_7, p_29_4, p_33_4))
        self.add_contour('balloon', 'balloon-1', 'balloon-2', 'balloon-3', 'balloon-4', closed=True)
        self.add_line('string-1', p_33_23, p_33_32)
        self.add_contour('string', 'string-1', closed=False)
        self.relate("connect", 'string', 'balloon')
        self.relate("connect", 'string', 'arm')
