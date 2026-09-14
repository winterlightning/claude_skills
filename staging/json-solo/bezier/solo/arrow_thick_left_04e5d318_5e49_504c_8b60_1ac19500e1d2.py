"""Arrow thick left (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '04e5d318-5e49-504c-8b60-1ac19500e1d2'
SOURCE_PATH = 'icons-json/arrows/arrow thick left_04e5d318-5e49-504c-8b60-1ac19500e1d2.json'
AUTHOR = 'json_to_solo'

class ArrowThickLeft04e5d318(Solo48):
    icon_id = 'arrow-thick-left-04e5d318'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (24, 15), (16, 24))
        self.add_line('e1', (16, 24), (34, 24))
        self.add_line('e2', (16, 24), (24, 32))
        self.add_line('e3', (40, 42), (8, 42))
        self.add_line('e4', (6, 40), (6, 8))
        self.add_line('e5', (8, 6), (40, 6))
        self.add_line('e6', (42, 9), (42, 40))
        self.add_bezier('e7', (8, 42), ((7.861, 42), (8.168, 41.992), (8.029, 41.992)), ((6.933, 41.992), (6.466, 40.826), (6, 40)))
        self.add_bezier('e8', (6, 8), ((6, 7.869), (6.008, 8.193), (6.008, 8.062)), ((6.008, 7.162), (6.957, 6.016), (7.898, 6.016)), ((7.964, 6.008), (8.021, 6.008), (8.086, 6)), ((8.209, 6), (7.877, 6), (8, 6)))
        self.add_bezier('e9', (40, 6), ((40.123, 6), (39.791, 6), (39.914, 6)), ((40.887, 6), (42, 7.105), (42, 8.078)), ((42, 8.479), (42, 8.599), (42, 9)))
        self.add_bezier('e10', (42, 40), ((42, 40.147), (41.984, 39.832), (41.984, 39.971)), ((41.984, 41.337), (41.105, 41.575), (40, 42)))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e7', 'e4', 'e8', 'e5', 'e9', 'e6', 'e10', closed=True)
