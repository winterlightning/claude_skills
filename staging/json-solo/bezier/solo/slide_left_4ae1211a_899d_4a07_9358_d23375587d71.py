"""Slide left (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ae1211a-899d-4a07-9358-d23375587d71'
SOURCE_PATH = 'icons-json/transportation/slide left_4ae1211a-899d-4a07-9358-d23375587d71.json'
AUTHOR = 'json_to_solo'

class SlideLeftTransportation(Solo48):
    icon_id = 'slide-left-transportation'
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
        self.add_bezier('e4', (39, 39), ((39.59, 38.464), (40, 36.927), (40, 36.182)), ((40, 36.179), (40, 36.176), (40, 36.174)), ((40, 36.004), (39.99, 35.834), (39.99, 35.664)), ((39.99, 34.718), (39.47, 33.8), (39, 33)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e4', 'e2')
        self.add_contour('c2', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
