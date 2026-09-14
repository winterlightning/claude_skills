"""Arrow thick left bottom corner (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '46acdcb2-6662-5746-9ae0-dffbec5c8d4e'
SOURCE_PATH = 'icons-json/arrows/arrow thick left bottom corner_46acdcb2-6662-5746-9ae0-dffbec5c8d4e.json'
AUTHOR = 'json_to_solo'

class ArrowThickLeftBottomCorner46acdcb2(Solo48):
    icon_id = 'arrow-thick-left-bottom-corner-46acdcb2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'left', 'bottom', 'corner', 'arrows')

    def build(self):
        self.add_line('e0', (32, 14), (17, 30))
        self.add_line('e1', (17, 30), (31, 30))
        self.add_line('e2', (17, 30), (17, 16))
        self.add_line('e3', (6, 39), (6, 8))
        self.add_line('e4', (8, 6), (40, 6))
        self.add_line('e5', (42, 8), (42, 40))
        self.add_line('e6', (41, 42), (8, 42))
        self.add_bezier('e7', (8, 42), ((7.918, 42), (7.473, 41.992), (7.391, 41.992)), ((6.728, 41.992), (6.016, 41.386), (6.016, 40.683)), ((6.016, 40.56), (6, 40.437), (6, 40.306)), ((6, 39.783), (6, 39.524), (6, 39)))
        self.add_bezier('e8', (6, 8), ((6, 7.869), (6.008, 8.201), (6.008, 8.07)), ((6.008, 7.17), (6.965, 6.016), (7.906, 6.016)), ((7.964, 6.008), (8.029, 6.008), (8.086, 6)), ((8.209, 6), (7.877, 6), (8, 6)))
        self.add_bezier('e9', (40, 6), ((40.123, 6), (39.799, 6), (39.922, 6)), ((40.855, 6), (41.992, 6.908), (41.992, 7.882)), ((41.992, 7.947), (42, 8.013), (42, 8.078)), ((42, 8.201), (42, 7.869), (42, 8)))
        self.add_bezier('e10', (42, 40), ((42, 40.082), (41.992, 40.527), (41.992, 40.609)), ((41.992, 41.37), (41.393, 41.55), (41, 42)))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e7', 'e3', 'e8', 'e4', 'e9', 'e5', 'e10', 'e6', closed=True)
