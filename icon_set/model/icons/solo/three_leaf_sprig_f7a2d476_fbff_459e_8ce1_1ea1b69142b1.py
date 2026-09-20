'Plant Stem with Three Leaves.\n\nSymbol plan: Three broad leaves join a shared stem at staggered heights. The stem stops at leaf attachment points; fine veins omitted.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: sprout.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f7a2d476-fbff-459e-8ce1-1ea1b69142b1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/greens_f7a2d476-fbff-459e-8ce1-1ea1b69142b1.svg'
AUTHOR = 'gpt-6'

class ThreeLeafSprig(Solo48):
    icon_id = 'three-leaf-sprig'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('three', 'leaf', 'sprig')

    def build(self):
        # Three broad leaves join a shared stem at staggered heights. The stem stops at leaf attachment points; fine veins omitted.
        axis_x = 24
        p_8_18 = (8, 18)
        p_8_23 = (8, 23)
        p_8_31 = (8, 31)
        p_19_18 = (19, 18)
        p_20_30 = (20, 30)
        p_20_39 = (20, 39)
        p_20_44 = (20, 44)
        p_23_24 = (23, 24)
        p_24_8 = (24, 8)
        p_26_18 = (26, 18)
        p_26_35 = (26, 35)
        p_30_46 = (30, 46)
        p_31_4 = (31, 4)
        p_32_33 = (32, 33)
        p_33_18 = (33, 18)
        p_38_4 = (38, 4)
        p_40_14 = (40, 14)
        p_40_33 = (40, 33)
        p_40_44 = (40, 44)
        self.add_bezier('top-1', p_26_18, (p_24_8, p_31_4, p_38_4))
        self.add_bezier('top-2', p_38_4, (p_40_14, p_33_18, p_26_18))
        self.add_contour('top', 'top-1', 'top-2', closed=True)
        self.add_bezier('left-1', p_20_30, (p_8_31, p_8_23, p_8_18))
        self.add_bezier('left-2', p_8_18, (p_19_18, p_23_24, p_20_30))
        self.add_contour('left', 'left-1', 'left-2', closed=True)
        self.add_bezier('right-1', p_20_39, (p_26_35, p_32_33, p_40_33))
        self.add_bezier('right-2', p_40_33, (p_40_44, p_30_46, p_20_39))
        self.add_contour('right', 'right-1', 'right-2', closed=True)
        self.add_line('stem-1', p_20_44, p_20_39)
        self.add_line('stem-2', p_20_39, p_20_30)
        self.add_line('stem-3', p_20_30, p_26_18)
        self.add_contour('stem', 'stem-1', 'stem-2', 'stem-3', closed=False)
        self.relate("connect", 'stem', 'top')
        self.relate("connect", 'stem', 'left')
        self.relate("connect", 'stem', 'right')
