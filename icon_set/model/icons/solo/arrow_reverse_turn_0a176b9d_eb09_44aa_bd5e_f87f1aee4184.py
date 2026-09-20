'Left Reverse Turn Arrow.\n\nSymbol plan: Upward reverse-turn arrow, broad outline with two right angle bends. Standalone directional sign.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a176b9d-eb09-44aa-bd5e-f87f1aee4184'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/left reverse turn ahead 1_0a176b9d-eb09-44aa-bd5e-f87f1aee4184.svg'
AUTHOR = 'gpt-6'

class ArrowReverseTurn(Solo48):
    icon_id = 'arrow-reverse-turn'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('arrow', 'reverse', 'turn')

    def build(self):
        # Upward reverse-turn arrow, broad outline with two right angle bends. Standalone directional sign.
        axis_x = 24
        p_8_18 = (8, 18)
        p_14_18 = (14, 18)
        p_14_37 = (14, 37)
        p_20_4 = (20, 4)
        p_25_18 = (25, 18)
        p_25_28 = (25, 28)
        p_29_37 = (29, 37)
        p_29_44 = (29, 44)
        p_32_18 = (32, 18)
        p_40_28 = (40, 28)
        p_40_44 = (40, 44)
        self.add_line('arrow-1', p_8_18, p_20_4)
        self.add_line('arrow-2', p_20_4, p_32_18)
        self.add_line('arrow-3', p_32_18, p_25_18)
        self.add_line('arrow-4', p_25_18, p_25_28)
        self.add_line('arrow-5', p_25_28, p_40_28)
        self.add_line('arrow-6', p_40_28, p_40_44)
        self.add_line('arrow-7', p_40_44, p_29_44)
        self.add_line('arrow-8', p_29_44, p_29_37)
        self.add_line('arrow-9', p_29_37, p_14_37)
        self.add_line('arrow-10', p_14_37, p_14_18)
        self.add_line('arrow-11', p_14_18, p_8_18)
        self.add_contour('arrow', 'arrow-1', 'arrow-2', 'arrow-3', 'arrow-4', 'arrow-5', 'arrow-6', 'arrow-7', 'arrow-8', 'arrow-9', 'arrow-10', 'arrow-11', closed=True)
