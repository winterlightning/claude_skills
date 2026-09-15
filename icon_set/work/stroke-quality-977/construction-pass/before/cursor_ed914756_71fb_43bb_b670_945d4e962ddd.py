"""Cursor (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ed914756-71fb-43bb-b670-945d4e962ddd'
SOURCE_PATH = 'pictographic-primitives/interface-essential/cursor_ed914756-71fb-43bb-b670-945d4e962ddd.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class CursorEd914756(Solo48):
    icon_id = 'cursor-ed914756'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('cursor', 'interface-essential')

    def build(self):
        self.add_line('e0', (8, 4), (40, 27))
        self.add_line('e1', (40, 27), (27, 30))
        self.add_line('e2', (24, 32), (16, 44))
        self.add_line('e3', (16, 44), (8, 4))
        self.add_arc('e4', (27, 30), (24, 32), radius_x=4, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e4', 'e2', 'e3', closed=True)
