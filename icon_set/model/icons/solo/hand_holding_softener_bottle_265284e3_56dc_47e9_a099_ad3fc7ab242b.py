'Laundry Softener and Folded Towels.\n\nSymbol plan: Hand encircles bottle with two broad finger edges and one raised thumb; reduce three folded-finger seams to one wide band.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: hand.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '265284e3-56dc-47e9-a099-ad3fc7ab242b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/liquid laundry softener_265284e3-56dc-47e9-a099-ad3fc7ab242b.svg'
AUTHOR = 'gpt-6'

class HandHoldingSoftenerBottle(Solo48):
    icon_id = 'hand-holding-softener-bottle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('hand', 'holding', 'softener', 'bottle')

    def build(self):
        # Hand encircles bottle with two broad finger edges and one raised thumb; reduce three folded-finger seams to one wide band.
        axis_x = 24
        p_6_22 = (6, 22)
        p_6_32 = (6, 32)
        p_6_42 = (6, 42)
        p_14_22 = (14, 22)
        p_14_32 = (14, 32)
        p_24_21 = (24, 21)
        p_24_32 = (24, 32)
        p_24_37 = (24, 37)
        p_28_6 = (28, 6)
        p_28_16 = (28, 16)
        p_29_16 = (29, 16)
        p_29_42 = (29, 42)
        p_37_16 = (37, 16)
        p_37_42 = (37, 42)
        p_38_6 = (38, 6)
        p_38_16 = (38, 16)
        p_42_21 = (42, 21)
        p_42_37 = (42, 37)
        self.add_line('bottle-1', p_29_16, p_37_16)
        self.add_arc('bottle-2', p_37_16, p_42_21, radius_x=5, radius_y=5, sweep=True)
        self.add_line('bottle-3', p_42_21, p_42_37)
        self.add_arc('bottle-4', p_42_37, p_37_42, radius_x=5, radius_y=5, sweep=True)
        self.add_line('bottle-5', p_37_42, p_29_42)
        self.add_arc('bottle-6', p_29_42, p_24_37, radius_x=5, radius_y=5, sweep=True)
        self.add_line('bottle-7', p_24_37, p_24_21)
        self.add_arc('bottle-8', p_24_21, p_29_16, radius_x=5, radius_y=5, sweep=True)
        self.add_contour('bottle', 'bottle-1', 'bottle-2', 'bottle-3', 'bottle-4', 'bottle-5', 'bottle-6', 'bottle-7', 'bottle-8', closed=True)
        self.add_line('neck-1', p_28_16, p_28_6)
        self.add_line('neck-2', p_28_6, p_38_6)
        self.add_line('neck-3', p_38_6, p_38_16)
        self.add_contour('neck', 'neck-1', 'neck-2', 'neck-3', closed=False)
        self.relate("connect", 'bottle', 'neck')
        self.add_line('palm-1', p_6_42, p_29_42)
        self.add_contour('palm', 'palm-1', closed=False)
        self.relate("connect", 'bottle', 'palm')
        self.add_line('finger-1', p_6_32, p_24_32)
        self.add_contour('finger', 'finger-1', closed=False)
        self.relate("connect", 'bottle', 'finger')
        self.add_line('thumb-1', p_6_22, p_14_22)
        self.add_line('thumb-2', p_14_22, p_14_32)
        self.add_contour('thumb', 'thumb-1', 'thumb-2', closed=False)
        self.relate("connect", 'finger', 'thumb')
