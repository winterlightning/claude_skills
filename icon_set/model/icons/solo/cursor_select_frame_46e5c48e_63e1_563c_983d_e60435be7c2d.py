"""Cursor select frame (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '46e5c48e-63e1-563c-983d-e60435be7c2d'
SOURCE_PATH = 'pictographic-primitives/interface-essential/cursor select frame_46e5c48e-63e1-563c-983d-e60435be7c2d.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class CursorSelectFrameInterfaceEssential(Solo48):
    icon_id = 'cursor-select-frame-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
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
