"""Skull (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '85266d86-6f31-4d3b-91ca-d5a232d0c46c'
SOURCE_PATH = 'icons-json/interface-essential/skull_85266d86-6f31-4d3b-91ca-d5a232d0c46c.json'
AUTHOR = 'gpt-6'

class Skull85266d86(Solo48):
    icon_id = 'skull-85266d86'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('skull', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (15, 44), (15, 38))
        self.add_line('e1', (33, 39), (33, 44))
        self.add_line('e2', (24, 38), (24, 44))
        self.add_line('e3-1', (15, 38), (9, 28))
        self.add_line('e3-2', (9, 28), (8, 22))
        self.add_line('e3-3', (8, 22), (10, 13))
        self.add_arc('e3-4', (10, 13), (14, 8), radius_x=18, radius_y=18, large_arc=False, sweep=True)
        self.add_arc('e3-5', (14, 8), (18, 5), radius_x=15, radius_y=15, large_arc=False, sweep=True)
        self.add_line('e3-6', (18, 5), (24, 4))
        self.add_line('e3-7', (24, 4), (32, 6))
        self.add_arc('e3-8', (32, 6), (38, 13), radius_x=19, radius_y=19, large_arc=False, sweep=True)
        self.add_line('e3-9', (38, 13), (40, 22))
        self.add_line('e3-10', (40, 22), (39, 28))
        self.add_arc('e3-11', (39, 28), (34, 36), radius_x=23, radius_y=23, large_arc=False, sweep=True)
        self.add_line('e3-12', (34, 36), (33, 39))
        self.add_line('e4', (31, 24), (31, 24))
        self.add_line('e5', (17, 24), (17, 24))
        self.add_contour('c0', *('e0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e3-8', 'e3-9', 'e3-10', 'e3-11', 'e3-12', 'e1'), closed=False)
        self.add_contour('c1', *('e2',), closed=False)
