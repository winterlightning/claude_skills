"""Red blood cell strem 1 (health), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b0a49c99-174d-4d2d-ac7c-9636f2302170'
SOURCE_PATH = 'pictographic-primitives/health/red blood cell strem 1_b0a49c99-174d-4d2d-ac7c-9636f2302170.svg'
AUTHOR = 'gpt-6'

class RedBloodCellStrem1(Solo48):
    icon_id = 'red-blood-cell-strem-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('red', 'blood', 'cell', 'strem', 'health')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('e0-1', (13, 15), (6, 30), radius_x=22, radius_y=22, large_arc=False, sweep=False)
        self.add_arc('e0-2', (6, 30), (18, 42), radius_x=12, radius_y=12, large_arc=False, sweep=False)
        self.add_arc('e0-3', (18, 42), (42, 18), radius_x=26, radius_y=26, large_arc=False, sweep=False)
        self.add_arc('e0-4', (42, 18), (30, 6), radius_x=12, radius_y=12, large_arc=False, sweep=False)
        self.add_arc('e0-5', (30, 6), (13, 15), radius_x=25, radius_y=25, large_arc=False, sweep=False)
        self.add_arc('e1-1', (23, 18), (15, 27), radius_x=19, radius_y=19, large_arc=False, sweep=False)
        self.add_arc('e1-2', (15, 27), (17, 33), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('e1-3', (17, 33), (32, 21), radius_x=18, radius_y=18, large_arc=False, sweep=False)
        self.add_arc('e1-4', (32, 21), (30, 16), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('e1-5', (30, 16), (23, 18), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_contour('c0', *('e0-1', 'e0-2', 'e0-3', 'e0-4', 'e0-5'), closed=True)
        self.add_contour('c1', *('e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5'), closed=True)
