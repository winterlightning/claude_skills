'Human Molar Tooth.\n\nSymbol plan: Broad notched crown and two rounded roots around a deep open central arch.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '048be910-fe54-4465-ad4f-213d3b2bebc2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/teeth_048be910-fe54-4465-ad4f-213d3b2bebc2.svg'
AUTHOR = 'gpt-6'

class TwoRootMolarTooth(Solo48):
    icon_id = 'two-root-molar-tooth'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('two', 'root', 'molar', 'tooth')

    def build(self):
        # Broad notched crown and two rounded roots around a deep open central arch.
        axis_x = 24
        p_8_4 = (8, 4)
        p_8_10 = (8, 10)
        p_8_17 = (8, 17)
        p_8_26 = (8, 26)
        p_10_44 = (10, 44)
        p_13_4 = (13, 4)
        p_16_4 = (16, 4)
        p_16_44 = (16, 44)
        p_17_27 = (17, 27)
        p_18_7 = (18, 7)
        p_20_44 = (20, 44)
        p_24_7 = (24, 7)
        p_24_27 = (24, 27)
        p_28_44 = (2 * axis_x - p_20_44[0], p_20_44[1])
        p_30_7 = (2 * axis_x - p_18_7[0], p_18_7[1])
        p_31_27 = (2 * axis_x - p_17_27[0], p_17_27[1])
        p_32_4 = (2 * axis_x - p_16_4[0], p_16_4[1])
        p_32_44 = (2 * axis_x - p_16_44[0], p_16_44[1])
        p_35_4 = (2 * axis_x - p_13_4[0], p_13_4[1])
        p_38_44 = (2 * axis_x - p_10_44[0], p_10_44[1])
        p_40_4 = (2 * axis_x - p_8_4[0], p_8_4[1])
        p_40_10 = (2 * axis_x - p_8_10[0], p_8_10[1])
        p_40_17 = (2 * axis_x - p_8_17[0], p_8_17[1])
        p_40_26 = (2 * axis_x - p_8_26[0], p_8_26[1])
        self.add_bezier('tooth-1', p_24_7, (p_18_7, p_16_4, p_13_4))
        self.add_bezier('tooth-2', p_13_4, (p_8_4, p_8_10, p_8_17))
        self.add_bezier('tooth-3', p_8_17, (p_8_26, p_10_44, p_16_44))
        self.add_bezier('tooth-4', p_16_44, (p_20_44, p_17_27, p_24_27))
        self.add_bezier('tooth-5', p_24_27, (p_31_27, p_28_44, p_32_44))
        self.add_bezier('tooth-6', p_32_44, (p_38_44, p_40_26, p_40_17))
        self.add_bezier('tooth-7', p_40_17, (p_40_10, p_40_4, p_35_4))
        self.add_bezier('tooth-8', p_35_4, (p_32_4, p_30_7, p_24_7))
        self.add_contour('tooth', 'tooth-1', 'tooth-2', 'tooth-3', 'tooth-4', 'tooth-5', 'tooth-6', 'tooth-7', 'tooth-8', closed=True)
