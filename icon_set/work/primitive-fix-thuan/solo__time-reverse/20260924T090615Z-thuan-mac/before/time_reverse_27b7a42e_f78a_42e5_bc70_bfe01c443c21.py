"""Time reverse (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '27b7a42e-f78a-42e5-bc70-bfe01c443c21'
SOURCE_PATH = 'pictographic-primitives/interface-essential/time reverse_27b7a42e-f78a-42e5-bc70-bfe01c443c21.svg'
AUTHOR = 'gpt-6'

class TimeReverse(Solo48):
    icon_id = 'time-reverse'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('time', 'reverse', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (28, 4), (31, 8))
        self.add_line('e1', (31, 8), (32, 10))
        self.add_line('e2', (28, 14), (32, 10))
        self.add_line('e3', (21, 18), (21, 27))
        self.add_line('e4', (21, 27), (25, 31))
        self.add_arc('e5-1', (40, 24), (40, 28), radius_x=50, radius_y=50, large_arc=False, sweep=False)
        self.add_arc('e5-2', (40, 28), (36, 38), radius_x=18, radius_y=18, large_arc=False, sweep=True)
        self.add_arc('e5-3', (36, 38), (24, 44), radius_x=15, radius_y=15, large_arc=False, sweep=True)
        self.add_line('e5-4', (24, 44), (18, 43))
        self.add_arc('e5-5', (18, 43), (15, 41), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_arc('e5-6', (15, 41), (8, 27), radius_x=18, radius_y=18, large_arc=False, sweep=True)
        self.add_line('e5-7', (8, 27), (9, 19))
        self.add_line('e5-8', (9, 19), (13, 13))
        self.add_arc('e5-9', (13, 13), (32, 10), radius_x=15, radius_y=15, large_arc=False, sweep=True)
        self.add_contour('c0', *('e0', 'e1'), closed=False)
        self.add_contour('c1', *('e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7', 'e5-8', 'e5-9'), closed=False)
        self.add_contour('c2', *('e2',), closed=False)
        self.add_contour('c3', *('e3', 'e4'), closed=False)
        self.relate('connect', *('c0', 'c1'))
        self.relate('connect', *('c0', 'c2'))
        self.relate('connect', *('c1', 'c2'))
