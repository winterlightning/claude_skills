"""Receipt register print (shopping), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd8074d08-1118-52c3-bdda-a63272612c12'
SOURCE_PATH = 'icons-json/shopping/receipt register print_d8074d08-1118-52c3-bdda-a63272612c12.json'
AUTHOR = 'json_to_solo'

class ReceiptRegisterPrintShopping(Solo48):
    icon_id = 'receipt-register-print-shopping'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('receipt', 'register', 'print', 'shopping')

    def build(self):
        self.add_line('e0', (36, 27), (12, 27))
        self.add_line('e1', (14, 27), (14, 40))
        self.add_line('e2', (14, 40), (17, 42))
        self.add_line('e3', (17, 42), (21, 40))
        self.add_line('e4', (21, 40), (26, 42))
        self.add_line('e5', (26, 42), (29, 40))
        self.add_line('e6', (29, 40), (34, 42))
        self.add_line('e7', (34, 42), (34, 27))
        self.add_line('e8', (14, 33), (9, 33))
        self.add_line('e9', (6, 29), (6, 21))
        self.add_line('e10', (8, 17), (39, 17))
        self.add_line('e11', (42, 21), (42, 31))
        self.add_line('e12', (39, 33), (34, 33))
        self.add_line('e13', (37, 17), (37, 9))
        self.add_line('e14', (35, 6), (14, 6))
        self.add_line('e15', (11, 10), (11, 17))
        self.add_line('e16-1', (9, 33), (7, 32))
        self.add_arc('e16-2', (7, 32), (6, 29), radius_x=5)
        self.add_line('e17', (6, 21), (8, 17))
        self.add_arc('e18-1', (39, 17), (42, 20), radius_x=3)
        self.add_line('e18-2', (42, 20), (42, 21))
        self.add_arc('e19', (42, 31), (39, 33), radius_x=3)
        self.add_arc('e20', (37, 9), (35, 6), radius_x=3, sweep=False)
        self.add_arc('e21', (14, 6), (11, 10), radius_x=4, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7')
        self.add_contour('c2', 'e8', 'e16-1', 'e16-2', 'e9', 'e17', 'e10', 'e18-1', 'e18-2', 'e11', 'e19', 'e12')
        self.add_contour('c3', 'e13', 'e20', 'e14', 'e21', 'e15')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c3', 'c2')
        self.relate('connect', 'c3', 'c2')
