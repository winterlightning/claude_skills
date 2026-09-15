"""@ (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c572fd17-f237-44a3-8722-0188d32a7da1'
SOURCE_PATH = 'pictographic-primitives/symbol/@_c572fd17-f237-44a3-8722-0188d32a7da1.svg'
AUTHOR = 'gpt-6'

class IconSymbol(Solo48):
    icon_id = 'icon-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('symbol',)

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('e0', (32, 28), (34, 31))
        self.add_arc('e1-1', (34, 31), (41, 29), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('e1-2', (41, 29), (42, 24))
        self.add_arc('e1-3', (42, 24), (24, 6), radius_x=18, radius_y=18, large_arc=False, sweep=False)
        self.add_arc('e1-4', (24, 6), (6, 24), radius_x=18, radius_y=18, large_arc=False, sweep=False)
        self.add_line('e1-5', (6, 24), (7, 30))
        self.add_arc('e1-6', (7, 30), (9, 34), radius_x=17, radius_y=17, large_arc=False, sweep=False)
        self.add_arc('e1-7', (9, 34), (18, 41), radius_x=17, radius_y=17, large_arc=False, sweep=False)
        self.add_line('e1-8', (18, 41), (23, 42))
        self.add_arc('e1-9', (23, 42), (28, 41), radius_x=21, radius_y=21, large_arc=False, sweep=True)
        self.add_arc('e2-1', (32, 28), (28, 18), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_arc('e2-2', (28, 18), (18, 20), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_arc('e2-3', (18, 20), (20, 32), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_arc('e2-4', (20, 32), (32, 28), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_contour('c0', *('e0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e1-9'), closed=False)
        self.add_contour('c1', *('e2-1', 'e2-2', 'e2-3', 'e2-4'), closed=True)
