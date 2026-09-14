"""Batch-06/astrology saturn (culture), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '235ce74c-a58a-5d23-8b5c-93f02e58c975'
SOURCE_PATH = 'icons-json/culture/batch-06/astrology saturn_235ce74c-a58a-5d23-8b5c-93f02e58c975.json'
AUTHOR = 'json_to_solo'

class Batch06AstrologySaturn(Solo48):
    icon_id = 'batch-06-astrology-saturn'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('batch', 'astrology', 'saturn', 'culture')

    def build(self):
        self.add_line('e0', (17, 21), (17, 4))
        self.add_line('e1', (8, 10), (29, 10))
        self.add_arc('e2-1', (19, 44), (34, 38), radius_x=28, sweep=False)
        self.add_arc('e2-2', (34, 38), (40, 26), radius_x=15, sweep=False)
        self.add_arc('e2-3', (40, 26), (33, 18), radius_x=9, sweep=False)
        self.add_arc('e2-4', (33, 18), (17, 21), radius_x=20, sweep=False)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e0')
        self.add_contour('c1', 'e1')
