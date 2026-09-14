"""Seat settings (wayfinding), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '07eded86-d9a7-4839-86f2-fdaf9ec4dd8c'
SOURCE_PATH = 'icons-json/wayfinding/seat settings_07eded86-d9a7-4839-86f2-fdaf9ec4dd8c.json'
AUTHOR = 'json_to_solo'

class SeatSettingsWayfinding(Solo48):
    icon_id = 'seat-settings-wayfinding'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('seat', 'settings', 'wayfinding')

    def build(self):
        self.add_line('e0', (42, 23), (35, 16))
        self.add_line('e1', (32, 22), (35, 16))
        self.add_line('e2', (35, 16), (40, 13))
        self.add_line('e3', (40, 13), (29, 8))
        self.add_line('e4', (27, 8), (32, 22))
        self.add_line('e5', (17, 34), (17, 26))
        self.add_line('e6', (17, 16), (15, 8))
        self.add_line('e7', (13, 6), (8, 6))
        self.add_line('e8', (11, 42), (35, 42))
        self.add_arc('e9', (29, 8), (27, 8), radius_x=51)
        self.add_line('e10', (17, 26), (17, 16))
        self.add_line('e11', (15, 8), (13, 6))
        self.add_arc('e12-1', (8, 6), (6, 8), radius_x=2, sweep=False)
        self.add_line('e12-2', (6, 8), (8, 39))
        self.add_arc('e12-3', (8, 39), (9, 41), radius_x=4, sweep=False)
        self.add_arc('e12-4', (9, 41), (11, 42), radius_x=3, sweep=False)
        self.add_arc('e13-1', (35, 42), (39, 37), radius_x=5, sweep=False)
        self.add_arc('e13-2', (39, 37), (37, 32), radius_x=4, sweep=False)
        self.add_line('e13-3', (37, 32), (17, 34))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', 'e9', 'e4', closed=True)
        self.add_contour('c2', 'e5', 'e10', 'e6', 'e11', 'e7', 'e12-1', 'e12-2', 'e12-3', 'e12-4', 'e8', 'e13-1', 'e13-2', 'e13-3', closed=True)
        self.relate('connect', 'c0', 'c1')
