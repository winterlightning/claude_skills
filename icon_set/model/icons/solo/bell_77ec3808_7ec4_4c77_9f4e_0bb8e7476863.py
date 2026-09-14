"""Bell (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '77ec3808-7ec4-4c77-9f4e-0bb8e7476863'
SOURCE_PATH = 'icons-json/symbol/bell_77ec3808-7ec4-4c77-9f4e-0bb8e7476863.json'
AUTHOR = 'json_to_solo'

class Bell77ec3808(Solo48):
    icon_id = 'bell-77ec3808'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('bell', 'symbol')

    def build(self):
        self.add_line('e0', (24, 38), (24, 42))
        self.add_line('e1', (6, 38), (42, 38))
        self.add_line('e2', (42, 38), (39, 34))
        self.add_line('e3', (37, 27), (37, 18))
        self.add_line('e4', (11, 19), (11, 26))
        self.add_line('e5', (9, 34), (6, 38))
        self.add_arc('e6', (39, 34), (37, 27), radius_x=13)
        self.add_arc('e7-1', (37, 18), (24, 6), radius_x=14, sweep=False)
        self.add_arc('e7-2', (24, 6), (11, 19), radius_x=14, sweep=False)
        self.add_arc('e8', (11, 26), (9, 34), radius_x=12)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e6', 'e3', 'e7-1', 'e7-2', 'e4', 'e8', 'e5', closed=True)
        self.relate('connect', 'c0', 'c1')
