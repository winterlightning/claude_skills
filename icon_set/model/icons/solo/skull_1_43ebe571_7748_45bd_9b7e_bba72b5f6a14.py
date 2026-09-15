"""Skull 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '43ebe571-7748-45bd-9b7e-bba72b5f6a14'
SOURCE_PATH = 'pictographic-primitives/interface-essential/skull 1_43ebe571-7748-45bd-9b7e-bba72b5f6a14.svg'
AUTHOR = 'gpt-6'

class Skull1(Solo48):
    icon_id = 'skull-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('skull', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (29, 24), (33, 22))
        self.add_line('e1', (19, 24), (15, 22))
        self.add_line('e2', (15, 42), (15, 38))
        self.add_line('e3', (38, 33), (35, 35))
        self.add_line('e4', (34, 38), (34, 42))
        self.add_line('e5', (24, 42), (24, 40))
        self.add_line('e6-1', (15, 38), (14, 35))
        self.add_arc('e6-2', (14, 35), (8, 31), radius_x=15, radius_y=15, large_arc=False, sweep=True)
        self.add_line('e6-3', (8, 31), (6, 24))
        self.add_arc('e6-4', (6, 24), (24, 6), radius_x=18, radius_y=18, large_arc=False, sweep=True)
        self.add_arc('e6-5', (24, 6), (42, 24), radius_x=18, radius_y=18, large_arc=False, sweep=True)
        self.add_arc('e6-6', (42, 24), (41, 29), radius_x=13, radius_y=13, large_arc=False, sweep=True)
        self.add_arc('e6-7', (41, 29), (38, 33), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('e7', (35, 35), (34, 38), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1',), closed=False)
        self.add_contour('c2', *('e2', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e6-6', 'e6-7', 'e3', 'e7', 'e4'), closed=False)
        self.add_contour('c3', *('e5',), closed=False)
