"""Phone box (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd7e72503-159f-4e5f-b0ad-c81408e24d67'
SOURCE_PATH = 'icons-json/symbol/phone box_d7e72503-159f-4e5f-b0ad-c81408e24d67.json'
AUTHOR = 'json_to_solo'

class PhoneBoxD7e72503(Solo48):
    icon_id = 'phone-box-d7e72503'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('phone', 'box', 'symbol')

    def build(self):
        self.add_line('e0', (36, 15), (36, 44))
        self.add_line('e1', (36, 29), (12, 29))
        self.add_line('e2', (40, 44), (8, 44))
        self.add_line('e3', (12, 44), (12, 13))
        self.add_line('e4', (40, 13), (8, 13))
        self.add_bezier('e5', (12, 13), ((11.95, 12.882), (11.9, 12.845), (11.85, 12.727)), ((11.84, 12.255), (12.47, 11.055), (12.68, 10.536)), ((14.26, 6.591), (18.91, 4.018), (23.49, 4.018)), ((23.75, 4.018), (24, 4), (24.26, 4)), ((24.264, 4), (24.268, 4), (24.272, 4)), ((24.528, 4), (24.784, 4.009), (25.04, 4.009)), ((26.53, 4.009), (28.32, 4.555), (29.64, 5.136)), ((32.44, 6.382), (34.67, 8.355), (35.6, 11.118)), ((35.87, 11.936), (35.78, 12.918), (35.84, 13.764)), ((35.87, 14.127), (36, 14.645), (36, 15)))
        self.add_contour('c0', 'e5', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c5', 'e4')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c3', 'c2')
