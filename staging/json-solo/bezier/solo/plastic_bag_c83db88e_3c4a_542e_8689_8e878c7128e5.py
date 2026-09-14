"""Plastic bag (ecology), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c83db88e-3c4a-542e-8689-8e878c7128e5'
SOURCE_PATH = 'icons-json/ecology/plastic bag_c83db88e-3c4a-542e-8689-8e878c7128e5.json'
AUTHOR = 'json_to_solo'

class PlasticBagEcology(Solo48):
    icon_id = 'plastic-bag-ecology'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'ecology'
    aliases = ()
    keywords = ('plastic', 'bag', 'ecology')

    def build(self):
        self.add_line('sym-e0', (29, 17), (24, 17))
        self.add_line('sym-e1', (24, 17), (19, 17))
        self.add_bezier('sym-e2', (19, 17), ((18.002, 16.624), (17.466, 16.039), (17, 15)))
        self.add_bezier('sym-e3', (17, 15), ((16.91, 14.804), (17, 14.221), (17, 14)))
        self.add_line('sym-e4', (17, 14), (17, 8))
        self.add_bezier('sym-e5', (17, 8), ((17, 6.846), (15.211, 6), (14, 6)))
        self.add_bezier('sym-e6', (14, 6), ((13.902, 6), (14.098, 6.008), (14, 6)))
        self.add_line('sym-e7', (14, 6), (10, 6))
        self.add_bezier('sym-e8', (10, 6), ((8.715, 6), (8.09, 7.01), (8, 8)))
        self.add_line('sym-e9', (8, 8), (6, 35))
        self.add_bezier('sym-e10', (6, 35), ((6, 35.949), (6, 37.051), (6, 38)))
        self.add_bezier('sym-e11', (6, 38), ((6, 40.045), (8.036, 42), (10, 42)))
        self.add_bezier('sym-e12', (10, 42), ((10.065, 42), (9.935, 42), (10, 42)))
        self.add_line('sym-e13', (10, 42), (24, 42))
        self.add_line('sym-e14', (24, 42), (38, 42))
        self.add_bezier('sym-e15', (38, 42), ((38.065, 42), (37.935, 42), (38, 42)))
        self.add_bezier('sym-e16', (38, 42), ((39.964, 42), (42, 40.045), (42, 38)))
        self.add_bezier('sym-e17', (42, 38), ((42, 37.051), (42, 35.949), (42, 35)))
        self.add_line('sym-e18', (42, 35), (40, 8))
        self.add_bezier('sym-e19', (40, 8), ((39.91, 7.01), (39.285, 6), (38, 6)))
        self.add_line('sym-e20', (38, 6), (34, 6))
        self.add_bezier('sym-e21', (34, 6), ((33.902, 6.008), (34.098, 6), (34, 6)))
        self.add_bezier('sym-e22', (34, 6), ((32.789, 6), (31, 6.846), (31, 8)))
        self.add_line('sym-e23', (31, 8), (31, 14))
        self.add_bezier('sym-e24', (31, 14), ((31, 14.221), (31.09, 14.804), (31, 15)))
        self.add_bezier('sym-e25', (31, 15), ((30.534, 16.039), (29.998, 16.624), (29, 17)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', closed=True)
