"""Book pages (state), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '89e4f18d-ea56-4da8-8bbf-763032c8091a'
SOURCE_PATH = 'icons-json/state/book pages_89e4f18d-ea56-4da8-8bbf-763032c8091a.json'
AUTHOR = 'json_to_solo'

class BookPages(Solo48):
    icon_id = 'book-pages'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('book', 'pages', 'state')

    def build(self):
        self.add_line('sym-e0', (24, 13), (24, 40))
        self.add_line('sym-e1', (24, 40), (27, 38))
        self.add_arc('sym-e2', (27, 38), (34, 37), radius_x=22)
        self.add_line('sym-e3', (34, 37), (42, 36))
        self.add_line('sym-e4', (42, 36), (44, 35))
        self.add_line('sym-e5', (44, 35), (44, 34))
        self.add_line('sym-e6', (44, 34), (44, 10))
        self.add_arc('sym-e7', (44, 10), (44, 9), radius_x=1)
        self.add_arc('sym-e8', (44, 9), (42, 8), radius_x=3, sweep=False)
        self.add_line('sym-e10', (42, 8), (41, 8))
        self.add_line('sym-e11', (41, 8), (39, 8))
        self.add_line('sym-e12-1', (39, 8), (31, 9))
        self.add_arc('sym-e12-2', (31, 9), (26, 11), radius_x=16, sweep=False)
        self.add_line('sym-e13', (26, 11), (24, 13))
        self.add_line('sym-e14', (24, 13), (22, 11))
        self.add_arc('sym-e15-1', (22, 11), (17, 9), radius_x=16, sweep=False)
        self.add_line('sym-e15-2', (17, 9), (9, 8))
        self.add_arc('sym-e16', (9, 8), (7, 8), radius_x=24)
        self.add_line('sym-e17', (7, 8), (6, 8))
        self.add_arc('sym-e19', (6, 8), (4, 9), radius_x=3, sweep=False)
        self.add_line('sym-e20', (4, 9), (4, 10))
        self.add_line('sym-e21', (4, 10), (4, 34))
        self.add_line('sym-e22', (4, 34), (4, 35))
        self.add_line('sym-e23', (4, 35), (6, 36))
        self.add_line('sym-e24', (6, 36), (14, 37))
        self.add_arc('sym-e25', (14, 37), (21, 38), radius_x=22)
        self.add_line('sym-e26', (21, 38), (24, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e10', 'sym-e11', 'sym-e12-1', 'sym-e12-2', 'sym-e13', 'sym-e14', 'sym-e15-1', 'sym-e15-2', 'sym-e16', 'sym-e17', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26')
