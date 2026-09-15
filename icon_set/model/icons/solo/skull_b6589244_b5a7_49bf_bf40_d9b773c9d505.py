"""Skull (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b6589244-b5a7-49bf-bf40-d9b773c9d505'
SOURCE_PATH = 'pictographic-primitives/interface-essential/skull_b6589244-b5a7-49bf-bf40-d9b773c9d505.svg'
AUTHOR = 'gpt-6'

class SkullB6589244(Solo48):
    icon_id = 'skull-b6589244'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('skull', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (24, 34), (24, 42))
        self.add_line('e1', (33, 22), (29, 26))
        self.add_line('e2', (15, 22), (20, 26))
        self.add_line('e3', (35, 35), (35, 39))
        self.add_line('e4', (31, 42), (19, 42))
        self.add_arc('e5-1', (19, 42), (16, 42), radius_x=25, radius_y=25, large_arc=False, sweep=False)
        self.add_arc('e5-2', (16, 42), (13, 39), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('e5-3', (13, 39), (12, 33))
        self.add_line('e5-4', (12, 33), (7, 29))
        self.add_line('e5-5', (7, 29), (6, 23))
        self.add_arc('e5-6', (6, 23), (23, 6), radius_x=17, radius_y=17, large_arc=False, sweep=True)
        self.add_line('e5-7', (23, 6), (30, 7))
        self.add_arc('e5-8', (30, 7), (37, 11), radius_x=19, radius_y=19, large_arc=False, sweep=True)
        self.add_arc('e5-9', (37, 11), (42, 23), radius_x=17, radius_y=17, large_arc=False, sweep=True)
        self.add_line('e5-10', (42, 23), (40, 30))
        self.add_arc('e5-11', (40, 30), (35, 35), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_arc('e6', (35, 39), (31, 42), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('c0', *('e0',), closed=False)
        self.add_contour('c1', *('e1',), closed=False)
        self.add_contour('c2', *('e2',), closed=False)
        self.add_contour('c3', *('e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7', 'e5-8', 'e5-9', 'e5-10', 'e5-11', 'e3', 'e6', 'e4'), closed=True)
        self.relate('connect', *('c0', 'c3'))
