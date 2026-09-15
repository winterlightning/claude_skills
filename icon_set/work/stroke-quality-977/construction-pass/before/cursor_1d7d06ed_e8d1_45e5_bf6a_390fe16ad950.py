"""Cursor (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1d7d06ed-e8d1-45e5-bf6a-390fe16ad950'
SOURCE_PATH = 'pictographic-primitives/interface-essential/cursor_1d7d06ed-e8d1-45e5-bf6a-390fe16ad950.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Cursor(Solo48):
    icon_id = 'cursor'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('cursor', 'interface-essential')

    def build(self):
        self.add_line('e0', (40, 21), (8, 4))
        self.add_line('e1', (8, 4), (11, 44))
        self.add_line('e2', (11, 44), (21, 26))
        self.add_line('e3', (21, 26), (40, 21))
        self.add_line('e4', (21, 26), (31, 41))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
