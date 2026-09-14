"""Photo (state), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'abfa4d34-f0c4-4ef1-8fdf-cc3a1edb6828'
SOURCE_PATH = 'icons-json/state/photo_abfa4d34-f0c4-4ef1-8fdf-cc3a1edb6828.json'
AUTHOR = 'json_to_solo'

class PhotoState(Solo48):
    icon_id = 'photo-state'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('photo', 'state')

    def build(self):
        self.add_line('e0', (9, 40), (18, 28))
        self.add_line('e1', (18, 28), (22, 32))
        self.add_line('e2', (22, 32), (32, 20))
        self.add_line('e3', (32, 20), (42, 34))
        self.add_line('e4', (38, 42), (11, 42))
        self.add_line('e5', (6, 38), (6, 11))
        self.add_line('e6', (12, 6), (38, 6))
        self.add_line('e7', (42, 10), (42, 34))
        self.add_bezier('e8', (42, 34), ((42, 34.115), (42, 34.047), (42, 34.162)), ((42, 34.219), (42, 34.268), (42, 34.325)), ((42, 35.307), (42, 36.281), (42, 37.263)), ((42, 39.357), (40.275, 42), (38, 42)))
        self.add_bezier('e9', (11, 42), ((10.967, 42), (10.844, 42), (10.811, 42)), ((10.459, 42), (10.001, 41.804), (9.674, 41.705)), ((8.127, 41.255), (6.72, 40.364), (6.131, 38.801)), ((6.09, 38.645), (6.041, 38.498), (6, 38.351)), ((6, 38.204), (6, 38.147), (6, 38)))
        self.add_bezier('e10', (6, 11), ((6, 10.853), (6, 10.615), (6, 10.467)), ((6, 10.115), (6.205, 9.698), (6.335, 9.379)), ((7.154, 7.44), (9.125, 6), (11.269, 6)), ((11.416, 6), (11.845, 6), (12, 6)))
        self.add_bezier('e11', (38, 6), ((38.098, 6.008), (38.097, 6.008), (38.195, 6.016)), ((40.028, 6.016), (42, 8.257), (42, 10)))
        self.add_bezier('e12', (18, 17), ((18, 17.27), (18, 16.73), (18, 17)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3')
        self.add_contour('c1', 'e8', 'e4', 'e9', 'e5', 'e10', 'e6', 'e11', 'e7', closed=True)
        self.add_contour('c2', 'e12')
        self.relate('connect', 'c0', 'c1')
