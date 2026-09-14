"""Disable (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '20229f13-5d90-5e24-aee8-4a486d31a0f9'
SOURCE_PATH = 'icons-json/interface-essential/disable_20229f13-5d90-5e24-aee8-4a486d31a0f9.json'
AUTHOR = 'json_to_solo'

class Disable(Solo48):
    icon_id = 'disable'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('disable', 'interface-essential')

    def build(self):
        self.add_line('e0', (37, 9), (10, 38))
        self.add_arc('e1-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e1-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
        self.relate('connect', 'c0', 'e1')
        self.relate('connect', 'c0', 'e1')
