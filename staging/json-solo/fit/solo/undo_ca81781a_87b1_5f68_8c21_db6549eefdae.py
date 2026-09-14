"""Undo (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca81781a-87b1-5f68-8c21-db6549eefdae'
SOURCE_PATH = 'icons-json/interface-essential/undo_ca81781a-87b1-5f68-8c21-db6549eefdae.json'
AUTHOR = 'json_to_solo'

class UndoInterfaceEssential(Solo48):
    icon_id = 'undo-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('undo', 'interface-essential')

    def build(self):
        self.add_line('e0', (8, 4), (8, 16))
        self.add_line('e1', (17, 16), (8, 16))
        self.add_line('e2', (8, 16), (11, 13))
        self.add_arc('e3-1', (11, 13), (26, 8), radius_x=16)
        self.add_arc('e3-2', (26, 8), (40, 27), radius_x=20)
        self.add_arc('e3-3', (40, 27), (30, 44), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3-1', 'e3-2', 'e3-3')
