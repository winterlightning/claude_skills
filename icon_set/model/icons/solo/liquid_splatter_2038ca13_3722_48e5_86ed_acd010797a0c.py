'Liquid Splatter and Droplets.\n\nSymbol plan: Asymmetric smooth splatter with one detached droplet; reduce two small droplets to one.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2038ca13-3722-48e5-86ed-acd010797a0c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/stain_2038ca13-3722-48e5-86ed-acd010797a0c.svg'
AUTHOR = 'gpt-6'

class LiquidSplatter(Solo48):
    icon_id = 'liquid-splatter'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('liquid', 'splatter')

    def build(self):
        # Asymmetric smooth splatter with one detached droplet; reduce two small droplets to one.
        axis_x = 24
        p_6_18 = (6, 18)
        p_6_28 = (6, 28)
        p_6_33 = (6, 33)
        p_8_38 = (8, 38)
        p_12_6 = (12, 6)
        p_14_15 = (14, 15)
        p_15_23 = (15, 23)
        p_16_34 = (16, 34)
        p_19_42 = (19, 42)
        p_22_6 = (22, 6)
        p_24_6 = (24, 6)
        p_24_18 = (24, 18)
        p_24_32 = (24, 32)
        p_27_42 = (27, 42)
        p_29_6 = (29, 6)
        p_29_31 = (29, 31)
        p_32_20 = (32, 20)
        p_35_29 = (35, 29)
        p_36_42 = (36, 42)
        p_38_8 = (38, 8)
        p_42_8 = (42, 8)
        p_42_21 = (42, 21)
        p_42_27 = (42, 27)
        self.add_bezier('splash-1', p_6_28, (p_6_18, p_15_23, p_14_15))
        self.add_bezier('splash-2', p_14_15, (p_12_6, p_22_6, p_24_6))
        self.add_bezier('splash-3', p_24_6, (p_29_6, p_24_18, p_32_20))
        self.add_bezier('splash-4', p_32_20, (p_42_21, p_42_27, p_35_29))
        self.add_bezier('splash-5', p_35_29, (p_29_31, p_36_42, p_27_42))
        self.add_bezier('splash-6', p_27_42, (p_19_42, p_24_32, p_16_34))
        self.add_bezier('splash-7', p_16_34, (p_8_38, p_6_33, p_6_28))
        self.add_contour('splash', 'splash-1', 'splash-2', 'splash-3', 'splash-4', 'splash-5', 'splash-6', 'splash-7', closed=True)
        self.add_arc('drop-1', p_38_8, p_42_8, radius_x=2, radius_y=2, sweep=True)
        self.add_arc('drop-2', p_42_8, p_38_8, radius_x=2, radius_y=2, sweep=True)
        self.add_contour('drop', 'drop-1', 'drop-2', closed=True)
