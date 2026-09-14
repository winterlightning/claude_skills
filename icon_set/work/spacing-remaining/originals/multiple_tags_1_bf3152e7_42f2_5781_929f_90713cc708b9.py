"""Multiple tags 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bf3152e7-42f2-5781-929f-90713cc708b9'
SOURCE_PATH = 'icons-json/interface-essential/multiple tags 1_bf3152e7-42f2-5781-929f-90713cc708b9.json'
AUTHOR = 'json_to_solo'

class MultipleTags1(Solo48):
    icon_id = 'multiple-tags-1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('multiple', 'tags', 'interface-essential')

    def build(self):
        self.add_line('e0', (42, 18), (38, 40))
        self.add_line('e1', (34, 42), (22, 40))
        self.add_line('e2', (35, 6), (26, 6))
        self.add_line('e3', (22, 8), (8, 24))
        self.add_line('e4', (8, 29), (17, 40))
        self.add_line('e5', (22, 40), (37, 23))
        self.add_line('e6', (39, 18), (39, 8))
        self.add_arc('e7-top', (27, 16), (31, 16), radius_x=2)
        self.add_arc('e7-bottom', (31, 16), (27, 16), radius_x=2)
        self.add_arc('e8', (39, 13), (42, 18), radius_x=7)
        self.add_line('e9-1', (38, 40), (35, 42))
        self.add_arc('e9-2', (35, 42), (34, 42), radius_x=36, sweep=False)
        self.add_line('e10-1', (39, 8), (37, 6))
        self.add_line('e10-2', (37, 6), (35, 6))
        self.add_line('e11', (26, 6), (22, 8))
        self.add_arc('e12-1', (8, 24), (6, 27), radius_x=4, sweep=False)
        self.add_line('e12-2', (6, 27), (8, 29))
        self.add_line('e13', (17, 40), (22, 40))
        self.add_arc('e14', (37, 23), (39, 18), radius_x=5, sweep=False)
        self.add_contour('c0', 'e8', 'e0', 'e9-1', 'e9-2', 'e1')
        self.add_contour('c1', 'e10-1', 'e10-2', 'e2', 'e11', 'e3', 'e12-1', 'e12-2', 'e4', 'e13', 'e5', 'e14', 'e6', closed=True)
        self.add_contour('e7', 'e7-top', 'e7-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
