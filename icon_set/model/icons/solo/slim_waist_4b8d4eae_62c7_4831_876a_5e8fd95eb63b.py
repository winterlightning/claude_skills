"""Slim waist (beauty), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b8d4eae-62c7-4831-876a-5e8fd95eb63b'
SOURCE_PATH = 'pictographic-primitives/beauty/slim waist_4b8d4eae-62c7-4831-876a-5e8fd95eb63b.svg'
AUTHOR = 'gpt-6'

class SlimWaist(Solo48):
    icon_id = 'slim-waist'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'beauty'
    aliases = ()
    keywords = ('slim', 'waist', 'beauty')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (13, 37), (19, 39))
        self.add_line('e1', (29, 39), (35, 37))
        self.add_line('e2', (16, 18), (20, 17))
        self.add_line('e3', (27, 17), (32, 17))
        self.add_line('e4', (36, 32), (40, 36))
        self.add_line('e5', (21, 6), (23, 8))
        self.add_line('e6-1', (7, 6), (6, 10))
        self.add_arc('e6-2', (6, 10), (12, 18), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_arc('e7-1', (6, 42), (8, 37), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('e7-2', (8, 37), (13, 37), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e8', (19, 39), (29, 39), radius_x=19, radius_y=19, large_arc=False, sweep=False)
        self.add_line('e9', (35, 37), (40, 36))
        self.add_line('e10', (42, 42), (40, 36))
        self.add_line('e11-1', (41, 6), (42, 10))
        self.add_arc('e11-2', (42, 10), (36, 17), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('e12', (12, 18), (16, 18), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_arc('e13', (20, 17), (27, 17), radius_x=13, radius_y=13, large_arc=False, sweep=True)
        self.add_arc('e14', (32, 17), (36, 17), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_arc('e15', (12, 18), (9, 35), radius_x=13, radius_y=13, large_arc=False, sweep=True)
        self.add_arc('e16', (36, 17), (36, 32), radius_x=15, radius_y=15, large_arc=False, sweep=False)
        self.add_arc('e17', (23, 8), (27, 6), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_arc('e18', (24, 31), (24, 30), radius_x=34, radius_y=34, large_arc=False, sweep=True)
        self.add_contour('c0', *('e6-1', 'e6-2'), closed=False)
        self.add_contour('c1', *('e7-1', 'e7-2', 'e0', 'e8', 'e1', 'e9'), closed=False)
        self.add_contour('c2', *('e10',), closed=False)
        self.add_contour('c3', *('e11-1', 'e11-2'), closed=False)
        self.add_contour('c4', *('e12', 'e2', 'e13', 'e3', 'e14'), closed=False)
        self.add_contour('c5', *('e15',), closed=False)
        self.add_contour('c6', *('e16', 'e4'), closed=False)
        self.add_contour('c7', *('e5', 'e17'), closed=False)
        self.add_contour('c8', *('e18',), closed=False)
        self.relate('connect', *('c0', 'c4'))
        self.relate('connect', *('c0', 'c5'))
        self.relate('connect', *('c4', 'c5'))
        self.relate('connect', *('c1', 'c2'))
        self.relate('connect', *('c1', 'c6'))
        self.relate('connect', *('c2', 'c6'))
        self.relate('connect', *('c3', 'c4'))
        self.relate('connect', *('c3', 'c6'))
        self.relate('connect', *('c4', 'c6'))
