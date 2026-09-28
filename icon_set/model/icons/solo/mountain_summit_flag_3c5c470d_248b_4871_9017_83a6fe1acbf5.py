'Mountain Peak with Flag.\n\nSymbol plan: Summit mountain, pole and notched flag retained; omit tight snow-cap seam.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: mountain-snow.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3c5c470d-248b-4871-9017-83a6fe1acbf5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/summit_3c5c470d-248b-4871-9017-83a6fe1acbf5.svg'
AUTHOR = 'gpt-6'

class MountainSummitFlag(Solo48):
    icon_id = 'mountain-summit-flag'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('mountain', 'summit', 'flag')

    def build(self):
        # Summit mountain, pole and notched flag retained; omit tight snow-cap seam.
        axis_x = 24
        p_8_44 = (8, 44)
        p_24_4 = (24, 4)
        p_24_16 = (24, 16)
        p_24_22 = (24, 22)
        p_35_10 = (35, 10)
        p_39_4 = (39, 4)
        p_39_16 = (39, 16)
        p_40_44 = (2 * axis_x - p_8_44[0], p_8_44[1])
        self.add_line('mountain-1', p_8_44, p_24_22)
        self.add_line('mountain-2', p_24_22, p_40_44)
        self.add_line('mountain-3', p_40_44, p_8_44)
        self.add_contour('mountain', 'mountain-1', 'mountain-2', 'mountain-3', closed=True)
        self.add_line('pole-1', p_24_22, p_24_4)
        self.add_contour('pole', 'pole-1', closed=False)
        self.relate("connect", 'mountain', 'pole')
        self.add_line('flag-1', p_24_4, p_39_4)
        self.add_line('flag-2', p_39_4, p_35_10)
        self.add_line('flag-3', p_35_10, p_39_16)
        self.add_line('flag-4', p_39_16, p_24_16)
        self.add_contour('flag', 'flag-1', 'flag-2', 'flag-3', 'flag-4', closed=False)
        self.relate("connect", 'flag', 'pole')
