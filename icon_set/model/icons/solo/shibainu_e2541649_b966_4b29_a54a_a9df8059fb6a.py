"""Shibainu (pets), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e2541649-b966-4b29-a54a-a9df8059fb6a'
SOURCE_PATH = 'pictographic-primitives/pets/shibainu_e2541649-b966-4b29-a54a-a9df8059fb6a.svg'
AUTHOR = 'gpt-6'

class Shibainu(Solo48):
    icon_id = 'shibainu'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    categories = ('pets', 'primitives')
    aliases = ()
    keywords = ('shibainu', 'pets')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (7, 36), (8, 33))
        self.add_line('e1', (13, 8), (17, 11))
        self.add_arc('e2', (7, 42), (7, 36), radius_x=15, radius_y=15, large_arc=False, sweep=True)
        self.add_arc('e3-1', (8, 33), (9, 18), radius_x=17, radius_y=17, large_arc=False, sweep=True)
        self.add_arc('e3-2', (9, 18), (6, 10), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('e3-3', (6, 10), (7, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e3-4', (7, 7), (9, 6), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('e3-5', (9, 6), (13, 8))
        self.add_arc('e4-1', (17, 11), (31, 11), radius_x=21, radius_y=21, large_arc=False, sweep=True)
        self.add_arc('e4-2', (31, 11), (39, 6), radius_x=17, radius_y=17, large_arc=False, sweep=True)
        self.add_arc('e4-3', (39, 6), (41, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('e4-4', (41, 7), (42, 10), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e4-5', (42, 10), (39, 18), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('e4-6', (39, 18), (40, 33), radius_x=17, radius_y=17, large_arc=False, sweep=True)
        self.add_arc('e5', (12, 29), (8, 33), radius_x=25, radius_y=25, large_arc=False, sweep=False)
        self.add_line('e6', (36, 28), (40, 33))
        self.add_line('e7', (40, 33), (41, 42))
        self.add_contour('c0', *('e2', 'e0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e1', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6'), closed=False)
        self.add_contour('c1', *('e5',), closed=False)
        self.add_contour('c2', *('e6',), closed=False)
        self.add_contour('c3', *('e7',), closed=False)
        self.relate('connect', *('c0', 'c2'))
        self.relate('connect', *('c0', 'c3'))
        self.relate('connect', *('c2', 'c3'))
