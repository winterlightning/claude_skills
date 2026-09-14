"""Cursor select frame (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2f57dc5d-637f-571a-8119-fe94fbeb9258'
SOURCE_PATH = 'icons-json/interface-essential/cursor select frame_2f57dc5d-637f-571a-8119-fe94fbeb9258.json'
AUTHOR = 'json_to_solo'

class CursorSelectFrame(Solo48):
    icon_id = 'cursor-select-frame'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('cursor', 'select', 'frame', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (6, 16), (6, 8))
        self.add_arc('sym-e2', (6, 8), (8, 6), radius_x=2)
        self.add_line('sym-e5', (8, 6), (17, 6))
        self.add_line('sym-e6', (31, 6), (40, 6))
        self.add_arc('sym-e8', (40, 6), (42, 8), radius_x=2)
        self.add_line('sym-e11', (42, 8), (42, 16))
        self.add_line('sym-e12', (6, 32), (6, 40))
        self.add_arc('sym-e14', (6, 40), (8, 42), radius_x=2, sweep=False)
        self.add_line('sym-e17', (8, 42), (17, 42))
        self.add_line('sym-e18', (31, 42), (40, 42))
        self.add_arc('sym-e20', (40, 42), (42, 40), radius_x=2, sweep=False)
        self.add_line('sym-e23', (42, 40), (42, 32))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e5')
        self.add_contour('sym-c1', 'sym-e6', 'sym-e8', 'sym-e11')
        self.add_contour('sym-c2', 'sym-e12', 'sym-e14', 'sym-e17')
        self.add_contour('sym-c3', 'sym-e18', 'sym-e20', 'sym-e23')
