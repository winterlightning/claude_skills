'Hyacinth Flower Bud Stem.\n\nSymbol plan: Three-lobed flower bud above two pairs of open leaf strokes; simplify enclosed leaves to preserve their count.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: flower-2.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '64c04d73-5ded-4395-9dd9-84ca81590c1d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/hyacinth_64c04d73-5ded-4395-9dd9-84ca81590c1d.svg'
AUTHOR = 'gpt-6'

class FlowerBudWithPairedLeaves(Solo48):
    icon_id = 'flower-bud-with-paired-leaves'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('flower', 'bud', 'with', 'paired', 'leaves')

    def build(self):
        # Three-lobed flower bud above two pairs of open leaf strokes; simplify enclosed leaves to preserve their count.
        axis_x = 24
        p_8_24 = (8, 24)
        p_8_36 = (8, 36)
        p_12_20 = (12, 20)
        p_12_30 = (12, 30)
        p_12_42 = (12, 42)
        p_14_12 = (14, 12)
        p_16_12 = (16, 12)
        p_18_8 = (18, 8)
        p_18_32 = (18, 32)
        p_18_44 = (18, 44)
        p_20_4 = (20, 4)
        p_20_14 = (20, 14)
        p_24_4 = (24, 4)
        p_24_20 = (24, 20)
        p_24_32 = (24, 32)
        p_24_44 = (24, 44)
        p_28_4 = (2 * axis_x - p_20_4[0], p_20_4[1])
        p_28_14 = (2 * axis_x - p_20_14[0], p_20_14[1])
        p_30_8 = (2 * axis_x - p_18_8[0], p_18_8[1])
        p_30_32 = (2 * axis_x - p_18_32[0], p_18_32[1])
        p_30_44 = (2 * axis_x - p_18_44[0], p_18_44[1])
        p_32_12 = (2 * axis_x - p_16_12[0], p_16_12[1])
        p_34_12 = (2 * axis_x - p_14_12[0], p_14_12[1])
        p_36_20 = (2 * axis_x - p_12_20[0], p_12_20[1])
        p_36_30 = (2 * axis_x - p_12_30[0], p_12_30[1])
        p_36_42 = (2 * axis_x - p_12_42[0], p_12_42[1])
        p_40_24 = (2 * axis_x - p_8_24[0], p_8_24[1])
        p_40_36 = (2 * axis_x - p_8_36[0], p_8_36[1])
        self.add_bezier('bloom-1', p_24_20, (p_12_20, p_14_12, p_16_12))
        self.add_line('bloom-2', p_16_12, p_20_14)
        self.add_bezier('bloom-3', p_20_14, (p_18_8, p_20_4, p_24_4))
        self.add_bezier('bloom-4', p_24_4, (p_28_4, p_30_8, p_28_14))
        self.add_line('bloom-5', p_28_14, p_32_12)
        self.add_bezier('bloom-6', p_32_12, (p_34_12, p_36_20, p_24_20))
        self.add_contour('bloom', 'bloom-1', 'bloom-2', 'bloom-3', 'bloom-4', 'bloom-5', 'bloom-6', closed=True)
        self.add_line('stem-1', p_24_20, p_24_44)
        self.add_contour('stem', 'stem-1', closed=False)
        self.relate("connect", 'bloom', 'stem')
        self.add_bezier('leaves-28-1', p_8_24, (p_12_30, p_18_32, p_24_32))
        self.add_bezier('leaves-28-2', p_24_32, (p_30_32, p_36_30, p_40_24))
        self.add_contour('leaves-28', 'leaves-28-1', 'leaves-28-2', closed=False)
        self.relate("connect", 'stem', 'leaves-28')
        self.add_bezier('leaves-40-1', p_8_36, (p_12_42, p_18_44, p_24_44))
        self.add_bezier('leaves-40-2', p_24_44, (p_30_44, p_36_42, p_40_36))
        self.add_contour('leaves-40', 'leaves-40-1', 'leaves-40-2', closed=False)
        self.relate("connect", 'stem', 'leaves-40')
