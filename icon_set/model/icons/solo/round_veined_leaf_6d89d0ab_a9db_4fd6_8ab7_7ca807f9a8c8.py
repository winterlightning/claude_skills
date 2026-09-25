'Plant Sprout Symbol.\n\nSymbol plan: Broad circular leaf with a central stalk and two curved side veins; reduce four vein branches to two generous sweeps.\nKeyshape: CIRCLE; authored on SOLO48, not scaled from source.\nLucide: sprout.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6d89d0ab-a9db-4fd6-8ab7-7ca807f9a8c8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/vegetable brussel sprout_6d89d0ab-a9db-4fd6-8ab7-7ca807f9a8c8.svg'
AUTHOR = 'gpt-6'

class RoundVeinedLeaf(Solo48):
    icon_id = 'round-veined-leaf'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('round', 'veined', 'leaf')

    def build(self):
        # Broad circular leaf with a central stalk and two curved side veins; reduce four vein branches to two generous sweeps.
        axis_x = 24
        p_12_22 = (12, 22)
        p_14_25 = (14, 25)
        p_19_28 = (19, 28)
        p_20_14 = (20, 14)
        p_23_21 = (23, 21)
        p_24_4 = (24, 4)
        p_24_32 = (24, 32)
        p_24_44 = (24, 44)
        p_28_25 = (28, 25)
        p_32_23 = (32, 23)
        p_36_22 = (2 * axis_x - p_12_22[0], p_12_22[1])
        self.add_arc('leaf-1', p_24_44, p_24_4, radius_x=20, radius_y=20, sweep=True)
        self.add_arc('leaf-2', p_24_4, p_24_44, radius_x=20, radius_y=20, sweep=True)
        self.add_contour('leaf', 'leaf-1', 'leaf-2', closed=True)
        self.add_bezier('stem-1', p_24_44, (p_24_32, p_23_21, p_20_14))
        self.add_contour('stem', 'stem-1', closed=False)
        self.add_bezier('left-vein-1', p_24_32, (p_19_28, p_14_25, p_12_22))
        self.add_contour('left-vein', 'left-vein-1', closed=False)
        self.add_bezier('right-vein-1', p_24_32, (p_28_25, p_32_23, p_36_22))
        self.add_contour('right-vein', 'right-vein-1', closed=False)
        self.relate("connect", 'stem', 'leaf')
        self.relate("connect", 'stem', 'left-vein')
        self.relate("connect", 'stem', 'right-vein')
