"""Elastic cloud logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd50f1116-3c70-4463-ad51-4e8b383b9cee'
SOURCE_PATH = 'icons-json/logos/elastic cloud logo_d50f1116-3c70-4463-ad51-4e8b383b9cee.json'
AUTHOR = 'json_to_solo'

class ElasticCloudLogoLogos(Solo48):
    icon_id = 'elastic-cloud-logo-logos'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('elastic', 'cloud', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (35, 32), (40, 38))
        self.add_line('e1', (20, 30), (16, 33))
        self.add_line('e2', (20, 18), (16, 15))
        self.add_line('e3', (35, 16), (40, 10))
        self.add_arc('e4-1', (20, 30), (23, 33), radius_x=15, sweep=False)
        self.add_arc('e4-2', (23, 33), (27, 34), radius_x=7, sweep=False)
        self.add_line('e4-3', (27, 34), (32, 32))
        self.add_arc('e4-4', (32, 32), (35, 32), radius_x=2)
        self.add_arc('e5-1', (40, 38), (27, 44), radius_x=18)
        self.add_arc('e5-2', (27, 44), (25, 44), radius_x=56, sweep=False)
        self.add_arc('e5-3', (25, 44), (17, 41), radius_x=16)
        self.add_arc('e5-4', (17, 41), (12, 37), radius_x=28, sweep=False)
        self.add_arc('e6', (16, 33), (12, 37), radius_x=20, sweep=False)
        self.add_arc('e7', (20, 30), (20, 18), radius_x=10)
        self.add_line('e8', (16, 15), (12, 11))
        self.add_arc('e9-1', (20, 18), (23, 15), radius_x=13)
        self.add_line('e9-2', (23, 15), (26, 14))
        self.add_arc('e9-3', (26, 14), (32, 16), radius_x=11)
        self.add_arc('e9-4', (32, 16), (35, 16), radius_x=3, sweep=False)
        self.add_arc('e10-1', (40, 10), (27, 4), radius_x=18, sweep=False)
        self.add_line('e10-2', (27, 4), (18, 6))
        self.add_line('e10-3', (18, 6), (12, 11))
        self.add_arc('e11-1', (12, 37), (9, 31), radius_x=24)
        self.add_line('e11-2', (9, 31), (8, 24))
        self.add_line('e11-3', (8, 24), (9, 18))
        self.add_line('e11-4', (9, 18), (12, 11))
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e0', 'e5-1', 'e5-2', 'e5-3', 'e5-4')
        self.add_contour('c1', 'e1', 'e6')
        self.add_contour('c2', 'e7')
        self.add_contour('c3', 'e2', 'e8')
        self.add_contour('c4', 'e9-1', 'e9-2', 'e9-3', 'e9-4', 'e3', 'e10-1', 'e10-2', 'e10-3')
        self.add_contour('c5', 'e11-1', 'e11-2', 'e11-3', 'e11-4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
