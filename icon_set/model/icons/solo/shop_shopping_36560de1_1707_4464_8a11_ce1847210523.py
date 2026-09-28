"""shop-shopping: approved original model.

Construction: Shopfront with a striped flat valance and a divided lower window; retain a single recognizable shop.
Keyshape: HRECT_L; exact SOLO48 envelope.
Construction reference: store from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = '36560de1-1707-4464-8a11-ce1847210523'
SOURCE_PATH = 'pictographic-primitives/shopping/shop_36560de1-1707-4464-8a11-ce1847210523.svg'
AUTHOR = 'gpt-6'

class ShopShopping(Solo48):
    icon_id = 'shop-shopping'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    categories = ('shopping', 'primitives')
    aliases = ()
    keywords = ('shop', 'shopping')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self, 'valance', 4, 8, 44, 20, 3, xs=(8, 14, 24, 34, 40))
        for x in (14, 24, 34):
            line(self, f'stripe-{x}', (x, 8), (x, 20))
        poly(self, 'shopfront', (8, 20), (8, 40), (40, 40), (40, 20))
        line(self, 'divider', (24, 20), (24, 40))
        contacts(self)
