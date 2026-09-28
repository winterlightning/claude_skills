'Leaf above wavy water.\n\nSymbol plan: Upright leaf with open vein grows from two water waves; natural plant-water scene.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '921de2f2-6120-4b0c-ac2b-49f805c2c36a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/floodplain_921de2f2-6120-4b0c-ac2b-49f805c2c36a.svg'
AUTHOR = 'gpt-6'

class LeafGrowingFromWater(Solo48):
    icon_id = 'leaf-growing-from-water'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('leaf', 'growing', 'from', 'water')

    def build(self):
        # Upright leaf with open vein grows from two water waves; natural plant-water scene.
        axis_x = 24
        p_8_33 = (8, 33)
        p_8_44 = (8, 44)
        p_10_14 = (10, 14)
        p_12_25 = (12, 25)
        p_13_33 = (13, 33)
        p_13_43 = (13, 43)
        p_15_4 = (15, 4)
        p_19_33 = (19, 33)
        p_19_43 = (19, 43)
        p_24_25 = (24, 25)
        p_24_33 = (24, 33)
        p_24_44 = (24, 44)
        p_28_4 = (28, 4)
        p_29_33 = (2 * axis_x - p_19_33[0], p_19_33[1])
        p_29_43 = (2 * axis_x - p_19_43[0], p_19_43[1])
        p_35_13 = (35, 13)
        p_35_33 = (2 * axis_x - p_13_33[0], p_13_33[1])
        p_35_43 = (2 * axis_x - p_13_43[0], p_13_43[1])
        p_40_33 = (2 * axis_x - p_8_33[0], p_8_33[1])
        p_40_44 = (2 * axis_x - p_8_44[0], p_8_44[1])
        self.add_bezier('leaf-1', p_24_25, (p_12_25, p_10_14, p_15_4))
        self.add_bezier('leaf-2', p_15_4, (p_28_4, p_35_13, p_24_25))
        self.add_contour('leaf', 'leaf-1', 'leaf-2', closed=True)
        self.add_line('stem-1', p_24_25, p_24_33)
        self.add_contour('stem', 'stem-1', closed=False)
        self.relate("connect", 'leaf', 'stem')
        self.add_bezier('water-33-1', p_8_33, (p_13_33, p_19_33, p_24_33))
        self.add_bezier('water-33-2', p_24_33, (p_29_33, p_35_33, p_40_33))
        self.add_contour('water-33', 'water-33-1', 'water-33-2', closed=False)
        self.add_bezier('water-44-1', p_8_44, (p_13_43, p_19_43, p_24_44))
        self.add_bezier('water-44-2', p_24_44, (p_29_43, p_35_43, p_40_44))
        self.add_contour('water-44', 'water-44-1', 'water-44-2', closed=False)
        self.relate("connect", 'stem', 'water-33')
