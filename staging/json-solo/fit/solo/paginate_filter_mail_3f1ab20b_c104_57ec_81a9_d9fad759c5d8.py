"""Paginate filter mail (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_line('e6-1', (44, 37), (44, 38))
        self.add_arc('e6-2', (44, 38), (42, 40), radius_x=2)
        self.add_line('e6-3', (42, 40), (41, 40))
        self.add_line('e7-1', (7, 40), (6, 40))
        self.add_arc('e7-2', (6, 40), (4, 38), radius_x=2)
        self.add_line('e7-3', (4, 38), (4, 37))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e6-1', 'e6-2', 'e6-3', 'e3', 'e7-1', 'e7-2', 'e7-3', 'e4', closed=True)
        self.add_contour('c1', 'e5')
        self.relate('connect', 'c0', 'c1')
