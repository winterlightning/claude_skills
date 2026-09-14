"""Common file book (office), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b96cc234-b92b-5a2e-85a0-53a3b86bbc71'
SOURCE_PATH = 'icons-json/office/common file book_b96cc234-b92b-5a2e-85a0-53a3b86bbc71.json'
AUTHOR = 'json_to_solo'

class CommonFileBookOffice(Solo48):
    icon_id = 'common-file-book-office'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('common', 'file', 'book', 'office')

    def build(self):
        self.add_line('sym-e0', (24, 40), (24, 8))
        self.add_line('sym-e1', (24, 8), (10, 8))
        self.add_bezier('sym-e2', (10, 8), ((9.018, 8), (8.673, 9.34), (8, 10)))
        self.add_bezier('sym-e3', (8, 10), ((6.982, 11), (5.982, 11.95), (5, 13)))
        self.add_bezier('sym-e4', (5, 13), ((4.718, 13.3), (4.218, 13.64), (4, 14)))
        self.add_bezier('sym-e5', (4, 14), ((4, 14.13), (4.082, 13.86), (4, 14)))
        self.add_line('sym-e6', (4, 14), (4, 37))
        self.add_bezier('sym-e7', (4, 37), ((4, 37.11), (4, 36.9), (4, 37)))
        self.add_bezier('sym-e8', (4, 37), ((4, 38.39), (5.755, 40), (7, 40)))
        self.add_bezier('sym-e9', (7, 40), ((7.073, 40), (6.927, 40), (7, 40)))
        self.add_line('sym-e10', (7, 40), (24, 40))
        self.add_line('sym-e11', (24, 40), (41, 40))
        self.add_bezier('sym-e12', (41, 40), ((41.073, 40), (40.927, 40), (41, 40)))
        self.add_bezier('sym-e13', (41, 40), ((42.245, 40), (44, 38.39), (44, 37)))
        self.add_bezier('sym-e14', (44, 37), ((44, 36.9), (44, 37.11), (44, 37)))
        self.add_line('sym-e15', (44, 37), (44, 14))
        self.add_bezier('sym-e16', (44, 14), ((43.918, 13.86), (44, 14.13), (44, 14)))
        self.add_bezier('sym-e17', (44, 14), ((43.782, 13.64), (43.282, 13.3), (43, 13)))
        self.add_bezier('sym-e18', (43, 13), ((42.018, 11.95), (41.018, 11), (40, 10)))
        self.add_bezier('sym-e19', (40, 10), ((39.327, 9.34), (38.982, 8), (38, 8)))
        self.add_line('sym-e20', (38, 8), (24, 8))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20')
