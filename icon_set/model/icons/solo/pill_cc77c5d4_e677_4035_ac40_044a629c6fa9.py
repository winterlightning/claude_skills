"""Pill (health), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc77c5d4-e677-4035-ac40-044a629c6fa9'
SOURCE_PATH = 'icons-json/health/pill_cc77c5d4-e677-4035-ac40-044a629c6fa9.json'
AUTHOR = 'json_to_solo'

class Pill(Solo48):
    icon_id = 'pill'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('pill', 'health')

    def build(self):
        self.add_line('e0', (32, 32), (16, 17))
        self.add_line('e1', (25, 40), (38, 26))
        self.add_line('e2', (23, 9), (8, 24))
        self.add_bezier('e3', (38, 26), ((40.185, 23.815), (41.984, 21.472), (41.984, 18.24)), ((41.984, 18.044), (42, 17.839), (42, 17.635)), ((42, 17.63), (42, 17.626), (42, 17.622)), ((42, 17.356), (41.984, 17.099), (41.984, 16.833)), ((41.984, 11.948), (38.253, 7.62), (33.605, 6.425)), ((32.918, 6.245), (32.125, 6), (31.413, 6)), ((31.412, 6), (31.411, 6), (31.41, 6)), ((31.345, 6), (31.272, 6), (31.2, 6)), ((31.061, 6), (30.922, 6.008), (30.783, 6.008)), ((28.009, 6.008), (24.955, 7.045), (23, 9)))
        self.add_bezier('e4', (8, 24), ((6.765, 25.235), (6.016, 28.688), (6.016, 30.431)), ((6.008, 30.562), (6.008, 30.693), (6, 30.815)), ((6, 30.819), (6, 30.822), (6, 30.825)), ((6, 31.018), (6.016, 31.203), (6.016, 31.388)), ((6.016, 32.345), (6.303, 33.36), (6.605, 34.26)), ((8.127, 38.752), (12.439, 42), (17.225, 42)), ((17.228, 42), (17.231, 42), (17.234, 42)), ((17.419, 42), (17.597, 41.992), (17.782, 41.992)), ((20.204, 41.992), (23.233, 41.767), (25, 40)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e3', 'e2', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
