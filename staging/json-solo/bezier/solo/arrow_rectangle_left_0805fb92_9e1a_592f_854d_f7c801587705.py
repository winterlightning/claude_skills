"""Arrow rectangle left (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0805fb92-9e1a-592f-854d-f7c801587705'
SOURCE_PATH = 'icons-json/arrows/arrow rectangle left_0805fb92-9e1a-592f-854d-f7c801587705.json'
AUTHOR = 'json_to_solo'

class ArrowRectangleLeft0805fb92(Solo48):
    icon_id = 'arrow-rectangle-left-0805fb92'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'rectangle', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (25, 16), (18, 24))
        self.add_line('e1', (18, 24), (26, 32))
        self.add_line('e2', (42, 8), (7, 8))
        self.add_line('e3', (4, 12), (4, 37))
        self.add_line('e4', (8, 40), (41, 40))
        self.add_line('e5', (44, 37), (44, 9))
        self.add_bezier('e6', (7, 8), ((6.855, 8), (6.436, 8), (6.3, 8)), ((5.236, 8), (4.009, 9.51), (4.009, 10.68)), ((4.009, 10.75), (4, 10.82), (4, 10.89)), ((4, 11.26), (4, 11.63), (4, 12)))
        self.add_bezier('e7', (4, 37), ((4, 37.15), (4.009, 37.3), (4.009, 37.45)), ((4.009, 38.64), (5.336, 40), (6.409, 40)), ((6.818, 40), (7.591, 40), (8, 40)))
        self.add_bezier('e8', (41, 40), ((41.145, 40), (41.555, 40), (41.7, 40)), ((42.3, 40), (43.991, 39.38), (43.991, 38.51)), ((43.991, 38.44), (44, 38.38), (44, 38.31)), ((44, 38.24), (44, 38.17), (44, 38.1)), ((44, 37.88), (44, 37.66), (44, 37.45)), ((44, 37.3), (44, 37.15), (44, 37)))
        self.add_bezier('e9', (44, 9), ((43.436, 8.53), (42.745, 8), (42, 8)))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e6', 'e3', 'e7', 'e4', 'e8', 'e5', 'e9', closed=True)
