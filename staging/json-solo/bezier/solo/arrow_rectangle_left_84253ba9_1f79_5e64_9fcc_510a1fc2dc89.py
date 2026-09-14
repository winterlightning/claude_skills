"""Arrow rectangle left (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '84253ba9-1f79-5e64-9fcc-510a1fc2dc89'
SOURCE_PATH = 'icons-json/arrows/arrow rectangle left_84253ba9-1f79-5e64-9fcc-510a1fc2dc89.json'
AUTHOR = 'json_to_solo'

class ArrowRectangleLeft(Solo48):
    icon_id = 'arrow-rectangle-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'rectangle', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (22, 8), (41, 8))
        self.add_line('e1', (44, 11), (44, 37))
        self.add_line('e2', (42, 40), (19, 40))
        self.add_line('e3', (12, 34), (5, 26))
        self.add_line('e4', (6, 22), (16, 10))
        self.add_line('e5', (30, 16), (23, 24))
        self.add_line('e6', (23, 24), (30, 32))
        self.add_bezier('e7', (14, 12), ((14.6, 11.33), (15.209, 10.66), (15.818, 10)), ((16.436, 9.33), (17.409, 8.02), (18.4, 8.02)), ((18.645, 8.02), (18.882, 8), (19.127, 8)), ((20.145, 8), (20.982, 8), (22, 8)))
        self.add_bezier('e8', (41, 8), ((41.2, 8), (41.673, 8.01), (41.873, 8.01)), ((43.009, 8.01), (44, 9.27), (44, 10.47)), ((44, 10.64), (44, 10.82), (44, 11)))
        self.add_bezier('e9', (44, 37), ((44, 37.1), (43.991, 37.19), (43.991, 37.29)), ((43.991, 38.31), (43.482, 39.2), (42.745, 39.77)), ((42.564, 39.9), (42.182, 39.88), (42, 40)))
        self.add_bezier('e10', (19, 40), ((18.864, 39.99), (19.182, 39.99), (19.045, 39.98)), ((17.464, 39.98), (12.918, 35.01), (12, 34)))
        self.add_bezier('e11', (5, 26), ((4.709, 25.68), (4.018, 25.19), (4.018, 24.68)), ((4.009, 24.62), (4.009, 24.57), (4, 24.52)), ((4, 24.519), (4, 24.518), (4, 24.517)), ((4, 24.458), (4.009, 24.409), (4.009, 24.36)), ((4.009, 23.39), (5.491, 22.61), (6, 22)))
        self.add_contour('c0', 'e7', 'e0', 'e8', 'e1', 'e9', 'e2', 'e10', 'e3', 'e11', 'e4')
        self.add_contour('c1', 'e5', 'e6')
