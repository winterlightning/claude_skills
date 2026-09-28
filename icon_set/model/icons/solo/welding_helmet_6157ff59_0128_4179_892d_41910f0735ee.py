'Protective Welding Helmet.\n\nSymbol plan: Rounded protective helmet with a large viewing slot and curved chin. Slot sized for clear negative space.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: shield.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6157ff59-0128-4179-892d-41910f0735ee'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/welding mask_6157ff59-0128-4179-892d-41910f0735ee.svg'
AUTHOR = 'gpt-6'

class WeldingHelmet(Solo48):
    icon_id = 'welding-helmet'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('welding', 'helmet')

    def build(self):
        # Rounded protective helmet with a large viewing slot and curved chin. Slot sized for clear negative space.
        axis_x = 24
        p_8_8 = (8, 8)
        p_8_16 = (8, 16)
        p_8_26 = (8, 26)
        p_8_36 = (8, 36)
        p_12_4 = (12, 4)
        p_15_44 = (15, 44)
        p_17_16 = (17, 16)
        p_17_21 = (17, 21)
        p_19_14 = (19, 14)
        p_19_23 = (19, 23)
        p_20_4 = (20, 4)
        p_24_44 = (24, 44)
        p_28_4 = (2 * axis_x - p_20_4[0], p_20_4[1])
        p_29_14 = (2 * axis_x - p_19_14[0], p_19_14[1])
        p_29_23 = (2 * axis_x - p_19_23[0], p_19_23[1])
        p_31_16 = (2 * axis_x - p_17_16[0], p_17_16[1])
        p_31_21 = (2 * axis_x - p_17_21[0], p_17_21[1])
        p_33_44 = (2 * axis_x - p_15_44[0], p_15_44[1])
        p_36_4 = (2 * axis_x - p_12_4[0], p_12_4[1])
        p_40_8 = (2 * axis_x - p_8_8[0], p_8_8[1])
        p_40_16 = (2 * axis_x - p_8_16[0], p_8_16[1])
        p_40_26 = (2 * axis_x - p_8_26[0], p_8_26[1])
        p_40_36 = (2 * axis_x - p_8_36[0], p_8_36[1])
        self.add_line('helmet-1', p_20_4, p_28_4)
        self.add_bezier('helmet-2', p_28_4, (p_36_4, p_40_8, p_40_16))
        self.add_line('helmet-3', p_40_16, p_40_26)
        self.add_bezier('helmet-4', p_40_26, (p_40_36, p_33_44, p_24_44))
        self.add_bezier('helmet-5', p_24_44, (p_15_44, p_8_36, p_8_26))
        self.add_line('helmet-6', p_8_26, p_8_16)
        self.add_bezier('helmet-7', p_8_16, (p_8_8, p_12_4, p_20_4))
        self.add_contour('helmet', 'helmet-1', 'helmet-2', 'helmet-3', 'helmet-4', 'helmet-5', 'helmet-6', 'helmet-7', closed=True)
        self.add_line('visor-1', p_19_14, p_29_14)
        self.add_arc('visor-2', p_29_14, p_31_16, radius_x=2, radius_y=2, sweep=True)
        self.add_line('visor-3', p_31_16, p_31_21)
        self.add_arc('visor-4', p_31_21, p_29_23, radius_x=2, radius_y=2, sweep=True)
        self.add_line('visor-5', p_29_23, p_19_23)
        self.add_arc('visor-6', p_19_23, p_17_21, radius_x=2, radius_y=2, sweep=True)
        self.add_line('visor-7', p_17_21, p_17_16)
        self.add_arc('visor-8', p_17_16, p_19_14, radius_x=2, radius_y=2, sweep=True)
        self.add_contour('visor', 'visor-1', 'visor-2', 'visor-3', 'visor-4', 'visor-5', 'visor-6', 'visor-7', 'visor-8', closed=True)
