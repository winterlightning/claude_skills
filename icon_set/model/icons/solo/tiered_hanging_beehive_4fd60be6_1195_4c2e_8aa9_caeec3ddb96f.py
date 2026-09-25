'Natural Hanging Beehive.\n\nSymbol plan: Suspended hive with three widening tiers and an open arched entrance integrated into lower outline.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4fd60be6-1195-4c2e-8aa9-caeec3ddb96f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hive_4fd60be6-1195-4c2e-8aa9-caeec3ddb96f.svg'
AUTHOR = 'gpt-6'

class TieredHangingBeehive(Solo48):
    icon_id = 'tiered-hanging-beehive'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('tiered', 'hanging', 'beehive')

    def build(self):
        # Suspended hive with three widening tiers and an open arched entrance integrated into lower outline.
        axis_x = 24
        p_8_31 = (8, 31)
        p_8_40 = (8, 40)
        p_12_23 = (12, 23)
        p_12_27 = (12, 27)
        p_12_44 = (12, 44)
        p_16_14 = (16, 14)
        p_16_18 = (16, 18)
        p_17_18 = (17, 18)
        p_20_10 = (20, 10)
        p_20_40 = (20, 40)
        p_20_44 = (20, 44)
        p_24_4 = (24, 4)
        p_24_10 = (24, 10)
        p_28_10 = (2 * axis_x - p_20_10[0], p_20_10[1])
        p_28_40 = (2 * axis_x - p_20_40[0], p_20_40[1])
        p_28_44 = (2 * axis_x - p_20_44[0], p_20_44[1])
        p_31_18 = (2 * axis_x - p_17_18[0], p_17_18[1])
        p_32_14 = (2 * axis_x - p_16_14[0], p_16_14[1])
        p_32_18 = (2 * axis_x - p_16_18[0], p_16_18[1])
        p_36_23 = (2 * axis_x - p_12_23[0], p_12_23[1])
        p_36_27 = (2 * axis_x - p_12_27[0], p_12_27[1])
        p_36_44 = (2 * axis_x - p_12_44[0], p_12_44[1])
        p_40_31 = (2 * axis_x - p_8_31[0], p_8_31[1])
        p_40_40 = (2 * axis_x - p_8_40[0], p_8_40[1])
        self.add_line('support-1', p_24_4, p_24_10)
        self.add_contour('support', 'support-1', closed=False)
        self.add_line('top-1', p_16_18, p_16_14)
        self.add_arc('top-2', p_16_14, p_20_10, radius_x=4, radius_y=4, sweep=True)
        self.add_line('top-3', p_20_10, p_28_10)
        self.add_arc('top-4', p_28_10, p_32_14, radius_x=4, radius_y=4, sweep=True)
        self.add_line('top-5', p_32_14, p_32_18)
        self.add_contour('top', 'top-1', 'top-2', 'top-3', 'top-4', 'top-5', closed=False)
        self.relate("connect", 'top', 'support')
        self.add_line('middle-1', p_12_27, p_12_23)
        self.add_arc('middle-2', p_12_23, p_17_18, radius_x=5, radius_y=5, sweep=True)
        self.add_line('middle-3', p_17_18, p_31_18)
        self.add_arc('middle-4', p_31_18, p_36_23, radius_x=5, radius_y=5, sweep=True)
        self.add_line('middle-5', p_36_23, p_36_27)
        self.add_contour('middle', 'middle-1', 'middle-2', 'middle-3', 'middle-4', 'middle-5', closed=False)
        self.relate("connect", 'top', 'middle')
        self.add_line('bottom-1', p_12_27, p_36_27)
        self.add_arc('bottom-2', p_36_27, p_40_31, radius_x=4, radius_y=4, sweep=True)
        self.add_line('bottom-3', p_40_31, p_40_40)
        self.add_arc('bottom-4', p_40_40, p_36_44, radius_x=4, radius_y=4, sweep=True)
        self.add_line('bottom-5', p_36_44, p_28_44)
        self.add_line('bottom-6', p_28_44, p_28_40)
        self.add_arc('bottom-7', p_28_40, p_20_40, radius_x=4, radius_y=4, sweep=False)
        self.add_line('bottom-8', p_20_40, p_20_44)
        self.add_line('bottom-9', p_20_44, p_12_44)
        self.add_arc('bottom-10', p_12_44, p_8_40, radius_x=4, radius_y=4, sweep=True)
        self.add_line('bottom-11', p_8_40, p_8_31)
        self.add_arc('bottom-12', p_8_31, p_12_27, radius_x=4, radius_y=4, sweep=True)
        self.add_contour('bottom', 'bottom-1', 'bottom-2', 'bottom-3', 'bottom-4', 'bottom-5', 'bottom-6', 'bottom-7', 'bottom-8', 'bottom-9', 'bottom-10', 'bottom-11', 'bottom-12', closed=True)
        self.relate("connect", 'middle', 'bottom')
