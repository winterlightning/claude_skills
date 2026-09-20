'Human Lips Mouth.\n\nSymbol plan: Mirrored upper lip peaks, broad lower lip and shared central seam.\nKeyshape: HRECT_M; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '40f781e9-ea6f-4ea3-8d54-5b55e8a9e013'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/lips_40f781e9-ea6f-4ea3-8d54-5b55e8a9e013.svg'
AUTHOR = 'gpt-6'

class ClosedLips(Solo48):
    icon_id = 'closed-lips'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('closed', 'lips')

    def build(self):
        # Mirrored upper lip peaks, broad lower lip and shared central seam.
        axis_x = 24
        p_4_24 = (4, 24)
        p_12_20 = (12, 20)
        p_13_10 = (13, 10)
        p_13_31 = (13, 31)
        p_14_27 = (14, 27)
        p_14_38 = (14, 38)
        p_15_22 = (15, 22)
        p_19_10 = (19, 10)
        p_21_10 = (21, 10)
        p_23_14 = (23, 14)
        p_24_14 = (24, 14)
        p_24_24 = (24, 24)
        p_24_38 = (24, 38)
        p_25_14 = (2 * axis_x - p_23_14[0], p_23_14[1])
        p_27_10 = (2 * axis_x - p_21_10[0], p_21_10[1])
        p_29_10 = (2 * axis_x - p_19_10[0], p_19_10[1])
        p_33_26 = (33, 26)
        p_34_23 = (34, 23)
        p_34_38 = (2 * axis_x - p_14_38[0], p_14_38[1])
        p_35_10 = (2 * axis_x - p_13_10[0], p_13_10[1])
        p_35_31 = (2 * axis_x - p_13_31[0], p_13_31[1])
        p_36_20 = (2 * axis_x - p_12_20[0], p_12_20[1])
        p_44_24 = (2 * axis_x - p_4_24[0], p_4_24[1])
        self.add_bezier('upper-1', p_4_24, (p_12_20, p_13_10, p_19_10))
        self.add_bezier('upper-2', p_19_10, (p_21_10, p_23_14, p_24_14))
        self.add_bezier('upper-3', p_24_14, (p_25_14, p_27_10, p_29_10))
        self.add_bezier('upper-4', p_29_10, (p_35_10, p_36_20, p_44_24))
        self.add_contour('upper', 'upper-1', 'upper-2', 'upper-3', 'upper-4', closed=False)
        self.add_bezier('lower-1', p_44_24, (p_35_31, p_34_38, p_24_38))
        self.add_bezier('lower-2', p_24_38, (p_14_38, p_13_31, p_4_24))
        self.add_contour('lower', 'lower-1', 'lower-2', closed=False)
        self.relate("connect", 'upper', 'lower')
        self.add_bezier('seam-1', p_4_24, (p_14_27, p_15_22, p_24_24))
        self.add_bezier('seam-2', p_24_24, (p_33_26, p_34_23, p_44_24))
        self.add_contour('seam', 'seam-1', 'seam-2', closed=False)
        self.relate("connect", 'seam', 'upper')
        self.relate("connect", 'seam', 'lower')
