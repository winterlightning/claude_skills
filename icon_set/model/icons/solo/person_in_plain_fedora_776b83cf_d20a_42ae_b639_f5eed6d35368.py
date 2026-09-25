'Man wearing a fedora hat.\n\nSymbol plan: Circular face with touching rounded shoulders using user.svg proportions; small source clothing seams omitted.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '776b83cf-d20a-42ae-b639-f5eed6d35368'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/godfather_776b83cf-d20a-42ae-b639-f5eed6d35368.svg'
AUTHOR = 'gpt-6'

class PersonInPlainFedora(Solo48):
    icon_id = 'person-in-plain-fedora'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('person', 'in', 'plain', 'fedora')

    def build(self):
        # Circular face with touching rounded shoulders using user.svg proportions; small source clothing seams omitted.
        axis_x = 24
        p_8_14 = (8, 14)
        p_8_44 = (8, 44)
        p_14_14 = (14, 14)
        p_24_28 = (24, 28)
        p_34_14 = (2 * axis_x - p_14_14[0], p_14_14[1])
        p_40_14 = (2 * axis_x - p_8_14[0], p_8_14[1])
        p_40_44 = (2 * axis_x - p_8_44[0], p_8_44[1])
        self.add_arc('head-top', p_14_14, p_34_14, radius_x=10)
        self.add_arc('head-bottom', p_34_14, p_14_14, radius_x=10)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('body-left', p_8_44, p_8_44)
        self.add_arc('body-top', p_8_44, p_24_28, radius_x=16)
        self.add_arc('body-right-shoulder', p_24_28, p_40_44, radius_x=16)
        self.add_contour('body', 'body-left', 'body-top', 'body-right-shoulder')
        self.relate('connect', 'head', 'body')
        self.add_line('hat-brim-1', p_8_14, p_40_14)
        self.add_contour('hat-brim', 'hat-brim-1', closed=False)
        self.relate("connect", 'head', 'hat-brim')
