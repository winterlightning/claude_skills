"""Right (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc3f3f31-93a3-4488-88c0-c6897ab403de'
SOURCE_PATH = 'icons-json/arrows/right_cc3f3f31-93a3-4488-88c0-c6897ab403de.json'
AUTHOR = 'json_to_solo'

class RightArrows(Solo48):
    icon_id = 'right-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('right', 'arrows')

    def build(self):
        self.add_line('e0', (26, 17), (26, 11))
        self.add_line('e1', (30, 8), (43, 22))
        self.add_line('e2', (44, 26), (30, 39))
        self.add_line('e3', (26, 37), (26, 30))
        self.add_line('e4', (26, 30), (7, 30))
        self.add_line('e5', (4, 27), (4, 20))
        self.add_line('e6', (7, 18), (26, 18))
        self.add_bezier('e7', (26, 11), ((26, 10.01), (27.3, 8), (28.218, 8)), ((28.509, 8), (28.791, 8.01), (29.082, 8.01)), ((29.255, 8.01), (29.427, 8.01), (29.6, 8.01)), ((29.645, 8.01), (29.682, 8), (29.727, 8)), ((29.936, 8), (29.791, 8), (30, 8)))
        self.add_bezier('e8', (43, 22), ((43.355, 22.39), (44, 22.93), (44, 23.53)), ((44, 23.85), (44, 24.17), (44, 24.49)), ((44, 24.73), (44, 24.98), (44, 25.23)), ((44, 25.48), (44, 25.74), (44, 26)))
        self.add_bezier('e9', (30, 39), ((29.591, 39.25), (29.173, 39.99), (28.7, 39.99)), ((28.655, 39.99), (28.619, 40), (28.575, 40)), ((28.574, 40), (28.573, 40), (28.573, 40)), ((28.545, 40), (28.509, 39.99), (28.482, 39.99)), ((27.273, 39.99), (26.4, 38.03), (26, 37)))
        self.add_bezier('e10', (7, 30), ((5.964, 30), (4, 28.29), (4, 27.13)), ((4, 27.09), (4, 27.04), (4, 27)))
        self.add_bezier('e11', (4, 20), ((4.109, 19.79), (4.091, 19.55), (4.218, 19.35)), ((4.618, 18.72), (6.318, 18), (7, 18)))
        self.add_bezier('e12', (26, 18), ((25.964, 17.67), (25.755, 17.34), (25.718, 17.02)), ((25.755, 17.01), (25.964, 17), (26, 17)))
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e8', 'e2', 'e9', 'e3', 'e4', 'e10', 'e5', 'e11', 'e6', 'e12', closed=True)
