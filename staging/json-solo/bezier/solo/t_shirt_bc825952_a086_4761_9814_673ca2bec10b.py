"""T shirt (clothes), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc825952-a086-4761-9814-673ca2bec10b'
SOURCE_PATH = 'icons-json/clothes/t shirt_bc825952-a086-4761-9814-673ca2bec10b.json'
AUTHOR = 'json_to_solo'

class TShirt(Solo48):
    icon_id = 't-shirt'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('t', 'shirt', 'clothes')

    def build(self):
        self.add_line('e0', (11, 11), (4, 18))
        self.add_line('e1', (4, 18), (10, 24))
        self.add_line('e2', (10, 24), (14, 21))
        self.add_line('e3', (14, 21), (14, 40))
        self.add_line('e4', (14, 40), (35, 40))
        self.add_line('e5', (35, 40), (35, 21))
        self.add_line('e6', (35, 21), (38, 24))
        self.add_line('e7', (38, 24), (44, 18))
        self.add_line('e8', (44, 18), (37, 10))
        self.add_bezier('e9', (37, 10), ((35.927, 8.82), (33.836, 8), (32.318, 8)), ((32.317, 8), (32.315, 8), (32.314, 8)), ((32.225, 8), (32.144, 8), (32.064, 8)), ((31.827, 8), (31.6, 8.02), (31.373, 8.02)), ((31.245, 8.02), (30.573, 8), (30.491, 8.12)), ((30.336, 8.33), (30.273, 8.8), (30.182, 9.06)), ((29.909, 9.85), (29.582, 10.54), (29.109, 11.2)), ((27.855, 12.92), (25.982, 13.97), (23.973, 14)), ((21.718, 14.04), (19.409, 12.59), (18.3, 10.43)), ((17.945, 9.74), (17.873, 8.81), (17.618, 8.26)), ((17.573, 8.18), (16.164, 8.22), (15.973, 8.24)), ((14.055, 8.49), (12.4, 9.65), (11, 11)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', closed=True)
