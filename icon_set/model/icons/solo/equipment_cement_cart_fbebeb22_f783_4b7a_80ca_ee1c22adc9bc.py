"""Equipment cement cart (tools), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fbebeb22-f783-4b7a-80ca-ee1c22adc9bc'
SOURCE_PATH = 'icons-json/tools/equipment cement cart_fbebeb22-f783-4b7a-80ca-ee1c22adc9bc.json'
AUTHOR = 'json_to_solo'

class EquipmentCementCart(Solo48):
    icon_id = 'equipment-cement-cart'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tools'
    aliases = ()
    keywords = ('equipment', 'cement', 'cart', 'tools')

    def build(self):
        self.add_line('e0', (44, 13), (39, 19))
        self.add_line('e1', (10, 29), (4, 19))
        self.add_line('e2', (4, 19), (8, 19))
        self.add_line('e3', (39, 21), (39, 36))
        self.add_line('e4', (37, 37), (29, 30))
        self.add_line('e5', (39, 19), (29, 30))
        self.add_line('e6', (39, 19), (37, 19))
        self.add_line('e7', (37, 19), (8, 19))
        self.add_line('e8', (19, 34), (24, 34))
        self.add_arc('e9-top', (9, 34), (19, 34), radius_x=5, radius_y=6)
        self.add_arc('e9-bottom', (19, 34), (9, 34), radius_x=5, radius_y=6)
        self.add_arc('e10', (39, 19), (39, 21), radius_x=24, sweep=False)
        self.add_line('e11', (39, 36), (37, 37))
        self.add_line('e12-1', (37, 19), (35, 15))
        self.add_arc('e12-2', (35, 15), (29, 14), radius_x=6, sweep=False)
        self.add_arc('e12-3', (29, 14), (27, 10), radius_x=7, sweep=False)
        self.add_line('e12-4', (27, 10), (22, 8))
        self.add_arc('e12-5', (22, 8), (15, 14), radius_x=8, sweep=False)
        self.add_arc('e12-6', (15, 14), (8, 17), radius_x=5, sweep=False)
        self.add_line('e12-7', (8, 17), (8, 19))
        self.add_line('e13', (24, 34), (29, 30))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e10', 'e3', 'e11', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e12-1', 'e12-2', 'e12-3', 'e12-4', 'e12-5', 'e12-6', 'e12-7')
        self.add_contour('c6', 'e7')
        self.add_contour('c7', 'e8', 'e13')
        self.add_contour('e9', 'e9-top', 'e9-bottom', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c3', 'c7')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c1', 'e9')
        self.relate('connect', 'c7', 'e9')
