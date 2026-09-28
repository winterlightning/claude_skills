'Industrial Lathe Machine.\n\nSymbol plan: Bench lathe with headstock, small tailstock, spindle and broad base; omit thin layered base and tiny chuck seams.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '63743e8d-1cca-4db9-8d88-5424e991415f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/lathe_63743e8d-1cca-4db9-8d88-5424e991415f.svg'
AUTHOR = 'gpt-6'

class BenchLathe(Solo48):
    icon_id = 'bench-lathe'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('bench', 'lathe')

    def build(self):
        # Bench lathe with headstock, small tailstock, spindle and broad base; omit thin layered base and tiny chuck seams.
        axis_x = 24
        p_4_33 = (4, 33)
        p_4_37 = (4, 37)
        p_6_8 = (6, 8)
        p_6_30 = (6, 30)
        p_7_30 = (7, 30)
        p_7_40 = (7, 40)
        p_18_8 = (18, 8)
        p_18_18 = (18, 18)
        p_18_30 = (18, 30)
        p_32_15 = (32, 15)
        p_32_18 = (32, 18)
        p_32_20 = (32, 20)
        p_34_13 = (34, 13)
        p_34_22 = (34, 22)
        p_37_22 = (37, 22)
        p_37_30 = (37, 30)
        p_40_13 = (40, 13)
        p_40_22 = (40, 22)
        p_41_30 = (2 * axis_x - p_7_30[0], p_7_30[1])
        p_41_40 = (2 * axis_x - p_7_40[0], p_7_40[1])
        p_42_15 = (42, 15)
        p_42_20 = (42, 20)
        p_44_33 = (2 * axis_x - p_4_33[0], p_4_33[1])
        p_44_37 = (2 * axis_x - p_4_37[0], p_4_37[1])
        self.add_line('base-1', p_7_30, p_41_30)
        self.add_arc('base-2', p_41_30, p_44_33, radius_x=3, radius_y=3, sweep=True)
        self.add_line('base-3', p_44_33, p_44_37)
        self.add_arc('base-4', p_44_37, p_41_40, radius_x=3, radius_y=3, sweep=True)
        self.add_line('base-5', p_41_40, p_7_40)
        self.add_arc('base-6', p_7_40, p_4_37, radius_x=3, radius_y=3, sweep=True)
        self.add_line('base-7', p_4_37, p_4_33)
        self.add_arc('base-8', p_4_33, p_7_30, radius_x=3, radius_y=3, sweep=True)
        self.add_contour('base', 'base-1', 'base-2', 'base-3', 'base-4', 'base-5', 'base-6', 'base-7', 'base-8', closed=True)
        self.add_line('headstock-1', p_6_30, p_6_8)
        self.add_line('headstock-2', p_6_8, p_18_8)
        self.add_line('headstock-3', p_18_8, p_18_30)
        self.add_contour('headstock', 'headstock-1', 'headstock-2', 'headstock-3', closed=False)
        self.relate("connect", 'headstock', 'base')
        self.add_line('tailstock-1', p_34_13, p_40_13)
        self.add_arc('tailstock-2', p_40_13, p_42_15, radius_x=2, radius_y=2, sweep=True)
        self.add_line('tailstock-3', p_42_15, p_42_20)
        self.add_arc('tailstock-4', p_42_20, p_40_22, radius_x=2, radius_y=2, sweep=True)
        self.add_line('tailstock-5', p_40_22, p_34_22)
        self.add_arc('tailstock-6', p_34_22, p_32_20, radius_x=2, radius_y=2, sweep=True)
        self.add_line('tailstock-7', p_32_20, p_32_15)
        self.add_arc('tailstock-8', p_32_15, p_34_13, radius_x=2, radius_y=2, sweep=True)
        self.add_contour('tailstock', 'tailstock-1', 'tailstock-2', 'tailstock-3', 'tailstock-4', 'tailstock-5', 'tailstock-6', 'tailstock-7', 'tailstock-8', closed=True)
        self.add_line('spindle-1', p_18_18, p_32_18)
        self.add_contour('spindle', 'spindle-1', closed=False)
        self.relate("connect", 'headstock', 'spindle')
        self.relate("connect", 'spindle', 'tailstock')
        self.add_line('support-1', p_37_22, p_37_30)
        self.add_contour('support', 'support-1', closed=False)
        self.relate("connect", 'support', 'base')
        self.relate("connect", 'support', 'tailstock')
