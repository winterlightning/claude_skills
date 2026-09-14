"""Batch-06/cap (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f6ee542-cdce-408a-b798-b60860e5b325'
SOURCE_PATH = 'icons-json/accessories/batch-06/cap_5f6ee542-cdce-408a-b798-b60860e5b325.json'
AUTHOR = 'json_to_solo'

class Batch06Cap(Solo48):
    icon_id = 'batch-06-cap'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'cap', 'accessories')

    def build(self):
        self.add_line('e0', (38, 20), (38, 33))
        self.add_line('e1', (38, 33), (27, 39))
        self.add_line('e2', (20, 39), (9, 33))
        self.add_line('e3', (9, 33), (9, 20))
        self.add_line('e4', (44, 17), (25, 26))
        self.add_line('e5', (20, 25), (4, 17))
        self.add_line('e6', (4, 17), (19, 10))
        self.add_line('e7', (25, 8), (44, 17))
        self.add_bezier('e8', (27, 39), ((26.073, 39.51), (24.509, 39.99), (23.464, 39.99)), ((23.391, 39.99), (23.318, 40), (23.236, 40)), ((23.235, 40), (23.234, 40), (23.233, 40)), ((23.161, 40), (23.09, 40), (23.018, 39.99)), ((22.018, 39.99), (20.864, 39.44), (20, 39)))
        self.add_bezier('e9', (25, 26), ((23.609, 26.66), (21.227, 25.6), (20, 25)))
        self.add_bezier('e10', (19, 10), ((19.864, 9.61), (22.518, 8.02), (23.373, 8.02)), ((23.473, 8.02), (23.573, 8), (23.682, 8)), ((23.7, 8), (23.727, 8), (23.745, 8)), ((23.909, 8), (24.082, 8.01), (24.245, 8.01)), ((24.318, 8.01), (24.391, 8), (24.464, 8)), ((24.609, 8), (24.855, 8), (25, 8)))
        self.add_contour('c0', 'e0', 'e1', 'e8', 'e2', 'e3')
        self.add_contour('c1', 'e4', 'e9', 'e5', 'e6', 'e10', 'e7', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
