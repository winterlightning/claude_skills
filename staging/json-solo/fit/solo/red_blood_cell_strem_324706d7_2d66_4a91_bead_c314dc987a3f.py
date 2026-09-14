"""Red blood cell strem (health), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '324706d7-2d66-4a91-bead-c314dc987a3f'
SOURCE_PATH = 'icons-json/health/red blood cell strem_324706d7-2d66-4a91-bead-c314dc987a3f.json'
AUTHOR = 'json_to_solo'

class RedBloodCellStremHealth(Solo48):
    icon_id = 'red-blood-cell-strem-health'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('red', 'blood', 'cell', 'strem', 'health')

    def build(self):
        self.add_line('e0', (21, 41), (17, 40))
        self.add_line('e1', (17, 40), (14, 39))
        self.add_line('e2', (9, 34), (8, 31))
        self.add_line('e3', (14, 9), (17, 8))
        self.add_line('e4', (17, 8), (21, 7))
        self.add_line('e5', (31, 8), (34, 9))
        self.add_line('e6', (39, 14), (40, 17))
        self.add_line('e7', (40, 31), (39, 34))
        self.add_arc('e8', (17, 19), (20, 16), radius_x=3)
        self.add_arc('e9', (29, 31), (34, 26), radius_x=6, sweep=False)
        self.add_arc('e10', (14, 39), (9, 34), radius_x=10)
        self.add_line('e11-1', (8, 31), (6, 24))
        self.add_arc('e11-2', (6, 24), (14, 9), radius_x=23)
        self.add_arc('e12-1', (21, 7), (24, 6), radius_x=7)
        self.add_line('e12-2', (24, 6), (31, 8))
        self.add_arc('e13', (34, 9), (39, 14), radius_x=9)
        self.add_line('e14-1', (40, 17), (42, 24))
        self.add_line('e14-2', (42, 24), (40, 31))
        self.add_arc('e15-1', (39, 34), (24, 42), radius_x=24)
        self.add_arc('e15-2', (24, 42), (21, 41), radius_x=7)
        self.add_contour('c0', 'e8')
        self.add_contour('c1', 'e9')
        self.add_contour('c2', 'e0', 'e1', 'e10', 'e2', 'e11-1', 'e11-2', 'e3', 'e4', 'e12-1', 'e12-2', 'e5', 'e13', 'e6', 'e14-1', 'e14-2', 'e7', 'e15-1', 'e15-2', closed=True)
