"""Batch-06/necklace with pearl (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1abfa79e-18a0-4f01-b0ce-90b012a88a6a'
SOURCE_PATH = 'icons-json/accessories/batch-06/necklace with pearl_1abfa79e-18a0-4f01-b0ce-90b012a88a6a.json'
AUTHOR = 'json_to_solo'

class Batch06NecklaceWithPearl(Solo48):
    icon_id = 'batch-06-necklace-with-pearl'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'necklace', 'with', 'pearl', 'accessories')

    def build(self):
        self.add_arc('sym-e0', (19, 39), (29, 39), radius_x=5)
        self.add_arc('sym-e1', (29, 39), (19, 39), radius_x=5)
        self.add_bezier('sym-e2', (21, 34), ((16.697, 30.818), (13.149, 28.691), (10, 24)))
        self.add_bezier('sym-e3', (10, 24), ((11.752, 21.327), (13.389, 18.755), (16, 17)))
        self.add_bezier('sym-e4', (16, 17), ((18.42, 15.375), (21.13, 15), (24, 15)))
        self.add_bezier('sym-e5', (24, 15), ((26.87, 15), (29.58, 15.375), (32, 17)))
        self.add_bezier('sym-e6', (32, 17), ((34.611, 18.755), (36.248, 21.327), (38, 24)))
        self.add_bezier('sym-e7', (38, 24), ((34.851, 28.691), (31.303, 30.818), (27, 34)))
        self.add_bezier('sym-e8', (10, 24), ((9.141, 22.036), (8, 20.218), (8, 18)))
        self.add_bezier('sym-e9', (8, 18), ((8, 17.718), (8, 17.291), (8, 17)))
        self.add_bezier('sym-e10', (8, 17), ((8, 16.791), (8, 16.218), (8, 16)))
        self.add_bezier('sym-e11', (8, 16), ((8, 7.127), (16.027, 4), (23, 4)))
        self.add_bezier('sym-e12', (23, 4), ((23.126, 4), (23.874, 4), (24, 4)))
        self.add_bezier('sym-e13', (24, 4), ((24.098, 4), (23.902, 4), (24, 4)))
        self.add_bezier('sym-e14', (24, 4), ((24.098, 4), (23.902, 4), (24, 4)))
        self.add_bezier('sym-e15', (24, 4), ((24.126, 4), (24.874, 4), (25, 4)))
        self.add_bezier('sym-e16', (25, 4), ((31.973, 4), (40, 7.127), (40, 16)))
        self.add_bezier('sym-e17', (40, 16), ((40, 16.218), (40, 16.791), (40, 17)))
        self.add_bezier('sym-e18', (40, 17), ((40, 17.291), (40, 17.718), (40, 18)))
        self.add_bezier('sym-e19', (40, 18), ((40, 20.218), (38.859, 22.036), (38, 24)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c2', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
