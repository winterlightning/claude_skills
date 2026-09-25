'Laundry Basket with Clothes.\n\nSymbol plan: Laundry basket with two clothing humps and two broad ventilation slots; reduce dense grid.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9fc3c42e-5298-479e-8cd3-100bcaf8d71d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/laundry basket_9fc3c42e-5298-479e-8cd3-100bcaf8d71d.svg'
AUTHOR = 'gpt-6'

class FilledLaundryBasket(Solo48):
    icon_id = 'filled-laundry-basket'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('filled', 'laundry', 'basket')

    def build(self):
        # Laundry basket with two clothing humps and two broad ventilation slots; reduce dense grid.
        axis_x = 24
        p_6_20 = (6, 20)
        p_8_9 = (8, 9)
        p_8_20 = (8, 20)
        p_11_42 = (11, 42)
        p_12_6 = (12, 6)
        p_18_6 = (18, 6)
        p_18_31 = (18, 31)
        p_23_6 = (23, 6)
        p_24_12 = (24, 12)
        p_25_12 = (25, 12)
        p_30_31 = (2 * axis_x - p_18_31[0], p_18_31[1])
        p_32_4 = (32, 4)
        p_37_42 = (2 * axis_x - p_11_42[0], p_11_42[1])
        p_40_9 = (2 * axis_x - p_8_9[0], p_8_9[1])
        p_40_20 = (2 * axis_x - p_8_20[0], p_8_20[1])
        p_42_20 = (2 * axis_x - p_6_20[0], p_6_20[1])
        self.add_line('basket-1', p_6_20, p_42_20)
        self.add_line('basket-2', p_42_20, p_37_42)
        self.add_line('basket-3', p_37_42, p_11_42)
        self.add_line('basket-4', p_11_42, p_6_20)
        self.add_contour('basket', 'basket-1', 'basket-2', 'basket-3', 'basket-4', closed=True)
        self.add_bezier('clothes-1', p_8_20, (p_8_9, p_12_6, p_18_6))
        self.add_bezier('clothes-2', p_18_6, (p_23_6, p_24_12, p_25_12))
        self.add_bezier('clothes-3', p_25_12, (p_32_4, p_40_9, p_40_20))
        self.add_contour('clothes', 'clothes-1', 'clothes-2', 'clothes-3', closed=False)
        self.relate("connect", 'basket', 'clothes')
        self.add_line('slot-1', p_18_31, p_30_31)
        self.add_contour('slot', 'slot-1', closed=False)
