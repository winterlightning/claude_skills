"""Cursor left horizontal (state), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a19d3d8c-ca4f-4084-a880-3c773e5774a7'
SOURCE_PATH = 'icons-json/state/cursor left horizontal_a19d3d8c-ca4f-4084-a880-3c773e5774a7.json'
AUTHOR = 'json_to_solo'

class CursorLeftHorizontal(Solo48):
    icon_id = 'cursor-left-horizontal'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('cursor', 'left', 'horizontal', 'state')

    def build(self):
        self.add_line('e0', (4, 22), (44, 8))
        self.add_line('e1', (44, 8), (39, 22))
        self.add_line('e2', (39, 25), (44, 40))
        self.add_line('e3', (44, 40), (4, 22))
        self.add_arc('e4', (39, 22), (39, 25), radius_x=4, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e4', 'e2', 'e3', closed=True)
