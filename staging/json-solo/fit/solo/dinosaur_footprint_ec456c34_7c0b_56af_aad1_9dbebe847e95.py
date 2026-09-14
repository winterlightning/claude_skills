"""Dinosaur footprint (animals), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ec456c34-7c0b-56af-aad1-9dbebe847e95'
SOURCE_PATH = 'icons-json/animals/dinosaur footprint_ec456c34-7c0b-56af-aad1-9dbebe847e95.json'
AUTHOR = 'json_to_solo'

class DinosaurFootprintAnimals(Solo48):
    icon_id = 'dinosaur-footprint-animals'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('dinosaur', 'footprint', 'animals')

    def build(self):
        self.add_arc('sym-e1', (24, 44), (32, 40), radius_x=10, sweep=False)
        self.add_line('sym-e2', (32, 40), (33, 38))
        self.add_line('sym-e3', (33, 38), (35, 31))
        self.add_line('sym-e4', (35, 31), (38, 25))
        self.add_arc('sym-e5', (38, 25), (40, 18), radius_x=17, sweep=False)
        self.add_arc('sym-e6', (40, 18), (40, 17), radius_x=23)
        self.add_line('sym-e8', (40, 17), (39, 12))
        self.add_arc('sym-e9', (39, 12), (37, 13), radius_x=21)
        self.add_line('sym-e10', (37, 13), (32, 19))
        self.add_line('sym-e11', (32, 19), (30, 24))
        self.add_line('sym-e12', (30, 24), (28, 20))
        self.add_line('sym-e13', (28, 20), (28, 16))
        self.add_arc('sym-e14', (28, 16), (26, 6), radius_x=18, sweep=False)
        self.add_arc('sym-e15', (26, 6), (24, 4), radius_x=19, sweep=False)
        self.add_arc('sym-e16', (24, 4), (22, 6), radius_x=19, sweep=False)
        self.add_arc('sym-e17', (22, 6), (20, 16), radius_x=18, sweep=False)
        self.add_line('sym-e18', (20, 16), (20, 20))
        self.add_line('sym-e19', (20, 20), (18, 24))
        self.add_line('sym-e20', (18, 24), (16, 19))
        self.add_line('sym-e21', (16, 19), (11, 13))
        self.add_arc('sym-e22', (11, 13), (9, 12), radius_x=21)
        self.add_line('sym-e23', (9, 12), (8, 17))
        self.add_line('sym-e25', (8, 17), (8, 18))
        self.add_arc('sym-e26', (8, 18), (10, 25), radius_x=18, sweep=False)
        self.add_line('sym-e27', (10, 25), (13, 31))
        self.add_line('sym-e28', (13, 31), (15, 38))
        self.add_arc('sym-e29', (15, 38), (16, 40), radius_x=6, sweep=False)
        self.add_arc('sym-e30', (16, 40), (24, 44), radius_x=10, sweep=False)
        self.add_contour('sym-c0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', closed=True)
