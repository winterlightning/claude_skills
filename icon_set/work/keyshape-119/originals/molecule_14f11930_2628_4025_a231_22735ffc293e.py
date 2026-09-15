"""Molecule (science), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '14f11930-2628-4025-a231-22735ffc293e'
SOURCE_PATH = 'icons-json/science/molecule_14f11930-2628-4025-a231-22735ffc293e.json'
AUTHOR = 'json_to_solo'

class MoleculeScience(Solo48):
    icon_id = 'molecule-science'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('molecule', 'science')

    def build(self):
        self.add_arc('sym-e0', (19, 13), (29, 13), radius_x=5)
        self.add_arc('sym-e1', (29, 13), (19, 13), radius_x=5)
        self.add_arc('sym-e2', (33, 35), (44, 35), radius_x=5)
        self.add_arc('sym-e3', (44, 35), (33, 35), radius_x=5)
        self.add_arc('sym-e4', (15, 35), (4, 35), radius_x=5, sweep=False)
        self.add_arc('sym-e5', (4, 35), (15, 35), radius_x=5, sweep=False)
        self.add_line('sym-e6', (33, 35), (15, 35))
        self.add_line('sym-e7', (38, 30), (28, 17))
        self.add_line('sym-e8', (10, 30), (20, 17))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', closed=True)
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', closed=True)
        self.add_contour('sym-c3', 'sym-e6')
        self.add_contour('sym-c4', 'sym-e7')
        self.add_contour('sym-c5', 'sym-e8')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c5')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c5')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
