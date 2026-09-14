"""Table cabinets (office), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e19', (42, 8), ((42.364, 8.16), (42.336, 8), (42.691, 8.093)), ((43.1, 8.244), (43.745, 8.859), (43.9, 9.238)), ((43.973, 9.423), (43.909, 9.823), (44, 10)))
        self.add_bezier('e20', (5, 8), ((4.9, 8.008), (4.7, 8.017), (4.6, 8.025)), ((4.209, 8.177), (4.2, 8.731), (4, 9)))
        self.add_bezier('e21', (4, 16), ((4, 16.076), (4, 15.731), (4, 15.806)), ((4, 16.514), (4.536, 16.537), (5, 17)))
        self.add_bezier('e22', (32, 38), ((32.327, 38.598), (32.782, 39.655), (33.545, 39.907)), ((33.736, 39.975), (33.809, 39.916), (34, 40)))
        self.add_bezier('e23', (42, 40), ((42.682, 39.739), (43.655, 39.478), (43.918, 38.72)), ((43.945, 38.585), (43.973, 38.135), (44, 38)))
        self.add_bezier('e24', (20, 23), ((18.964, 23.177), (18.436, 23.537), (17.864, 24.472)), ((17.791, 24.598), (18, 24.857), (18, 25)))
        self.add_bezier('e25', (18, 30), ((18, 30.741), (17.236, 31.672), (16.573, 32.126)), ((16.336, 32.286), (16.255, 31.882), (16, 32)))
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
