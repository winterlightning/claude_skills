'Octagon Faceted Gemstone.\n\nSymbol plan: Elongated octagonal gem with rectangular center and four bevel seams; remove four tiny triangular corner facets.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd90fb3c8-645e-4603-bbc3-4fad85460ae4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/jade_d90fb3c8-645e-4603-bbc3-4fad85460ae4.svg'
AUTHOR = 'gpt-6'

class RectangularFacetedGem(Solo48):
    icon_id = 'rectangular-faceted-gem'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('rectangular', 'faceted', 'gem')

    def build(self):
        # Elongated octagonal gem with rectangular center and four bevel seams; remove four tiny triangular corner facets.
        axis_x = 24
        p_8_12 = (8, 12)
        p_8_36 = (8, 36)
        p_16_4 = (16, 4)
        p_16_44 = (16, 44)
        p_17_14 = (17, 14)
        p_17_34 = (17, 34)
        p_31_14 = (2 * axis_x - p_17_14[0], p_17_14[1])
        p_31_34 = (2 * axis_x - p_17_34[0], p_17_34[1])
        p_32_4 = (2 * axis_x - p_16_4[0], p_16_4[1])
        p_32_44 = (2 * axis_x - p_16_44[0], p_16_44[1])
        p_40_12 = (2 * axis_x - p_8_12[0], p_8_12[1])
        p_40_36 = (2 * axis_x - p_8_36[0], p_8_36[1])
        self.add_line('gem-1', p_16_4, p_32_4)
        self.add_line('gem-2', p_32_4, p_40_12)
        self.add_line('gem-3', p_40_12, p_40_36)
        self.add_line('gem-4', p_40_36, p_32_44)
        self.add_line('gem-5', p_32_44, p_16_44)
        self.add_line('gem-6', p_16_44, p_8_36)
        self.add_line('gem-7', p_8_36, p_8_12)
        self.add_line('gem-8', p_8_12, p_16_4)
        self.add_contour('gem', 'gem-1', 'gem-2', 'gem-3', 'gem-4', 'gem-5', 'gem-6', 'gem-7', 'gem-8', closed=True)
        self.add_line('center-1', p_17_14, p_31_14)
        self.add_line('center-2', p_31_14, p_31_34)
        self.add_line('center-3', p_31_34, p_17_34)
        self.add_line('center-4', p_17_34, p_17_14)
        self.add_contour('center', 'center-1', 'center-2', 'center-3', 'center-4', closed=True)
        self.add_line('ul-1', p_8_12, p_17_14)
        self.add_contour('ul', 'ul-1', closed=False)
        self.relate("connect", 'ul', 'gem')
        self.relate("connect", 'ul', 'center')
        self.add_line('ru-1', p_40_12, p_31_14)
        self.add_contour('ru', 'ru-1', closed=False)
        self.relate("connect", 'ru', 'gem')
        self.relate("connect", 'ru', 'center')
        self.add_line('rl-1', p_40_36, p_31_34)
        self.add_contour('rl', 'rl-1', closed=False)
        self.relate("connect", 'rl', 'gem')
        self.relate("connect", 'rl', 'center')
        self.add_line('ll-1', p_8_36, p_17_34)
        self.add_contour('ll', 'll-1', closed=False)
        self.relate("connect", 'll', 'gem')
        self.relate("connect", 'll', 'center')
