'Low Temperature Thermometer.\n\nSymbol plan: Thermometer bulb with a short inner mercury stroke; omit nested bulb ring.\nKeyshape: VRECT_M; authored on SOLO48, not scaled from source.\nLucide: thermometer.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5074d2b2-162c-4fd5-9c6a-c95bcbfca5d8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/temperature low_5074d2b2-162c-4fd5-9c6a-c95bcbfca5d8.svg'
AUTHOR = 'gpt-6'

class LowTemperatureThermometer(Solo48):
    icon_id = 'low-temperature-thermometer'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('low', 'temperature', 'thermometer')

    def build(self):
        # Thermometer bulb with a short inner mercury stroke; omit nested bulb ring.
        axis_x = 24
        p_10_31 = (10, 31)
        p_10_35 = (10, 35)
        p_10_41 = (10, 41)
        p_12_28 = (12, 28)
        p_16_44 = (16, 44)
        p_18_10 = (18, 10)
        p_18_26 = (18, 26)
        p_24_34 = (24, 34)
        p_24_35 = (24, 35)
        p_24_44 = (24, 44)
        p_30_10 = (2 * axis_x - p_18_10[0], p_18_10[1])
        p_30_26 = (2 * axis_x - p_18_26[0], p_18_26[1])
        p_32_44 = (2 * axis_x - p_16_44[0], p_16_44[1])
        p_36_28 = (2 * axis_x - p_12_28[0], p_12_28[1])
        p_38_31 = (2 * axis_x - p_10_31[0], p_10_31[1])
        p_38_35 = (2 * axis_x - p_10_35[0], p_10_35[1])
        p_38_41 = (2 * axis_x - p_10_41[0], p_10_41[1])
        self.add_line('thermometer-1', p_18_26, p_18_10)
        self.add_arc('thermometer-2', p_18_10, p_30_10, radius_x=6, radius_y=6, sweep=True)
        self.add_line('thermometer-3', p_30_10, p_30_26)
        self.add_bezier('thermometer-4', p_30_26, (p_36_28, p_38_31, p_38_35))
        self.add_bezier('thermometer-5', p_38_35, (p_38_41, p_32_44, p_24_44))
        self.add_bezier('thermometer-6', p_24_44, (p_16_44, p_10_41, p_10_35))
        self.add_bezier('thermometer-7', p_10_35, (p_10_31, p_12_28, p_18_26))
        self.add_contour('thermometer', 'thermometer-1', 'thermometer-2', 'thermometer-3', 'thermometer-4', 'thermometer-5', 'thermometer-6', 'thermometer-7', closed=True)
        self.add_line('mercury-1', p_24_34, p_24_35)
        self.add_contour('mercury', 'mercury-1', closed=False)
