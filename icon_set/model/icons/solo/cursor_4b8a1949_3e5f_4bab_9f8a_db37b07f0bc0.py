"""Cursor (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b8a1949-3e5f-4bab-9f8a-db37b07f0bc0'
SOURCE_PATH = 'icons-json/interface-essential/cursor_4b8a1949-3e5f-4bab-9f8a-db37b07f0bc0.json'
AUTHOR = 'json_to_solo'

class CursorInterfaceEssential(Solo48):
    icon_id = 'cursor-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('cursor', 'interface-essential')

    def build(self):
        self.add_line('e0', (42, 42), (24, 6))
        self.add_line('e1', (24, 6), (6, 42))
        self.add_line('e2', (6, 42), (24, 31))
        self.add_line('e3', (24, 31), (42, 42))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3')
