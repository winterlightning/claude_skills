'Jicama Root Vegetable.\n\nSymbol plan: Rounded tapered jicama root with three open leaf strokes; omit closed leaf walls and veins to maintain spacing.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'baf35a0e-9b14-4dcb-8486-4f5d7ba488b6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/jicama_baf35a0e-9b14-4dcb-8486-4f5d7ba488b6.svg'
AUTHOR = 'gpt-6'

class RoundRootWithThreeLeaves(Solo48):
    icon_id = 'round-root-with-three-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('round', 'root', 'with', 'three', 'leaves')

    def build(self):
        # Rounded tapered jicama root with three open leaf strokes; omit closed leaf walls and veins to maintain spacing.
        axis_x = 24
        p_8_28 = (8, 28)
        p_8_33 = (8, 33)
        p_8_39 = (8, 39)
        p_10_10 = (10, 10)
        p_14_13 = (14, 13)
        p_14_24 = (14, 24)
        p_18_17 = (18, 17)
        p_18_40 = (18, 40)
        p_24_4 = (24, 4)
        p_24_24 = (24, 24)
        p_24_44 = (24, 44)
        p_30_17 = (2 * axis_x - p_18_17[0], p_18_17[1])
        p_30_40 = (2 * axis_x - p_18_40[0], p_18_40[1])
        p_34_13 = (2 * axis_x - p_14_13[0], p_14_13[1])
        p_34_24 = (2 * axis_x - p_14_24[0], p_14_24[1])
        p_38_10 = (2 * axis_x - p_10_10[0], p_10_10[1])
        p_40_28 = (2 * axis_x - p_8_28[0], p_8_28[1])
        p_40_33 = (2 * axis_x - p_8_33[0], p_8_33[1])
        p_40_39 = (2 * axis_x - p_8_39[0], p_8_39[1])
        self.add_bezier('root-1', p_24_24, (p_14_24, p_8_28, p_8_33))
        self.add_bezier('root-2', p_8_33, (p_8_39, p_18_40, p_24_44))
        self.add_bezier('root-3', p_24_44, (p_30_40, p_40_39, p_40_33))
        self.add_bezier('root-4', p_40_33, (p_40_28, p_34_24, p_24_24))
        self.add_contour('root', 'root-1', 'root-2', 'root-3', 'root-4', closed=True)
        self.add_bezier('leaves-1', p_10_10, (p_14_13, p_18_17, p_24_24))
        self.add_bezier('leaves-2', p_24_24, (p_30_17, p_34_13, p_38_10))
        self.add_contour('leaves', 'leaves-1', 'leaves-2', closed=False)
        self.relate("connect", 'root', 'leaves')
        self.add_line('central-leaf-1', p_24_4, p_24_24)
        self.add_contour('central-leaf', 'central-leaf-1', closed=False)
        self.relate("connect", 'root', 'central-leaf')
        self.relate("connect", 'leaves', 'central-leaf')
