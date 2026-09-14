"""Circuit lock (products), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aad274a9-6341-4a33-9772-7b8d5f95c1bd'
SOURCE_PATH = 'icons-json/products/circuit lock_aad274a9-6341-4a33-9772-7b8d5f95c1bd.json'
AUTHOR = 'json_to_solo'

class CircuitLock(Solo48):
    icon_id = 'circuit-lock'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'products'
    aliases = ()
    keywords = ('circuit', 'lock', 'products')

    def build(self):
        self.add_line('e0', (39, 8), (44, 8))
        self.add_line('e1', (29, 18), (32, 15))
        self.add_line('e2', (32, 15), (35, 16))
        self.add_line('e3', (35, 16), (44, 8))
        self.add_line('e4', (44, 13), (44, 8))
        self.add_line('e5', (7, 20), (20, 20))
        self.add_line('e6', (4, 21), (4, 31))
        self.add_line('e7', (8, 33), (20, 33))
        self.add_line('e8', (23, 31), (23, 21))
        self.add_line('e9', (29, 30), (32, 34))
        self.add_line('e10', (32, 34), (35, 32))
        self.add_line('e11', (35, 32), (44, 40))
        self.add_line('e12', (44, 40), (39, 40))
        self.add_line('e13', (44, 35), (44, 40))
        self.add_line('e14', (14, 23), (14, 30))
        self.add_arc('e15', (7, 20), (4, 21), radius_x=2, sweep=False)
        self.add_arc('e16', (4, 31), (8, 33), radius_x=3, sweep=False)
        self.add_arc('e17', (20, 33), (23, 31), radius_x=2, sweep=False)
        self.add_arc('e18', (23, 21), (20, 20), radius_x=2, sweep=False)
        self.add_arc('e19-1', (7, 20), (15, 9), radius_x=8)
        self.add_arc('e19-2', (15, 9), (20, 20), radius_x=8)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e15', 'e6', 'e16', 'e7', 'e17', 'e8', 'e18')
        self.add_contour('c5', 'e19-1', 'e19-2')
        self.add_contour('c6', 'e9', 'e10', 'e11', 'e12')
        self.add_contour('c7', 'e13')
        self.add_contour('c8', 'e14')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
