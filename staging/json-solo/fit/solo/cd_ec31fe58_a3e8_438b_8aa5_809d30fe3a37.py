"""Cd (electronics), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ec31fe58-a3e8-438b-8aa5-809d30fe3a37'
SOURCE_PATH = 'icons-json/electronics/cd_ec31fe58-a3e8-438b-8aa5-809d30fe3a37.json'
AUTHOR = 'json_to_solo'

class CdEc31fe58(Solo48):
    icon_id = 'cd-ec31fe58'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    aliases = ()
    keywords = ('cd', 'electronics')

    def build(self):
        self.add_arc('sym-e0', (14, 24), (34, 24), radius_x=10)
        self.add_arc('sym-e1', (34, 24), (14, 24), radius_x=10)
        self.add_arc('sym-e2', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e3', (44, 24), (4, 24), radius_x=20)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', closed=True)
