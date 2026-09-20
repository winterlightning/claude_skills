'Night Cloud with Hail.\n\nSymbol plan: Night weather scene with crescent sharing the cloud silhouette. Occluded cloud edge removed beneath the moon, with precipitation below in clear negative space.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7389d596-ba6d-4622-a96a-4308a96a11cd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/weather night hail_7389d596-ba6d-4622-a96a-4308a96a11cd.svg'
AUTHOR = 'gpt-6'

class NightHail(Solo48):
    icon_id = 'night-hail'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('night', 'hail')

    def build(self):
        # Night weather scene with crescent sharing the cloud silhouette. Occluded cloud edge removed beneath the moon, with precipitation below in clear negative space.
        axis_x = 24
        p_6_15 = (6, 15)
        p_6_20 = (6, 20)
        p_6_22 = (6, 22)
        p_6_25 = (6, 25)
        p_6_42 = (6, 42)
        p_8_25 = (8, 25)
        p_10_14 = (10, 14)
        p_14_7 = (14, 7)
        p_14_15 = (14, 15)
        p_14_36 = (14, 36)
        p_20_30 = (20, 30)
        p_23_10 = (23, 10)
        p_24_38 = (24, 38)
        p_25_7 = (25, 7)
        p_27_6 = (27, 6)
        p_27_18 = (27, 18)
        p_30_32 = (30, 32)
        p_31_13 = (31, 13)
        p_35_18 = (35, 18)
        p_36_6 = (36, 6)
        p_37_28 = (37, 28)
        p_37_42 = (37, 42)
        p_40_28 = (40, 28)
        p_42_16 = (42, 16)
        p_42_24 = (42, 24)
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
        self.add_line('rain-left-1', p_20_30, p_14_36)
        self.add_contour('rain-left', 'rain-left-1', closed=False)
        self.add_line('rain-right-1', p_30_32, p_24_38)
        self.add_contour('rain-right', 'rain-right-1', closed=False)
        self.add_line('hail-left-1', p_6_42, p_6_42)
        self.add_contour('hail-left', 'hail-left-1', closed=False)
        self.add_line('hail-right-1', p_37_42, p_37_42)
        self.add_contour('hail-right', 'hail-right-1', closed=False)
