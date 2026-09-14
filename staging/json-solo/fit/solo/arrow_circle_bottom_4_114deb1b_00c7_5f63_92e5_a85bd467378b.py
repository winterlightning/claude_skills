"""Arrow circle bottom 4 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '114deb1b-00c7-5f63-92e5-a85bd467378b'
SOURCE_PATH = 'icons-json/arrows/arrow circle bottom 4_114deb1b-00c7-5f63-92e5-a85bd467378b.json'
AUTHOR = 'json_to_solo'

class ArrowCircleBottom4Arrows(Solo48):
    icon_id = 'arrow-circle-bottom-4-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'circle', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (24, 35), (24, 7))
        self.add_line('e1', (24, 35), (14, 26))
        self.add_line('e2', (24, 35), (34, 26))
        self.add_arc('e3-1', (24, 7), (23, 6), radius_x=1, sweep=False)
        self.add_arc('e3-2', (23, 6), (6, 23), radius_x=18, sweep=False)
        self.add_arc('e3-3', (6, 23), (13, 38), radius_x=20, sweep=False)
        self.add_arc('e3-4', (13, 38), (18, 41), radius_x=17, sweep=False)
        self.add_line('e3-5', (18, 41), (24, 42))
        self.add_line('e3-6', (24, 42), (30, 41))
        self.add_arc('e3-7', (30, 41), (34, 39), radius_x=16, sweep=False)
        self.add_arc('e3-8', (34, 39), (42, 23), radius_x=20, sweep=False)
        self.add_line('e3-9', (42, 23), (40, 15))
        self.add_line('e3-10', (40, 15), (38, 12))
        self.add_arc('e3-11', (38, 12), (28, 7), radius_x=17, sweep=False)
        self.add_contour('c0', 'e0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e3-8', 'e3-9', 'e3-10', 'e3-11')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
