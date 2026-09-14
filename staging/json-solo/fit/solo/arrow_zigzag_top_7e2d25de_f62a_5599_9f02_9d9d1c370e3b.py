"""Arrow zigzag top (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7e2d25de-f62a-5599-9f02-9d9d1c370e3b'
SOURCE_PATH = 'icons-json/arrows/arrow zigzag top_7e2d25de-f62a-5599-9f02-9d9d1c370e3b.json'
AUTHOR = 'json_to_solo'

class ArrowZigzagTopArrows(Solo48):
    icon_id = 'arrow-zigzag-top-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'zigzag', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (8, 31), (19, 44))
        self.add_line('e1', (19, 44), (19, 31))
        self.add_line('e2', (19, 31), (8, 31))
        self.add_line('e3', (19, 44), (30, 44))
        self.add_line('e4', (30, 44), (30, 4))
        self.add_line('e5', (40, 16), (30, 4))
        self.add_line('e6', (30, 4), (19, 16))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)
        self.add_contour('c1', 'e3', 'e4')
        self.add_contour('c2', 'e5', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c2')
