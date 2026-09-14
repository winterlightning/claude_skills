"""Cursor select frame (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '46e5c48e-63e1-563c-983d-e60435be7c2d'
SOURCE_PATH = 'icons-json/interface-essential/cursor select frame_46e5c48e-63e1-563c-983d-e60435be7c2d.json'
AUTHOR = 'json_to_solo'

class CursorSelectFrame46e5c48e(Solo48):
    icon_id = 'cursor-select-frame-46e5c48e'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('cursor', 'select', 'frame', 'interface-essential')

    def build(self):
        self.add_line('e0', (24, 17), (24, 6))
        self.add_line('e1', (31, 24), (42, 24))
        self.add_line('e2', (6, 24), (17, 24))
        self.add_line('e3', (24, 42), (24, 31))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
