'Man with Mustache.\n\nSymbol plan: Portrait with larger circular face retaining a visibly downturned facial arc; shoulder top is4 centerline units below face, giving zero ink gap.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b1a7bb2e-afc5-4b1e-bd84-6da58d21d8c4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/forebear_b1a7bb2e-afc5-4b1e-bd84-6da58d21d8c4.svg'
AUTHOR = 'gpt-6'

class PersonWithDownturnedFacialArc(Solo48):
    icon_id = 'person-with-downturned-facial-arc'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('person', 'with', 'downturned', 'facial', 'arc')

    def build(self):
        # Portrait with larger circular face retaining a visibly downturned facial arc; shoulder top is4 centerline units below face, giving zero ink gap.
        axis_x = 24
        p_8_44 = (8, 44)
        p_12_16 = (12, 16)
        p_21_18 = (21, 18)
        p_22_14 = (22, 14)
        p_24_32 = (24, 32)
        p_26_14 = (2 * axis_x - p_22_14[0], p_22_14[1])
        p_27_18 = (2 * axis_x - p_21_18[0], p_21_18[1])
        p_36_16 = (2 * axis_x - p_12_16[0], p_12_16[1])
        p_40_44 = (2 * axis_x - p_8_44[0], p_8_44[1])
        self.add_arc('head-top', p_12_16, p_36_16, radius_x=12)
        self.add_arc('head-bottom', p_36_16, p_12_16, radius_x=12)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_arc('body-top', p_8_44, p_24_32, radius_x=16, radius_y=12)
        self.add_arc('body-right', p_24_32, p_40_44, radius_x=16, radius_y=12)
        self.add_contour('body', 'body-top', 'body-right')
        self.relate('connect', 'head', 'body')
        self.add_bezier('facial-arc-1', p_21_18, (p_22_14, p_26_14, p_27_18))
        self.add_contour('facial-arc', 'facial-arc-1', closed=False)
