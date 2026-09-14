"""Sigma (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9884e826-6f7f-5b39-9937-d7073601df26'
SOURCE_PATH = 'icons-json/interface-essential/sigma_9884e826-6f7f-5b39-9937-d7073601df26.json'
AUTHOR = 'json_to_solo'

class Sigma9884e826(Solo48):
    icon_id = 'sigma-9884e826'
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
