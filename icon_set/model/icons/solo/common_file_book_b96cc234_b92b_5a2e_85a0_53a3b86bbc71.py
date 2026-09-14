"""Common file book (office), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b96cc234-b92b-5a2e-85a0-53a3b86bbc71'
SOURCE_PATH = 'icons-json/office/common file book_b96cc234-b92b-5a2e-85a0-53a3b86bbc71.json'
AUTHOR = 'json_to_solo'

class CommonFileBook(Solo48):
    icon_id = 'common-file-book'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('common', 'file', 'book', 'office')

    def build(self):
        self.add_line('sym-e0', (24, 40), (24, 8))
        self.add_line('sym-e1', (24, 8), (10, 8))
        self.add_line('sym-e2', (10, 8), (8, 10))
        self.add_line('sym-e3', (8, 10), (5, 13))
        self.add_arc('sym-e4', (5, 13), (4, 14), radius_x=6, sweep=False)
        self.add_line('sym-e6', (4, 14), (4, 37))
        self.add_arc('sym-e8', (4, 37), (7, 40), radius_x=3, sweep=False)
        self.add_line('sym-e10', (7, 40), (24, 40))
        self.add_line('sym-e11', (24, 40), (41, 40))
        self.add_arc('sym-e13', (41, 40), (44, 37), radius_x=3, sweep=False)
        self.add_line('sym-e15', (44, 37), (44, 14))
        self.add_line('sym-e17', (44, 14), (43, 13))
        self.add_line('sym-e18', (43, 13), (40, 10))
        self.add_line('sym-e19', (40, 10), (38, 8))
        self.add_line('sym-e20', (38, 8), (24, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e6', 'sym-e8', 'sym-e10', 'sym-e11', 'sym-e13', 'sym-e15', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20')
