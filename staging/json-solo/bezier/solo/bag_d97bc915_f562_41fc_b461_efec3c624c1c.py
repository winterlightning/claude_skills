"""Bag (shopping), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd97bc915-f562-41fc-b461-efec3c624c1c'
SOURCE_PATH = 'icons-json/shopping/bag_d97bc915-f562-41fc-b461-efec3c624c1c.json'
AUTHOR = 'json_to_solo'

class Bag(Solo48):
    icon_id = 'bag'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('bag', 'shopping')

    def build(self):
        self.add_line('e0', (17, 21), (17, 9))
        self.add_line('e1', (32, 11), (32, 21))
        self.add_line('e2', (40, 44), (36, 44))
        self.add_line('e3', (36, 44), (10, 44))
        self.add_line('e4', (8, 44), (11, 16))
        self.add_line('e5', (11, 16), (37, 16))
        self.add_line('e6', (37, 16), (40, 44))
        self.add_bezier('e7', (17, 9), ((18.187, 5.909), (20.227, 4.009), (23.646, 4.009)), ((23.779, 4.009), (23.903, 4), (24.028, 4)), ((24.03, 4), (24.032, 4), (24.034, 4)), ((24.168, 4), (24.303, 4.009), (24.429, 4.009)), ((27.983, 4.009), (32, 7.082), (32, 11)))
        self.add_bezier('e8', (10, 44), ((9.436, 44), (8.564, 44), (8, 44)))
        self.add_contour('c0', 'e0', 'e7', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e8', 'e4', 'e5', 'e6', closed=True)
