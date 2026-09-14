"""Book open (content), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '03b427a0-f791-44b1-9798-ea43bb973886'
SOURCE_PATH = 'icons-json/content/book open_03b427a0-f791-44b1-9798-ea43bb973886.json'
AUTHOR = 'json_to_solo'

class BookOpen03b427a0(Solo48):
    icon_id = 'book-open-03b427a0'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('book', 'open', 'content')

    def build(self):
        self.add_line('e0', (44, 11), (44, 37))
        self.add_line('e1', (24, 12), (24, 40))
        self.add_line('e2', (4, 11), (4, 37))
        self.add_bezier('e3', (24, 12), ((27.518, 9.92), (30.945, 8.02), (35.027, 8.02)), ((35.127, 8.02), (35.227, 8.02), (35.327, 8.02)), ((35.8, 8.02), (36.273, 8.01), (36.755, 8.01)), ((37.112, 8.01), (37.479, 8), (37.837, 8)), ((37.843, 8), (37.849, 8), (37.855, 8)), ((38.055, 8), (38.255, 8.01), (38.445, 8.01)), ((39.873, 8.01), (41.9, 8.48), (43.055, 9.43)), ((43.164, 9.52), (44, 10.3), (44, 10.46)), ((44, 10.64), (44, 10.82), (44, 11)))
        self.add_bezier('e4', (44, 37), ((42.9, 36.68), (41.764, 36.29), (40.636, 36.06)), ((36.273, 35.2), (31.618, 35.89), (27.591, 37.91)), ((26.373, 38.53), (25.164, 39.31), (24, 40)))
        self.add_bezier('e5', (24, 12), ((20.509, 9.92), (16.945, 8.02), (12.882, 8.02)), ((12.309, 8.02), (11.736, 8), (11.164, 8)), ((11.055, 8), (10.955, 8.01), (10.855, 8.01)), ((9.455, 8.01), (4, 8.49), (4, 10.68)), ((4, 10.79), (4, 10.89), (4, 11)))
        self.add_bezier('e6', (4, 37), ((5.155, 36.68), (6.345, 36.26), (7.536, 36.05)), ((11.9, 35.29), (16.236, 36.02), (20.3, 37.91)), ((21.545, 38.48), (22.8, 39.33), (24, 40)))
        self.add_contour('c0', 'e3', 'e0', 'e4')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e5', 'e2', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
