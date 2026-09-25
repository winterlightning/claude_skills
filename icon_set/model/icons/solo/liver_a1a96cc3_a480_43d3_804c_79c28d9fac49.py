'Human Anatomical Liver Organ.\n\nSymbol plan: Large lower left liver lobe and tapered right lobe; shared seam distinguishes the two lobes.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a1a96cc3-a480-43d3-804c-79c28d9fac49'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/liver_a1a96cc3-a480-43d3-804c-79c28d9fac49.svg'
AUTHOR = 'gpt-6'

class Liver(Solo48):
    icon_id = 'liver'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('liver',)

    def build(self):
        # Large lower left liver lobe and tapered right lobe; shared seam distinguishes the two lobes.
        axis_x = 24
        p_4_8 = (4, 8)
        p_4_16 = (4, 16)
        p_4_24 = (4, 24)
        p_6_37 = (6, 37)
        p_6_39 = (6, 39)
        p_7_40 = (7, 40)
        p_8_40 = (8, 40)
        p_11_40 = (11, 40)
        p_12_8 = (12, 8)
        p_15_8 = (15, 8)
        p_18_31 = (18, 31)
        p_19_8 = (19, 8)
        p_23_29 = (23, 29)
        p_27_12 = (27, 12)
        p_27_23 = (27, 23)
        p_27_26 = (27, 26)
        p_27_27 = (27, 27)
        p_34_30 = (34, 30)
        p_37_8 = (37, 8)
        p_44_9 = (44, 9)
        p_44_14 = (44, 14)
        p_44_22 = (44, 22)
        self.add_bezier('left-lobe-1', p_27_12, (p_19_8, p_15_8, p_12_8))
        self.add_bezier('left-lobe-2', p_12_8, (p_4_8, p_4_16, p_4_24))
        self.add_line('left-lobe-3', p_4_24, p_6_37)
        self.add_bezier('left-lobe-4', p_6_37, (p_6_39, p_7_40, p_8_40))
        self.add_bezier('left-lobe-5', p_8_40, (p_11_40, p_18_31, p_23_29))
        self.add_bezier('left-lobe-6', p_23_29, (p_27_27, p_27_26, p_27_23))
        self.add_line('left-lobe-7', p_27_23, p_27_12)
        self.add_contour('left-lobe', 'left-lobe-1', 'left-lobe-2', 'left-lobe-3', 'left-lobe-4', 'left-lobe-5', 'left-lobe-6', 'left-lobe-7', closed=True)
        self.add_bezier('right-lobe-1', p_27_12, (p_37_8, p_44_9, p_44_14))
        self.add_bezier('right-lobe-2', p_44_14, (p_44_22, p_34_30, p_23_29))
        self.add_contour('right-lobe', 'right-lobe-1', 'right-lobe-2', closed=False)
        self.relate("connect", 'left-lobe', 'right-lobe')
