"""Format catalog hive (programing), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a99356b9-4a4e-46d2-a937-aba6dd12d9e1'
SOURCE_PATH = 'icons-json/programing/format catalog hive_a99356b9-4a4e-46d2-a937-aba6dd12d9e1.json'
AUTHOR = 'json_to_solo'

class FormatCatalogHivePrograming(Solo48):
    icon_id = 'format-catalog-hive-programing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('format', 'catalog', 'hive', 'programing')

    def build(self):
        self.add_line('e0', (33, 22), (42, 26))
        self.add_line('e1', (42, 26), (42, 36))
        self.add_line('e2', (41, 37), (34, 42))
        self.add_line('e3', (33, 42), (24, 37))
        self.add_line('e4', (33, 22), (24, 26))
        self.add_line('e5', (33, 22), (33, 12))
        self.add_line('e6', (32, 11), (24, 6))
        self.add_line('e7', (23, 6), (16, 11))
        self.add_line('e8', (15, 12), (15, 22))
        self.add_line('e9', (15, 22), (24, 26))
        self.add_line('e10', (15, 22), (7, 26))
        self.add_line('e11', (6, 27), (6, 36))
        self.add_line('e12', (7, 37), (15, 42))
        self.add_line('e13', (15, 42), (24, 37))
        self.add_line('e14', (24, 37), (24, 26))
        self.add_arc('e15', (42, 36), (41, 37), radius_x=1)
        self.add_line('e16', (34, 42), (33, 42))
        self.add_arc('e17', (33, 12), (32, 11), radius_x=10)
        self.add_line('e18', (24, 6), (23, 6))
        self.add_arc('e19', (16, 11), (15, 12), radius_x=3, sweep=False)
        self.add_arc('e20', (7, 26), (6, 27), radius_x=4, sweep=False)
        self.add_arc('e21', (6, 36), (7, 37), radius_x=1, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e15', 'e2', 'e16', 'e3')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e5', 'e17', 'e6', 'e18', 'e7', 'e19', 'e8')
        self.add_contour('c3', 'e9')
        self.add_contour('c4', 'e10', 'e20', 'e11', 'e21', 'e12', 'e13')
        self.add_contour('c5', 'e14')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
