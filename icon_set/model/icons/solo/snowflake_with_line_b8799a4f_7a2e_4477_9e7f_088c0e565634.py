"""Snowflake with line (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8799a4f-7a2e-4477-9e7f-088c0e565634'
SOURCE_PATH = 'icons-json/symbol/snowflake with line_b8799a4f-7a2e-4477-9e7f-088c0e565634.json'
AUTHOR = 'json_to_solo'

class SnowflakeWithLine(Solo48):
    icon_id = 'snowflake-with-line'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('snowflake', 'with', 'line', 'symbol')

    def build(self):
        self.add_line('e0', (24, 6), (24, 13))
        self.add_line('e1', (19, 9), (24, 13))
        self.add_line('e2', (24, 13), (24, 42))
        self.add_line('e3', (24, 13), (29, 9))
        self.add_line('e4', (35, 24), (6, 24))
        self.add_line('e5', (35, 24), (39, 28))
        self.add_line('e6', (35, 24), (39, 19))
        self.add_line('e7', (9, 19), (13, 24))
        self.add_line('e8', (9, 28), (13, 24))
        self.add_line('e9', (19, 39), (24, 35))
        self.add_line('e10', (24, 35), (29, 39))
        self.add_line('e11', (35, 24), (42, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7')
        self.add_contour('c8', 'e8')
        self.add_contour('c9', 'e9', 'e10')
        self.add_contour('c10', 'e11')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c7', 'c4')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c8', 'c4')
        self.relate('connect', 'c9', 'c2')
