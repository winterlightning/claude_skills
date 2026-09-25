'Pile of Gravel and Pebbles.\n\nSymbol plan: Gravel mound with three falling pebbles; omit tiny stones within the mound because their gaps fail MIC.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6736bbe1-5291-4317-956b-ba1af4ae2d06'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/gravel_6736bbe1-5291-4317-956b-ba1af4ae2d06.svg'
AUTHOR = 'gpt-6'

class FallingGravelPile(Solo48):
    icon_id = 'falling-gravel-pile'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('falling', 'gravel', 'pile')

    def build(self):
        # Gravel mound with three falling pebbles; omit tiny stones within the mound because their gaps fail MIC.
        axis_x = 24
        p_4_32 = (4, 32)
        p_4_40 = (4, 40)
        p_11_18 = (11, 18)
        p_12_33 = (12, 33)
        p_17_26 = (17, 26)
        p_21_19 = (21, 19)
        p_24_8 = (24, 8)
        p_28_26 = (28, 26)
        p_32_28 = (32, 28)
        p_37_32 = (37, 32)
        p_38_17 = (38, 17)
        p_44_32 = (2 * axis_x - p_4_32[0], p_4_32[1])
        p_44_40 = (2 * axis_x - p_4_40[0], p_4_40[1])
        self.add_bezier('pile-1', p_4_40, (p_4_32, p_12_33, p_17_26))
        self.add_bezier('pile-2', p_17_26, (p_21_19, p_28_26, p_32_28))
        self.add_bezier('pile-3', p_32_28, (p_37_32, p_44_32, p_44_40))
        self.add_line('pile-4', p_44_40, p_4_40)
        self.add_contour('pile', 'pile-1', 'pile-2', 'pile-3', 'pile-4', closed=True)
        self.add_line('a-1', p_11_18, p_11_18)
        self.add_contour('a', 'a-1', closed=False)
        self.add_line('b-1', p_24_8, p_24_8)
        self.add_contour('b', 'b-1', closed=False)
        self.add_line('c-1', p_38_17, p_38_17)
        self.add_contour('c', 'c-1', closed=False)
