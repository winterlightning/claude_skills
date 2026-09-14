"""Shipment (shipping), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f81566bc-109e-4b31-b542-b141f1b9c51d'
SOURCE_PATH = 'icons-json/shipping/shipment_f81566bc-109e-4b31-b542-b141f1b9c51d.json'
AUTHOR = 'json_to_solo'

class ShipmentShipping(Solo48):
    icon_id = 'shipment-shipping'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    aliases = ()
    keywords = ('shipment', 'shipping')

    def build(self):
        self.add_line('e0', (30, 35), (29, 35))
        self.add_line('e1', (9, 35), (6, 35))
        self.add_line('e2', (4, 33), (4, 10))
        self.add_line('e3', (6, 8), (27, 8))
        self.add_line('e4', (29, 10), (29, 13))
        self.add_line('e5', (39, 35), (42, 35))
        self.add_line('e6', (44, 33), (44, 24))
        self.add_line('e7', (44, 23), (39, 14))
        self.add_line('e8', (37, 13), (29, 13))
        self.add_line('e9', (19, 35), (29, 35))
        self.add_line('e10', (29, 35), (29, 13))
        self.add_arc('e11-top', (30, 35), (40, 35), radius_x=5)
        self.add_arc('e11-bottom', (40, 35), (30, 35), radius_x=5)
        self.add_arc('e12-1', (9, 34), (14, 30), radius_x=5)
        self.add_arc('e12-2', (14, 30), (19, 35), radius_x=6)
        self.add_arc('e13-1', (9, 35), (14, 40), radius_x=5, sweep=False)
        self.add_arc('e13-2', (14, 40), (19, 35), radius_x=5, sweep=False)
        self.add_arc('e14', (6, 35), (4, 33), radius_x=3)
        self.add_arc('e15', (4, 10), (6, 8), radius_x=2)
        self.add_line('e16', (27, 8), (29, 10))
        self.add_arc('e17', (42, 35), (44, 33), radius_x=3, sweep=False)
        self.add_arc('e18', (44, 24), (44, 23), radius_x=29)
        self.add_line('e19', (39, 14), (37, 13))
        self.add_contour('c0', 'e12-1', 'e12-2')
        self.add_contour('c1', 'e13-1', 'e13-2')
        self.add_contour('c2', 'e0')
        self.add_contour('c3', 'e1', 'e14', 'e2', 'e15', 'e3', 'e16', 'e4')
        self.add_contour('c4', 'e5', 'e17', 'e6', 'e18', 'e7', 'e19', 'e8')
        self.add_contour('c5', 'e9')
        self.add_contour('c6', 'e10')
        self.add_contour('e11', 'e11-top', 'e11-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c2', 'e11')
        self.relate('connect', 'c4', 'e11')
