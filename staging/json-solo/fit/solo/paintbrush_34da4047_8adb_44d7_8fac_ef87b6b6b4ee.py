"""Paintbrush (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '34da4047-8adb-44d7-8fac-ef87b6b6b4ee'
SOURCE_PATH = 'icons-json/symbol/paintbrush_34da4047-8adb-44d7-8fac-ef87b6b6b4ee.json'
AUTHOR = 'json_to_solo'

class Paintbrush34da4047(Solo48):
    icon_id = 'paintbrush-34da4047'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('paintbrush', 'symbol')

    def build(self):
        self.add_line('e0', (11, 33), (10, 37))
        self.add_line('e1', (19, 29), (20, 31))
        self.add_line('e2', (20, 22), (39, 6))
        self.add_line('e3', (42, 9), (27, 30))
        self.add_arc('e4', (19, 29), (11, 33), radius_x=5, sweep=False)
        self.add_arc('e5-1', (10, 37), (6, 41), radius_x=7)
        self.add_line('e5-2', (6, 41), (11, 42))
        self.add_arc('e5-3', (11, 42), (20, 37), radius_x=11, sweep=False)
        self.add_arc('e5-4', (20, 37), (20, 31), radius_x=7, sweep=False)
        self.add_arc('e6', (19, 29), (20, 22), radius_x=5)
        self.add_arc('e7', (39, 6), (42, 9), radius_x=3)
        self.add_arc('e8', (27, 30), (20, 31), radius_x=6)
        self.add_contour('c0', 'e4', 'e0', 'e5-1', 'e5-2', 'e5-3', 'e5-4')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e6', 'e2', 'e7', 'e3', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
