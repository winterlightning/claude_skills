"""Mastodon logo 1 (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '64a67a06-6c5c-4d48-a6cd-25ab4d165966'
SOURCE_PATH = 'icons-json/logos/mastodon logo 1_64a67a06-6c5c-4d48-a6cd-25ab4d165966.json'
AUTHOR = 'json_to_solo'

class MastodonLogo1Logos(Solo48):
    icon_id = 'mastodon-logo-1-logos'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('mastodon', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (24, 38), (28, 38))
        self.add_line('e1', (28, 42), (20, 42))
        self.add_line('e2', (6, 26), (6, 16))
        self.add_line('e3', (14, 6), (35, 6))
        self.add_line('e4', (42, 14), (42, 24))
        self.add_line('e5', (33, 32), (18, 32))
        self.add_bezier('e6', (18, 32), ((18.155, 33.08), (18.453, 34.481), (18.878, 35.495)), ((19.639, 37.32), (22.233, 38), (24, 38)))
        self.add_bezier('e7', (28, 38), ((30.185, 38), (30.235, 41.984), (28.181, 41.984)), ((28.148, 41.992), (28.033, 41.992), (28, 42)))
        self.add_bezier('e8', (20, 42), ((19.935, 41.992), (19.77, 41.992), (19.705, 41.984)), ((18.256, 41.984), (16.669, 41.501), (15.344, 40.953)), ((10.435, 38.915), (7.047, 34.595), (6.327, 29.302)), ((6.205, 28.369), (6, 26.941), (6, 26)))
        self.add_bezier('e9', (6, 16), ((6, 15.746), (6.008, 15.303), (6.008, 15.049)), ((6.008, 11.089), (7.514, 7.669), (11.547, 6.466)), ((12.308, 6.245), (13.192, 6.008), (13.985, 6.008)), ((14.051, 6.008), (13.935, 6), (14, 6)))
        self.add_bezier('e10', (35, 6), ((35.033, 6), (34.694, 6.008), (34.726, 6.016)), ((35.455, 6.016), (36.248, 6.213), (36.944, 6.417)), ((40.396, 7.448), (41.984, 10.443), (41.984, 13.928)), ((41.992, 13.969), (41.992, 14.018), (42, 14.059)), ((42, 14.1), (42, 13.959), (42, 14)))
        self.add_bezier('e11', (42, 24), ((42, 24.532), (41.861, 25.096), (41.771, 25.62)), ((41.1, 29.326), (38.245, 31.355), (34.669, 31.895)), ((34.154, 31.977), (33.491, 32), (33, 32)))
        self.add_contour('c0', 'e6', 'e0', 'e7', 'e1', 'e8', 'e2', 'e9', 'e3', 'e10', 'e4', 'e11', 'e5', closed=True)
