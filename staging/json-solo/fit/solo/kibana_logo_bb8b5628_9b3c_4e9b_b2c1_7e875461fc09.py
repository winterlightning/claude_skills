"""Kibana logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb8b5628-9b3c-4e9b-b2c1-7e875461fc09'
SOURCE_PATH = 'icons-json/logos/kibana logo_bb8b5628-9b3c-4e9b-b2c1-7e875461fc09.json'
AUTHOR = 'json_to_solo'

class KibanaLogoLogos(Solo48):
    icon_id = 'kibana-logo-logos'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('kibana', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (9, 44), (37, 44))
        self.add_line('e1', (8, 19), (8, 42))
        self.add_line('e2', (8, 42), (24, 23))
        self.add_line('e3', (8, 19), (8, 4))
        self.add_line('e4', (8, 4), (40, 4))
        self.add_line('e5', (40, 4), (24, 23))
        self.add_arc('e6', (8, 43), (9, 44), radius_x=1, sweep=False)
        self.add_arc('e7', (37, 44), (24, 23), radius_x=35, sweep=False)
        self.add_arc('e8', (8, 19), (24, 23), radius_x=25)
        self.add_contour('c0', 'e6', 'e0', 'e7')
        self.add_contour('c1', 'e8')
        self.add_contour('c2', 'e1', 'e2')
        self.add_contour('c3', 'e3', 'e4', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
