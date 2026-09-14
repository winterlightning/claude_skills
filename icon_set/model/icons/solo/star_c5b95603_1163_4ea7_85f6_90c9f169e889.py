"""Star (holidays), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c5b95603-1163-4ea7-85f6-90c9f169e889'
SOURCE_PATH = 'icons-json/holidays/star_c5b95603-1163-4ea7-85f6-90c9f169e889.json'
AUTHOR = 'json_to_solo'

class StarHolidays(Solo48):
    icon_id = 'star-holidays'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    aliases = ()
    keywords = ('star', 'holidays')

    def build(self):
        self.add_line('e0', (29, 19), (24, 6))
        self.add_line('e1', (24, 6), (19, 19))
        self.add_line('e2', (19, 19), (6, 19))
        self.add_line('e3', (6, 19), (17, 28))
        self.add_line('e4', (17, 28), (13, 42))
        self.add_line('e5', (13, 42), (24, 34))
        self.add_line('e6', (24, 34), (35, 42))
        self.add_line('e7', (35, 42), (31, 28))
        self.add_line('e8', (31, 28), (42, 19))
        self.add_line('e9', (42, 19), (29, 19))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', closed=True)
