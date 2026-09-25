'Meditating Buddha Statue.\n\nSymbol plan: Seated Buddha with circular head, robe and broad crossed-leg base; omit small halo rays to preserve proportions.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9c4fcc62-4575-453e-9566-a7f24bb9a3bd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/landmark buddha statue_9c4fcc62-4575-453e-9566-a7f24bb9a3bd.svg'
AUTHOR = 'gpt-6'

class SeatedBuddhaStatue(Solo48):
    icon_id = 'seated-buddha-statue'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('seated', 'buddha', 'statue')

    def build(self):
        # Seated Buddha with circular head, robe and broad crossed-leg base; omit small halo rays to preserve proportions.
        axis_x = 24
        p_8_34 = (8, 34)
        p_8_37 = (8, 37)
        p_8_39 = (8, 39)
        p_8_44 = (8, 44)
        p_12_27 = (12, 27)
        p_12_34 = (12, 34)
        p_16_44 = (16, 44)
        p_17_24 = (17, 24)
        p_18_10 = (18, 10)
        p_24_24 = (24, 24)
        p_24_31 = (24, 31)
        p_24_44 = (24, 44)
        p_30_10 = (2 * axis_x - p_18_10[0], p_18_10[1])
        p_31_24 = (2 * axis_x - p_17_24[0], p_17_24[1])
        p_32_44 = (2 * axis_x - p_16_44[0], p_16_44[1])
        p_36_27 = (2 * axis_x - p_12_27[0], p_12_27[1])
        p_36_34 = (2 * axis_x - p_12_34[0], p_12_34[1])
        p_40_34 = (2 * axis_x - p_8_34[0], p_8_34[1])
        p_40_37 = (2 * axis_x - p_8_37[0], p_8_37[1])
        p_40_39 = (2 * axis_x - p_8_39[0], p_8_39[1])
        p_40_44 = (2 * axis_x - p_8_44[0], p_8_44[1])
        self.add_arc('head-1', p_18_10, p_30_10, radius_x=6, radius_y=6, sweep=True)
        self.add_arc('head-2', p_30_10, p_18_10, radius_x=6, radius_y=6, sweep=True)
        self.add_contour('head', 'head-1', 'head-2', closed=True)
        self.add_line('torso-1', p_24_24, p_24_31)
        self.add_contour('torso', 'torso-1', closed=False)
        self.add_bezier('robe-1', p_12_34, (p_12_27, p_17_24, p_24_24))
        self.add_bezier('robe-2', p_24_24, (p_31_24, p_36_27, p_36_34))
        self.add_contour('robe', 'robe-1', 'robe-2', closed=False)
        self.relate("connect", 'torso', 'robe')
        self.add_bezier('legs-1', p_12_34, (p_8_34, p_8_37, p_8_39))
        self.add_bezier('legs-2', p_8_39, (p_8_44, p_16_44, p_24_44))
        self.add_bezier('legs-3', p_24_44, (p_32_44, p_40_44, p_40_39))
        self.add_bezier('legs-4', p_40_39, (p_40_37, p_40_34, p_36_34))
        self.add_line('legs-5', p_36_34, p_12_34)
        self.add_contour('legs', 'legs-1', 'legs-2', 'legs-3', 'legs-4', 'legs-5', closed=True)
        self.relate("connect", 'robe', 'legs')
        self.mark_human_figure("buddha", head="head", torso="torso-1", torso_junction="start")
