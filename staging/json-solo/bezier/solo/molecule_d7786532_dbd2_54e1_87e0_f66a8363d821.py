"""Molecule (science), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd7786532-dbd2-54e1-87e0-f66a8363d821'
SOURCE_PATH = 'icons-json/science/molecule_d7786532-dbd2-54e1-87e0-f66a8363d821.json'
AUTHOR = 'json_to_solo'

class Molecule(Solo48):
    icon_id = 'molecule'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('molecule', 'science')

    def build(self):
        self.add_line('sym-e0', (24, 38), (24, 29))
        self.add_bezier('sym-e1', (24, 29), ((25.448, 27.879), (26.544, 27.105), (28, 26)))
        self.add_bezier('sym-e2', (28, 26), ((29.874, 24.576), (32.01, 23.217), (33, 21)))
        self.add_bezier('sym-e3', (33, 21), ((37.205, 22.514), (40.961, 24.304), (42, 29)))
        self.add_bezier('sym-e4', (42, 29), ((42, 29.671), (42, 30.305), (42, 31)))
        self.add_bezier('sym-e5', (42, 31), ((42, 31.041), (41.992, 30.951), (42, 31)))
        self.add_bezier('sym-e6', (42, 31), ((42, 31.213), (42, 31.787), (42, 32)))
        self.add_bezier('sym-e7', (42, 32), ((42, 37.335), (37.474, 42), (32, 42)))
        self.add_bezier('sym-e8', (32, 42), ((31.689, 42), (31.311, 42), (31, 42)))
        self.add_bezier('sym-e9', (31, 42), ((27.678, 42), (26.152, 40.185), (24, 38)))
        self.add_bezier('sym-e10', (24, 38), ((21.848, 40.185), (20.322, 42), (17, 42)))
        self.add_bezier('sym-e11', (17, 42), ((16.689, 42), (16.311, 42), (16, 42)))
        self.add_bezier('sym-e12', (16, 42), ((10.526, 42), (6, 37.335), (6, 32)))
        self.add_bezier('sym-e13', (6, 32), ((6, 31.787), (6, 31.213), (6, 31)))
        self.add_bezier('sym-e14', (6, 31), ((6.008, 30.951), (6, 31.041), (6, 31)))
        self.add_bezier('sym-e15', (6, 31), ((6, 30.305), (6, 29.671), (6, 29)))
        self.add_bezier('sym-e16', (6, 29), ((7.039, 24.304), (10.795, 22.514), (15, 21)))
        self.add_bezier('sym-e17', (15, 21), ((15.99, 23.217), (18.126, 24.576), (20, 26)))
        self.add_bezier('sym-e18', (20, 26), ((21.456, 27.105), (22.552, 27.879), (24, 29)))
        self.add_bezier('sym-e19', (33, 21), ((35.16, 16.165), (33.574, 9.692), (29, 7)))
        self.add_bezier('sym-e20', (29, 7), ((27.642, 6.198), (25.595, 6), (24, 6)))
        self.add_bezier('sym-e21', (24, 6), ((23.943, 6), (24.057, 6), (24, 6)))
        self.add_bezier('sym-e22', (24, 6), ((23.978, 6), (24.022, 6), (24, 6)))
        self.add_bezier('sym-e23', (24, 6), ((23.989, 6), (24.011, 6), (24, 6)))
        self.add_bezier('sym-e24', (24, 6), ((23.989, 6), (24.011, 6), (24, 6)))
        self.add_bezier('sym-e25', (24, 6), ((23.978, 6), (24.022, 6), (24, 6)))
        self.add_bezier('sym-e26', (24, 6), ((23.943, 6), (24.057, 6), (24, 6)))
        self.add_bezier('sym-e27', (24, 6), ((22.405, 6), (20.358, 6.198), (19, 7)))
        self.add_bezier('sym-e28', (19, 7), ((14.426, 9.692), (12.84, 16.165), (15, 21)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18')
        self.add_contour('sym-c1', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
