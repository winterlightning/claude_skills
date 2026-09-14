"""Holi color (holidays), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '99bb91be-d96c-4254-9c63-821b30541452'
SOURCE_PATH = 'icons-json/holidays/holi color_99bb91be-d96c-4254-9c63-821b30541452.json'
AUTHOR = 'json_to_solo'

class HoliColorHolidays(Solo48):
    icon_id = 'holi-color-holidays'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    aliases = ()
    keywords = ('holi', 'color', 'holidays')

    def build(self):
        self.add_line('e0', (13, 19), (11, 14))
        self.add_line('e1', (21, 9), (23, 14))
        self.add_line('e2', (37, 31), (34, 31))
        self.add_arc('e3-1', (11, 14), (16, 6), radius_x=6)
        self.add_arc('e3-2', (16, 6), (21, 9), radius_x=6)
        self.add_arc('e4-1', (23, 14), (25, 15), radius_x=2, sweep=False)
        self.add_arc('e4-2', (25, 15), (32, 12), radius_x=5)
        self.add_arc('e4-3', (32, 12), (33, 14), radius_x=4)
        self.add_line('e4-4', (33, 14), (33, 19))
        self.add_arc('e4-5', (33, 19), (42, 24), radius_x=7)
        self.add_line('e4-6', (42, 24), (41, 28))
        self.add_line('e4-7', (41, 28), (37, 31))
        self.add_arc('e5-1', (34, 31), (32, 32), radius_x=2, sweep=False)
        self.add_arc('e5-2', (32, 32), (34, 38), radius_x=8)
        self.add_arc('e5-3', (34, 38), (30, 41), radius_x=4)
        self.add_arc('e5-4', (30, 41), (27, 40), radius_x=4)
        self.add_line('e5-5', (27, 40), (25, 36))
        self.add_arc('e5-6', (25, 36), (24, 36), radius_x=1)
        self.add_arc('e5-7', (24, 36), (18, 42), radius_x=8)
        self.add_line('e5-8', (18, 42), (16, 42))
        self.add_arc('e5-9', (16, 42), (13, 39), radius_x=5)
        self.add_arc('e5-10', (13, 39), (13, 35), radius_x=5)
        self.add_arc('e5-11', (13, 35), (14, 31), radius_x=6, sweep=False)
        self.add_arc('e5-12', (14, 31), (10, 30), radius_x=3, sweep=False)
        self.add_arc('e5-13', (10, 30), (6, 26), radius_x=4)
        self.add_line('e5-14', (6, 26), (7, 23))
        self.add_line('e5-15', (7, 23), (13, 21))
        self.add_arc('e5-16', (13, 21), (13, 19), radius_x=2, sweep=False)
        self.add_contour('c0', 'e0', 'e3-1', 'e3-2', 'e1', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e4-5', 'e4-6', 'e4-7', 'e2', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7', 'e5-8', 'e5-9', 'e5-10', 'e5-11', 'e5-12', 'e5-13', 'e5-14', 'e5-15', 'e5-16', closed=True)
