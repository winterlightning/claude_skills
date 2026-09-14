"""Arrow rectangle top (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4968e7eb-0c17-5914-a579-92bd1c46e9f0'
SOURCE_PATH = 'icons-json/arrows/arrow rectangle top_4968e7eb-0c17-5914-a579-92bd1c46e9f0.json'
AUTHOR = 'json_to_solo'

class ArrowRectangleTopArrows(Solo48):
    icon_id = 'arrow-rectangle-top-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'rectangle', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (32, 26), (24, 18))
        self.add_line('e1', (24, 18), (15, 26))
        self.add_line('e2', (6, 35), (6, 13))
        self.add_line('e3', (15, 6), (35, 6))
        self.add_line('e4', (42, 15), (42, 37))
        self.add_line('e5', (35, 42), (10, 42))
        self.add_bezier('e6', (6, 13), ((6, 12.869), (6.008, 12.292), (6.008, 12.161)), ((6.008, 8.913), (8.864, 6.016), (12.12, 6.016)), ((12.938, 6.016), (13.756, 6), (14.575, 6)), ((14.714, 6), (14.861, 6), (15, 6)))
        self.add_bezier('e7', (35, 6), ((35.147, 6), (35.741, 6.016), (35.888, 6.016)), ((38.883, 6.016), (41.247, 8.577), (41.885, 11.335)), ((42, 11.875), (41.984, 12.48), (41.984, 13.02)), ((41.984, 13.544), (42, 14.067), (42, 14.583)), ((42, 14.722), (42, 14.861), (42, 15)))
        self.add_bezier('e8', (42, 37), ((42, 37.131), (41.992, 37.345), (41.992, 37.475)), ((41.992, 39.619), (40.11, 41.378), (38.122, 41.853)), ((37.541, 41.992), (36.845, 41.992), (36.24, 41.992)), ((36.068, 41.992), (35.896, 42), (35.733, 42)), ((35.635, 42), (35.09, 42), (35, 42)))
        self.add_bezier('e9', (10, 42), ((9.869, 41.992), (9.829, 41.992), (9.698, 41.984)), ((7.923, 41.984), (6.016, 40.331), (6.016, 38.515)), ((6.016, 37.901), (6, 37.295), (6, 36.69)), ((6, 36.003), (6, 35.679), (6, 35)))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e6', 'e3', 'e7', 'e4', 'e8', 'e5', 'e9', closed=True)
