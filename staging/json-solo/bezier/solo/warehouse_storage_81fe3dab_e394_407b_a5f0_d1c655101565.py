"""Warehouse storage (shipping), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81fe3dab-e394-407b-a5f0-d1c655101565'
SOURCE_PATH = 'icons-json/shipping/warehouse storage_81fe3dab-e394-407b-a5f0-d1c655101565.json'
AUTHOR = 'json_to_solo'

class WarehouseStorageShipping(Solo48):
    icon_id = 'warehouse-storage-shipping'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    aliases = ()
    keywords = ('warehouse', 'storage', 'shipping')

    def build(self):
        self.add_line('e0', (24, 40), (24, 23))
        self.add_line('e1', (33, 28), (33, 23))
        self.add_line('e2', (15, 28), (15, 23))
        self.add_line('e3', (24, 8), (24, 13))
        self.add_line('e4', (35, 23), (35, 8))
        self.add_line('e5', (31, 8), (18, 8))
        self.add_line('e6', (18, 8), (13, 8))
        self.add_line('e7', (13, 8), (13, 23))
        self.add_line('e8', (44, 23), (4, 23))
        self.add_line('e9', (4, 23), (4, 40))
        self.add_line('e10', (4, 40), (44, 40))
        self.add_line('e11', (44, 40), (44, 23))
        self.add_bezier('e12', (35, 8), ((34.7, 8), (34.309, 8.008), (34.018, 8.008)), ((33.745, 8.008), (33.455, 8.008), (33.182, 8.008)), ((33.109, 8.008), (33.027, 8), (32.955, 8)), ((32.391, 8), (31.564, 8), (31, 8)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e12', 'e5', 'e6', 'e7')
        self.add_contour('c5', 'e8', 'e9', 'e10', 'e11', closed=True)
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c5')
