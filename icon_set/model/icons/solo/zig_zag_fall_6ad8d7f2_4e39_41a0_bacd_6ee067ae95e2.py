"""Zig zag fall (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6ad8d7f2-4e39-41a0-bacd-6ee067ae95e2'
SOURCE_PATH = 'icons-json/arrows/zig zag fall_6ad8d7f2-4e39-41a0-bacd-6ee067ae95e2.json'
AUTHOR = 'json_to_solo'

class ZigZagFall(Solo48):
    icon_id = 'zig-zag-fall'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('zig', 'zag', 'fall', 'arrows')

    def build(self):
        self.add_line('e0', (19, 4), (19, 16))
        self.add_line('e1', (19, 16), (40, 16))
        self.add_line('e2', (40, 16), (8, 28))
        self.add_line('e3', (8, 28), (27, 28))
        self.add_line('e4', (27, 28), (27, 44))
        self.add_line('e5', (16, 39), (27, 44))
        self.add_line('e6', (38, 38), (27, 44))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4')
        self.add_contour('c1', 'e5')
        self.add_contour('c2', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
