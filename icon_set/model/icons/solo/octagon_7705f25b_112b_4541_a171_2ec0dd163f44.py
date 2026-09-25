'Octagon Geometric Shape.\n\nSymbol plan: Regular broad octagon with equal paired diagonals and empty interior.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: octagon.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7705f25b-112b-4541-a171-2ec0dd163f44'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/stopsign_7705f25b-112b-4541-a171-2ec0dd163f44.svg'
AUTHOR = 'gpt-6'

class Octagon(Solo48):
    icon_id = 'octagon'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('octagon',)

    def build(self):
        # Regular broad octagon with equal paired diagonals and empty interior.
        axis_x = 24
        p_6_17 = (6, 17)
        p_6_31 = (6, 31)
        p_17_6 = (17, 6)
        p_17_42 = (17, 42)
        p_31_6 = (2 * axis_x - p_17_6[0], p_17_6[1])
        p_31_42 = (2 * axis_x - p_17_42[0], p_17_42[1])
        p_42_17 = (2 * axis_x - p_6_17[0], p_6_17[1])
        p_42_31 = (2 * axis_x - p_6_31[0], p_6_31[1])
        self.add_line('octagon-1', p_17_6, p_31_6)
        self.add_line('octagon-2', p_31_6, p_42_17)
        self.add_line('octagon-3', p_42_17, p_42_31)
        self.add_line('octagon-4', p_42_31, p_31_42)
        self.add_line('octagon-5', p_31_42, p_17_42)
        self.add_line('octagon-6', p_17_42, p_6_31)
        self.add_line('octagon-7', p_6_31, p_6_17)
        self.add_line('octagon-8', p_6_17, p_17_6)
        self.add_contour('octagon', 'octagon-1', 'octagon-2', 'octagon-3', 'octagon-4', 'octagon-5', 'octagon-6', 'octagon-7', 'octagon-8', closed=True)
