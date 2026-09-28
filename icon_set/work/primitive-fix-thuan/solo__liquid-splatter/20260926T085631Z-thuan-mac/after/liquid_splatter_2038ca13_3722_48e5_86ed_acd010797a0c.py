'Liquid Splatter and Droplets.\n\nSymbol plan: Asymmetric smooth splatter with one detached ring droplet; reduce two small droplets to one.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "2038ca13-3722-48e5-86ed-acd010797a0c"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__liquid-splatter/20260926T085631Z-thuan-mac/reference/stain_2038ca13-3722-48e5-86ed-acd010797a0c.svg"
AUTHOR = "claude-opus-5-5"

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
        # Asymmetric smooth splatter with one detached ring droplet; reduce two small droplets to one.
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
        # Detached droplet: hollow r3 ring at (39,9), touching the SQUARE top and
        # right edges, drawn from four cardinal quarter arcs.
        cx, cy, r = 39, 9, 3
        pts = ((cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy))
        for k in range(4):
            self.add_arc(f'drop-{k}', pts[k], pts[(k + 1) % 4], radius_x=r, radius_y=r, sweep=True)
        self.add_contour('drop', *[f'drop-{k}' for k in range(4)], closed=True)
