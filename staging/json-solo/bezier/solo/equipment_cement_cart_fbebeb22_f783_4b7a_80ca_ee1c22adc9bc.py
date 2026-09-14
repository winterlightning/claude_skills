"""Equipment cement cart (tools), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fbebeb22-f783-4b7a-80ca-ee1c22adc9bc'
SOURCE_PATH = 'icons-json/tools/equipment cement cart_fbebeb22-f783-4b7a-80ca-ee1c22adc9bc.json'
AUTHOR = 'json_to_solo'

class EquipmentCementCartTools(Solo48):
    icon_id = 'equipment-cement-cart-tools'
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
        self.add_bezier('e10', (39, 19), ((39, 19.67), (39, 20.33), (39, 21)))
        self.add_bezier('e11', (39, 36), ((38.273, 37.23), (38.209, 37.04), (37, 37)))
        self.add_bezier('e12', (37, 19), ((36.264, 15.93), (34.645, 13.55), (31.373, 13.72)), ((30.945, 13.74), (30.527, 13.84), (30.118, 13.99)), ((29.727, 14.13), (29.336, 14.28), (28.945, 14.42)), ((28.845, 14.39), (28.8, 13.71), (28.736, 13.43)), ((28.591, 12.75), (28.327, 12.1), (27.982, 11.51)), ((26.891, 9.64), (24.827, 8.02), (22.727, 8.02)), ((22.6, 8.01), (22.464, 8.01), (22.336, 8)), ((22.334, 8), (22.331, 8), (22.328, 8)), ((22.149, 8), (21.961, 8.02), (21.782, 8.02)), ((19.573, 8.02), (17.409, 9.69), (16.3, 11.69)), ((16.064, 12.12), (15.891, 12.6), (15.755, 13.08)), ((15.655, 13.43), (15.555, 13.77), (15.455, 14.12)), ((15.427, 14.14), (14.909, 13.83), (14.673, 13.72)), ((14.1, 13.45), (13.418, 13.36), (12.791, 13.38)), ((9.545, 13.49), (8.455, 15.77), (8, 19)))
        self.add_bezier('e13', (24, 34), ((25.855, 33.24), (27.618, 31.52), (29, 30)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e10', 'e3', 'e11', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e12')
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
