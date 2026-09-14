"""Code (programing), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '13ea8366-b426-4bc2-a649-eea82df87819'
SOURCE_PATH = 'icons-json/programing/code_13ea8366-b426-4bc2-a649-eea82df87819.json'
AUTHOR = 'json_to_solo'

class Code(Solo48):
    icon_id = 'code'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('code', 'programing')

    def build(self):
        self.add_line('e0', (13, 8), (4, 24))
        self.add_line('e1', (4, 24), (13, 40))
        self.add_line('e2', (35, 8), (44, 24))
        self.add_line('e3', (44, 24), (35, 40))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3')
