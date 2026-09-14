"""Oval shape (design), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a601ae14-5727-58ec-8f56-e0bbb59e184e'
SOURCE_PATH = 'icons-json/design/oval shape_a601ae14-5727-58ec-8f56-e0bbb59e184e.json'
AUTHOR = 'json_to_solo'

class OvalShapeDesign(Solo48):
    icon_id = 'oval-shape-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('oval', 'shape', 'design')

    def build(self):
        self.add_bezier('sym-e0', (4, 24), ((4.002, 23.931), (4, 24.071), (4, 24)))
        self.add_bezier('sym-e1', (4, 24), ((4, 15.1), (10.864, 10.43), (18, 9)))
        self.add_bezier('sym-e2', (18, 9), ((19.318, 8.74), (20.645, 8), (22, 8)))
        self.add_bezier('sym-e3', (22, 8), ((22.436, 8), (23.564, 8), (24, 8)))
        self.add_bezier('sym-e4', (24, 8), ((24.052, 8), (23.947, 8), (24, 8)))
        self.add_bezier('sym-e5', (24, 8), ((24.026, 8), (23.974, 8), (24, 8)))
        self.add_bezier('sym-e6', (24, 8), ((24.026, 8), (23.974, 8), (24, 8)))
        self.add_bezier('sym-e7', (24, 8), ((24.053, 8), (23.948, 8), (24, 8)))
        self.add_bezier('sym-e8', (24, 8), ((24.436, 8), (25.564, 8), (26, 8)))
        self.add_bezier('sym-e9', (26, 8), ((27.355, 8), (28.682, 8.74), (30, 9)))
        self.add_bezier('sym-e10', (30, 9), ((37.136, 10.43), (44, 15.1), (44, 24)))
        self.add_bezier('sym-e11', (44, 24), ((44, 24.071), (43.998, 23.931), (44, 24)))
        self.add_bezier('sym-e12', (44, 24), ((43.998, 24.069), (44, 23.929), (44, 24)))
        self.add_bezier('sym-e13', (44, 24), ((44, 32.9), (37.136, 37.57), (30, 39)))
        self.add_bezier('sym-e14', (30, 39), ((28.682, 39.26), (27.355, 40), (26, 40)))
        self.add_bezier('sym-e15', (26, 40), ((25.564, 40), (24.436, 40), (24, 40)))
        self.add_bezier('sym-e16', (24, 40), ((23.948, 40), (24.053, 40), (24, 40)))
        self.add_bezier('sym-e17', (24, 40), ((23.974, 40), (24.026, 40), (24, 40)))
        self.add_bezier('sym-e18', (24, 40), ((23.974, 40), (24.026, 40), (24, 40)))
        self.add_bezier('sym-e19', (24, 40), ((23.947, 40), (24.052, 40), (24, 40)))
        self.add_bezier('sym-e20', (24, 40), ((23.564, 40), (22.436, 40), (22, 40)))
        self.add_bezier('sym-e21', (22, 40), ((20.645, 40), (19.318, 39.26), (18, 39)))
        self.add_bezier('sym-e22', (18, 39), ((10.864, 37.57), (4, 32.9), (4, 24)))
        self.add_bezier('sym-e23', (4, 24), ((4, 23.929), (4.002, 24.069), (4, 24)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', closed=True)
