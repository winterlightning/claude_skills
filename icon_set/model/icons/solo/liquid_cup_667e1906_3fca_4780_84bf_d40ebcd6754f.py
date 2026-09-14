"""Liquid cup (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '667e1906-3fca-4780-84bf-d40ebcd6754f'
SOURCE_PATH = 'icons-json/symbol/liquid cup_667e1906-3fca-4780-84bf-d40ebcd6754f.json'
AUTHOR = 'json_to_solo'

class LiquidCup(Solo48):
    icon_id = 'liquid-cup'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('liquid', 'cup', 'symbol')

    def build(self):
        self.add_line('e0', (21, 22), (29, 24))
        self.add_line('e1', (8, 23), (9, 37))
        self.add_line('e2', (14, 42), (34, 42))
        self.add_line('e3', (39, 38), (40, 23))
        self.add_line('e4', (8, 23), (6, 6))
        self.add_line('e5', (6, 6), (42, 6))
        self.add_line('e6', (42, 6), (40, 23))
        self.add_arc('e7', (8, 23), (21, 22), radius_x=20)
        self.add_arc('e8', (29, 24), (40, 23), radius_x=23, sweep=False)
        self.add_arc('e9', (9, 37), (14, 42), radius_x=6, sweep=False)
        self.add_arc('e10', (34, 42), (39, 38), radius_x=6, sweep=False)
        self.add_contour('c0', 'e7', 'e0', 'e8')
        self.add_contour('c1', 'e1', 'e9', 'e2', 'e10', 'e3')
        self.add_contour('c2', 'e4', 'e5', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
