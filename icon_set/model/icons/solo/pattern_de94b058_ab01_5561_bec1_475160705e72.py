'Pattern: nine identical rounded cells on a regular grid, replacing warped unequal loops.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'de94b058-ab01-5561-bec1-475160705e72'
SOURCE_PATH = 'icons-json/design/pattern_de94b058-ab01-5561-bec1-475160705e72.json'
AUTHOR = 'gpt-6'

class Pattern(Solo48):
    icon_id = 'pattern'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pattern', 'design')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('cell-0-0-0', (9, 6), (15, 6))
        self.add_arc('cell-0-0-1', (15, 6), (18, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('cell-0-0-2', (18, 9), (18, 15))
        self.add_arc('cell-0-0-3', (18, 15), (15, 18), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('cell-0-0-4', (15, 18), (9, 18))
        self.add_arc('cell-0-0-5', (9, 18), (6, 15), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('cell-0-0-6', (6, 15), (6, 9))
        self.add_arc('cell-0-0-7', (6, 9), (9, 6), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('cell-0-1-0', (33, 6), (39, 6))
        self.add_arc('cell-0-1-1', (39, 6), (42, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('cell-0-1-2', (42, 9), (42, 15))
        self.add_arc('cell-0-1-3', (42, 15), (39, 18), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('cell-0-1-4', (39, 18), (33, 18))
        self.add_arc('cell-0-1-5', (33, 18), (30, 15), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('cell-0-1-6', (30, 15), (30, 9))
        self.add_arc('cell-0-1-7', (30, 9), (33, 6), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('cell-1-0-0', (9, 30), (15, 30))
        self.add_arc('cell-1-0-1', (15, 30), (18, 33), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('cell-1-0-2', (18, 33), (18, 39))
        self.add_arc('cell-1-0-3', (18, 39), (15, 42), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('cell-1-0-4', (15, 42), (9, 42))
        self.add_arc('cell-1-0-5', (9, 42), (6, 39), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('cell-1-0-6', (6, 39), (6, 33))
        self.add_arc('cell-1-0-7', (6, 33), (9, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('cell-1-1-0', (33, 30), (39, 30))
        self.add_arc('cell-1-1-1', (39, 30), (42, 33), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('cell-1-1-2', (42, 33), (42, 39))
        self.add_arc('cell-1-1-3', (42, 39), (39, 42), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('cell-1-1-4', (39, 42), (33, 42))
        self.add_arc('cell-1-1-5', (33, 42), (30, 39), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('cell-1-1-6', (30, 39), (30, 33))
        self.add_arc('cell-1-1-7', (30, 33), (33, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('cell-0-0', *('cell-0-0-0', 'cell-0-0-1', 'cell-0-0-2', 'cell-0-0-3', 'cell-0-0-4', 'cell-0-0-5', 'cell-0-0-6', 'cell-0-0-7'), closed=True)
        self.add_contour('cell-0-1', *('cell-0-1-0', 'cell-0-1-1', 'cell-0-1-2', 'cell-0-1-3', 'cell-0-1-4', 'cell-0-1-5', 'cell-0-1-6', 'cell-0-1-7'), closed=True)
        self.add_contour('cell-1-0', *('cell-1-0-0', 'cell-1-0-1', 'cell-1-0-2', 'cell-1-0-3', 'cell-1-0-4', 'cell-1-0-5', 'cell-1-0-6', 'cell-1-0-7'), closed=True)
        self.add_contour('cell-1-1', *('cell-1-1-0', 'cell-1-1-1', 'cell-1-1-2', 'cell-1-1-3', 'cell-1-1-4', 'cell-1-1-5', 'cell-1-1-6', 'cell-1-1-7'), closed=True)
