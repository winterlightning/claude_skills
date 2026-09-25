'Laughing Face with Squinting Eyes.\n\nSymbol plan: Round face with widely spaced expression strokes; open mouth reduced to one smooth smile to retain clear interior.\nKeyshape: CIRCLE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ec870ab-b1bd-4990-b99b-ecbf9579ffe8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/face grin squint_4ec870ab-b1bd-4990-b99b-ecbf9579ffe8.svg'
AUTHOR = 'gpt-6'

class SquintingFaceWithWideGrin(Solo48):
    icon_id = 'squinting-face-with-wide-grin'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('squinting', 'face', 'with', 'wide', 'grin')

    def build(self):
        # Round face with widely spaced expression strokes; open mouth reduced to one smooth smile to retain clear interior.
        axis_x = 24
        p_4_24 = (4, 24)
        p_15_18 = (15, 18)
        p_15_22 = (15, 22)
        p_16_31 = (16, 31)
        p_18_20 = (18, 20)
        p_20_35 = (20, 35)
        p_28_35 = (2 * axis_x - p_20_35[0], p_20_35[1])
        p_30_20 = (2 * axis_x - p_18_20[0], p_18_20[1])
        p_32_31 = (2 * axis_x - p_16_31[0], p_16_31[1])
        p_33_18 = (2 * axis_x - p_15_18[0], p_15_18[1])
        p_33_22 = (2 * axis_x - p_15_22[0], p_15_22[1])
        p_44_24 = (2 * axis_x - p_4_24[0], p_4_24[1])
        self.add_arc('face-1', p_4_24, p_44_24, radius_x=20, radius_y=20, sweep=True)
        self.add_arc('face-2', p_44_24, p_4_24, radius_x=20, radius_y=20, sweep=True)
        self.add_contour('face', 'face-1', 'face-2', closed=True)
        self.add_line('left-eye-1', p_15_18, p_18_20)
        self.add_line('left-eye-2', p_18_20, p_15_22)
        self.add_contour('left-eye', 'left-eye-1', 'left-eye-2', closed=False)
        self.add_line('right-eye-1', p_33_18, p_30_20)
        self.add_line('right-eye-2', p_30_20, p_33_22)
        self.add_contour('right-eye', 'right-eye-1', 'right-eye-2', closed=False)
        self.add_bezier('smile-1', p_16_31, (p_20_35, p_28_35, p_32_31))
        self.add_contour('smile', 'smile-1', closed=False)
