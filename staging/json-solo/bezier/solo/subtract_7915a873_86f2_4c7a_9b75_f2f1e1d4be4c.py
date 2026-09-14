"""Subtract (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7915a873-86f2-4c7a-9b75-f2f1e1d4be4c'
SOURCE_PATH = 'icons-json/interface-essential/subtract_7915a873-86f2-4c7a-9b75-f2f1e1d4be4c.json'
AUTHOR = 'json_to_solo'

class Subtract7915a873(Solo48):
    icon_id = 'subtract-7915a873'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('subtract', 'interface-essential')

    def build(self):
        self.add_line('e0', (4, 24), (44, 24))
        self.add_contour('c0', 'e0')
