"""Scale 1 (products), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5e3fffa5-d7af-5545-8af0-f19ba6fc443d'
SOURCE_PATH = 'pictographic-primitives/products/scale 1_5e3fffa5-d7af-5545-8af0-f19ba6fc443d.svg'
AUTHOR = 'gpt-6'

class Scale1(Solo48):
    icon_id = 'scale-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'products'
    categories = ('products', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('scale', 'products')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (24, 18), (24, 23))
        self.add_line('e1', (20, 23), (28, 23))
        self.add_line('e2', (15, 42), (35, 42))
        self.add_line('e3', (42, 35), (42, 13))
        self.add_line('e4', (35, 6), (13, 6))
        self.add_line('e5', (6, 14), (6, 35))
        self.add_arc('e6-1', (28, 23), (32, 17), radius_x=22, radius_y=22, large_arc=False, sweep=False)
        self.add_arc('e6-2', (32, 17), (22, 15), radius_x=13, radius_y=13, large_arc=False, sweep=False)
        self.add_arc('e6-3', (22, 15), (16, 17), radius_x=14, radius_y=14, large_arc=False, sweep=False)
        self.add_arc('e6-4', (16, 17), (20, 23), radius_x=12, radius_y=12, large_arc=False, sweep=False)
        self.add_line('e7-1', (6, 35), (7, 39))
        self.add_arc('e7-2', (7, 39), (9, 41), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('e7-3', (9, 41), (14, 42))
        self.add_arc('e7-4', (14, 42), (15, 42), radius_x=23, radius_y=23, large_arc=False, sweep=True)
        self.add_arc('e8', (35, 42), (42, 35), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_arc('e9', (42, 13), (35, 6), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('e10-1', (13, 6), (8, 8))
        self.add_arc('e10-2', (8, 8), (6, 12), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('e10-3', (6, 12), (6, 14))
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1', 'e6-1', 'e6-2', 'e6-3', 'e6-4'), closed=True)
        self.add_contour('c2', *('e7-1', 'e7-2', 'e7-3', 'e7-4', 'e2', 'e8', 'e3', 'e9', 'e4', 'e10-1', 'e10-2', 'e10-3', 'e5'), closed=True)
        self.relate('connect', *('c0', 'c1'))
