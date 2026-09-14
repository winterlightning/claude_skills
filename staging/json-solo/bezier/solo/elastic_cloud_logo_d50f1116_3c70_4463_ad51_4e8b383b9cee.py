"""Elastic cloud logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e4', (20, 30), ((22.493, 32.5), (24.598, 34.436), (28.126, 33.645)), ((28.909, 33.473), (29.659, 33.173), (30.375, 32.791)), ((31.857, 32), (33.383, 30.255), (35, 32)))
        self.add_bezier('e5', (40, 38), ((36.261, 41.473), (32.438, 43.991), (27.276, 43.991)), ((27.185, 43.991), (27.093, 44), (27.002, 44)), ((27.001, 44), (26.999, 44), (26.998, 44)), ((26.627, 44), (26.248, 43.991), (25.878, 43.991)), ((20.312, 43.991), (15.731, 41.136), (12, 37)))
        self.add_bezier('e6', (16, 33), ((14.358, 34.327), (13.415, 35.264), (12, 37)))
        self.add_bezier('e7', (20, 30), ((17.28, 25.455), (17.347, 22.573), (20, 18)))
        self.add_bezier('e8', (16, 15), ((14.653, 14.127), (13.027, 12.245), (12, 11)))
        self.add_bezier('e9', (20, 18), ((22.333, 15.473), (24.716, 13.618), (28.093, 14.427)), ((28.968, 14.636), (29.802, 14.973), (30.611, 15.391)), ((31.823, 16.018), (32.733, 16.973), (34.147, 16.327)), ((34.417, 16.2), (34.789, 16.227), (35, 16)))
        self.add_bezier('e10', (40, 10), ((36.606, 6.255), (31.958, 4.009), (27.023, 4.009)), ((26.932, 4.009), (26.849, 4), (26.758, 4)), ((26.757, 4), (26.755, 4), (26.754, 4)), ((26.442, 4), (26.131, 4.009), (25.819, 4.009)), ((22.173, 4.009), (18.164, 5.555), (15.284, 7.955)), ((14.131, 8.927), (12.968, 9.818), (12, 11)))
        self.add_bezier('e11', (12, 37), ((9.6, 33.609), (8.017, 29.291), (8.017, 24.918)), ((8.017, 24.775), (8, 24.641), (8, 24.498)), ((8, 24.495), (8, 24.493), (8, 24.491)), ((8, 23.991), (8.017, 23.482), (8.017, 22.982)), ((8.017, 18.664), (9.726, 14.418), (12, 11)))
        self.add_contour('c0', 'e4', 'e0', 'e5')
        self.add_contour('c1', 'e1', 'e6')
        self.add_contour('c2', 'e7')
        self.add_contour('c3', 'e2', 'e8')
        self.add_contour('c4', 'e9', 'e3', 'e10')
        self.add_contour('c5', 'e11')
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
