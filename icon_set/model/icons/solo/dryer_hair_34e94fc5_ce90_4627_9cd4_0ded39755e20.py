"""Dryer hair (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '34e94fc5-ce90-4627-9cd4-0ded39755e20'
SOURCE_PATH = 'icons-json/symbol/dryer hair_34e94fc5-ce90-4627-9cd4-0ded39755e20.json'
AUTHOR = 'json_to_solo'

class DryerHair(Solo48):
    icon_id = 'dryer-hair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('dryer', 'hair', 'symbol')

    def build(self):
        self.add_line('e0', (31, 39), (37, 26))
        self.add_line('e1', (37, 26), (40, 24))
        self.add_line('e2', (29, 6), (6, 9))
        self.add_line('e3', (6, 9), (6, 22))
        self.add_line('e4', (6, 22), (26, 25))
        self.add_line('e5', (26, 28), (22, 40))
        self.add_line('e6-1', (22, 40), (26, 42))
        self.add_arc('e6-2', (26, 42), (31, 39), radius_x=7, sweep=False)
        self.add_line('e7-1', (40, 24), (42, 16))
        self.add_arc('e7-2', (42, 16), (32, 6), radius_x=11, sweep=False)
        self.add_line('e7-3', (32, 6), (29, 6))
        self.add_line('e8', (26, 25), (26, 28))
        self.add_contour('c0', 'e6-1', 'e6-2', 'e0', 'e1', 'e7-1', 'e7-2', 'e7-3', 'e2', 'e3', 'e4', 'e8', 'e5', closed=True)
