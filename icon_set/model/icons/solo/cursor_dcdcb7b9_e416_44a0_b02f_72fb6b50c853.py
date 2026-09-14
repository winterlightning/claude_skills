"""Cursor (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dcdcb7b9-e416-44a0-b02f-72fb6b50c853'
SOURCE_PATH = 'icons-json/interface-essential/cursor_dcdcb7b9-e416-44a0-b02f-72fb6b50c853.json'
AUTHOR = 'json_to_solo'

class CursorDcdcb7b9(Solo48):
    icon_id = 'cursor-dcdcb7b9'
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
