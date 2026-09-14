"""Cursor (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ed914756-71fb-43bb-b670-945d4e962ddd'
SOURCE_PATH = 'icons-json/interface-essential/cursor_ed914756-71fb-43bb-b670-945d4e962ddd.json'
AUTHOR = 'json_to_solo'

class Cursor(Solo48):
    icon_id = 'cursor'
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
        self.add_bezier('e4', (27, 30), ((26.006, 30.273), (24.623, 31.127), (24, 32)))
        self.add_contour('c0', 'e0', 'e1', 'e4', 'e2', 'e3', closed=True)
