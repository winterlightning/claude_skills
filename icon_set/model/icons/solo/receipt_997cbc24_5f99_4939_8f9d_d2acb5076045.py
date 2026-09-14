"""Receipt (shopping), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '997cbc24-5f99-4939-8f9d-d2acb5076045'
SOURCE_PATH = 'icons-json/shopping/receipt_997cbc24-5f99-4939-8f9d-d2acb5076045.json'
AUTHOR = 'json_to_solo'

class Receipt(Solo48):
    icon_id = 'receipt'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('receipt', 'shopping')

    def build(self):
        self.add_line('e0', (37, 44), (35, 42))
        self.add_line('e1', (35, 42), (32, 44))
        self.add_line('e2', (32, 44), (29, 42))
        self.add_line('e3', (29, 42), (27, 44))
        self.add_line('e4', (27, 44), (23, 42))
        self.add_line('e5', (23, 42), (20, 44))
        self.add_line('e6', (20, 44), (16, 42))
        self.add_line('e7', (16, 42), (12, 44))
        self.add_line('e8', (12, 44), (10, 43))
        self.add_line('e9', (8, 40), (8, 7))
        self.add_line('e10', (8, 7), (8, 5))
        self.add_line('e11', (8, 5), (15, 8))
        self.add_line('e12', (15, 8), (19, 4))
        self.add_line('e13', (19, 4), (22, 7))
        self.add_line('e14', (22, 7), (26, 4))
        self.add_line('e15', (26, 4), (29, 7))
        self.add_line('e16', (29, 7), (32, 4))
        self.add_line('e17', (32, 4), (36, 7))
        self.add_line('e18', (36, 7), (38, 4))
        self.add_line('e19', (40, 7), (40, 40))
        self.add_arc('e20', (10, 43), (8, 40), radius_x=4)
        self.add_arc('e21', (38, 4), (40, 7), radius_x=4)
        self.add_line('e22-1', (40, 40), (40, 42))
        self.add_arc('e22-2', (40, 42), (38, 44), radius_x=3)
        self.add_line('e22-3', (38, 44), (37, 44))
        self.add_line('e23', (37, 44), (38, 44))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e20', 'e9', 'e10', 'e11', 'e12', 'e13', 'e14', 'e15', 'e16', 'e17', 'e18', 'e21', 'e19', 'e22-1', 'e22-2', 'e22-3')
        self.add_contour('c1', 'e23')
        self.relate('connect', 'c1', 'c0')
