'Kitchen Box Grater.\n\nSymbol plan: Tapered grater with loop handle and four filled perforation marks; nine source holes reduced to four for spacing.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'df8e757d-9437-4457-8951-4c7bbff79295'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/grate_df8e757d-9437-4457-8951-4c7bbff79295.svg'
AUTHOR = 'gpt-6'

class BoxGraterWithNineHoles(Solo48):
    icon_id = 'box-grater-with-nine-holes'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('box', 'grater', 'with', 'nine', 'holes')

    def build(self):
        # Tapered grater with loop handle and four filled perforation marks; nine source holes reduced to four for spacing.
        axis_x = 24
        p_8_44 = (8, 44)
        p_11_16 = (11, 16)
        p_16_8 = (16, 8)
        p_16_16 = (16, 16)
        p_20_4 = (20, 4)
        p_20_26 = (20, 26)
        p_20_35 = (20, 35)
        p_28_4 = (2 * axis_x - p_20_4[0], p_20_4[1])
        p_28_26 = (2 * axis_x - p_20_26[0], p_20_26[1])
        p_28_35 = (2 * axis_x - p_20_35[0], p_20_35[1])
        p_32_8 = (2 * axis_x - p_16_8[0], p_16_8[1])
        p_32_16 = (2 * axis_x - p_16_16[0], p_16_16[1])
        p_37_16 = (2 * axis_x - p_11_16[0], p_11_16[1])
        p_40_44 = (2 * axis_x - p_8_44[0], p_8_44[1])
        self.add_line('body-1', p_11_16, p_37_16)
        self.add_line('body-2', p_37_16, p_40_44)
        self.add_line('body-3', p_40_44, p_8_44)
        self.add_line('body-4', p_8_44, p_11_16)
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', closed=True)
        self.add_line('handle-1', p_16_16, p_16_8)
        self.add_arc('handle-2', p_16_8, p_20_4, radius_x=4, radius_y=4, sweep=True)
        self.add_line('handle-3', p_20_4, p_28_4)
        self.add_arc('handle-4', p_28_4, p_32_8, radius_x=4, radius_y=4, sweep=True)
        self.add_line('handle-5', p_32_8, p_32_16)
        self.add_contour('handle', 'handle-1', 'handle-2', 'handle-3', 'handle-4', 'handle-5', closed=False)
        self.relate("connect", 'body', 'handle')
        self.add_line('hole-20-26-1', p_20_26, p_20_26)
        self.add_contour('hole-20-26', 'hole-20-26-1', closed=False)
        self.add_line('hole-20-35-1', p_20_35, p_20_35)
        self.add_contour('hole-20-35', 'hole-20-35-1', closed=False)
        self.add_line('hole-28-26-1', p_28_26, p_28_26)
        self.add_contour('hole-28-26', 'hole-28-26-1', closed=False)
        self.add_line('hole-28-35-1', p_28_35, p_28_35)
        self.add_contour('hole-28-35', 'hole-28-35-1', closed=False)
