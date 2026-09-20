'Open Hand Offering Support.\n\nSymbol plan: Upturned offering palm with folded thumb and raised right fingertips; shorten thumb to keep its channel open.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: hand.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '28ebd0ec-a7a1-4063-b621-7c3eb8b9fd1a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/give hand_28ebd0ec-a7a1-4063-b621-7c3eb8b9fd1a.svg'
AUTHOR = 'gpt-6'

class UpturnedOfferingHand(Solo48):
    icon_id = 'upturned-offering-hand'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('upturned', 'offering', 'hand')

    def build(self):
        # Upturned offering palm with folded thumb and raised right fingertips; shorten thumb to keep its channel open.
        axis_x = 24
        p_4_19 = (4, 19)
        p_4_34 = (4, 34)
        p_10_19 = (10, 19)
        p_11_14 = (11, 14)
        p_13_34 = (13, 34)
        p_13_40 = (13, 40)
        p_17_29 = (17, 29)
        p_19_14 = (19, 14)
        p_21_40 = (21, 40)
        p_24_29 = (24, 29)
        p_25_14 = (25, 14)
        p_27_19 = (27, 19)
        p_29_29 = (29, 29)
        p_30_23 = (30, 23)
        p_31_19 = (31, 19)
        p_32_40 = (32, 40)
        p_37_10 = (37, 10)
        p_39_8 = (39, 8)
        p_40_8 = (40, 8)
        p_42_8 = (42, 8)
        p_44_8 = (44, 8)
        p_44_10 = (44, 10)
        p_44_12 = (44, 12)
        p_44_25 = (44, 25)
        self.add_bezier('palm-1', p_4_19, (p_10_19, p_11_14, p_19_14))
        self.add_bezier('palm-2', p_19_14, (p_25_14, p_27_19, p_31_19))
        self.add_line('palm-3', p_31_19, p_37_10)
        self.add_bezier('palm-4', p_37_10, (p_39_8, p_40_8, p_42_8))
        self.add_bezier('palm-5', p_42_8, (p_44_8, p_44_10, p_44_12))
        self.add_bezier('palm-6', p_44_12, (p_44_25, p_32_40, p_21_40))
        self.add_bezier('palm-7', p_21_40, (p_13_40, p_13_34, p_4_34))
        self.add_contour('palm', 'palm-1', 'palm-2', 'palm-3', 'palm-4', 'palm-5', 'palm-6', 'palm-7', closed=False)
        self.add_line('thumb-1', p_17_29, p_24_29)
        self.add_bezier('thumb-2', p_24_29, (p_29_29, p_30_23, p_31_19))
        self.add_contour('thumb', 'thumb-1', 'thumb-2', closed=False)
        self.relate("connect", 'palm', 'thumb')
