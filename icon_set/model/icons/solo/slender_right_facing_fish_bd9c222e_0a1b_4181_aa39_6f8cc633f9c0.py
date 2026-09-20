'Minimalist Swimming Fish.\n\nSymbol plan: Slender right-facing fish with forked tail and two fins integrated into the silhouette; omit tight gill crease.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: fish.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd9c222e-0a1b-4181-aa39-6f8cc633f9c0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/herring_bd9c222e-0a1b-4181-aa39-6f8cc633f9c0.svg'
AUTHOR = 'gpt-6'

class SlenderRightFacingFish(Solo48):
    icon_id = 'slender-right-facing-fish'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('slender', 'right', 'facing', 'fish')

    def build(self):
        # Slender right-facing fish with forked tail and two fins integrated into the silhouette; omit tight gill crease.
        axis_x = 24
        p_4_14 = (4, 14)
        p_4_34 = (4, 34)
        p_5_24 = (5, 24)
        p_13_24 = (13, 24)
        p_17_28 = (17, 28)
        p_18_19 = (18, 19)
        p_21_31 = (21, 31)
        p_22_8 = (22, 8)
        p_22_16 = (22, 16)
        p_24_40 = (24, 40)
        p_25_16 = (25, 16)
        p_26_32 = (26, 32)
        p_31_16 = (31, 16)
        p_31_32 = (31, 32)
        p_36_17 = (36, 17)
        p_36_31 = (36, 31)
        p_40_29 = (40, 29)
        p_41_20 = (41, 20)
        p_44_24 = (44, 24)
        self.add_bezier('fish-1', p_13_24, (p_18_19, p_22_16, p_25_16))
        self.add_line('fish-2', p_25_16, p_22_8)
        self.add_line('fish-3', p_22_8, p_31_16)
        self.add_bezier('fish-4', p_31_16, (p_36_17, p_41_20, p_44_24))
        self.add_bezier('fish-5', p_44_24, (p_40_29, p_36_31, p_31_32))
        self.add_line('fish-6', p_31_32, p_24_40)
        self.add_line('fish-7', p_24_40, p_26_32)
        self.add_bezier('fish-8', p_26_32, (p_21_31, p_17_28, p_13_24))
        self.add_line('fish-9', p_13_24, p_4_34)
        self.add_line('fish-10', p_4_34, p_5_24)
        self.add_line('fish-11', p_5_24, p_4_14)
        self.add_line('fish-12', p_4_14, p_13_24)
        self.add_contour('fish', 'fish-1', 'fish-2', 'fish-3', 'fish-4', 'fish-5', 'fish-6', 'fish-7', 'fish-8', 'fish-9', 'fish-10', 'fish-11', 'fish-12', closed=True)
