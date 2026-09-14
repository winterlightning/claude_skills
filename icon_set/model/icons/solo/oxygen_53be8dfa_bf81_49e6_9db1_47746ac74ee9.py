"""Oxygen (health), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '53be8dfa-bf81-49e6-9db1-47746ac74ee9'
SOURCE_PATH = 'icons-json/health/oxygen_53be8dfa-bf81-49e6-9db1-47746ac74ee9.json'
AUTHOR = 'json_to_solo'

class Oxygen(Solo48):
    icon_id = 'oxygen'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('oxygen', 'health')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e1-top', (23, 17), (33, 17), radius_x=5)
        self.add_arc('e1-bottom', (33, 17), (23, 17), radius_x=5)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
