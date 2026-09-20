'Mountain Landscape with Sun.\n\nSymbol plan: Overlapping unequal mountain peaks below a circular sun and above two crossing foreground slopes. Broaden foreground separation.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f6513a3-703e-49bf-b2c9-afd351378405'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/landscape_1f6513a3-703e-49bf-b2c9-afd351378405.svg'
AUTHOR = 'gpt-6'

class MountainLandscapeSun(Solo48):
    icon_id = 'mountain-landscape-sun'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('mountain', 'landscape', 'sun')

    def build(self):
        # Overlapping unequal mountain peaks below a circular sun and above two crossing foreground slopes. Broaden foreground separation.
        axis_x = 24
        p_6_26 = (6, 26)
        p_6_36 = (6, 36)
        p_14_32 = (14, 32)
        p_16_42 = (16, 42)
        p_17_10 = (17, 10)
        p_23_39 = (23, 39)
        p_24_36 = (24, 36)
        p_29_26 = (29, 26)
        p_31_35 = (31, 35)
        p_32_10 = (32, 10)
        p_32_42 = (2 * axis_x - p_16_42[0], p_16_42[1])
        p_34_23 = (34, 23)
        p_40_10 = (40, 10)
        p_42_27 = (42, 27)
        p_42_35 = (42, 35)
        self.add_line('peaks-1', p_6_26, p_17_10)
        self.add_line('peaks-2', p_17_10, p_29_26)
        self.add_contour('peaks', 'peaks-1', 'peaks-2', closed=False)
        self.add_line('right-peak-1', p_29_26, p_34_23)
        self.add_line('right-peak-2', p_34_23, p_42_27)
        self.add_contour('right-peak', 'right-peak-1', 'right-peak-2', closed=False)
        self.relate("connect", 'peaks', 'right-peak')
        self.add_arc('sun-1', p_32_10, p_40_10, radius_x=4, radius_y=4, sweep=True)
        self.add_arc('sun-2', p_40_10, p_32_10, radius_x=4, radius_y=4, sweep=True)
        self.add_contour('sun', 'sun-1', 'sun-2', closed=True)
        self.add_bezier('foreground-1', p_6_36, (p_14_32, p_24_36, p_32_42))
        self.add_contour('foreground', 'foreground-1', closed=False)
        self.add_bezier('front-curve-1', p_16_42, (p_23_39, p_31_35, p_42_35))
        self.add_contour('front-curve', 'front-curve-1', closed=False)
        self.relate("connect", 'foreground', 'front-curve')
