'Modern Vertical Air Purifier.\n\nSymbol plan: Rounded vertical purifier with horizontal upper control and separate circular lower control.\nKeyshape: VRECT_M; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8473c20-5d06-455b-9524-833714ec6486'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/air purifier 3_e8473c20-5d06-455b-9524-833714ec6486.svg'
AUTHOR = 'gpt-6'

class VerticalAirPurifierTwoControls(Solo48):
    icon_id = 'vertical-air-purifier-two-controls'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('vertical', 'air', 'purifier', 'two', 'controls')

    def build(self):
        # Rounded vertical purifier with horizontal upper control and separate circular lower control.
        axis_x = 24
        p_10_10 = (10, 10)
        p_10_38 = (10, 38)
        p_16_4 = (16, 4)
        p_16_44 = (16, 44)
        p_21_15 = (21, 15)
        p_21_29 = (21, 29)
        p_27_15 = (2 * axis_x - p_21_15[0], p_21_15[1])
        p_27_29 = (2 * axis_x - p_21_29[0], p_21_29[1])
        p_32_4 = (2 * axis_x - p_16_4[0], p_16_4[1])
        p_32_44 = (2 * axis_x - p_16_44[0], p_16_44[1])
        p_38_10 = (2 * axis_x - p_10_10[0], p_10_10[1])
        p_38_38 = (2 * axis_x - p_10_38[0], p_10_38[1])
        self.add_line('body-1', p_16_4, p_32_4)
        self.add_arc('body-2', p_32_4, p_38_10, radius_x=6, radius_y=6, sweep=True)
        self.add_line('body-3', p_38_10, p_38_38)
        self.add_arc('body-4', p_38_38, p_32_44, radius_x=6, radius_y=6, sweep=True)
        self.add_line('body-5', p_32_44, p_16_44)
        self.add_arc('body-6', p_16_44, p_10_38, radius_x=6, radius_y=6, sweep=True)
        self.add_line('body-7', p_10_38, p_10_10)
        self.add_arc('body-8', p_10_10, p_16_4, radius_x=6, radius_y=6, sweep=True)
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', closed=True)
        self.add_line('upper-control-1', p_21_15, p_27_15)
        self.add_contour('upper-control', 'upper-control-1', closed=False)
        self.add_arc('lower-control-1', p_21_29, p_27_29, radius_x=3, radius_y=3, sweep=True)
        self.add_arc('lower-control-2', p_27_29, p_21_29, radius_x=3, radius_y=3, sweep=True)
        self.add_contour('lower-control', 'lower-control-1', 'lower-control-2', closed=True)
