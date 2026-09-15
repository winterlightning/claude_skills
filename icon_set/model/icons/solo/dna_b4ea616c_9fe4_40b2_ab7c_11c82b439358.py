"""Dna (artificial-intelligence), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b4ea616c-9fe4-40b2-ab7c-11c82b439358'
SOURCE_PATH = 'icons-json/artificial-intelligence/dna_b4ea616c-9fe4-40b2-ab7c-11c82b439358.json'
AUTHOR = 'gpt-6'

class Dna(Solo48):
    icon_id = 'dna'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('dna', 'artificial-intelligence')

    def build(self):
        self.add_line('sym-e0', (8, 40), (40, 40))
        self.add_line('sym-e1', (40, 40), (39, 37))
        self.add_arc('sym-e2', (39, 37), (33, 29), radius_x=27, radius_y=27, large_arc=False, sweep=False)
        self.add_arc('sym-e3', (33, 29), (30, 27), radius_x=17, radius_y=17, large_arc=False, sweep=False)
        self.add_line('sym-e4', (30, 27), (24, 23))
        self.add_line('sym-e5', (24, 23), (25, 22))
        self.add_arc('sym-e6', (25, 22), (29, 20), radius_x=40, radius_y=40, large_arc=False, sweep=True)
        self.add_arc('sym-e7', (29, 20), (39, 9), radius_x=21, radius_y=21, large_arc=False, sweep=False)
        self.add_line('sym-e8', (39, 9), (9, 9))
        self.add_arc('sym-e9', (9, 9), (19, 20), radius_x=21, radius_y=21, large_arc=False, sweep=False)
        self.add_arc('sym-e10', (19, 20), (23, 22), radius_x=40, radius_y=40, large_arc=False, sweep=True)
        self.add_line('sym-e11', (23, 22), (24, 23))
        self.add_line('sym-e12', (24, 23), (18, 27))
        self.add_arc('sym-e13', (18, 27), (15, 29), radius_x=17, radius_y=17, large_arc=False, sweep=False)
        self.add_arc('sym-e14', (15, 29), (9, 37), radius_x=27, radius_y=27, large_arc=False, sweep=False)
        self.add_line('sym-e15', (9, 37), (8, 40))
        self.add_line('sym-e16-1', (8, 40), (8, 44))
        self.add_arc('sym-e17', (40, 40), (40, 44), radius_x=43, radius_y=43, large_arc=False, sweep=False)
        self.add_line('sym-e18', (39, 9), (40, 4))
        self.add_line('sym-e21', (9, 9), (8, 4))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16-1', closed=False)
        self.add_contour('sym-c1', 'sym-e17', closed=False)
        self.add_contour('sym-c2', 'sym-e18', closed=False)
        self.add_contour('sym-c3', 'sym-e21', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
