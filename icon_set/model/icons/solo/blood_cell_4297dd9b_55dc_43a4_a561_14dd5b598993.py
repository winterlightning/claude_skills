"""Blood cell (other), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4297dd9b-55dc-43a4-a561-14dd5b598993'
SOURCE_PATH = 'icons-json/other/blood cell_4297dd9b-55dc-43a4-a561-14dd5b598993.json'
AUTHOR = 'json_to_solo'

class BloodCell(Solo48):
    icon_id = 'blood-cell'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('blood', 'cell', 'other')

    def build(self):
        self.add_arc('sym-e1', (24, 42), (28, 40), radius_x=5, sweep=False)
        self.add_arc('sym-e2', (28, 40), (29, 39), radius_x=7)
        self.add_line('sym-e5', (29, 39), (31, 39))
        self.add_line('sym-e6', (31, 39), (34, 39))
        self.add_arc('sym-e7', (34, 39), (37, 35), radius_x=6, sweep=False)
        self.add_line('sym-e8', (37, 35), (38, 33))
        self.add_line('sym-e10', (38, 33), (40, 32))
        self.add_line('sym-e11', (40, 32), (42, 27))
        self.add_arc('sym-e13', (42, 27), (42, 26), radius_x=30)
        self.add_line('sym-e14', (42, 26), (41, 22))
        self.add_line('sym-e15', (41, 22), (40, 21))
        self.add_line('sym-e16', (40, 21), (40, 20))
        self.add_arc('sym-e17', (40, 20), (40, 17), radius_x=10)
        self.add_arc('sym-e18', (40, 17), (35, 12), radius_x=7, sweep=False)
        self.add_line('sym-e19', (35, 12), (34, 12))
        self.add_line('sym-e20', (34, 12), (33, 12))
        self.add_arc('sym-e21', (33, 12), (33, 11), radius_x=7)
        self.add_arc('sym-e22', (33, 11), (31, 9), radius_x=8)
        self.add_arc('sym-e23', (31, 9), (25, 6), radius_x=8, sweep=False)
        self.add_line('sym-e24', (25, 6), (24, 6))
        self.add_line('sym-e25', (24, 6), (23, 6))
        self.add_arc('sym-e26', (23, 6), (17, 9), radius_x=8, sweep=False)
        self.add_arc('sym-e27', (17, 9), (15, 11), radius_x=7, sweep=False)
        self.add_arc('sym-e28', (15, 11), (15, 12), radius_x=7)
        self.add_line('sym-e29', (15, 12), (14, 12))
        self.add_line('sym-e30', (14, 12), (13, 12))
        self.add_arc('sym-e31', (13, 12), (8, 17), radius_x=7, sweep=False)
        self.add_arc('sym-e32', (8, 17), (8, 20), radius_x=10, sweep=False)
        self.add_line('sym-e33', (8, 20), (8, 21))
        self.add_arc('sym-e34', (8, 21), (7, 22), radius_x=9, sweep=False)
        self.add_line('sym-e35', (7, 22), (6, 26))
        self.add_line('sym-e36', (6, 26), (6, 27))
        self.add_line('sym-e38', (6, 27), (8, 32))
        self.add_line('sym-e39', (8, 32), (10, 33))
        self.add_arc('sym-e41', (10, 33), (11, 35), radius_x=38, sweep=False)
        self.add_arc('sym-e42', (11, 35), (14, 39), radius_x=7, sweep=False)
        self.add_line('sym-e43', (14, 39), (17, 39))
        self.add_line('sym-e44', (17, 39), (19, 39))
        self.add_arc('sym-e47', (19, 39), (20, 40), radius_x=7)
        self.add_arc('sym-e48', (20, 40), (24, 42), radius_x=5, sweep=False)
        self.add_contour('sym-c0', 'sym-e1', 'sym-e2', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e10', 'sym-e11', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35', 'sym-e36', 'sym-e38', 'sym-e39', 'sym-e41', 'sym-e42', 'sym-e43', 'sym-e44', 'sym-e47', 'sym-e48', closed=True)
