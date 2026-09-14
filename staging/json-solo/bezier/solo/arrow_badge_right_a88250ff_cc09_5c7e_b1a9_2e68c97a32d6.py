"""Arrow badge right (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a88250ff-cc09-5c7e-b1a9-2e68c97a32d6'
SOURCE_PATH = 'icons-json/arrows/arrow badge right_a88250ff-cc09-5c7e-b1a9-2e68c97a32d6.json'
AUTHOR = 'json_to_solo'

class ArrowBadgeRightA88250ff(Solo48):
    icon_id = 'arrow-badge-right-a88250ff'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'badge', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (26, 40), (7, 40))
        self.add_line('e1', (4, 37), (4, 11))
        self.add_line('e2', (6, 8), (29, 8))
        self.add_line('e3', (36, 14), (43, 22))
        self.add_line('e4', (42, 26), (32, 38))
        self.add_line('e5', (18, 32), (25, 24))
        self.add_line('e6', (25, 24), (18, 16))
        self.add_bezier('e7', (34, 36), ((33.4, 36.67), (32.791, 37.34), (32.182, 38)), ((31.491, 38.75), (30.564, 39.99), (29.491, 39.99)), ((29.282, 39.99), (29.082, 40), (28.873, 40)), ((27.855, 40), (27.018, 40), (26, 40)))
        self.add_bezier('e8', (7, 40), ((6.8, 40), (6.327, 39.99), (6.127, 39.99)), ((4.991, 39.99), (4, 38.73), (4, 37.53)), ((4, 37.36), (4, 37.18), (4, 37)))
        self.add_bezier('e9', (4, 11), ((4, 10.9), (4.009, 10.81), (4.009, 10.71)), ((4.009, 9.69), (4.518, 8.8), (5.255, 8.23)), ((5.436, 8.1), (5.818, 8.12), (6, 8)))
        self.add_bezier('e10', (29, 8), ((29.136, 8.01), (28.818, 8.01), (28.955, 8.02)), ((30.536, 8.02), (35.082, 12.99), (36, 14)))
        self.add_bezier('e11', (43, 22), ((43.291, 22.32), (43.982, 22.81), (43.982, 23.32)), ((43.991, 23.38), (43.991, 23.43), (44, 23.48)), ((44, 23.481), (44, 23.482), (44, 23.483)), ((44, 23.542), (43.991, 23.591), (43.991, 23.64)), ((43.991, 24.61), (42.509, 25.39), (42, 26)))
        self.add_contour('c0', 'e7', 'e0', 'e8', 'e1', 'e9', 'e2', 'e10', 'e3', 'e11', 'e4')
        self.add_contour('c1', 'e5', 'e6')
