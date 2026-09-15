"""Number (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1edccb27-38c1-5d49-b045-3faf028ee95b'
SOURCE_PATH = 'pictographic-primitives/interface-essential/number_1edccb27-38c1-5d49-b045-3faf028ee95b.svg'
AUTHOR = 'gpt-6'

class Number(Solo48):
    icon_id = 'number'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('number', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (8, 44), (18, 44))
        self.add_line('e1', (37, 35), (34, 35))
        self.add_line('e2', (19, 7), (24, 4))
        self.add_line('e3', (24, 4), (24, 20))
        self.add_line('e4', (19, 19), (29, 19))
        self.add_arc('e5-1', (8, 30), (15, 27), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e5-2', (15, 27), (17, 33), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('e5-3', (17, 33), (10, 40), radius_x=35, radius_y=35, large_arc=False, sweep=True)
        self.add_arc('e5-4', (10, 40), (8, 44), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_arc('e6-1', (30, 29), (37, 27), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e6-2', (37, 27), (40, 31), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e6-3', (40, 31), (37, 35), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e7-1', (37, 35), (40, 38), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('e7-2', (40, 38), (40, 40))
        self.add_arc('e7-3', (40, 40), (36, 44), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('e7-4', (36, 44), (30, 40), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_contour('c0', *('e5-1', 'e5-2', 'e5-3', 'e5-4', 'e0'), closed=False)
        self.add_contour('c1', *('e6-1', 'e6-2', 'e6-3'), closed=False)
        self.add_contour('c2', *('e7-1', 'e7-2', 'e7-3', 'e7-4'), closed=False)
        self.add_contour('c3', *('e1',), closed=False)
        self.add_contour('c4', *('e2', 'e3'), closed=False)
        self.add_contour('c5', *('e4',), closed=False)
        self.relate('connect', *('c1', 'c2'))
        self.relate('connect', *('c1', 'c3'))
        self.relate('connect', *('c2', 'c3'))
        self.relate('connect', *('c4', 'c5'))
