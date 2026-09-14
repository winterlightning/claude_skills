"""Plastic bag (ecology), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c83db88e-3c4a-542e-8689-8e878c7128e5'
SOURCE_PATH = 'icons-json/ecology/plastic bag_c83db88e-3c4a-542e-8689-8e878c7128e5.json'
AUTHOR = 'json_to_solo'

class PlasticBag(Solo48):
    icon_id = 'plastic-bag'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'ecology'
    aliases = ()
    keywords = ('plastic', 'bag', 'ecology')

    def build(self):
        self.add_line('sym-e0', (29, 17), (24, 17))
        self.add_line('sym-e1', (24, 17), (19, 17))
        self.add_line('sym-e2', (19, 17), (17, 15))
        self.add_line('sym-e3', (17, 15), (17, 14))
        self.add_line('sym-e4', (17, 14), (17, 8))
        self.add_line('sym-e5', (17, 8), (14, 6))
        self.add_line('sym-e7', (14, 6), (10, 6))
        self.add_line('sym-e8', (10, 6), (8, 8))
        self.add_line('sym-e9', (8, 8), (6, 35))
        self.add_line('sym-e10', (6, 35), (6, 38))
        self.add_arc('sym-e11', (6, 38), (10, 42), radius_x=4, sweep=False)
        self.add_line('sym-e13', (10, 42), (24, 42))
        self.add_line('sym-e14', (24, 42), (38, 42))
        self.add_arc('sym-e16', (38, 42), (42, 38), radius_x=4, sweep=False)
        self.add_arc('sym-e17', (42, 38), (42, 35), radius_x=37)
        self.add_line('sym-e18', (42, 35), (40, 8))
        self.add_line('sym-e19', (40, 8), (38, 6))
        self.add_line('sym-e20', (38, 6), (34, 6))
        self.add_line('sym-e22', (34, 6), (31, 8))
        self.add_line('sym-e23', (31, 8), (31, 14))
        self.add_line('sym-e24', (31, 14), (31, 15))
        self.add_line('sym-e25', (31, 15), (29, 17))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e13', 'sym-e14', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', closed=True)
