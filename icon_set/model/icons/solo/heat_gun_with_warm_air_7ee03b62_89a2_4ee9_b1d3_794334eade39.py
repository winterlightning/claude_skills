'Industrial Heat Gun Tool.\n\nSymbol plan: Pistol heat gun with broad barrel, hooked grip and two heat waves; omit barrel seam and trigger.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: coffee.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7ee03b62-89a2-4ee9-b1d3-794334eade39'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/heat gun_7ee03b62-89a2-4ee9-b1d3-794334eade39.svg'
AUTHOR = 'gpt-6'

class HeatGunWithWarmAir(Solo48):
    icon_id = 'heat-gun-with-warm-air'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('heat', 'gun', 'with', 'warm', 'air')

    def build(self):
        # Pistol heat gun with broad barrel, hooked grip and two heat waves; omit barrel seam and trigger.
        axis_x = 24
        p_4_10 = (4, 10)
        p_4_20 = (4, 20)
        p_7_7 = (7, 7)
        p_7_17 = (7, 17)
        p_8_13 = (8, 13)
        p_8_23 = (8, 23)
        p_10_10 = (10, 10)
        p_10_20 = (10, 20)
        p_18_8 = (18, 8)
        p_18_22 = (18, 22)
        p_25_22 = (25, 22)
        p_27_40 = (27, 40)
        p_29_36 = (29, 36)
        p_35_20 = (35, 20)
        p_38_8 = (38, 8)
        p_39_40 = (39, 40)
        p_44_14 = (44, 14)
        p_44_20 = (2 * axis_x - p_4_20[0], p_4_20[1])
        self.add_line('tool-1', p_18_8, p_38_8)
        self.add_arc('tool-2', p_38_8, p_44_14, radius_x=6, radius_y=6, sweep=True)
        self.add_line('tool-3', p_44_14, p_44_20)
        self.add_line('tool-4', p_44_20, p_35_20)
        self.add_line('tool-5', p_35_20, p_39_40)
        self.add_line('tool-6', p_39_40, p_27_40)
        self.add_line('tool-7', p_27_40, p_29_36)
        self.add_line('tool-8', p_29_36, p_25_22)
        self.add_line('tool-9', p_25_22, p_18_22)
        self.add_line('tool-10', p_18_22, p_18_8)
        self.add_contour('tool', 'tool-1', 'tool-2', 'tool-3', 'tool-4', 'tool-5', 'tool-6', 'tool-7', 'tool-8', 'tool-9', 'tool-10', closed=True)
        self.add_bezier('heat-10-1', p_4_10, (p_7_7, p_8_13, p_10_10))
        self.add_contour('heat-10', 'heat-10-1', closed=False)
        self.add_bezier('heat-20-1', p_4_20, (p_7_17, p_8_23, p_10_20))
        self.add_contour('heat-20', 'heat-20-1', closed=False)
