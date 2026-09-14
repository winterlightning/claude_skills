"""Oculus logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '12bd1899-000c-4b67-950e-b0cf9be91bc2'
SOURCE_PATH = 'icons-json/logos/oculus logo_12bd1899-000c-4b67-950e-b0cf9be91bc2.json'
AUTHOR = 'json_to_solo'

class OculusLogoLogos(Solo48):
    icon_id = 'oculus-logo-logos'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('oculus', 'logo', 'logos')

    def build(self):
        self.add_line('sym-e0', (35, 40), (24, 40))
        self.add_line('sym-e1', (24, 40), (13, 40))
        self.add_arc('sym-e2', (13, 40), (11, 39), radius_x=5)
        self.add_arc('sym-e3', (11, 39), (4, 25), radius_x=18)
        self.add_line('sym-e4', (4, 25), (4, 24))
        self.add_line('sym-e5', (4, 24), (4, 23))
        self.add_arc('sym-e6', (4, 23), (11, 9), radius_x=18)
        self.add_arc('sym-e7', (11, 9), (13, 8), radius_x=4)
        self.add_line('sym-e9', (13, 8), (24, 8))
        self.add_line('sym-e10', (24, 8), (35, 8))
        self.add_arc('sym-e12', (35, 8), (37, 9), radius_x=4)
        self.add_arc('sym-e13', (37, 9), (44, 23), radius_x=18)
        self.add_line('sym-e14', (44, 23), (44, 24))
        self.add_arc('sym-e15', (44, 24), (44, 25), radius_x=28, sweep=False)
        self.add_arc('sym-e16', (44, 25), (37, 39), radius_x=18)
        self.add_arc('sym-e17', (37, 39), (35, 40), radius_x=5)
        self.add_line('sym-e18', (33, 19), (24, 19))
        self.add_line('sym-e19', (24, 19), (15, 19))
        self.add_arc('sym-e20', (15, 19), (12, 23), radius_x=5, sweep=False)
        self.add_arc('sym-e21', (12, 23), (15, 29), radius_x=5, sweep=False)
        self.add_line('sym-e22', (15, 29), (24, 29))
        self.add_line('sym-e23', (24, 29), (33, 29))
        self.add_arc('sym-e24', (33, 29), (36, 23), radius_x=5, sweep=False)
        self.add_arc('sym-e25', (36, 23), (33, 19), radius_x=5, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e9', 'sym-e10', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
        self.add_contour('sym-c1', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', closed=True)
