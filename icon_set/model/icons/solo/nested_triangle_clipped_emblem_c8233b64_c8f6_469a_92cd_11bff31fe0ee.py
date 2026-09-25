'Nested Geometric Triangle Symbol.\n\nSymbol plan: Clipped outer triangle enclosing a smaller upright triangle with an open lower edge; wide nested clearance.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c8233b64-c8f6-469a-92cd-11bff31fe0ee'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/affinity logo_c8233b64-c8f6-469a-92cd-11bff31fe0ee.svg'
AUTHOR = 'gpt-6'

class NestedTriangleClippedEmblem(Solo48):
    icon_id = 'nested-triangle-clipped-emblem'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('nested', 'triangle', 'clipped', 'emblem')

    def build(self):
        # Clipped outer triangle enclosing a smaller upright triangle with an open lower edge; wide nested clearance.
        axis_x = 24
        p_4_34 = (4, 34)
        p_8_40 = (8, 40)
        p_16_31 = (16, 31)
        p_20_8 = (20, 8)
        p_21_31 = (21, 31)
        p_24_19 = (24, 19)
        p_27_31 = (2 * axis_x - p_21_31[0], p_21_31[1])
        p_28_8 = (2 * axis_x - p_20_8[0], p_20_8[1])
        p_32_31 = (2 * axis_x - p_16_31[0], p_16_31[1])
        p_40_40 = (2 * axis_x - p_8_40[0], p_8_40[1])
        p_44_34 = (2 * axis_x - p_4_34[0], p_4_34[1])
        self.add_line('outer-1', p_20_8, p_28_8)
        self.add_line('outer-2', p_28_8, p_44_34)
        self.add_line('outer-3', p_44_34, p_40_40)
        self.add_line('outer-4', p_40_40, p_8_40)
        self.add_line('outer-5', p_8_40, p_4_34)
        self.add_line('outer-6', p_4_34, p_20_8)
        self.add_contour('outer', 'outer-1', 'outer-2', 'outer-3', 'outer-4', 'outer-5', 'outer-6', closed=True)
        self.add_line('inner-1', p_21_31, p_16_31)
        self.add_line('inner-2', p_16_31, p_24_19)
        self.add_line('inner-3', p_24_19, p_32_31)
        self.add_line('inner-4', p_32_31, p_27_31)
        self.add_contour('inner', 'inner-1', 'inner-2', 'inner-3', 'inner-4', closed=False)
