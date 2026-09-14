"""Stumble upon logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cce1a6f4-5cef-4475-9809-0249af388f82'
SOURCE_PATH = 'icons-json/logos/stumble upon logo_cce1a6f4-5cef-4475-9809-0249af388f82.json'
AUTHOR = 'json_to_solo'

class StumbleUponLogoLogos(Solo48):
    icon_id = 'stumble-upon-logo-logos'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('stumble', 'upon', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (4, 40), (19, 40))
        self.add_line('e1', (16, 21), (28, 21))
        self.add_line('e2', (31, 24), (31, 35))
        self.add_line('e3', (44, 35), (44, 8))
        self.add_bezier('e4', (19, 40), ((19.555, 40), (19.764, 39.688), (20.245, 39.444)), ((22.991, 38.055), (23.773, 34.611), (22.091, 32.227)), ((19.391, 28.396), (15.127, 31.655), (12.355, 28.084)), ((10.527, 25.735), (11.564, 22.282), (14.355, 21.053)), ((14.773, 20.859), (15.518, 21), (16, 21)))
        self.add_bezier('e5', (28, 21), ((29.609, 21), (31, 22.518), (31, 24)))
        self.add_bezier('e6', (31, 35), ((31, 35.126), (31.391, 35.326), (31.418, 35.469)), ((31.891, 37.659), (34.636, 39.992), (37.136, 39.992)), ((37.236, 39.992), (37.336, 40), (37.445, 40)), ((37.582, 40), (37.727, 39.983), (37.864, 39.983)), ((40.309, 39.983), (44, 37.4), (44, 35)))
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e5', 'e2', 'e6', 'e3')
