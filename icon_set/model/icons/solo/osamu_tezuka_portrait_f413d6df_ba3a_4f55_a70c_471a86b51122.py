'Manga Artist with Beret and Glasses.\n\nSymbol plan: Tezuka head portrait with beret and two rectangular glasses sharing outer facial edges. Remove ears and smile to preserve clear lens openings.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f413d6df-ba3a-4f55-a70c-471a86b51122'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/kawaii manga father original creator tetsuka osamu_f413d6df-ba3a-4f55-a70c-471a86b51122.svg'
AUTHOR = 'gpt-6'

class OsamuTezukaPortrait(Solo48):
    icon_id = 'osamu-tezuka-portrait'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('osamu', 'tezuka', 'portrait')

    def build(self):
        # Tezuka head portrait with beret and two rectangular glasses sharing outer facial edges. Remove ears and smile to preserve clear lens openings.
        axis_x = 24
        p_6_8 = (6, 8)
        p_6_14 = (6, 14)
        p_6_24 = (6, 24)
        p_6_32 = (6, 32)
        p_6_39 = (6, 39)
        p_13_6 = (13, 6)
        p_15_42 = (15, 42)
        p_18_24 = (18, 24)
        p_18_32 = (18, 32)
        p_24_6 = (24, 6)
        p_24_42 = (24, 42)
        p_30_24 = (2 * axis_x - p_18_24[0], p_18_24[1])
        p_30_32 = (2 * axis_x - p_18_32[0], p_18_32[1])
        p_33_42 = (2 * axis_x - p_15_42[0], p_15_42[1])
        p_35_6 = (2 * axis_x - p_13_6[0], p_13_6[1])
        p_42_8 = (2 * axis_x - p_6_8[0], p_6_8[1])
        p_42_14 = (2 * axis_x - p_6_14[0], p_6_14[1])
        p_42_24 = (2 * axis_x - p_6_24[0], p_6_24[1])
        p_42_32 = (2 * axis_x - p_6_32[0], p_6_32[1])
        p_42_39 = (2 * axis_x - p_6_39[0], p_6_39[1])
        self.add_bezier('beret-1', p_6_14, (p_6_8, p_13_6, p_24_6))
        self.add_bezier('beret-2', p_24_6, (p_35_6, p_42_8, p_42_14))
        self.add_line('beret-3', p_42_14, p_6_14)
        self.add_contour('beret', 'beret-1', 'beret-2', 'beret-3', closed=True)
        self.add_line('face-1', p_6_14, p_6_32)
        self.add_bezier('face-2', p_6_32, (p_6_39, p_15_42, p_24_42))
        self.add_bezier('face-3', p_24_42, (p_33_42, p_42_39, p_42_32))
        self.add_line('face-4', p_42_32, p_42_14)
        self.add_contour('face', 'face-1', 'face-2', 'face-3', 'face-4', closed=False)
        self.relate("connect", 'beret', 'face')
        self.add_line('glasses-1', p_6_24, p_18_24)
        self.add_line('glasses-2', p_18_24, p_18_32)
        self.add_line('glasses-3', p_18_32, p_6_32)
        self.add_contour('glasses', 'glasses-1', 'glasses-2', 'glasses-3', closed=False)
        self.relate("connect", 'glasses', 'face')
        self.add_line('right-glasses-1', p_42_24, p_30_24)
        self.add_line('right-glasses-2', p_30_24, p_30_32)
        self.add_line('right-glasses-3', p_30_32, p_42_32)
        self.add_contour('right-glasses', 'right-glasses-1', 'right-glasses-2', 'right-glasses-3', closed=False)
        self.relate("connect", 'right-glasses', 'face')
        self.add_line('bridge-1', p_18_24, p_30_24)
        self.add_contour('bridge', 'bridge-1', closed=False)
        self.relate("connect", 'glasses', 'bridge')
        self.relate("connect", 'right-glasses', 'bridge')
