'Hot Burning Flame.\n\nSymbol plan: Flame silhouette and three rays; omit inner flame to preserve negative space at 48.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: flame.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c5b0b448-77ee-4674-a6e6-7741df51c3d9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/flicker_c5b0b448-77ee-4674-a6e6-7741df51c3d9.svg'
AUTHOR = 'gpt-6'

class RadiantFlame(Solo48):
    icon_id = 'radiant-flame'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('radiant', 'flame')

    def build(self):
        # Flame silhouette and three rays; omit inner flame to preserve negative space at 48.
        axis_x = 24
        p_8_16 = (8, 16)
        p_10_18 = (10, 18)
        p_12_4 = (12, 4)
        p_12_23 = (12, 23)
        p_12_33 = (12, 33)
        p_12_40 = (12, 40)
        p_14_7 = (14, 7)
        p_17_44 = (17, 44)
        p_24_10 = (24, 10)
        p_24_44 = (24, 44)
        p_27_34 = (27, 34)
        p_28_21 = (28, 21)
        p_33_18 = (33, 18)
        p_34_26 = (34, 26)
        p_34_44 = (34, 44)
        p_38_14 = (38, 14)
        p_39_35 = (39, 35)
        p_40_12 = (40, 12)
        self.add_bezier('flame-1', p_24_10, (p_28_21, p_12_23, p_12_33))
        self.add_bezier('flame-2', p_12_33, (p_12_40, p_17_44, p_24_44))
        self.add_bezier('flame-3', p_24_44, (p_34_44, p_39_35, p_34_26))
        self.add_bezier('flame-4', p_34_26, (p_27_34, p_33_18, p_24_10))
        self.add_contour('flame', 'flame-1', 'flame-2', 'flame-3', 'flame-4', closed=True)
        self.add_line('ray-left-1', p_8_16, p_10_18)
        self.add_contour('ray-left', 'ray-left-1', closed=False)
        self.add_line('ray-top-1', p_12_4, p_14_7)
        self.add_contour('ray-top', 'ray-top-1', closed=False)
        self.add_line('ray-right-1', p_38_14, p_40_12)
        self.add_contour('ray-right', 'ray-right-1', closed=False)
