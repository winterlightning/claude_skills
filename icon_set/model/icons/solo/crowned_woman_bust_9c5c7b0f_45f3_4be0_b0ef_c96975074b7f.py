'Queen wearing crown.\n\nSymbol plan: Crowned woman portrait with exposed circular jaw, three-point crown and simplified long hair. Upper face edge is hidden by the crown.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9c5c7b0f-45f3-4be0-b0ef-c96975074b7f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/history africa_9c5c7b0f-45f3-4be0-b0ef-c96975074b7f.svg'
AUTHOR = 'gpt-6'

class CrownedWomanBust(Solo48):
    icon_id = 'crowned-woman-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('crowned', 'woman', 'bust')

    def build(self):
        # Crowned woman portrait with exposed circular jaw, three-point crown and simplified long hair. Upper face edge is hidden by the crown.
        axis_x = 24
        p_8_44 = (8, 44)
        p_10_6 = (10, 6)
        p_10_31 = (10, 31)
        p_10_34 = (10, 34)
        p_12_27 = (12, 27)
        p_14_22 = (14, 22)
        p_18_13 = (18, 13)
        p_24_4 = (24, 4)
        p_24_36 = (24, 36)
        p_30_13 = (2 * axis_x - p_18_13[0], p_18_13[1])
        p_34_22 = (2 * axis_x - p_14_22[0], p_14_22[1])
        p_36_27 = (2 * axis_x - p_12_27[0], p_12_27[1])
        p_38_6 = (2 * axis_x - p_10_6[0], p_10_6[1])
        p_38_31 = (2 * axis_x - p_10_31[0], p_10_31[1])
        p_38_34 = (2 * axis_x - p_10_34[0], p_10_34[1])
        p_40_44 = (2 * axis_x - p_8_44[0], p_8_44[1])
        self.add_arc('head-1', p_14_22, p_34_22, radius_x=10, radius_y=10, sweep=False)
        self.add_contour('head', 'head-1', closed=False)
        self.add_arc('body-1', p_8_44, p_24_36, radius_x=16, radius_y=8, sweep=True)
        self.add_arc('body-2', p_24_36, p_40_44, radius_x=16, radius_y=8, sweep=True)
        self.add_contour('body', 'body-1', 'body-2', closed=False)
        self.relate("connect", 'head', 'body')
        self.add_line('crown-1', p_14_22, p_10_6)
        self.add_line('crown-2', p_10_6, p_18_13)
        self.add_line('crown-3', p_18_13, p_24_4)
        self.add_line('crown-4', p_24_4, p_30_13)
        self.add_line('crown-5', p_30_13, p_38_6)
        self.add_line('crown-6', p_38_6, p_34_22)
        self.add_line('crown-7', p_34_22, p_14_22)
        self.add_contour('crown', 'crown-1', 'crown-2', 'crown-3', 'crown-4', 'crown-5', 'crown-6', 'crown-7', closed=False)
        self.relate("connect", 'head', 'crown')
        self.add_bezier('hair-left-1', p_14_22, (p_12_27, p_10_31, p_10_34))
        self.add_contour('hair-left', 'hair-left-1', closed=False)
        self.add_bezier('hair-right-1', p_34_22, (p_36_27, p_38_31, p_38_34))
        self.add_contour('hair-right', 'hair-right-1', closed=False)
        self.relate("connect", 'head', 'hair-left')
        self.relate("connect", 'head', 'hair-right')
