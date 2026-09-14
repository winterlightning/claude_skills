"""Receipt register print (shopping), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e16', (9, 33), ((7.11, 33), (6.016, 31.233), (6.016, 29.449)), ((6.016, 29.269), (6, 29.18), (6, 29)))
        self.add_bezier('e17', (6, 21), ((6, 20.918), (6.008, 20.564), (6.008, 20.482)), ((6.008, 18.764), (6.486, 17.466), (8, 17)))
        self.add_bezier('e18', (39, 17), ((40.391, 17), (41.984, 18.33), (41.984, 19.999)), ((41.992, 20.122), (41.992, 20.236), (42, 20.359)), ((42, 20.482), (42, 20.877), (42, 21)))
        self.add_bezier('e19', (42, 31), ((42, 31.123), (41.992, 30.783), (41.992, 30.905)), ((41.992, 32.763), (40.366, 33), (39, 33)))
        self.add_bezier('e20', (37, 9), ((37, 7.175), (36.53, 6.704), (35, 6)))
        self.add_bezier('e21', (14, 6), ((13.918, 6), (14.01, 6), (13.928, 6)), ((11.785, 6), (11, 8.233), (11, 10)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7')
        self.add_contour('c2', 'e8', 'e16', 'e9', 'e17', 'e10', 'e18', 'e11', 'e19', 'e12')
        self.add_contour('c3', 'e13', 'e20', 'e14', 'e21', 'e15')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c3', 'c2')
        self.relate('connect', 'c3', 'c2')
