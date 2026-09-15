"""Cursor select frame (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc15b5b4-ea42-56a6-846f-6d7e3d22e58a'
SOURCE_PATH = 'pictographic-primitives/interface-essential/cursor select frame_bc15b5b4-ea42-56a6-846f-6d7e3d22e58a.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class CursorSelectFrameBc15b5b4(Solo48):
    icon_id = 'cursor-select-frame-bc15b5b4'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('cursor', 'select', 'frame', 'interface-essential')

    def build(self):
        self.add_line('e0', (28, 6), (42, 6))
        self.add_line('e1', (42, 6), (42, 20))
        self.add_line('e2', (20, 6), (6, 6))
        self.add_line('e3', (6, 6), (6, 20))
        self.add_line('e4', (42, 28), (42, 42))
        self.add_line('e5', (42, 42), (28, 42))
        self.add_line('e6', (6, 28), (6, 42))
        self.add_line('e7', (6, 42), (20, 42))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3')
        self.add_contour('c2', 'e4', 'e5')
        self.add_contour('c3', 'e6', 'e7')
