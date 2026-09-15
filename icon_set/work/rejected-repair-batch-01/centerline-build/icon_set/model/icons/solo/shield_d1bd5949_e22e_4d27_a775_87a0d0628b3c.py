"""Shield (protection), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd1bd5949-e22e-4d27-a775-87a0d0628b3c'
SOURCE_PATH = 'pictographic-primitives/protection/shield_d1bd5949-e22e-4d27-a775-87a0d0628b3c.svg'
AUTHOR = 'gpt-6'

class ShieldD1bd5949(Solo48):
    icon_id = 'shield-d1bd5949'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('shield', 'protection')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (31, 23), (29, 25))
        self.add_line('e1', (38, 7), (32, 5))
        self.add_line('e2', (16, 6), (10, 8))
        self.add_line('e3', (8, 9), (8, 25))
        self.add_line('e4', (40, 26), (40, 8))
        self.add_arc('e5-1', (29, 25), (28, 25), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('e5-2', (28, 25), (28, 18))
        self.add_arc('e5-3', (28, 18), (25, 14), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_arc('e5-4', (25, 14), (24, 13), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_line('e5-5', (24, 13), (23, 18))
        self.add_arc('e5-6', (23, 18), (18, 24), radius_x=11, radius_y=11, large_arc=False, sweep=False)
        self.add_arc('e5-7', (18, 24), (19, 30), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_arc('e5-8', (19, 30), (28, 32), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_arc('e5-9', (28, 32), (31, 23), radius_x=9, radius_y=9, large_arc=False, sweep=False)
        self.add_arc('e6', (40, 8), (38, 7), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('e7-1', (32, 5), (25, 4))
        self.add_line('e7-2', (25, 4), (16, 6))
        self.add_arc('e8', (10, 8), (8, 9), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('e9-1', (8, 25), (24, 44), radius_x=23, radius_y=23, large_arc=False, sweep=False)
        self.add_arc('e9-2', (24, 44), (40, 26), radius_x=22, radius_y=22, large_arc=False, sweep=False)
        self.add_contour('c0', *('e0', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7', 'e5-8', 'e5-9'), closed=True)
        self.add_contour('c1', *('e6', 'e1', 'e7-1', 'e7-2', 'e2', 'e8', 'e3', 'e9-1', 'e9-2', 'e4'), closed=True)
