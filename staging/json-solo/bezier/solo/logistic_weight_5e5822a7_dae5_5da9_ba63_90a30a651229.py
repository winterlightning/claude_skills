"""Logistic weight (shipping), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5e5822a7-dae5-5da9-ba63-90a30a651229'
SOURCE_PATH = 'icons-json/shipping/logistic weight_5e5822a7-dae5-5da9-ba63-90a30a651229.json'
AUTHOR = 'json_to_solo'

class LogisticWeightShipping(Solo48):
    icon_id = 'logistic-weight-shipping'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    aliases = ()
    keywords = ('logistic', 'weight', 'shipping')

    def build(self):
        self.add_bezier('sym-e0', (28, 14), ((28.368, 13.051), (28.918, 12.031), (29, 11)))
        self.add_bezier('sym-e1', (29, 11), ((29.188, 8.783), (28.062, 6.687), (26, 6)))
        self.add_bezier('sym-e2', (26, 6), ((25.64, 6), (25.376, 6), (25, 6)))
        self.add_bezier('sym-e3', (25, 6), ((24.869, 6), (24.139, 6), (24, 6)))
        self.add_bezier('sym-e4', (24, 6), ((23.953, 6), (24.047, 6), (24, 6)))
        self.add_bezier('sym-e5', (24, 6), ((23.976, 6), (24.024, 6), (24, 6)))
        self.add_bezier('sym-e6', (24, 6), ((23.976, 6), (24.024, 6), (24, 6)))
        self.add_bezier('sym-e7', (24, 6), ((23.953, 6), (24.047, 6), (24, 6)))
        self.add_bezier('sym-e8', (24, 6), ((23.861, 6), (23.131, 6), (23, 6)))
        self.add_bezier('sym-e9', (23, 6), ((22.624, 6), (22.36, 6), (22, 6)))
        self.add_bezier('sym-e10', (22, 6), ((19.938, 6.687), (18.812, 8.783), (19, 11)))
        self.add_bezier('sym-e11', (19, 11), ((19.082, 12.031), (19.632, 13.051), (20, 14)))
        self.add_line('sym-e12', (20, 14), (24, 14))
        self.add_line('sym-e13', (24, 14), (28, 14))
        self.add_line('sym-e14', (28, 14), (34, 14))
        self.add_bezier('sym-e15', (34, 14), ((35.8, 14), (36.64, 15.437), (37, 17)))
        self.add_line('sym-e16', (37, 17), (42, 39))
        self.add_bezier('sym-e17', (42, 39), ((42, 39.417), (42, 39.583), (42, 40)))
        self.add_bezier('sym-e18', (42, 40), ((42, 40.974), (40.884, 42), (40, 42)))
        self.add_line('sym-e19', (40, 42), (24, 42))
        self.add_line('sym-e20', (24, 42), (8, 42))
        self.add_bezier('sym-e21', (8, 42), ((7.116, 42), (6, 40.974), (6, 40)))
        self.add_bezier('sym-e22', (6, 40), ((6, 39.583), (6, 39.417), (6, 39)))
        self.add_line('sym-e23', (6, 39), (11, 17))
        self.add_bezier('sym-e24', (11, 17), ((11.36, 15.437), (12.2, 14), (14, 14)))
        self.add_line('sym-e25', (14, 14), (20, 14))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25')
