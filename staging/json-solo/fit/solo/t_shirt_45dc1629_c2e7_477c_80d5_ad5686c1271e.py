"""T shirt (clothes), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '45dc1629-c2e7-477c-80d5-ad5686c1271e'
SOURCE_PATH = 'icons-json/clothes/t shirt_45dc1629-c2e7-477c-80d5-ad5686c1271e.json'
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
        self.add_line('e0', (36, 26), (44, 26))
        self.add_line('e1', (44, 26), (44, 16))
        self.add_line('e2', (4, 18), (4, 26))
        self.add_line('e3', (4, 26), (12, 26))
        self.add_line('e4', (36, 21), (36, 40))
        self.add_line('e5', (36, 40), (12, 40))
        self.add_line('e6', (12, 40), (12, 21))
        self.add_arc('e7-1', (44, 16), (40, 10), radius_x=10, sweep=False)
        self.add_line('e7-2', (40, 10), (33, 8))
        self.add_line('e7-3', (33, 8), (32, 8))
        self.add_arc('e7-4', (32, 8), (27, 14), radius_x=8)
        self.add_arc('e7-5', (27, 14), (21, 14), radius_x=8)
        self.add_arc('e7-6', (21, 14), (16, 8), radius_x=8)
        self.add_line('e7-7', (16, 8), (10, 9))
        self.add_line('e7-8', (10, 9), (7, 11))
        self.add_arc('e7-9', (7, 11), (4, 18), radius_x=10, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e7-5', 'e7-6', 'e7-7', 'e7-8', 'e7-9', 'e2', 'e3')
        self.add_contour('c1', 'e4', 'e5', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
