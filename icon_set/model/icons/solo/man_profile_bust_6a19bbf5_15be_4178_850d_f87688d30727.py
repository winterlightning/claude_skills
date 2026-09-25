'Man User Profile Avatar.\n\nSymbol plan: Circular face with touching rounded shoulders using user.svg proportions; small source clothing seams omitted.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a19bbf5-15be-4178-850d-f87688d30727'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/step father_6a19bbf5-15be-4178-850d-f87688d30727.svg'
AUTHOR = 'gpt-6'

class ManProfileBust(Solo48):
    icon_id = 'man-profile-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('man', 'profile', 'bust')

    def build(self):
        # Circular face with touching rounded shoulders using user.svg proportions; small source clothing seams omitted.
        axis_x = 24
        p_8_44 = (8, 44)
        p_14_14 = (14, 14)
        p_19_14 = (19, 14)
        p_23_12 = (23, 12)
        p_24_28 = (24, 28)
        p_26_7 = (26, 7)
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
        self.add_bezier('hair-1', p_14_14, (p_19_14, p_23_12, p_26_7))
        self.add_contour('hair', 'hair-1', closed=False)
        self.relate("connect", 'head', 'hair')
