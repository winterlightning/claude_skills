"""Ui browser slider (websites), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c74d64ad-377c-4fc3-b4f9-ee7249035374'
SOURCE_PATH = 'icons-json/websites/ui browser slider_c74d64ad-377c-4fc3-b4f9-ee7249035374.json'
AUTHOR = 'json_to_solo'

class UiBrowserSliderWebsites(Solo48):
    icon_id = 'ui-browser-slider-websites'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'websites'
    aliases = ()
    keywords = ('ui', 'browser', 'slider', 'websites')

    def build(self):
        self.add_line('e0', (42, 16), (6, 16))
        self.add_line('e1', (13, 25), (34, 25))
        self.add_line('e2', (38, 6), (10, 6))
        self.add_line('e3', (6, 10), (6, 38))
        self.add_line('e4', (10, 42), (38, 42))
        self.add_line('e5', (42, 36), (42, 10))
        self.add_bezier('e6', (10, 6), ((8.077, 6), (6.016, 7.857), (6.016, 9.87)), ((6.008, 9.944), (6.008, 9.926), (6, 10)))
        self.add_bezier('e7', (6, 38), ((6, 38.196), (6.016, 38.31), (6.016, 38.506)), ((6.016, 40.028), (7.317, 41.992), (8.986, 41.992)), ((9.052, 42), (9.109, 42), (9.166, 42)), ((9.477, 42), (9.689, 42), (10, 42)))
        self.add_bezier('e8', (38, 42), ((38.131, 41.992), (38.171, 41.992), (38.31, 41.984)), ((40.781, 41.984), (41.984, 39.856), (41.984, 37.631)), ((41.984, 37.181), (42, 36.45), (42, 36)))
        self.add_bezier('e9', (42, 10), ((42, 9.853), (41.984, 9.805), (41.984, 9.657)), ((41.984, 7.636), (40.159, 6.008), (38.187, 6.008)), ((38.089, 6.008), (38.09, 6), (38, 6)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e6', 'e3', 'e7', 'e4', 'e8', 'e5', 'e9', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
