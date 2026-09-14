"""Whistle (sports), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c3a5ced3-e720-4af3-8b39-b0f56b9fee0f'
SOURCE_PATH = 'icons-json/sports/whistle_c3a5ced3-e720-4af3-8b39-b0f56b9fee0f.json'
AUTHOR = 'json_to_solo'

class WhistleC3a5ced3(Solo48):
    icon_id = 'whistle-c3a5ced3'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('whistle', 'sports')

    def build(self):
        self.add_line('e0', (40, 6), (42, 13))
        self.add_line('e1', (42, 13), (31, 22))
        self.add_line('e2', (13, 17), (40, 6))
        self.add_arc('e3-1', (31, 22), (19, 42), radius_x=14)
        self.add_arc('e3-2', (19, 42), (10, 38), radius_x=13)
        self.add_line('e3-3', (10, 38), (7, 34))
        self.add_line('e3-4', (7, 34), (6, 28))
        self.add_arc('e3-5', (6, 28), (13, 17), radius_x=13)
        self.add_contour('c0', 'e0', 'e1', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e2', closed=True)
