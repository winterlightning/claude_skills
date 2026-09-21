"""2-0 (text) (other), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7166f712-4d90-4e1d-9e81-eb0a413b8372'
SOURCE_PATH = 'icons-json/other/2-0 (text)_7166f712-4d90-4e1d-9e81-eb0a413b8372.json'
AUTHOR = 'json_to_solo'

class Icon20Text(Solo48):
    icon_id = 'icon-2-0-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('text', 'other')

    def build(self):
        self.add_line('e0', (11, 24), (4, 40))
        self.add_line('e1', (4, 40), (13, 40))
        self.add_bezier('e2', (4, 14), ((4.009, 13.984), (4.009, 14.368), (4.018, 14.352)), ((4.018, 12.848), (7.3, 8.032), (8.173, 8.032)), ((8.255, 8.016), (8.327, 8.016), (8.4, 8)), ((8.401, 8), (8.403, 8), (8.404, 8)), ((8.484, 8), (8.565, 8), (8.645, 8.016)), ((9.355, 8.016), (10.091, 8.832), (10.627, 9.584)), ((13.164, 13.04), (12.955, 19.696), (11, 24)))
        self.add_bezier('e3', (23, 18), ((23, 18.528), (23, 18.472), (23, 19)))
        self.add_bezier('e4', (23, 35), ((23, 35.528), (23, 36.472), (23, 37)))
        self.add_bezier('e5', (33, 24), ((33.045, 18.624), (34.082, 8.016), (38.1, 8.016)), ((38.182, 8.016), (38.273, 8), (38.355, 8)), ((38.436, 8), (38.527, 8.016), (38.618, 8.016)), ((42.2, 8.016), (43.991, 17.104), (43.991, 22.384)), ((43.991, 22.762), (44, 23.14), (44, 23.518)), ((44, 23.524), (44, 23.53), (44, 23.536)), ((44, 24.272), (43.982, 24.992), (43.982, 25.728)), ((43.982, 30.752), (42.382, 39.984), (38.918, 39.984)), ((38.836, 39.984), (38.745, 40), (38.664, 40)), ((38.582, 40), (38.491, 39.984), (38.4, 39.984)), ((34.264, 39.984), (33.036, 29.6), (33, 24)))
        self.add_contour('c0', 'e2', 'e0', 'e1')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5', closed=True)
