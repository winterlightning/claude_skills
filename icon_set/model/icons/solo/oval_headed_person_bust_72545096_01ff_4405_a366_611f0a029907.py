'Human User Profile Avatar.\n\nSymbol plan: Generic portrait rebuilt with circular face and broad rounded shoulders. Head bottom y20 and body top y24 give zero ink gap.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '72545096-01ff-4405-a366-611f0a029907'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/guy_72545096-01ff-4405-a366-611f0a029907.svg'
AUTHOR = 'gpt-6'

class OvalHeadedPersonBust(Solo48):
    icon_id = 'oval-headed-person-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    aliases = ()
    keywords = ('oval', 'headed', 'person', 'bust')

    def build(self):
        # Generic portrait rebuilt with circular face and broad rounded shoulders. Head bottom y20 and body top y24 give zero ink gap.
        axis_x = 24
        p_8_40 = (8, 40)
        p_8_44 = (8, 44)
        p_16_12 = (16, 12)
        p_24_24 = (24, 24)
        p_32_12 = (2 * axis_x - p_16_12[0], p_16_12[1])
        p_40_40 = (2 * axis_x - p_8_40[0], p_8_40[1])
        p_40_44 = (2 * axis_x - p_8_44[0], p_8_44[1])
        self.add_arc('head-top', p_16_12, p_32_12, radius_x=8)
        self.add_arc('head-bottom', p_32_12, p_16_12, radius_x=8)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('body-left', p_8_44, p_8_40)
        self.add_arc('body-top', p_8_40, p_24_24, radius_x=16)
        self.add_arc('body-right-shoulder', p_24_24, p_40_40, radius_x=16)
        self.add_line('body-right', p_40_40, p_40_44)
        self.add_contour('body', 'body-left', 'body-top', 'body-right-shoulder', 'body-right')
        self.relate('connect', 'head', 'body')
