"""Cd (electronics), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7e0a4e79-2735-5a14-b83c-a5f3468c7540'
SOURCE_PATH = 'icons-json/electronics/cd_7e0a4e79-2735-5a14-b83c-a5f3468c7540.json'
AUTHOR = 'json_to_solo'

class Cd7e0a4e79(Solo48):
    icon_id = 'cd-7e0a4e79'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    aliases = ()
    keywords = ('cd', 'electronics')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e1-top', (18, 24), (30, 24), radius_x=6)
        self.add_arc('e1-bottom', (30, 24), (18, 24), radius_x=6)
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
