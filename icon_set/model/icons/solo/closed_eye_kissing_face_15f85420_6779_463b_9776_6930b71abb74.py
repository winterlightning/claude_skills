'Kissing Face with Closed Eyes.\n\nSymbol plan: Round kissing face with closed downward eye arcs and puckered double mouth; no heart modifier.\nKeyshape: CIRCLE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '15f85420-6779-463b-9776-6930b71abb74'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/face kiss closed eyes_15f85420-6779-463b-9776-6930b71abb74.svg'
AUTHOR = 'gpt-6'

class ClosedEyeKissingFace(Solo48):
    icon_id = 'closed-eye-kissing-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('closed', 'eye', 'kissing', 'face')

    def build(self):
        # Round kissing face with closed downward eye arcs and puckered double mouth; no heart modifier.
        axis_x = 24
        p_4_24 = (4, 24)
        p_14_18 = (14, 18)
        p_15_20 = (15, 20)
        p_18_20 = (18, 20)
        p_19_18 = (19, 18)
        p_22_28 = (22, 28)
        p_22_35 = (22, 35)
        p_25_32 = (25, 32)
        p_28_37 = (28, 37)
        p_29_18 = (2 * axis_x - p_19_18[0], p_19_18[1])
        p_30_20 = (2 * axis_x - p_18_20[0], p_18_20[1])
        p_30_26 = (30, 26)
        p_30_30 = (30, 30)
        p_30_34 = (30, 34)
        p_33_20 = (2 * axis_x - p_15_20[0], p_15_20[1])
        p_34_18 = (2 * axis_x - p_14_18[0], p_14_18[1])
        p_44_24 = (2 * axis_x - p_4_24[0], p_4_24[1])
        self.add_arc('face-1', p_4_24, p_44_24, radius_x=20, radius_y=20, sweep=True)
        self.add_arc('face-2', p_44_24, p_4_24, radius_x=20, radius_y=20, sweep=True)
        self.add_contour('face', 'face-1', 'face-2', closed=True)
        self.add_bezier('left-eye-1', p_14_18, (p_15_20, p_18_20, p_19_18))
        self.add_contour('left-eye', 'left-eye-1', closed=False)
        self.add_bezier('right-eye-1', p_29_18, (p_30_20, p_33_20, p_34_18))
        self.add_contour('right-eye', 'right-eye-1', closed=False)
        self.add_bezier('kiss-1', p_22_28, (p_30_26, p_30_30, p_25_32))
        self.add_bezier('kiss-2', p_25_32, (p_30_34, p_28_37, p_22_35))
        self.add_contour('kiss', 'kiss-1', 'kiss-2', closed=False)
