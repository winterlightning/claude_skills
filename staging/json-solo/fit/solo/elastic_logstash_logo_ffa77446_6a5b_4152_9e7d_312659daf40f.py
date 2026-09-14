"""Elastic logstash logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ffa77446-6a5b-4152-9e7d-312659daf40f'
SOURCE_PATH = 'icons-json/logos/elastic logstash logo_ffa77446-6a5b-4152-9e7d-312659daf40f.json'
AUTHOR = 'json_to_solo'

class ElasticLogstashLogoLogos(Solo48):
    icon_id = 'elastic-logstash-logo-logos'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('elastic', 'logstash', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (23, 42), (23, 25))
        self.add_line('e1', (23, 42), (42, 42))
        self.add_line('e2', (42, 42), (42, 25))
        self.add_line('e3', (42, 25), (23, 25))
        self.add_line('e4', (23, 42), (17, 42))
        self.add_line('e5', (6, 31), (6, 25))
        self.add_line('e6', (6, 25), (23, 25))
        self.add_line('e7', (6, 25), (6, 6))
        self.add_line('e8', (6, 6), (13, 6))
        self.add_line('e9', (23, 16), (23, 25))
        self.add_arc('e10', (17, 42), (6, 31), radius_x=12)
        self.add_arc('e11', (13, 6), (23, 16), radius_x=10)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3')
        self.add_contour('c2', 'e4', 'e10', 'e5')
        self.add_contour('c3', 'e6')
        self.add_contour('c4', 'e7', 'e8', 'e11', 'e9')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
