'Laughing Face with Smiling Eyes.\n\nSymbol plan: Round face with widely spaced expression strokes; open mouth reduced to one smooth smile to retain clear interior.\nKeyshape: CIRCLE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5dd014bc-91cd-4d1e-9c77-a3ff108c5674'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/face laugh_5dd014bc-91cd-4d1e-9c77-a3ff108c5674.svg'
AUTHOR = 'gpt-6'

class LaughingFaceWithShallowOpenMouth(Solo48):
    icon_id = 'laughing-face-with-shallow-open-mouth'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('laughing', 'face', 'with', 'shallow', 'open', 'mouth')

    def build(self):
        # Round face with widely spaced expression strokes; open mouth reduced to one smooth smile to retain clear interior.
        axis_x = 24
        p_4_24 = (4, 24)
        p_14_19 = (14, 19)
        p_15_16 = (15, 16)
        p_15_29 = (15, 29)
        p_17_16 = (17, 16)
        p_18_37 = (18, 37)
        p_19_19 = (19, 19)
        p_29_19 = (2 * axis_x - p_19_19[0], p_19_19[1])
        p_30_37 = (2 * axis_x - p_18_37[0], p_18_37[1])
        p_31_16 = (2 * axis_x - p_17_16[0], p_17_16[1])
        p_33_16 = (2 * axis_x - p_15_16[0], p_15_16[1])
        p_33_29 = (2 * axis_x - p_15_29[0], p_15_29[1])
        p_34_19 = (2 * axis_x - p_14_19[0], p_14_19[1])
        p_44_24 = (2 * axis_x - p_4_24[0], p_4_24[1])
        self.add_arc('face-1', p_4_24, p_44_24, radius_x=20, radius_y=20, sweep=True)
        self.add_arc('face-2', p_44_24, p_4_24, radius_x=20, radius_y=20, sweep=True)
        self.add_contour('face', 'face-1', 'face-2', closed=True)
        self.add_bezier('left-eye-1', p_14_19, (p_15_16, p_17_16, p_19_19))
        self.add_contour('left-eye', 'left-eye-1', closed=False)
        self.add_bezier('right-eye-1', p_29_19, (p_31_16, p_33_16, p_34_19))
        self.add_contour('right-eye', 'right-eye-1', closed=False)
        self.add_bezier('smile-1', p_15_29, (p_18_37, p_30_37, p_33_29))
        self.add_contour('smile', 'smile-1', closed=False)
