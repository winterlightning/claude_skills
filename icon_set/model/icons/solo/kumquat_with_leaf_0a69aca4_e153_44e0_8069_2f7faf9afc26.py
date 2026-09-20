'Lemon with Leaf.\n\nSymbol plan: Rounded kumquat at lower left with pointed upper-right leaf; omit leaf vein.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a69aca4-e153-44e0-8069-2f7faf9afc26'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/kumquat_0a69aca4-e153-44e0-8069-2f7faf9afc26.svg'
AUTHOR = 'gpt-6'

class KumquatWithLeaf(Solo48):
    icon_id = 'kumquat-with-leaf'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('kumquat', 'with', 'leaf')

    def build(self):
        # Rounded kumquat at lower left with pointed upper-right leaf; omit leaf vein.
        axis_x = 24
        p_6_20 = (6, 20)
        p_6_29 = (6, 29)
        p_6_37 = (6, 37)
        p_10_42 = (10, 42)
        p_13_16 = (13, 16)
        p_17_42 = (17, 42)
        p_20_16 = (20, 16)
        p_24_42 = (24, 42)
        p_27_16 = (27, 16)
        p_27_17 = (27, 17)
        p_28_7 = (28, 7)
        p_32_21 = (32, 21)
        p_32_28 = (32, 28)
        p_32_36 = (32, 36)
        p_35_6 = (35, 6)
        p_36_17 = (36, 17)
        p_42_6 = (42, 6)
        p_42_14 = (42, 14)
        self.add_bezier('fruit-1', p_6_29, (p_6_20, p_13_16, p_20_16))
        self.add_bezier('fruit-2', p_20_16, (p_27_16, p_32_21, p_32_28))
        self.add_bezier('fruit-3', p_32_28, (p_32_36, p_24_42, p_17_42))
        self.add_bezier('fruit-4', p_17_42, (p_10_42, p_6_37, p_6_29))
        self.add_contour('fruit', 'fruit-1', 'fruit-2', 'fruit-3', 'fruit-4', closed=True)
        self.add_bezier('leaf-1', p_27_17, (p_28_7, p_35_6, p_42_6))
        self.add_bezier('leaf-2', p_42_6, (p_42_14, p_36_17, p_27_17))
        self.add_contour('leaf', 'leaf-1', 'leaf-2', closed=True)
        self.relate("connect", 'fruit', 'leaf')
