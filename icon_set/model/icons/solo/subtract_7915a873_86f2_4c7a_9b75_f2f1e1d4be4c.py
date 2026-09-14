"""Subtract (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7915a873-86f2-4c7a-9b75-f2f1e1d4be4c'
SOURCE_PATH = 'icons-json/interface-essential/subtract_7915a873-86f2-4c7a-9b75-f2f1e1d4be4c.json'
AUTHOR = 'gpt-6'

class Subtract(Solo48):
    icon_id = 'subtract'
    keyshape = Keyshape.FREE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('subtract', 'interface-essential')

    def build(self):
        self.add_line('e0', (4, 24), (44, 24))
        self.add_contour('c0', 'e0')
