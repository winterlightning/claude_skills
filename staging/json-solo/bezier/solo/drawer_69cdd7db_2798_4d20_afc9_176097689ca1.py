"""Drawer (office), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '69cdd7db-2798-4d20-afc9-176097689ca1'
SOURCE_PATH = 'icons-json/office/drawer_69cdd7db-2798-4d20-afc9-176097689ca1.json'
AUTHOR = 'json_to_solo'

class Drawer69cdd7db(Solo48):
    icon_id = 'drawer-69cdd7db'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('drawer', 'office')

    def build(self):
        self.add_line('e0', (8, 29), (14, 29))
        self.add_line('e1', (21, 34), (37, 34))
        self.add_line('e2', (42, 37), (42, 40))
        self.add_line('e3', (40, 42), (8, 42))
        self.add_line('e4', (6, 40), (6, 31))
        self.add_line('e5', (8, 29), (8, 8))
        self.add_line('e6', (10, 6), (17, 6))
        self.add_line('e7', (20, 7), (23, 9))
        self.add_line('e8', (26, 11), (38, 11))
        self.add_line('e9', (39, 13), (39, 34))
        self.add_bezier('e10', (14, 29), ((16.34, 30.268), (18.439, 34), (21, 34)))
        self.add_bezier('e11', (37, 34), ((37.548, 34), (38.179, 33.818), (38.727, 33.818)), ((39.055, 33.818), (41.345, 33.728), (41.525, 33.884)), ((41.836, 34.129), (41.984, 35.504), (41.984, 35.847)), ((41.984, 36.142), (42, 36.436), (42, 36.731)), ((42, 36.854), (42, 36.877), (42, 37)))
        self.add_bezier('e12', (42, 40), ((41.992, 40.131), (41.992, 39.807), (41.984, 39.93)), ((41.984, 40.879), (41.059, 41.992), (40.085, 41.992)), ((40.02, 41.992), (39.963, 42), (39.905, 42)), ((39.783, 42), (40.123, 42), (40, 42)))
        self.add_bezier('e13', (8, 42), ((7.918, 42), (8.299, 42), (8.217, 41.992)), ((6.982, 41.992), (6.532, 40.941), (6, 40)))
        self.add_bezier('e14', (6, 31), ((6.09, 30.836), (6.074, 30.194), (6.18, 30.03)), ((6.745, 29.13), (6.977, 29.09), (8, 29)))
        self.add_bezier('e15', (8, 8), ((8, 7.763), (8.348, 7.98), (8.348, 7.735)), ((8.356, 6.99), (8.847, 6.016), (9.715, 6.016)), ((9.772, 6.008), (9.837, 6.008), (9.895, 6)), ((9.96, 6), (9.935, 6), (10, 6)))
        self.add_bezier('e16', (17, 6), ((17.998, 6), (19.231, 6.427), (20, 7)))
        self.add_bezier('e17', (23, 9), ((23.818, 9.614), (24.83, 11), (26, 11)))
        self.add_bezier('e18', (38, 11), ((38.695, 11.687), (38.91, 12.018), (39, 13)))
        self.add_contour('c0', 'e0', 'e10', 'e1', 'e11', 'e2', 'e12', 'e3', 'e13', 'e4', 'e14')
        self.add_contour('c1', 'e5', 'e15', 'e6', 'e16', 'e7', 'e17', 'e8', 'e18', 'e9')
        self.relate('connect', 'c1', 'c0')
