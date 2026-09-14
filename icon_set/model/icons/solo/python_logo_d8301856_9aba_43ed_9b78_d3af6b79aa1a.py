"""Python logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd8301856-9aba-43ed-9b78-d3af6b79aa1a'
SOURCE_PATH = 'icons-json/logos/python logo_d8301856-9aba-43ed-9b78-d3af6b79aa1a.json'
AUTHOR = 'json_to_solo'

class PythonLogo(Solo48):
    icon_id = 'python-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('python', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (24, 32), (32, 32))
        self.add_line('e1', (24, 16), (16, 16))
        self.add_line('e2', (36, 16), (32, 16))
        self.add_line('e3', (32, 32), (32, 37))
        self.add_line('e4', (16, 38), (16, 32))
        self.add_line('e5', (26, 24), (22, 24))
        self.add_line('e6', (16, 29), (16, 32))
        self.add_line('e7', (16, 10), (16, 16))
        self.add_bezier('e8', (32, 32), ((33.767, 32), (35.937, 32.501), (37.647, 31.994)), ((40.789, 31.069), (41.992, 27.535), (41.992, 24.556)), ((41.992, 24.492), (42, 24.435), (42, 24.371)), ((42, 24.37), (42, 24.369), (42, 24.368)), ((42, 24.065), (41.992, 23.771), (41.992, 23.468)), ((41.992, 20.155), (39.903, 16), (36, 16)))
        self.add_bezier('e9', (32, 37), ((32, 40.641), (27.371, 41.992), (24.466, 41.992)), ((24.16, 41.992), (23.862, 42), (23.556, 42)), ((23.552, 42), (23.547, 42), (23.542, 42)), ((23.354, 42), (23.174, 41.984), (22.985, 41.984)), ((20.605, 41.984), (17.487, 41.354), (16.235, 39.104)), ((16.055, 38.776), (16, 38.385), (16, 38)))
        self.add_bezier('e10', (32, 16), ((31.984, 19.191), (32.002, 21.627), (28.729, 23.182)), ((27.788, 23.624), (27.055, 24), (26, 24)))
        self.add_bezier('e11', (22, 24), ((19.619, 24), (16, 26.439), (16, 29)))
        self.add_bezier('e12', (32, 16), ((31.967, 11.778), (32.73, 7.505), (27.543, 6.311)), ((26.667, 6.106), (25.743, 6.008), (24.843, 6.008)), ((24.722, 6.008), (24.593, 6), (24.472, 6)), ((24.47, 6), (24.468, 6), (24.466, 6)), ((23.943, 6), (23.419, 6.016), (22.895, 6.016)), ((20.506, 6.016), (16.915, 6.54), (16.055, 9.175)), ((15.965, 9.428), (16, 9.73), (16, 10)))
        self.add_bezier('e13', (16, 32), ((11.844, 32.016), (7.489, 32.763), (6.327, 27.518)), ((6.139, 26.675), (6.008, 25.792), (6.008, 24.925)), ((6.008, 24.868), (6, 24.804), (6, 24.747)), ((6, 24.746), (6, 24.745), (6, 24.745)), ((6, 24.417), (6.008, 24.082), (6.008, 23.755)), ((6.008, 20.474), (7.325, 16.923), (10.745, 15.974)), ((12.357, 15.524), (14.347, 16), (16, 16)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e8', 'e2')
        self.add_contour('c3', 'e3', 'e9', 'e4')
        self.add_contour('c4', 'e10', 'e5', 'e11', 'e6')
        self.add_contour('c5', 'e12', 'e7')
        self.add_contour('c6', 'e13')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c6')
