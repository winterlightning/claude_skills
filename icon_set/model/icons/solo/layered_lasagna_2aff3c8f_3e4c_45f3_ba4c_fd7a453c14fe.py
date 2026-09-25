'Layered Food Sandwich.\n\nSymbol plan: Three broad lasagna layers with a wavy filling edge; simplify tight layered seams.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2aff3c8f-3e4c-45f3-ba4c-fd7a453c14fe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/lasagna_2aff3c8f-3e4c-45f3-ba4c-fd7a453c14fe.svg'
AUTHOR = 'gpt-6'

class LayeredLasagna(Solo48):
    icon_id = 'layered-lasagna'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('layered', 'lasagna')

    def build(self):
        # Three broad lasagna layers with a wavy filling edge; simplify tight layered seams.
        axis_x = 24
        p_4_18 = (4, 18)
        p_4_28 = (4, 28)
        p_4_39 = (4, 39)
        p_4_40 = (4, 40)
        p_11_25 = (11, 25)
        p_12_40 = (12, 40)
        p_14_8 = (14, 8)
        p_17_31 = (17, 31)
        p_24_28 = (24, 28)
        p_24_40 = (24, 40)
        p_31_25 = (31, 25)
        p_36_8 = (36, 8)
        p_36_40 = (2 * axis_x - p_12_40[0], p_12_40[1])
        p_37_31 = (37, 31)
        p_44_18 = (2 * axis_x - p_4_18[0], p_4_18[1])
        p_44_28 = (2 * axis_x - p_4_28[0], p_4_28[1])
        p_44_39 = (2 * axis_x - p_4_39[0], p_4_39[1])
        p_44_40 = (2 * axis_x - p_4_40[0], p_4_40[1])
        self.add_line('top-1', p_4_18, p_14_8)
        self.add_line('top-2', p_14_8, p_36_8)
        self.add_line('top-3', p_36_8, p_44_18)
        self.add_line('top-4', p_44_18, p_4_18)
        self.add_contour('top', 'top-1', 'top-2', 'top-3', 'top-4', closed=False)
        self.add_bezier('middle-1', p_4_28, (p_11_25, p_17_31, p_24_28))
        self.add_bezier('middle-2', p_24_28, (p_31_25, p_37_31, p_44_28))
        self.add_contour('middle', 'middle-1', 'middle-2', closed=False)
        self.add_bezier('bottom-1', p_4_39, (p_4_40, p_12_40, p_24_40))
        self.add_bezier('bottom-2', p_24_40, (p_36_40, p_44_40, p_44_39))
        self.add_contour('bottom', 'bottom-1', 'bottom-2', closed=False)
