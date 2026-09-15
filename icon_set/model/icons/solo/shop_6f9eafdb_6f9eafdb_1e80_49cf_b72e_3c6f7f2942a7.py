"""shop-6f9eafdb: approved original model.

Construction: Shop with two wide scallops and a central storefront divider, using exact common attachment points.
Keyshape: HRECT_L; exact SOLO48 envelope.
Construction reference: store from the previously inspected Lucide original and atomic-debug library.
Approved design replaces the original model; previous revisions are archived."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts
SOURCE_ICON_ID = '6f9eafdb-1e80-49cf-b72e-3c6f7f2942a7'
SOURCE_PATH = 'pictographic-primitives/shopping/shop_6f9eafdb-1e80-49cf-b72e-3c6f7f2942a7.svg'
AUTHOR = 'gpt-6'

class Shop6f9eafdb(Solo48):
    icon_id = 'shop-6f9eafdb'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('shop', 'shopping')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self, 'awning', (4, 20), ('L', (8, 8)), ('L', (40, 8)), ('L', (44, 20)), ('C', (44, 28), (28, 28), (24, 20)), ('C', (20, 28), (4, 28), (4, 20)), closed=True)
        poly(self, 'shopfront', (4, 20), (4, 40), (44, 40), (44, 20))
        line(self, 'divider', (24, 20), (24, 40))
        contacts(self)
