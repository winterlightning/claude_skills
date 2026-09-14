"""Dna (artificial-intelligence), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c3ad20f0-3e47-4b9f-8ec6-40806e89dc7f'
SOURCE_PATH = 'icons-json/artificial-intelligence/dna_c3ad20f0-3e47-4b9f-8ec6-40806e89dc7f.json'
AUTHOR = 'json_to_solo'

class DnaArtificialIntelligence(Solo48):
    icon_id = 'dna-artificial-intelligence'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('dna', 'artificial-intelligence')

    def build(self):
        self.add_line('e0', (29, 16), (30, 17))
        self.add_line('e1', (30, 17), (26, 17))
        self.add_line('e2', (17, 25), (18, 34))
        self.add_line('e3', (35, 18), (30, 18))
        self.add_arc('e4', (31, 6), (29, 16), radius_x=10, sweep=False)
        self.add_arc('e5', (26, 17), (17, 25), radius_x=8, sweep=False)
        self.add_arc('e6', (18, 34), (16, 42), radius_x=9)
        self.add_arc('e7', (42, 15), (35, 18), radius_x=9)
        self.add_arc('e8-1', (30, 18), (28, 29), radius_x=11)
        self.add_arc('e8-2', (28, 29), (26, 30), radius_x=6)
        self.add_line('e8-3', (26, 30), (23, 31))
        self.add_arc('e8-4', (23, 31), (10, 30), radius_x=39, sweep=False)
        self.add_arc('e8-5', (10, 30), (6, 32), radius_x=8, sweep=False)
        self.add_contour('c0', 'e4', 'e0', 'e1', 'e5', 'e2', 'e6')
        self.add_contour('c1', 'e7', 'e3', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e8-5')
