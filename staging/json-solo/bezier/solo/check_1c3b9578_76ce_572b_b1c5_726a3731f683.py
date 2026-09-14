"""Check (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1c3b9578-76ce-572b-b1c5-726a3731f683'
SOURCE_PATH = 'icons-json/interface-essential/check_1c3b9578-76ce-572b-b1c5-726a3731f683.json'
AUTHOR = 'json_to_solo'

class Check(Solo48):
    icon_id = 'check'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('check', 'interface-essential')

    def build(self):
        self.add_line('e0', (42, 6), (16, 42))
        self.add_line('e1', (16, 42), (6, 31))
        self.add_contour('c0', 'e0', 'e1')
