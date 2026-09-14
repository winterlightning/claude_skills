"""Fly (animals), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c154bd5e-85cc-4682-977f-bac1bfee4f64'
SOURCE_PATH = 'icons-json/animals/fly_c154bd5e-85cc-4682-977f-bac1bfee4f64.json'
AUTHOR = 'json_to_solo'

class Fly(Solo48):
    icon_id = 'fly'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('fly', 'animals')

    def build(self):
        self.add_line('sym-e0', (24, 40), (29, 40))
        self.add_line('sym-e1', (29, 40), (32, 31))
        self.add_line('sym-e2', (32, 31), (40, 34))
        self.add_line('sym-e3', (40, 34), (42, 33))
        self.add_arc('sym-e4', (42, 33), (44, 29), radius_x=6, sweep=False)
        self.add_arc('sym-e7', (44, 29), (42, 25), radius_x=5, sweep=False)
        self.add_line('sym-e8', (42, 25), (24, 8))
        self.add_line('sym-e9', (24, 8), (6, 25))
        self.add_arc('sym-e10', (6, 25), (4, 29), radius_x=5, sweep=False)
        self.add_arc('sym-e13', (4, 29), (6, 33), radius_x=6, sweep=False)
        self.add_line('sym-e14', (6, 33), (8, 34))
        self.add_line('sym-e15', (8, 34), (16, 31))
        self.add_line('sym-e16', (16, 31), (19, 40))
        self.add_line('sym-e17', (19, 40), (24, 40))
        self.add_line('sym-e18', (32, 31), (24, 29))
        self.add_line('sym-e19', (24, 29), (16, 31))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
        self.add_contour('sym-c1', 'sym-e18', 'sym-e19')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
