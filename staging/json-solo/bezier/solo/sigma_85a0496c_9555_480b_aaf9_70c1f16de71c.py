"""Sigma (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '85a0496c-9555-480b-aaf9-70c1f16de71c'
SOURCE_PATH = 'icons-json/interface-essential/sigma_85a0496c-9555-480b-aaf9-70c1f16de71c.json'
AUTHOR = 'json_to_solo'

class Sigma85a0496c(Solo48):
    icon_id = 'sigma-85a0496c'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('sigma', 'interface-essential')

    def build(self):
        self.add_line('e0', (40, 4), (8, 4))
        self.add_line('e1', (8, 4), (27, 24))
        self.add_line('e2', (27, 24), (8, 44))
        self.add_line('e3', (8, 44), (40, 44))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3')
