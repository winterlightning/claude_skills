"""Ello logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ffdc3f61-3f5e-4ec1-ab2c-725ed785dddc'
SOURCE_PATH = 'icons-json/logos/ello logo_ffdc3f61-3f5e-4ec1-ab2c-725ed785dddc.json'
AUTHOR = 'json_to_solo'

class ElloLogo(Solo48):
    icon_id = 'ello-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('ello', 'logo', 'logos')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e1-1', (14, 26), (20, 34), radius_x=11, sweep=False)
        self.add_arc('e1-2', (20, 34), (34, 26), radius_x=10, sweep=False)
        self.add_contour('c0', 'e1-1', 'e1-2')
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
