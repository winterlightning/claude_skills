"""Ui browser slider (websites), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('e6', (10, 6), (6, 10), radius_x=4, sweep=False)
        self.add_arc('e7-1', (6, 38), (7, 41), radius_x=5, sweep=False)
        self.add_line('e7-2', (7, 41), (9, 42))
        self.add_arc('e7-3', (9, 42), (10, 42), radius_x=22)
        self.add_line('e8-1', (38, 42), (41, 41))
        self.add_line('e8-2', (41, 41), (42, 36))
        self.add_arc('e9', (42, 10), (38, 6), radius_x=4, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e6', 'e3', 'e7-1', 'e7-2', 'e7-3', 'e4', 'e8-1', 'e8-2', 'e5', 'e9', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
