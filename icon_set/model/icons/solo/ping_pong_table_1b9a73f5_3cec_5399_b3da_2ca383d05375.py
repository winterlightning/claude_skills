"""Ping pong table (sports), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1b9a73f5-3cec-5399-b3da-2ca383d05375'
SOURCE_PATH = 'icons-json/sports/ping pong table_1b9a73f5-3cec-5399-b3da-2ca383d05375.json'
AUTHOR = 'json_to_solo'

class PingPongTable(Solo48):
    icon_id = 'ping-pong-table'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('ping', 'pong', 'table', 'sports')

    def build(self):
        self.add_line('e0', (43, 19), (5, 19))
        self.add_line('e1', (24, 8), (24, 30))
        self.add_line('e2', (8, 40), (8, 30))
        self.add_line('e3', (40, 40), (40, 30))
        self.add_line('e4', (44, 30), (4, 30))
        self.add_line('e5', (4, 30), (6, 8))
        self.add_line('e6', (6, 8), (42, 8))
        self.add_line('e7', (42, 8), (44, 30))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e5', 'e6', 'e7', closed=True)
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
