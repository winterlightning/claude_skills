'Potato Masher Utensil.\n\nSymbol plan: Diagonal masher with rounded pounding head and broad end-face seam. Handle cap has explicit keyshape extrema.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1b8310a2-51b7-40c4-b347-f5ebe42d0640'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/kitchenware masher_1b8310a2-51b7-40c4-b347-f5ebe42d0640.svg'
AUTHOR = 'gpt-6'

class KitchenMasher(Solo48):
    icon_id = 'kitchen-masher'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('kitchen', 'masher')

    def build(self):
        # Diagonal masher with rounded pounding head and broad end-face seam. Handle cap has explicit keyshape extrema.
        axis_x = 24
        p_6_23 = (6, 23)
        p_6_30 = (6, 30)
        p_6_35 = (6, 35)
        p_6_42 = (6, 42)
        p_12_42 = (12, 42)
        p_13_18 = (13, 18)
        p_14_28 = (14, 28)
        p_17_42 = (17, 42)
        p_20_21 = (20, 21)
        p_23_34 = (23, 34)
        p_23_39 = (23, 39)
        p_23_42 = (23, 42)
        p_27_28 = (27, 28)
        p_30_35 = (30, 35)
        p_35_6 = (35, 6)
        p_38_6 = (38, 6)
        p_40_6 = (40, 6)
        p_42_8 = (42, 8)
        p_42_10 = (42, 10)
        p_42_13 = (42, 13)
        self.add_bezier('tool-1', p_12_42, (p_6_42, p_6_35, p_6_30))
        self.add_bezier('tool-2', p_6_30, (p_6_23, p_13_18, p_20_21))
        self.add_line('tool-3', p_20_21, p_35_6)
        self.add_line('tool-4', p_35_6, p_38_6)
        self.add_bezier('tool-5', p_38_6, (p_40_6, p_42_8, p_42_10))
        self.add_line('tool-6', p_42_10, p_42_13)
        self.add_line('tool-7', p_42_13, p_27_28)
        self.add_bezier('tool-8', p_27_28, (p_30_35, p_23_42, p_17_42))
        self.add_line('tool-9', p_17_42, p_12_42)
        self.add_contour('tool', 'tool-1', 'tool-2', 'tool-3', 'tool-4', 'tool-5', 'tool-6', 'tool-7', 'tool-8', 'tool-9', closed=True)
        self.add_bezier('face-1', p_6_30, (p_14_28, p_23_34, p_23_39))
        self.add_contour('face', 'face-1', closed=False)
        self.relate("connect", 'face', 'tool')
