"""Dice (entertainment), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '56c4bb3a-2663-5bb0-8f4d-f5de1cfcafb7'
SOURCE_PATH = 'pictographic-primitives/entertainment/dice_56c4bb3a-2663-5bb0-8f4d-f5de1cfcafb7.svg'
AUTHOR = 'gpt-6'

class DiceEntertainment(Solo48):
    icon_id = 'dice-entertainment'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    aliases = ()
    keywords = ('dice', 'entertainment')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (6, 35), (6, 13))
        self.add_line('e1', (13, 6), (36, 6))
        self.add_line('e2', (42, 11), (42, 35))
        self.add_line('e3', (35, 42), (13, 42))
        self.add_arc('e4', (15, 15), (15, 16), radius_x=15, radius_y=15, large_arc=False, sweep=False)
        self.add_arc('e5', (33, 15), (33, 16), radius_x=20, radius_y=20, large_arc=False, sweep=False)
        self.add_arc('e6', (33, 32), (33, 33), radius_x=34, radius_y=34, large_arc=False, sweep=False)
        self.add_arc('e7', (24, 24), (24, 25), radius_x=24, radius_y=24, large_arc=False, sweep=False)
        self.add_arc('e8', (15, 32), (15, 33), radius_x=44, radius_y=44, large_arc=False, sweep=False)
        self.add_line('e9-1', (13, 42), (9, 41))
        self.add_arc('e9-2', (9, 41), (6, 36), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('e9-3', (6, 36), (6, 35))
        self.add_arc('e10', (6, 13), (13, 6), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('e11', (36, 6), (42, 11), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('e12-1', (42, 35), (42, 36))
        self.add_arc('e12-2', (42, 36), (36, 42), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('e12-3', (36, 42), (35, 42))
        self.add_contour('c0', *('e4',), closed=False)
        self.add_contour('c1', *('e5',), closed=False)
        self.add_contour('c2', *('e6',), closed=False)
        self.add_contour('c3', *('e7',), closed=False)
        self.add_contour('c4', *('e8',), closed=False)
        self.add_contour('c5', *('e9-1', 'e9-2', 'e9-3', 'e0', 'e10', 'e1', 'e11', 'e2', 'e12-1', 'e12-2', 'e12-3', 'e3'), closed=True)
