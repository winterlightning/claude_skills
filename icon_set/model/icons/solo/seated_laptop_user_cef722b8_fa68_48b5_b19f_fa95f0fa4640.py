'Person Working on Laptop.\n\nSymbol plan: Seated laptop user facing left with chair back, open screen and bent legs. Exact 4-unit head gap.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cef722b8-fa68-48b5-b19f-fa95f0fa4640'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/work from home user sit_cef722b8-fa68-48b5-b19f-fa95f0fa4640.svg'
AUTHOR = 'gpt-6'

class SeatedLaptopUser(Solo48):
    icon_id = 'seated-laptop-user'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('seated', 'laptop', 'user')

    def build(self):
        # Seated laptop user facing left with chair back, open screen and bent legs. Exact 4-unit head gap.
        axis_x = 24
        p_8_15 = (8, 15)
        p_10_44 = (10, 44)
        p_12_26 = (12, 26)
        p_14_26 = (14, 26)
        p_15_34 = (15, 34)
        p_22_26 = (22, 26)
        p_23_9 = (23, 9)
        p_28_22 = (28, 22)
        p_28_34 = (28, 34)
        p_28_42 = (28, 42)
        p_33_9 = (33, 9)
        p_40_20 = (40, 20)
        p_40_34 = (40, 34)
        p_40_42 = (40, 42)
        self.add_arc('head-1', p_23_9, p_33_9, radius_x=5, radius_y=5, sweep=True)
        self.add_arc('head-2', p_33_9, p_23_9, radius_x=5, radius_y=5, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('torso-1', p_28_22, p_28_34)
        self.add_contour('torso', 'torso-1', closed=False)
        self.mark_human_figure("person", head="head", torso="torso-1", torso_junction="start")
        self.add_line('legs-1', p_28_34, p_15_34)
        self.add_line('legs-2', p_15_34, p_10_44)
        self.add_contour('legs', 'legs-1', 'legs-2', closed=False)
        self.relate("connect", 'legs', 'torso')
        self.add_line('arm-1', p_28_22, p_22_26)
        self.add_line('arm-2', p_22_26, p_14_26)
        self.add_contour('arm', 'arm-1', 'arm-2', closed=False)
        self.relate("connect", 'arm', 'torso')
        self.add_line('screen-1', p_8_15, p_12_26)
        self.add_line('screen-2', p_12_26, p_14_26)
        self.add_contour('screen', 'screen-1', 'screen-2', closed=False)
        self.relate("connect", 'screen', 'arm')
        self.add_line('chair-1', p_40_20, p_40_34)
        self.add_line('chair-1-join-1', p_40_34, p_40_42)
        self.add_line('chair-2', p_40_42, p_28_42)
        self.add_contour('chair', 'chair-1', 'chair-1-join-1', 'chair-2', closed=False)
        self.add_line('seat-1', p_28_34, p_40_34)
        self.add_contour('seat', 'seat-1', closed=False)
        self.relate("connect", 'seat', 'chair')
        self.relate("connect", 'seat', 'torso')
