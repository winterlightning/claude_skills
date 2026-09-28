'Man with Mustache.\n\nSymbol plan: Circular face with touching rounded shoulders using user.svg proportions; small source clothing seams omitted.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dfe9a00c-d4b3-4b57-8968-26310380286a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/father in law_dfe9a00c-d4b3-4b57-8968-26310380286a.svg'
AUTHOR = 'gpt-6'

class ManBustWithLargeMustache(Solo48):
    icon_id = 'man-bust-with-large-mustache'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('man', 'bust', 'with', 'large', 'mustache')

    def build(self):
        # Circular face with touching rounded shoulders using user.svg proportions; small source clothing seams omitted.
        axis_x = 24
        p_8_44 = (8, 44)
        p_14_14 = (14, 14)
        p_16_18 = (16, 18)
        p_20_12 = (20, 12)
        p_20_19 = (20, 19)
        p_24_16 = (24, 16)
        p_24_28 = (24, 28)
        p_28_12 = (2 * axis_x - p_20_12[0], p_20_12[1])
        p_28_19 = (2 * axis_x - p_20_19[0], p_20_19[1])
        p_32_18 = (2 * axis_x - p_16_18[0], p_16_18[1])
        p_34_14 = (2 * axis_x - p_14_14[0], p_14_14[1])
        p_40_44 = (2 * axis_x - p_8_44[0], p_8_44[1])
        self.add_arc('head-top', p_14_14, p_34_14, radius_x=10)
        self.add_arc('head-bottom', p_34_14, p_14_14, radius_x=10)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('body-left', p_8_44, p_8_44)
        self.add_arc('body-top', p_8_44, p_24_28, radius_x=16)
        self.add_arc('body-right-shoulder', p_24_28, p_40_44, radius_x=16)
        self.add_contour('body', 'body-left', 'body-top', 'body-right-shoulder')
        self.relate('connect', 'head', 'body')
        self.add_bezier('mustache-1', p_16_18, (p_20_19, p_20_12, p_24_16))
        self.add_bezier('mustache-2', p_24_16, (p_28_12, p_28_19, p_32_18))
        self.add_contour('mustache', 'mustache-1', 'mustache-2', closed=False)
        self.relate("connect", 'head', 'mustache')
