"""Shopping basket (shopping), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '661269e3-4651-4b14-9a50-0909d2b863c5'
SOURCE_PATH = 'icons-json/shopping/shopping basket_661269e3-4651-4b14-9a50-0909d2b863c5.json'
AUTHOR = 'gpt-6'

class ShoppingBasket(Solo48):
    icon_id = 'shopping-basket'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('shopping', 'basket')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (16, 8), (9, 20))
        self.add_line('e1', (32, 8), (39, 20))
        self.add_line('e2', (9, 20), (4, 21))
        self.add_line('e3', (4, 21), (9, 34))
        self.add_line('e4', (13, 40), (34, 40))
        self.add_line('e5', (37, 38), (43, 23))
        self.add_line('e6', (44, 21), (39, 20))
        self.add_line('e7', (9, 20), (39, 20))
        self.add_line('e8', (28, 31), (28, 28))
        self.add_line('e9', (19, 28), (19, 31))
        self.add_arc('e10', (9, 34), (13, 40), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_arc('e11', (34, 40), (37, 38), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('e12', (43, 23), (44, 21))
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1',), closed=False)
        self.add_contour('c2', *('e2', 'e3', 'e10', 'e4', 'e11', 'e5', 'e12', 'e6'), closed=False)
        self.add_contour('c3', *('e7',), closed=False)
        self.add_contour('c4', *('e8',), closed=False)
        self.add_contour('c5', *('e9',), closed=False)
        self.relate('connect', *('c0', 'c2'))
        self.relate('connect', *('c0', 'c3'))
        self.relate('connect', *('c2', 'c3'))
        self.relate('connect', *('c1', 'c2'))
        self.relate('connect', *('c1', 'c3'))
