"""Dna (artificial-intelligence), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd1f58ed3-739f-4dc3-b1ea-9283b94d4d2c'
SOURCE_PATH = 'icons-json/artificial-intelligence/dna_d1f58ed3-739f-4dc3-b1ea-9283b94d4d2c.json'
AUTHOR = 'gpt-6'

class DnaD1f58ed3(Solo48):
    icon_id = 'dna-d1f58ed3'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('dna', 'artificial-intelligence')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (29, 16), (30, 17))
        self.add_line('e1', (30, 17), (26, 17))
        self.add_line('e2', (17, 25), (18, 34))
        self.add_line('e3', (35, 17), (30, 17))
        self.add_arc('e4', (31, 6), (29, 16), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_arc('e5', (26, 17), (17, 25), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_arc('e6', (18, 34), (16, 42), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('e7', (42, 14), (35, 17), radius_x=9, radius_y=9, large_arc=False, sweep=True)
        self.add_arc('e8-1', (30, 17), (28, 28), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('e8-2', (28, 28), (26, 29), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('e8-3', (26, 29), (23, 30))
        self.add_arc('e8-4', (23, 30), (10, 29), radius_x=39, radius_y=39, large_arc=False, sweep=False)
        self.add_arc('e8-5', (10, 29), (6, 31), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_contour('c0', *('e4', 'e0', 'e1', 'e5', 'e2', 'e6'), closed=False)
        self.add_contour('c1', *('e7', 'e3', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e8-5'), closed=False)
