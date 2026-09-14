"""Stumble upon logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cce1a6f4-5cef-4475-9809-0249af388f82'
SOURCE_PATH = 'icons-json/logos/stumble upon logo_cce1a6f4-5cef-4475-9809-0249af388f82.json'
AUTHOR = 'json_to_solo'

class StumbleUponLogo(Solo48):
    icon_id = 'stumble-upon-logo'
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
        self.add_arc('e4-1', (19, 40), (23, 35), radius_x=5, sweep=False)
        self.add_arc('e4-2', (23, 35), (21, 31), radius_x=5, sweep=False)
        self.add_line('e4-3', (21, 31), (13, 29))
        self.add_arc('e4-4', (13, 29), (12, 23), radius_x=5)
        self.add_arc('e4-5', (12, 23), (16, 21), radius_x=5)
        self.add_arc('e5', (28, 21), (31, 24), radius_x=4)
        self.add_arc('e6-1', (31, 35), (37, 40), radius_x=7, sweep=False)
        self.add_arc('e6-2', (37, 40), (44, 35), radius_x=8, sweep=False)
        self.add_contour('c0', 'e0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e1', 'e5', 'e2', 'e6-1', 'e6-2', 'e3')
