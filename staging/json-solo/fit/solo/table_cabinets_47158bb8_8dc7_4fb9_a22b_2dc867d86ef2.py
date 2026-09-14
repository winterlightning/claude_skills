"""Table cabinets (office), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47158bb8-8dc7-4fb9-a22b-2dc867d86ef2'
SOURCE_PATH = 'icons-json/office/table cabinets_47158bb8-8dc7-4fb9-a22b-2dc867d86ef2.json'
AUTHOR = 'json_to_solo'

class TableCabinetsOffice(Solo48):
    icon_id = 'table-cabinets-office'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('table', 'cabinets', 'office')

    def build(self):
        self.add_line('e0', (25, 26), (32, 26))
        self.add_line('e1', (32, 8), (32, 17))
        self.add_line('e2', (32, 8), (42, 8))
        self.add_line('e3', (44, 10), (44, 26))
        self.add_line('e4', (32, 8), (5, 8))
        self.add_line('e5', (4, 9), (4, 16))
        self.add_line('e6', (5, 17), (32, 17))
        self.add_line('e7', (32, 17), (32, 26))
        self.add_line('e8', (32, 26), (44, 26))
        self.add_line('e9', (32, 26), (32, 38))
        self.add_line('e10', (34, 40), (42, 40))
        self.add_line('e11', (44, 38), (44, 26))
        self.add_line('e12', (18, 25), (18, 30))
        self.add_line('e13', (16, 32), (14, 32))
        self.add_line('e14', (10, 32), (14, 32))
        self.add_line('e15', (9, 39), (14, 37))
        self.add_line('e16', (18, 39), (14, 37))
        self.add_line('e17', (14, 32), (14, 37))
        self.add_line('e18', (4, 40), (4, 27))
        self.add_arc('e19', (42, 8), (44, 10), radius_x=2)
        self.add_arc('e20', (5, 8), (4, 9), radius_x=1, sweep=False)
        self.add_line('e21', (4, 16), (5, 17))
        self.add_arc('e22', (32, 38), (34, 40), radius_x=2, sweep=False)
        self.add_arc('e23', (42, 40), (44, 38), radius_x=2, sweep=False)
        self.add_arc('e24', (20, 23), (18, 25), radius_x=3, sweep=False)
        self.add_arc('e25', (18, 30), (16, 32), radius_x=2)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e19', 'e3')
        self.add_contour('c3', 'e4', 'e20', 'e5', 'e21', 'e6')
        self.add_contour('c4', 'e7')
        self.add_contour('c5', 'e8')
        self.add_contour('c6', 'e9', 'e22', 'e10', 'e23', 'e11')
        self.add_contour('c7', 'e24', 'e12', 'e25', 'e13')
        self.add_contour('c8', 'e14')
        self.add_contour('c9', 'e15')
        self.add_contour('c10', 'e16')
        self.add_contour('c11', 'e17')
        self.add_contour('c12', 'e18')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c11', 'c7')
        self.relate('connect', 'c11', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c10', 'c11')
        self.relate('connect', 'c10', 'c9')
        self.relate('connect', 'c11', 'c9')
