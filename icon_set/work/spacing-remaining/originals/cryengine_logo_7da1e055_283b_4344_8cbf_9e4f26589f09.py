"""Cryengine logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7da1e055-283b-4344-8cbf-9e4f26589f09'
SOURCE_PATH = 'icons-json/logos/cryengine logo_7da1e055-283b-4344-8cbf-9e4f26589f09.json'
AUTHOR = 'json_to_solo'

class CryengineLogo(Solo48):
    icon_id = 'cryengine-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('cryengine', 'logo', 'logos')

    def build(self):
        self.add_arc('e0-top', (19, 24), (29, 24), radius_x=5, radius_y=10)
        self.add_arc('e0-bottom', (29, 24), (19, 24), radius_x=5, radius_y=10)
        self.add_arc('e1-1', (18, 8), (4, 24), radius_x=29, sweep=False)
        self.add_arc('e1-2', (4, 24), (16, 38), radius_x=28, sweep=False)
        self.add_arc('e2-1', (30, 8), (44, 24), radius_x=30)
        self.add_arc('e2-2', (44, 24), (29, 40), radius_x=24)
        self.add_contour('c0', 'e1-1', 'e1-2')
        self.add_contour('c1', 'e2-1', 'e2-2')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
