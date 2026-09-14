"""Photo (state), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'abfa4d34-f0c4-4ef1-8fdf-cc3a1edb6828'
SOURCE_PATH = 'icons-json/state/photo_abfa4d34-f0c4-4ef1-8fdf-cc3a1edb6828.json'
AUTHOR = 'json_to_solo'

class PhotoState(Solo48):
    icon_id = 'photo-state'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('photo', 'state')

    def build(self):
        self.add_line('e0', (9, 40), (18, 28))
        self.add_line('e1', (18, 28), (22, 32))
        self.add_line('e2', (22, 32), (32, 20))
        self.add_line('e3', (32, 20), (42, 34))
        self.add_line('e4', (38, 42), (11, 42))
        self.add_line('e5', (6, 38), (6, 11))
        self.add_line('e6', (12, 6), (38, 6))
        self.add_line('e7', (42, 10), (42, 34))
        self.add_line('e8-1', (42, 34), (41, 40))
        self.add_arc('e8-2', (41, 40), (38, 42), radius_x=4)
        self.add_arc('e9', (11, 42), (6, 38), radius_x=6)
        self.add_arc('e10-1', (6, 11), (11, 6), radius_x=6)
        self.add_line('e10-2', (11, 6), (12, 6))
        self.add_arc('e11', (38, 6), (42, 10), radius_x=5)
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3')
        self.add_contour('c1', 'e8-1', 'e8-2', 'e4', 'e9', 'e5', 'e10-1', 'e10-2', 'e6', 'e11', 'e7', closed=True)
        self.relate('connect', 'c0', 'c1')
