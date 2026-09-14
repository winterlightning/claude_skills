"""Arrow circle bottom 4 (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '114deb1b-00c7-5f63-92e5-a85bd467378b'
SOURCE_PATH = 'icons-json/arrows/arrow circle bottom 4_114deb1b-00c7-5f63-92e5-a85bd467378b.json'
AUTHOR = 'json_to_solo'

class ArrowCircleBottom4Arrows(Solo48):
    icon_id = 'arrow-circle-bottom-4-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'circle', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (24, 35), (24, 7))
        self.add_line('e1', (24, 35), (14, 26))
        self.add_line('e2', (24, 35), (34, 26))
        self.add_bezier('e3', (24, 7), ((23.779, 6.509), (23.943, 6.008), (23.206, 6.008)), ((23.067, 6), (22.936, 6), (22.797, 6)), ((22.794, 6), (22.791, 6), (22.788, 6)), ((22.586, 6), (22.385, 6), (22.184, 6)), ((14.493, 6), (6.016, 14.836), (6.016, 22.454)), ((6.016, 22.703), (6, 22.961), (6, 23.219)), ((6, 23.223), (6, 23.227), (6, 23.231)), ((6, 23.501), (6.016, 23.771), (6.016, 24.041)), ((6.016, 25.571), (6.319, 27.125), (6.728, 28.59)), ((8.847, 36.15), (15.597, 41.992), (23.648, 41.992)), ((23.841, 41.992), (24.043, 42), (24.244, 42)), ((24.247, 42), (24.25, 42), (24.254, 42)), ((24.45, 42), (24.646, 41.992), (24.851, 41.992)), ((26.569, 41.992), (28.32, 41.599), (29.948, 41.051)), ((37.377, 38.523), (41.984, 31.192), (41.984, 23.46)), ((41.984, 23.255), (42, 23.043), (42, 22.838)), ((42, 22.837), (42, 22.836), (42, 22.835)), ((42, 22.77), (41.992, 22.698), (41.992, 22.634)), ((41.992, 17.487), (39.095, 12.046), (34.694, 9.338)), ((32.665, 8.095), (30.291, 7.581), (28, 7)))
        self.add_contour('c0', 'e0', 'e3')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
