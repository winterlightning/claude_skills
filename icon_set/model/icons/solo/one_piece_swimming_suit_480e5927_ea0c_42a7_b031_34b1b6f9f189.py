'One Piece Swimsuit.\n\nSymbol plan: Swimsuit with broad shoulders, deep U neckline, waisted sides and high leg openings. Broaden straps to maintain their clear interiors.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '480e5927-ea0c-42a7-b031-34b1b6f9f189'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/swimsuit_480e5927-ea0c-42a7-b031-34b1b6f9f189.svg'
AUTHOR = 'gpt-6'

class OnePieceSwimmingSuit(Solo48):
    icon_id = 'one-piece-swimming-suit'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('one', 'piece', 'swimming', 'suit')

    def build(self):
        # Swimsuit with broad shoulders, deep U neckline, waisted sides and high leg openings. Broaden straps to maintain their clear interiors.
        axis_x = 24
        p_8_4 = (8, 4)
        p_8_17 = (8, 17)
        p_8_34 = (8, 34)
        p_15_30 = (15, 30)
        p_16_25 = (16, 25)
        p_17_4 = (17, 4)
        p_17_12 = (17, 12)
        p_18_34 = (18, 34)
        p_18_44 = (18, 44)
        p_24_44 = (24, 44)
        p_30_34 = (2 * axis_x - p_18_34[0], p_18_34[1])
        p_30_44 = (2 * axis_x - p_18_44[0], p_18_44[1])
        p_31_4 = (2 * axis_x - p_17_4[0], p_17_4[1])
        p_31_12 = (2 * axis_x - p_17_12[0], p_17_12[1])
        p_32_25 = (2 * axis_x - p_16_25[0], p_16_25[1])
        p_33_30 = (2 * axis_x - p_15_30[0], p_15_30[1])
        p_40_4 = (2 * axis_x - p_8_4[0], p_8_4[1])
        p_40_17 = (2 * axis_x - p_8_17[0], p_8_17[1])
        p_40_34 = (2 * axis_x - p_8_34[0], p_8_34[1])
        self.add_line('suit-1', p_8_4, p_17_4)
        self.add_line('suit-2', p_17_4, p_17_12)
        self.add_arc('suit-3', p_17_12, p_31_12, radius_x=7, radius_y=7, sweep=False)
        self.add_line('suit-4', p_31_12, p_31_4)
        self.add_line('suit-5', p_31_4, p_40_4)
        self.add_line('suit-6', p_40_4, p_40_17)
        self.add_bezier('suit-7', p_40_17, (p_32_25, p_33_30, p_40_34))
        self.add_bezier('suit-8', p_40_34, (p_30_34, p_30_44, p_24_44))
        self.add_bezier('suit-9', p_24_44, (p_18_44, p_18_34, p_8_34))
        self.add_bezier('suit-10', p_8_34, (p_15_30, p_16_25, p_8_17))
        self.add_line('suit-11', p_8_17, p_8_4)
        self.add_contour('suit', 'suit-1', 'suit-2', 'suit-3', 'suit-4', 'suit-5', 'suit-6', 'suit-7', 'suit-8', 'suit-9', 'suit-10', 'suit-11', closed=True)
