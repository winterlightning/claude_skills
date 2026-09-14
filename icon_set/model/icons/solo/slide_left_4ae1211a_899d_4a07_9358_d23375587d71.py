"""Slide left (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ae1211a-899d-4a07-9358-d23375587d71'
SOURCE_PATH = 'icons-json/transportation/slide left_4ae1211a-899d-4a07-9358-d23375587d71.json'
AUTHOR = 'json_to_solo'

class SlideLeft(Solo48):
    icon_id = 'slide-left'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('slide', 'left', 'transportation')

    def build(self):
        self.add_line('e0', (21, 4), (8, 4))
        self.add_line('e1', (33, 44), (39, 39))
        self.add_line('e2', (39, 33), (8, 4))
        self.add_line('e3', (8, 16), (8, 4))
        self.add_line('e4-1', (39, 39), (40, 36))
        self.add_arc('e4-2', (40, 36), (39, 33), radius_x=5, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e4-1', 'e4-2', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
