"""Geforce now logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e6855ea8-e1c6-427a-b592-b290b849c8c2'
SOURCE_PATH = 'icons-json/logos/geforce now logo_e6855ea8-e1c6-427a-b592-b290b849c8c2.json'
AUTHOR = 'json_to_solo'

class GeforceNowLogoLogos(Solo48):
    icon_id = 'geforce-now-logo-logos'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('geforce', 'now', 'logo', 'logos')

    def build(self):
        self.add_arc('sym-e0', (19, 34), (29, 34), radius_x=5, radius_y=6)
        self.add_arc('sym-e1', (29, 34), (19, 34), radius_x=5, radius_y=6)
        self.add_bezier('sym-e2', (24, 8), ((24.3, 8), (24.702, 8), (25, 8)))
        self.add_bezier('sym-e3', (25, 8), ((32.064, 8), (39.064, 11.56), (44, 17)))
        self.add_bezier('sym-e4', (24, 18), ((28.619, 18), (33.561, 19.68), (37, 23)))
        self.add_bezier('sym-e5', (24, 8), ((23.7, 8), (23.298, 8), (23, 8)))
        self.add_bezier('sym-e6', (23, 8), ((15.936, 8), (8.936, 11.56), (4, 17)))
        self.add_bezier('sym-e7', (24, 18), ((19.381, 18), (14.439, 19.68), (11, 23)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4')
        self.add_contour('sym-c3', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c4', 'sym-e7')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c4')
