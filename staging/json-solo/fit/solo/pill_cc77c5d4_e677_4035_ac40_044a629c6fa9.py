"""Pill (health), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc77c5d4-e677-4035-ac40-044a629c6fa9'
SOURCE_PATH = 'icons-json/health/pill_cc77c5d4-e677-4035-ac40-044a629c6fa9.json'
AUTHOR = 'json_to_solo'

class PillHealth(Solo48):
    icon_id = 'pill-health'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('pill', 'health')

    def build(self):
        self.add_line('e0', (32, 32), (16, 17))
        self.add_line('e1', (25, 40), (38, 26))
        self.add_line('e2', (23, 9), (8, 24))
        self.add_arc('e3-1', (38, 26), (42, 18), radius_x=11, sweep=False)
        self.add_line('e3-2', (42, 18), (40, 11))
        self.add_arc('e3-3', (40, 11), (31, 6), radius_x=12, sweep=False)
        self.add_line('e3-4', (31, 6), (23, 9))
        self.add_line('e4-1', (8, 24), (6, 31))
        self.add_arc('e4-2', (6, 31), (17, 42), radius_x=12, sweep=False)
        self.add_line('e4-3', (17, 42), (25, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e2', 'e4-1', 'e4-2', 'e4-3', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
