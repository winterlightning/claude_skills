"""Batch-02/astrology tail node (culture), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '42841092-ec74-56d4-aedd-b98302173838'
SOURCE_PATH = 'icons-json/culture/batch-02/astrology tail node_42841092-ec74-56d4-aedd-b98302173838.json'
AUTHOR = 'json_to_solo'

class Batch02AstrologyTailNode(Solo48):
    icon_id = 'batch-02-astrology-tail-node'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('batch', 'astrology', 'tail', 'node', 'culture')

    def build(self):
        self.add_line('sym-e0', (17, 16), (14, 30))
        self.add_bezier('sym-e1', (14, 30), ((12.74, 35.351), (17.305, 42), (23, 42)))
        self.add_bezier('sym-e2', (23, 42), ((23.188, 42), (23.812, 42), (24, 42)))
        self.add_bezier('sym-e3', (24, 42), ((24.022, 42), (23.978, 42), (24, 42)))
        self.add_bezier('sym-e4', (24, 42), ((24.022, 42), (23.978, 42), (24, 42)))
        self.add_bezier('sym-e5', (24, 42), ((24.188, 42), (24.812, 42), (25, 42)))
        self.add_bezier('sym-e6', (25, 42), ((30.695, 42), (35.26, 35.351), (34, 30)))
        self.add_line('sym-e7', (34, 30), (31, 16))
        self.add_bezier('sym-e8', (31, 16), ((30.059, 12.85), (29.218, 9.258), (32, 7)))
        self.add_bezier('sym-e9', (32, 7), ((32.957, 6.223), (34.748, 6), (36, 6)))
        self.add_bezier('sym-e10', (36, 6), ((36.065, 6), (35.935, 6), (36, 6)))
        self.add_bezier('sym-e11', (36, 6), ((39.191, 6), (42, 8.866), (42, 12)))
        self.add_bezier('sym-e12', (42, 12), ((42, 12.139), (42, 12.861), (42, 13)))
        self.add_bezier('sym-e13', (42, 13), ((42, 13.188), (42, 12.812), (42, 13)))
        self.add_bezier('sym-e14', (42, 13), ((42, 13.933), (41.475, 15.231), (41, 16)))
        self.add_bezier('sym-e15', (41, 16), ((39.511, 18.405), (36.667, 19.006), (34, 18)))
        self.add_bezier('sym-e16', (34, 18), ((33.427, 17.787), (32.515, 17.319), (32, 17)))
        self.add_line('sym-e17', (32, 17), (31, 16))
        self.add_bezier('sym-e18', (31, 16), ((31.065, 16.205), (30.943, 15.804), (31, 16)))
        self.add_bezier('sym-e19', (16, 17), ((15.485, 17.319), (14.573, 17.787), (14, 18)))
        self.add_bezier('sym-e20', (14, 18), ((11.333, 19.006), (8.489, 18.405), (7, 16)))
        self.add_bezier('sym-e21', (7, 16), ((6.525, 15.231), (6, 13.933), (6, 13)))
        self.add_bezier('sym-e22', (6, 13), ((6, 12.812), (6, 13.188), (6, 13)))
        self.add_bezier('sym-e23', (6, 13), ((6, 12.861), (6, 12.139), (6, 12)))
        self.add_bezier('sym-e24', (6, 12), ((6, 8.866), (8.809, 6), (12, 6)))
        self.add_bezier('sym-e25', (12, 6), ((12.065, 6), (11.935, 6), (12, 6)))
        self.add_bezier('sym-e26', (12, 6), ((13.252, 6), (15.043, 6.223), (16, 7)))
        self.add_bezier('sym-e27', (16, 7), ((18.782, 9.258), (17.941, 12.85), (17, 16)))
        self.add_bezier('sym-e28', (17, 16), ((16.935, 16.205), (17.057, 15.804), (17, 16)))
        self.add_line('sym-e29', (17, 16), (16, 17))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18')
        self.add_contour('sym-c1', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
