"""Arrow rectangle bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4e217a5a-400f-51f6-982e-5a7f9c09448f'
SOURCE_PATH = 'icons-json/arrows/arrow rectangle bottom_4e217a5a-400f-51f6-982e-5a7f9c09448f.json'
AUTHOR = 'json_to_solo'

class ArrowRectangleBottomArrows(Solo48):
    icon_id = 'arrow-rectangle-bottom-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'rectangle', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (16, 22), (24, 30))
        self.add_line('e1', (24, 30), (33, 22))
        self.add_line('e2', (42, 13), (42, 35))
        self.add_line('e3', (33, 42), (13, 42))
        self.add_line('e4', (6, 33), (6, 11))
        self.add_line('e5', (13, 6), (38, 6))
        self.add_bezier('e6', (42, 35), ((42, 35.131), (41.992, 35.708), (41.992, 35.839)), ((41.992, 39.087), (39.136, 41.984), (35.88, 41.984)), ((35.062, 41.984), (34.244, 42), (33.425, 42)), ((33.286, 42), (33.139, 42), (33, 42)))
        self.add_bezier('e7', (13, 42), ((12.853, 42), (12.259, 41.984), (12.112, 41.984)), ((9.117, 41.984), (6.753, 39.423), (6.115, 36.665)), ((6, 36.125), (6.016, 35.52), (6.016, 34.98)), ((6.016, 34.456), (6, 33.933), (6, 33.417)), ((6, 33.278), (6, 33.139), (6, 33)))
        self.add_bezier('e8', (6, 11), ((6, 10.869), (6.008, 10.655), (6.008, 10.525)), ((6.008, 8.381), (7.89, 6.622), (9.878, 6.147)), ((10.459, 6.008), (11.155, 6.008), (11.76, 6.008)), ((11.932, 6.008), (12.104, 6), (12.267, 6)), ((12.365, 6), (12.91, 6), (13, 6)))
        self.add_bezier('e9', (38, 6), ((38.131, 6.008), (38.171, 6.008), (38.302, 6.016)), ((40.077, 6.016), (41.984, 7.669), (41.984, 9.485)), ((41.984, 10.099), (42, 10.705), (42, 11.31)), ((42, 11.997), (42, 12.321), (42, 13)))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e6', 'e3', 'e7', 'e4', 'e8', 'e5', 'e9', closed=True)
