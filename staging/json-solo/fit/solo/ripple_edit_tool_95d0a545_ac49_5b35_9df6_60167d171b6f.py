"""Ripple edit tool (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95d0a545-ac49-5b35-9df6-60167d171b6f'
SOURCE_PATH = 'icons-json/arrows/ripple edit tool_95d0a545-ac49-5b35-9df6-60167d171b6f.json'
AUTHOR = 'json_to_solo'

class RippleEditToolArrows(Solo48):
    icon_id = 'ripple-edit-tool-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('ripple', 'edit', 'tool', 'arrows')

    def build(self):
        self.add_line('e0', (24, 6), (24, 42))
        self.add_line('e1', (42, 24), (6, 24))
        self.add_line('e2', (42, 24), (38, 28))
        self.add_line('e3', (42, 24), (38, 20))
        self.add_line('e4', (6, 24), (10, 20))
        self.add_line('e5', (6, 24), (10, 28))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c4', 'c5')
