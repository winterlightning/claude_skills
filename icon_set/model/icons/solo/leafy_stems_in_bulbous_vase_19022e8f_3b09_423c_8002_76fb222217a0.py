'Potted Plant with Leaves.\n\nSymbol plan: Two leaves grow from a round vase; four decorative floating leaflets omitted for spacing.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: sprout.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '19022e8f-3b09-423c-8002-76fb222217a0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/flowers 1_19022e8f-3b09-423c-8002-76fb222217a0.svg'
AUTHOR = 'gpt-6'

class LeafyStemsInBulbousVase(Solo48):
    icon_id = 'leafy-stems-in-bulbous-vase'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'Uncategorized'
    aliases = ()
    keywords = ('leafy', 'stems', 'in', 'bulbous', 'vase')

    def build(self):
        # Two leaves grow from a round vase; four decorative floating leaflets omitted for spacing.
        axis_x = 24
        p_8_4 = (8, 4)
        p_8_8 = (8, 8)
        p_8_12 = (8, 12)
        p_12_34 = (12, 34)
        p_12_39 = (12, 39)
        p_12_44 = (12, 44)
        p_16_44 = (16, 44)
        p_17_12 = (17, 12)
        p_17_26 = (17, 26)
        p_17_32 = (17, 32)
        p_19_4 = (19, 4)
        p_21_8 = (21, 8)
        p_24_22 = (24, 22)
        p_24_26 = (24, 26)
        p_24_44 = (24, 44)
        p_27_8 = (2 * axis_x - p_21_8[0], p_21_8[1])
        p_29_4 = (2 * axis_x - p_19_4[0], p_19_4[1])
        p_31_12 = (2 * axis_x - p_17_12[0], p_17_12[1])
        p_31_26 = (2 * axis_x - p_17_26[0], p_17_26[1])
        p_31_32 = (2 * axis_x - p_17_32[0], p_17_32[1])
        p_32_44 = (2 * axis_x - p_16_44[0], p_16_44[1])
        p_36_34 = (2 * axis_x - p_12_34[0], p_12_34[1])
        p_36_39 = (2 * axis_x - p_12_39[0], p_12_39[1])
        p_36_44 = (2 * axis_x - p_12_44[0], p_12_44[1])
        p_40_4 = (2 * axis_x - p_8_4[0], p_8_4[1])
        p_40_8 = (2 * axis_x - p_8_8[0], p_8_8[1])
        p_40_12 = (2 * axis_x - p_8_12[0], p_8_12[1])
        self.add_line('vase-1', p_17_26, p_24_26)
        self.add_line('vase-1-join-1', p_24_26, p_31_26)
        self.add_bezier('vase-2', p_31_26, (p_31_32, p_36_34, p_36_39))
        self.add_bezier('vase-3', p_36_39, (p_36_44, p_32_44, p_24_44))
        self.add_bezier('vase-4', p_24_44, (p_16_44, p_12_44, p_12_39))
        self.add_bezier('vase-5', p_12_39, (p_12_34, p_17_32, p_17_26))
        self.add_contour('vase', 'vase-1', 'vase-1-join-1', 'vase-2', 'vase-3', 'vase-4', 'vase-5', closed=True)
        self.add_line('stems-1', p_17_12, p_24_22)
        self.add_line('stems-2', p_24_22, p_24_26)
        self.add_contour('stems', 'stems-1', 'stems-2', closed=False)
        self.add_line('branch-1', p_24_22, p_31_12)
        self.add_contour('branch', 'branch-1', closed=False)
        self.relate("connect", 'stems', 'branch')
        self.relate("connect", 'stems', 'vase')
        self.add_bezier('left-leaf-1', p_17_12, (p_8_12, p_8_8, p_8_4))
        self.add_bezier('left-leaf-2', p_8_4, (p_19_4, p_21_8, p_17_12))
        self.add_contour('left-leaf', 'left-leaf-1', 'left-leaf-2', closed=True)
        self.add_bezier('right-leaf-1', p_31_12, (p_27_8, p_29_4, p_40_4))
        self.add_bezier('right-leaf-2', p_40_4, (p_40_8, p_40_12, p_31_12))
        self.add_contour('right-leaf', 'right-leaf-1', 'right-leaf-2', closed=True)
        self.relate("connect", 'stems', 'left-leaf')
        self.relate("connect", 'branch', 'right-leaf')
