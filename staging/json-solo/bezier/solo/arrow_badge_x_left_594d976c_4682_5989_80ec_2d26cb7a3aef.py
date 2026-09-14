"""Arrow badge x left (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '594d976c-4682-5989-80ec-2d26cb7a3aef'
SOURCE_PATH = 'icons-json/arrows/arrow badge x left_594d976c-4682-5989-80ec-2d26cb7a3aef.json'
AUTHOR = 'json_to_solo'

class ArrowBadgeXLeftArrows(Solo48):
    icon_id = 'arrow-badge-x-left-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'badge', 'x', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (23, 32), (37, 16))
        self.add_line('e1', (23, 17), (37, 32))
        self.add_line('e2', (6, 27), (17, 39))
        self.add_line('e3', (20, 40), (41, 40))
        self.add_line('e4', (44, 37), (44, 10))
        self.add_line('e5', (40, 8), (19, 8))
        self.add_line('e6', (19, 8), (5, 22))
        self.add_bezier('e7', (17, 39), ((17.745, 39.82), (18.909, 40), (19.891, 40)), ((20.055, 40), (19.845, 40), (20, 40)))
        self.add_bezier('e8', (41, 40), ((41.145, 40), (41.564, 39.99), (41.718, 39.99)), ((42.782, 39.99), (43.991, 38.9), (43.991, 37.69)), ((43.991, 37.62), (44, 37.54), (44, 37.46)), ((44, 37.31), (44, 37.15), (44, 37)))
        self.add_bezier('e9', (44, 10), ((44, 9.91), (44, 9.82), (43.991, 9.73)), ((43.991, 8.89), (43.291, 8), (42.5, 8)), ((41.791, 8), (40.709, 8), (40, 8)))
        self.add_bezier('e10', (5, 22), ((4.609, 22.4), (4.009, 23.25), (4.009, 23.87)), ((4, 23.939), (4, 24.008), (4, 24.067)), ((4, 24.068), (4, 24.069), (4, 24.07)), ((4.009, 24.14), (4.009, 24.21), (4.018, 24.27)), ((4.018, 25.26), (5.418, 26.36), (6, 27)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e7', 'e3', 'e8', 'e4', 'e9', 'e5', 'e6', 'e10', closed=True)
