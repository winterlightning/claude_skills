'Night Thunderstorm with Rain.\n\nSymbol plan: Night weather scene with crescent sharing the cloud silhouette. Occluded cloud edge removed beneath the moon, with precipitation below in clear negative space.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80960573-ef64-4ff4-b9d2-b76f3147f1a6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/weather night thunder rain_80960573-ef64-4ff4-b9d2-b76f3147f1a6.svg'
AUTHOR = 'gpt-6'

class NightThunderstormRain(Solo48):
    icon_id = 'night-thunderstorm-rain'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('night', 'thunderstorm', 'rain')

    def build(self):
        # Night weather scene with crescent sharing the cloud silhouette. Occluded cloud edge removed beneath the moon, with precipitation below in clear negative space.
        axis_x = 24
        p_6_15 = (6, 15)
        p_6_20 = (6, 20)
        p_6_22 = (6, 22)
        p_6_25 = (6, 25)
        p_8_25 = (8, 25)
        p_10_14 = (10, 14)
        p_14_7 = (14, 7)
        p_14_15 = (14, 15)
        p_14_32 = (14, 32)
        p_20_26 = (20, 26)
        p_20_42 = (20, 42)
        p_23_10 = (23, 10)
        p_25_7 = (25, 7)
        p_26_32 = (26, 32)
        p_27_6 = (27, 6)
        p_27_18 = (27, 18)
        p_30_42 = (30, 42)
        p_31_13 = (31, 13)
        p_32_38 = (32, 38)
        p_35_18 = (35, 18)
        p_36_6 = (36, 6)
        p_37_28 = (37, 28)
        p_40_28 = (40, 28)
        p_40_42 = (40, 42)
        p_42_16 = (42, 16)
        p_42_24 = (42, 24)
        p_42_38 = (42, 38)
        self.add_bezier('cloud-left-1', p_8_25, (p_6_25, p_6_22, p_6_20))
        self.add_bezier('cloud-left-2', p_6_20, (p_6_15, p_10_14, p_14_15))
        self.add_bezier('cloud-left-3', p_14_15, (p_14_7, p_25_7, p_27_18))
        self.add_contour('cloud-left', 'cloud-left-1', 'cloud-left-2', 'cloud-left-3', closed=False)
        self.add_bezier('moon-1', p_27_18, (p_23_10, p_27_6, p_36_6))
        self.add_bezier('moon-2', p_36_6, (p_31_13, p_35_18, p_42_16))
        self.add_contour('moon', 'moon-1', 'moon-2', closed=False)
        self.relate("connect", 'cloud-left', 'moon')
        self.add_bezier('cloud-right-1', p_42_16, (p_42_24, p_40_28, p_37_28))
        self.add_contour('cloud-right', 'cloud-right-1', closed=False)
        self.relate("connect", 'moon', 'cloud-right')
        self.add_line('lightning-1', p_20_26, p_14_32)
        self.add_line('lightning-2', p_14_32, p_26_32)
        self.add_line('lightning-3', p_26_32, p_20_42)
        self.add_contour('lightning', 'lightning-1', 'lightning-2', 'lightning-3', closed=False)
        self.add_line('rain-left-1', p_32_38, p_30_42)
        self.add_contour('rain-left', 'rain-left-1', closed=False)
        self.add_line('rain-right-1', p_42_38, p_40_42)
        self.add_contour('rain-right', 'rain-right-1', closed=False)
