'Lucky Horseshoe Symbol.\n\nSymbol plan: Broad U horseshoe with flat tips and concentric bottom curves.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '707aefe4-5cb6-4a10-8642-455a8f4143eb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hoof_707aefe4-5cb6-4a10-8642-455a8f4143eb.svg'
AUTHOR = 'gpt-6'

class OpenHorseshoe(Solo48):
    icon_id = 'open-horseshoe'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('open', 'horseshoe')

    def build(self):
        # Broad U horseshoe with flat tips and concentric bottom curves.
        axis_x = 24
        p_8_4 = (8, 4)
        p_8_28 = (8, 28)
        p_17_4 = (17, 4)
        p_17_27 = (17, 27)
        p_31_4 = (2 * axis_x - p_17_4[0], p_17_4[1])
        p_31_27 = (2 * axis_x - p_17_27[0], p_17_27[1])
        p_40_4 = (2 * axis_x - p_8_4[0], p_8_4[1])
        p_40_28 = (2 * axis_x - p_8_28[0], p_8_28[1])
        self.add_line('horseshoe-1', p_8_4, p_17_4)
        self.add_line('horseshoe-2', p_17_4, p_17_27)
        self.add_arc('horseshoe-3', p_17_27, p_31_27, radius_x=7, radius_y=7, sweep=False)
        self.add_line('horseshoe-4', p_31_27, p_31_4)
        self.add_line('horseshoe-5', p_31_4, p_40_4)
        self.add_line('horseshoe-6', p_40_4, p_40_28)
        self.add_arc('horseshoe-7', p_40_28, p_8_28, radius_x=16, radius_y=16, sweep=True)
        self.add_line('horseshoe-8', p_8_28, p_8_4)
        self.add_contour('horseshoe', 'horseshoe-1', 'horseshoe-2', 'horseshoe-3', 'horseshoe-4', 'horseshoe-5', 'horseshoe-6', 'horseshoe-7', 'horseshoe-8', closed=True)
