"""Keyboard arrow top (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9ac4fae5-c371-5faf-8ca1-01fe89c4d4ce'
SOURCE_PATH = 'icons-json/arrows/keyboard arrow top_9ac4fae5-c371-5faf-8ca1-01fe89c4d4ce.json'
AUTHOR = 'json_to_solo'

class KeyboardArrowTopArrows(Solo48):
    icon_id = 'keyboard-arrow-top-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('keyboard', 'arrow', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (18, 4), (27, 13))
        self.add_line('e1', (8, 13), (17, 4))
        self.add_line('e2', (17, 4), (17, 34))
        self.add_line('e3', (40, 33), (40, 25))
        self.add_arc('e4-1', (17, 34), (27, 44), radius_x=10, sweep=False)
        self.add_line('e4-2', (27, 44), (34, 42))
        self.add_arc('e4-3', (34, 42), (40, 33), radius_x=12, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e4-1', 'e4-2', 'e4-3', 'e3')
