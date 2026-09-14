"""Geforce now logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e6855ea8-e1c6-427a-b592-b290b849c8c2'
SOURCE_PATH = 'icons-json/logos/geforce now logo_e6855ea8-e1c6-427a-b592-b290b849c8c2.json'
AUTHOR = 'json_to_solo'

class GeforceNowLogo(Solo48):
    icon_id = 'geforce-now-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('geforce', 'now', 'logo', 'logos')

    def build(self):
        self.add_arc('sym-e0', (19, 34), (29, 34), radius_x=5, radius_y=6)
        self.add_arc('sym-e1', (29, 34), (19, 34), radius_x=5, radius_y=6)
        self.add_arc('sym-e2', (24, 8), (25, 8), radius_x=1, sweep=False)
        self.add_arc('sym-e3', (25, 8), (44, 17), radius_x=27)
        self.add_arc('sym-e4', (24, 18), (37, 23), radius_x=18)
        self.add_arc('sym-e5', (24, 8), (23, 8), radius_x=1)
        self.add_arc('sym-e6', (23, 8), (4, 17), radius_x=27, sweep=False)
        self.add_arc('sym-e7', (24, 18), (11, 23), radius_x=19, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4')
        self.add_contour('sym-c3', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c4', 'sym-e7')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c4')
