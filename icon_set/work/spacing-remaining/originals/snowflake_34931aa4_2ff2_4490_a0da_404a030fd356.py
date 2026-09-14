"""Snowflake (holidays), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '34931aa4-2ff2-4490-a0da-404a030fd356'
SOURCE_PATH = 'icons-json/holidays/snowflake_34931aa4-2ff2-4490-a0da-404a030fd356.json'
AUTHOR = 'json_to_solo'

class SnowflakeHolidays(Solo48):
    icon_id = 'snowflake-holidays'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    aliases = ()
    keywords = ('snowflake', 'holidays')

    def build(self):
        self.add_line('e0', (25, 6), (25, 16))
        self.add_line('e1', (25, 16), (30, 11))
        self.add_line('e2', (18, 11), (25, 17))
        self.add_line('e3', (25, 17), (25, 42))
        self.add_line('e4', (13, 15), (16, 22))
        self.add_line('e5', (16, 22), (25, 26))
        self.add_line('e6', (25, 26), (32, 32))
        self.add_line('e7', (32, 32), (33, 40))
        self.add_line('e8', (6, 18), (16, 22))
        self.add_line('e9', (16, 22), (8, 25))
        self.add_line('e10', (8, 32), (16, 32))
        self.add_line('e11', (16, 32), (9, 39))
        self.add_line('e12', (16, 40), (17, 32))
        self.add_line('e13', (17, 32), (19, 31))
        self.add_line('e14', (33, 22), (37, 14))
        self.add_line('e15', (40, 39), (32, 32))
        self.add_line('e16', (32, 32), (41, 32))
        self.add_line('e17', (41, 25), (33, 22))
        self.add_line('e18', (33, 22), (42, 18))
        self.add_arc('e19', (19, 31), (33, 22), radius_x=70)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3')
        self.add_contour('c2', 'e4', 'e5', 'e6', 'e7')
        self.add_contour('c3', 'e8', 'e9')
        self.add_contour('c4', 'e10', 'e11')
        self.add_contour('c5', 'e12', 'e13', 'e19', 'e14')
        self.add_contour('c6', 'e15', 'e16')
        self.add_contour('c7', 'e17', 'e18')
        self.relate('connect', 'c2', 'c1')
