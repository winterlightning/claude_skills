"""Gift (holidays), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e0615c2-d799-4df4-a1fd-c57312609fdf'
SOURCE_PATH = 'icons-json/holidays/gift_8e0615c2-d799-4df4-a1fd-c57312609fdf.json'
AUTHOR = 'json_to_solo'

class GiftHolidays(Solo48):
    icon_id = 'gift-holidays'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    aliases = ()
    keywords = ('gift', 'holidays')

    def build(self):
        self.add_line('e0', (10, 16), (10, 39))
        self.add_line('e1', (13, 42), (35, 42))
        self.add_line('e2', (38, 32), (38, 16))
        self.add_line('e3', (23, 13), (24, 16))
        self.add_line('e4', (26, 13), (24, 16))
        self.add_line('e5', (6, 16), (42, 16))
        self.add_arc('e6-1', (10, 39), (12, 42), radius_x=3, sweep=False)
        self.add_line('e6-2', (12, 42), (13, 42))
        self.add_line('e7-1', (35, 42), (38, 41))
        self.add_line('e7-2', (38, 41), (38, 32))
        self.add_arc('e8-1', (24, 16), (13, 11), radius_x=12)
        self.add_arc('e8-2', (13, 11), (16, 6), radius_x=4)
        self.add_arc('e8-3', (16, 6), (23, 13), radius_x=8)
        self.add_arc('e9-1', (25, 16), (35, 12), radius_x=15, sweep=False)
        self.add_arc('e9-2', (35, 12), (32, 6), radius_x=4, sweep=False)
        self.add_arc('e9-3', (32, 6), (26, 13), radius_x=9, sweep=False)
        self.add_arc('e10', (24, 16), (26, 16), radius_x=27, sweep=False)
        self.add_contour('c0', 'e0', 'e6-1', 'e6-2', 'e1', 'e7-1', 'e7-2', 'e2')
        self.add_contour('c1', 'e8-1', 'e8-2', 'e8-3', 'e3')
        self.add_contour('c2', 'e9-1', 'e9-2', 'e9-3', 'e4', 'e10')
        self.add_contour('c3', 'e5')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c3')
