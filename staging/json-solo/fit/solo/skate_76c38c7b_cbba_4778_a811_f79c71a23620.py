"""Skate (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '76c38c7b-cbba-4778-a811-f79c71a23620'
SOURCE_PATH = 'icons-json/symbol/skate_76c38c7b-cbba-4778-a811-f79c71a23620.json'
AUTHOR = 'json_to_solo'

class SkateSymbol(Solo48):
    icon_id = 'skate-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('skate', 'symbol')

    def build(self):
        self.add_line('e0', (12, 24), (38, 24))
        self.add_arc('e1', (4, 8), (12, 24), radius_x=24, sweep=False)
        self.add_arc('e2-1', (38, 24), (41, 22), radius_x=3, sweep=False)
        self.add_arc('e2-2', (41, 22), (44, 13), radius_x=22, sweep=False)
        self.add_dot('e3', (13, 40))
        self.add_dot('e4', (34, 40))
        self.add_contour('c0', 'e1', 'e0', 'e2-1', 'e2-2')
