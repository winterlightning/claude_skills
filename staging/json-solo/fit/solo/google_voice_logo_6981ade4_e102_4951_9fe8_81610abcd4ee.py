"""Google voice logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6981ade4-e102-4951-9fe8-81610abcd4ee'
SOURCE_PATH = 'icons-json/logos/google voice logo_6981ade4-e102-4951-9fe8-81610abcd4ee.json'
AUTHOR = 'json_to_solo'

class GoogleVoiceLogoLogos(Solo48):
    icon_id = 'google-voice-logo-logos'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('google', 'voice', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (27, 18), (27, 8))
        self.add_line('e1', (41, 20), (29, 20))
        self.add_line('e2', (40, 36), (33, 30))
        self.add_line('e3', (16, 21), (18, 17))
        self.add_line('e4', (18, 15), (12, 8))
        self.add_arc('e5-1', (27, 8), (29, 6), radius_x=2)
        self.add_arc('e5-2', (29, 6), (42, 18), radius_x=14)
        self.add_line('e5-3', (42, 18), (41, 20))
        self.add_arc('e6', (29, 20), (27, 18), radius_x=2)
        self.add_arc('e7-1', (33, 30), (30, 30), radius_x=2, sweep=False)
        self.add_arc('e7-2', (30, 30), (26, 33), radius_x=7)
        self.add_arc('e7-3', (26, 33), (19, 28), radius_x=14)
        self.add_arc('e7-4', (19, 28), (16, 21), radius_x=6)
        self.add_arc('e8', (18, 17), (18, 15), radius_x=2, sweep=False)
        self.add_arc('e9-1', (12, 8), (8, 10), radius_x=3, sweep=False)
        self.add_arc('e9-2', (8, 10), (6, 16), radius_x=13, sweep=False)
        self.add_arc('e9-3', (6, 16), (31, 42), radius_x=30, sweep=False)
        self.add_line('e9-4', (31, 42), (38, 40))
        self.add_arc('e9-5', (38, 40), (40, 36), radius_x=3, sweep=False)
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e5-3', 'e1', 'e6', closed=True)
        self.add_contour('c1', 'e2', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e3', 'e8', 'e4', 'e9-1', 'e9-2', 'e9-3', 'e9-4', 'e9-5', closed=True)
