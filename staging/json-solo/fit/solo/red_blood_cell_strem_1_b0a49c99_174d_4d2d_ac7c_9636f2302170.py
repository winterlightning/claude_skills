"""Red blood cell strem 1 (health), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b0a49c99-174d-4d2d-ac7c-9636f2302170'
SOURCE_PATH = 'icons-json/health/red blood cell strem 1_b0a49c99-174d-4d2d-ac7c-9636f2302170.json'
AUTHOR = 'json_to_solo'

class RedBloodCellStrem1Health(Solo48):
    icon_id = 'red-blood-cell-strem-1-health'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('red', 'blood', 'cell', 'strem', 'health')

    def build(self):
        self.add_arc('e0-1', (13, 15), (6, 30), radius_x=22, sweep=False)
        self.add_arc('e0-2', (6, 30), (18, 42), radius_x=12, sweep=False)
        self.add_arc('e0-3', (18, 42), (42, 18), radius_x=26, sweep=False)
        self.add_arc('e0-4', (42, 18), (30, 6), radius_x=12, sweep=False)
        self.add_arc('e0-5', (30, 6), (13, 15), radius_x=25, sweep=False)
        self.add_arc('e1-1', (23, 17), (15, 26), radius_x=19, sweep=False)
        self.add_arc('e1-2', (15, 26), (17, 32), radius_x=4, sweep=False)
        self.add_arc('e1-3', (17, 32), (32, 20), radius_x=18, sweep=False)
        self.add_arc('e1-4', (32, 20), (30, 15), radius_x=4, sweep=False)
        self.add_arc('e1-5', (30, 15), (23, 17), radius_x=10, sweep=False)
        self.add_contour('c0', 'e0-1', 'e0-2', 'e0-3', 'e0-4', 'e0-5', closed=True)
        self.add_contour('c1', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', closed=True)
