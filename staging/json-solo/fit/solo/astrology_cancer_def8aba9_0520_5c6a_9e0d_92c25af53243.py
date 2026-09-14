"""Batch-05/astrology cancer (culture), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'def8aba9-0520-5c6a-9e0d-92c25af53243'
SOURCE_PATH = 'icons-json/culture/batch-05/astrology cancer_def8aba9-0520-5c6a-9e0d-92c25af53243.json'
AUTHOR = 'json_to_solo'

class Batch05AstrologyCancer(Solo48):
    icon_id = 'batch-05-astrology-cancer'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('batch', 'astrology', 'cancer', 'culture')

    def build(self):
        self.add_line('e0', (32, 17), (31, 21))
        self.add_line('e1', (8, 22), (40, 22))
        self.add_arc('e2-1', (6, 6), (16, 17), radius_x=14)
        self.add_arc('e2-2', (16, 17), (7, 42), radius_x=21)
        self.add_arc('e3', (42, 6), (32, 17), radius_x=14, sweep=False)
        self.add_arc('e4', (31, 21), (41, 42), radius_x=20, sweep=False)
        self.add_contour('c0', 'e2-1', 'e2-2')
        self.add_contour('c1', 'e3', 'e0', 'e4')
        self.add_contour('c2', 'e1')
