"""Molecule (science), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd7786532-dbd2-54e1-87e0-f66a8363d821'
SOURCE_PATH = 'icons-json/science/molecule_d7786532-dbd2-54e1-87e0-f66a8363d821.json'
AUTHOR = 'json_to_solo'

class MoleculeD7786532(Solo48):
    icon_id = 'molecule-d7786532'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('molecule', 'science')

    def build(self):
        self.add_line('sym-e0', (24, 38), (24, 29))
        self.add_line('sym-e1', (24, 29), (28, 26))
        self.add_line('sym-e2', (28, 26), (33, 21))
        self.add_arc('sym-e3', (33, 21), (42, 29), radius_x=11)
        self.add_line('sym-e4', (42, 29), (42, 31))
        self.add_line('sym-e6', (42, 31), (42, 32))
        self.add_arc('sym-e7', (42, 32), (32, 42), radius_x=10)
        self.add_line('sym-e8', (32, 42), (31, 42))
        self.add_arc('sym-e9', (31, 42), (24, 38), radius_x=9)
        self.add_arc('sym-e10', (24, 38), (17, 42), radius_x=9)
        self.add_line('sym-e11', (17, 42), (16, 42))
        self.add_arc('sym-e12', (16, 42), (6, 32), radius_x=10)
        self.add_line('sym-e13', (6, 32), (6, 31))
        self.add_line('sym-e15', (6, 31), (6, 29))
        self.add_arc('sym-e16', (6, 29), (15, 21), radius_x=11)
        self.add_line('sym-e17', (15, 21), (20, 26))
        self.add_line('sym-e18', (20, 26), (24, 29))
        self.add_arc('sym-e19', (33, 21), (29, 7), radius_x=11, sweep=False)
        self.add_line('sym-e20', (29, 7), (24, 6))
        self.add_line('sym-e27', (24, 6), (19, 7))
        self.add_arc('sym-e28', (19, 7), (15, 21), radius_x=11, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18')
        self.add_contour('sym-c1', 'sym-e19', 'sym-e20', 'sym-e27', 'sym-e28')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
