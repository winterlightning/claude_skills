"""Paginate filter mail (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f1ab20b-c104-57ec-81a9-d9fad759c5d8'
SOURCE_PATH = 'icons-json/interface-essential/paginate filter mail_3f1ab20b-c104-57ec-81a9-d9fad759c5d8.json'
AUTHOR = 'json_to_solo'

class PaginateFilterMailInterfaceEssential(Solo48):
    icon_id = 'paginate-filter-mail-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('paginate', 'filter', 'mail', 'interface-essential')

    def build(self):
        self.add_line('e0', (4, 9), (24, 27))
        self.add_line('e1', (24, 27), (44, 8))
        self.add_line('e2', (44, 8), (44, 37))
        self.add_line('e3', (41, 40), (7, 40))
        self.add_line('e4', (4, 37), (4, 9))
        self.add_line('e5', (44, 8), (4, 8))
        self.add_bezier('e6', (44, 37), ((44, 37.135), (43.991, 37.735), (43.991, 37.869)), ((43.991, 38.897), (43.055, 39.992), (41.909, 39.992)), ((41.836, 40), (41.773, 40), (41.7, 40)), ((41.555, 40), (41.145, 40), (41, 40)))
        self.add_bezier('e7', (7, 40), ((6.855, 40), (6.445, 39.992), (6.3, 39.992)), ((5.236, 39.992), (4.009, 39.032), (4.009, 38.021)), ((4.009, 37.962), (4, 37.903), (4, 37.844)), ((4, 37.718), (4, 37.126), (4, 37)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e6', 'e3', 'e7', 'e4', closed=True)
        self.add_contour('c1', 'e5')
        self.relate('connect', 'c0', 'c1')
