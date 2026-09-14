"""Kibana logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e6', (8, 43), ((8.135, 43.209), (8.034, 43.636), (8.185, 43.827)), ((8.337, 44), (8.823, 43.845), (9, 44)))
        self.add_bezier('e7', (37, 44), ((34.785, 35.164), (31.006, 28.218), (24, 23)))
        self.add_bezier('e8', (8, 19), ((13.912, 18.927), (18.973, 19.518), (24, 23)))
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
