'Person Working from Home with Laptop.\n\nSymbol plan: Person using a laptop beneath a roof. Shared circular-head construction and clear architectural context; omit hidden body detail.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '44ffdb4d-63c5-4a9d-96a6-0694a78bbb7c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/work from home user laptop 2_44ffdb4d-63c5-4a9d-96a6-0694a78bbb7c.svg'
AUTHOR = 'gpt-6'

class WorkingFromHome(Solo48):
    icon_id = 'working-from-home'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('working', 'from', 'home')

    def build(self):
        # Person using a laptop beneath a roof. Shared circular-head construction and clear architectural context; omit hidden body detail.
        axis_x = 24
        p_6_15 = (6, 15)
        p_9_25 = (9, 25)
        p_13_37 = (13, 37)
        p_13_42 = (13, 42)
        p_17_25 = (17, 25)
        p_24_6 = (24, 6)
        p_24_42 = (24, 42)
        p_30_27 = (30, 27)
        p_38_42 = (38, 42)
        p_42_15 = (2 * axis_x - p_6_15[0], p_6_15[1])
        p_42_27 = (42, 27)
        self.add_line('roof-1', p_6_15, p_24_6)
        self.add_line('roof-2', p_24_6, p_42_15)
        self.add_contour('roof', 'roof-1', 'roof-2', closed=False)
        self.add_arc('head-1', p_9_25, p_17_25, radius_x=4, radius_y=4, sweep=True)
        self.add_arc('head-2', p_17_25, p_9_25, radius_x=4, radius_y=4, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('torso-1', p_13_37, p_13_42)
        self.add_contour('torso', 'torso-1', closed=False)
        self.mark_human_figure("person", head="head", torso="torso-1", torso_junction="start")
        self.add_line('laptop-1', p_24_42, p_30_27)
        self.add_line('laptop-2', p_30_27, p_42_27)
        self.add_line('laptop-3', p_42_27, p_38_42)
        self.add_line('laptop-4', p_38_42, p_24_42)
        self.add_contour('laptop', 'laptop-1', 'laptop-2', 'laptop-3', 'laptop-4', closed=False)
        self.add_line('arm-1', p_13_37, p_24_42)
        self.add_contour('arm', 'arm-1', closed=False)
        self.relate("connect", 'arm', 'torso')
        self.relate("connect", 'arm', 'laptop')
