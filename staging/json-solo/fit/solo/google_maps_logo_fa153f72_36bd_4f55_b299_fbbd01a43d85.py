"""Google maps logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa153f72-36bd-4f55-b299-fbbd01a43d85'
SOURCE_PATH = 'icons-json/logos/google maps logo_fa153f72-36bd-4f55-b299-fbbd01a43d85.json'
AUTHOR = 'json_to_solo'

class GoogleMapsLogoLogos(Solo48):
    icon_id = 'google-maps-logo-logos'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('google', 'maps', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (17, 35), (29, 23))
        self.add_line('e1', (17, 35), (11, 28))
        self.add_line('e2', (17, 35), (22, 43))
        self.add_line('e3', (26, 14), (11, 28))
        self.add_line('e4', (26, 14), (34, 7))
        self.add_arc('e5', (29, 23), (26, 14), radius_x=6, sweep=False)
        self.add_arc('e6-1', (22, 43), (24, 44), radius_x=3, sweep=False)
        self.add_arc('e6-2', (24, 44), (26, 43), radius_x=3, sweep=False)
        self.add_arc('e6-3', (26, 43), (34, 32), radius_x=56)
        self.add_arc('e6-4', (34, 32), (40, 20), radius_x=17, sweep=False)
        self.add_line('e6-5', (40, 20), (39, 14))
        self.add_arc('e6-6', (39, 14), (37, 10), radius_x=16, sweep=False)
        self.add_arc('e6-7', (37, 10), (34, 7), radius_x=16, sweep=False)
        self.add_arc('e7-1', (11, 28), (8, 20), radius_x=13)
        self.add_arc('e7-2', (8, 20), (24, 4), radius_x=16)
        self.add_line('e7-3', (24, 4), (30, 5))
        self.add_arc('e7-4', (30, 5), (34, 7), radius_x=22)
        self.add_contour('c0', 'e0', 'e5')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e6-6', 'e6-7')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e7-1', 'e7-2', 'e7-3', 'e7-4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
