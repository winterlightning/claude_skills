"""Arrow thick 3 top right (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8fad2e27-b997-5300-b5e0-5c6556df18a6'
SOURCE_PATH = 'icons-json/arrows/arrow thick 3 top right_8fad2e27-b997-5300-b5e0-5c6556df18a6.json'
AUTHOR = 'json_to_solo'

class ArrowThick3TopRight(Solo48):
    icon_id = 'arrow-thick-3-top-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'top', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (13, 40), (33, 22))
        self.add_line('e1', (33, 22), (33, 36))
        self.add_line('e2', (42, 36), (42, 6))
        self.add_line('e3', (42, 6), (14, 6))
        self.add_line('e4', (12, 15), (27, 15))
        self.add_line('e5', (27, 15), (8, 34))
        self.add_arc('e6-1', (8, 34), (6, 37), radius_x=4, sweep=False)
        self.add_arc('e6-2', (6, 37), (7, 40), radius_x=5, sweep=False)
        self.add_arc('e6-3', (7, 40), (10, 42), radius_x=4, sweep=False)
        self.add_arc('e6-4', (10, 42), (13, 40), radius_x=5, sweep=False)
        self.add_arc('e7-1', (33, 36), (34, 40), radius_x=5, sweep=False)
        self.add_line('e7-2', (34, 40), (38, 42))
        self.add_line('e7-3', (38, 42), (41, 40))
        self.add_line('e7-4', (41, 40), (42, 36))
        self.add_line('e8-1', (14, 6), (8, 7))
        self.add_line('e8-2', (8, 7), (6, 10))
        self.add_arc('e8-3', (6, 10), (12, 15), radius_x=6, sweep=False)
        self.add_contour('c0', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e0', 'e1', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e2', 'e3', 'e8-1', 'e8-2', 'e8-3', 'e4', 'e5', closed=True)
