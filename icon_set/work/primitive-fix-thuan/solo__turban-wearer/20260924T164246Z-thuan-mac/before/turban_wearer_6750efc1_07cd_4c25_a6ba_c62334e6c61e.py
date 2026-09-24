'Man Wearing a Turban.\n\nSymbol plan: Circular face with touching rounded shoulders using user.svg proportions; small source clothing seams omitted.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6750efc1-07cd-4c25-a6ba-c62334e6c61e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/sultan_6750efc1-07cd-4c25-a6ba-c62334e6c61e.svg'
AUTHOR = 'gpt-6'

class TurbanWearer(Solo48):
    icon_id = 'turban-wearer'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'avatars'
    aliases = ()
    keywords = ('turban', 'wearer')

    def build(self):
        # Circular face with touching rounded shoulders using user.svg proportions; small source clothing seams omitted.
        axis_x = 24
        p_8_44 = (8, 44)
        p_14_9 = (14, 9)
        p_14_14 = (14, 14)
        p_24_13 = (24, 13)
        p_24_28 = (24, 28)
        p_34_9 = (2 * axis_x - p_14_9[0], p_14_9[1])
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
        self.add_line('turban-band-1', p_14_9, p_24_13)
        self.add_line('turban-band-2', p_24_13, p_34_9)
        self.add_contour('turban-band', 'turban-band-1', 'turban-band-2', closed=False)
        self.relate("connect", 'head', 'turban-band')
