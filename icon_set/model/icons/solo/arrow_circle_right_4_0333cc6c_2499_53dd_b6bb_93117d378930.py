"""Arrow circle right 4 (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0333cc6c-2499-53dd-b6bb-93117d378930'
SOURCE_PATH = 'icons-json/arrows/arrow circle right 4_0333cc6c-2499-53dd-b6bb-93117d378930.json'
AUTHOR = 'json_to_solo'

class ArrowCircleRight4(Solo48):
    icon_id = 'arrow-circle-right-4'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'circle', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (35, 24), (7, 24))
        self.add_line('e1', (35, 24), (26, 34))
        self.add_line('e2', (35, 24), (26, 15))
        self.add_bezier('e3', (7, 24), ((6.509, 24.221), (6.008, 24.057), (6.008, 24.794)), ((6, 24.933), (6, 25.064), (6, 25.203)), ((6, 25.206), (6, 25.209), (6, 25.212)), ((6, 25.414), (6, 25.615), (6, 25.816)), ((6, 33.507), (14.836, 41.984), (22.454, 41.984)), ((22.707, 41.984), (22.969, 42), (23.231, 42)), ((23.235, 42), (23.239, 42), (23.244, 42)), ((23.509, 42), (23.775, 41.984), (24.041, 41.984)), ((25.571, 41.984), (27.125, 41.681), (28.59, 41.272)), ((36.15, 39.153), (41.992, 32.403), (41.992, 24.352)), ((41.992, 24.159), (42, 23.957), (42, 23.756)), ((42, 23.753), (42, 23.75), (42, 23.746)), ((42, 23.55), (41.992, 23.354), (41.992, 23.149)), ((41.992, 21.431), (41.599, 19.68), (41.051, 18.052)), ((38.523, 10.623), (31.192, 6.016), (23.46, 6.016)), ((23.255, 6.016), (23.043, 6), (22.838, 6)), ((22.837, 6), (22.836, 6), (22.835, 6)), ((22.77, 6), (22.698, 6.008), (22.634, 6.008)), ((17.487, 6.008), (12.046, 8.905), (9.338, 13.306)), ((8.095, 15.335), (7.581, 17.709), (7, 20)))
        self.add_contour('c0', 'e0', 'e3')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
