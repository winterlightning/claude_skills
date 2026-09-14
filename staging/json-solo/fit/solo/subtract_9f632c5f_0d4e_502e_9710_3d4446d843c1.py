"""Subtract (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f632c5f-0d4e-502e-9710-3d4446d843c1'
SOURCE_PATH = 'icons-json/interface-essential/subtract_9f632c5f-0d4e-502e-9710-3d4446d843c1.json'
AUTHOR = 'json_to_solo'

class Subtract9f632c5f(Solo48):
    icon_id = 'subtract-9f632c5f'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('subtract', 'interface-essential')

    def build(self):
        self.add_line('e0', (4, 24), (44, 24))
        self.add_contour('c0', 'e0')
