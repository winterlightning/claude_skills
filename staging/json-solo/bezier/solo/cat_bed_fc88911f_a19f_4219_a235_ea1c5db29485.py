"""Cat bed (pets), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fc88911f-a19f-4219-a235-ea1c5db29485'
SOURCE_PATH = 'icons-json/pets/cat bed_fc88911f-a19f-4219-a235-ea1c5db29485.json'
AUTHOR = 'json_to_solo'

class CatBedPets(Solo48):
    icon_id = 'cat-bed-pets'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('cat', 'bed', 'pets')

    def build(self):
        self.add_bezier('sym-e0', (24, 40), ((24.442, 40), (24.555, 40), (25, 40)))
        self.add_bezier('sym-e1', (25, 40), ((29.918, 40), (35.582, 39.47), (40, 37)))
        self.add_bezier('sym-e2', (40, 37), ((41.282, 36.28), (44, 33.79), (44, 32)))
        self.add_bezier('sym-e3', (44, 32), ((44, 31.97), (43.991, 32.03), (44, 32)))
        self.add_bezier('sym-e4', (44, 32), ((44, 31.92), (44, 32.08), (44, 32)))
        self.add_line('sym-e5', (44, 32), (44, 18))
        self.add_line('sym-e6', (44, 18), (41, 20))
        self.add_bezier('sym-e7', (41, 20), ((39.609, 19.3), (38.473, 18.44), (37, 18)))
        self.add_bezier('sym-e8', (37, 18), ((33.38, 16.924), (28.717, 16), (24, 16)))
        self.add_bezier('sym-e9', (24, 16), ((19.283, 16), (14.62, 16.924), (11, 18)))
        self.add_bezier('sym-e10', (11, 18), ((9.527, 18.44), (8.391, 19.3), (7, 20)))
        self.add_line('sym-e11', (7, 20), (4, 18))
        self.add_line('sym-e12', (4, 18), (4, 32))
        self.add_bezier('sym-e13', (4, 32), ((4, 32.08), (4, 31.92), (4, 32)))
        self.add_bezier('sym-e14', (4, 32), ((4.009, 32.03), (4, 31.97), (4, 32)))
        self.add_bezier('sym-e15', (4, 32), ((4, 33.79), (6.718, 36.28), (8, 37)))
        self.add_bezier('sym-e16', (8, 37), ((12.418, 39.47), (18.082, 40), (23, 40)))
        self.add_bezier('sym-e17', (23, 40), ((23.445, 40), (23.558, 40), (24, 40)))
        self.add_line('sym-e18', (44, 18), (44, 15))
        self.add_bezier('sym-e19', (44, 15), ((43.909, 14.77), (44, 14.22), (44, 14)))
        self.add_bezier('sym-e20', (44, 14), ((42.909, 12.1), (40.845, 11.78), (39, 11)))
        self.add_bezier('sym-e21', (39, 11), ((34.9, 9.25), (30.4, 8), (26, 8)))
        self.add_bezier('sym-e22', (26, 8), ((25.673, 8), (25.327, 8), (25, 8)))
        self.add_bezier('sym-e23', (25, 8), ((24.691, 8), (24.309, 8), (24, 8)))
        self.add_bezier('sym-e24', (24, 8), ((23.691, 8), (23.309, 8), (23, 8)))
        self.add_bezier('sym-e25', (23, 8), ((22.673, 8), (22.327, 8), (22, 8)))
        self.add_bezier('sym-e26', (22, 8), ((17.6, 8), (13.1, 9.25), (9, 11)))
        self.add_bezier('sym-e27', (9, 11), ((7.155, 11.78), (5.091, 12.1), (4, 14)))
        self.add_bezier('sym-e28', (4, 14), ((4, 14.22), (4.091, 14.77), (4, 15)))
        self.add_line('sym-e29', (4, 15), (4, 18))
        self.add_line('sym-e30', (24, 30), (30, 30))
        self.add_bezier('sym-e31', (30, 30), ((30.473, 30), (31.627, 29.29), (32, 29)))
        self.add_bezier('sym-e32', (32, 29), ((33.864, 27.54), (32.564, 25.95), (33, 24)))
        self.add_bezier('sym-e33', (33, 24), ((33.136, 23.4), (33.645, 23.42), (34, 23)))
        self.add_line('sym-e34', (34, 23), (39, 21))
        self.add_line('sym-e35', (39, 21), (41, 20))
        self.add_line('sym-e36', (24, 30), (18, 30))
        self.add_bezier('sym-e37', (18, 30), ((17.527, 30), (16.373, 29.29), (16, 29)))
        self.add_bezier('sym-e38', (16, 29), ((14.136, 27.54), (15.436, 25.95), (15, 24)))
        self.add_bezier('sym-e39', (15, 24), ((14.864, 23.4), (14.355, 23.42), (14, 23)))
        self.add_line('sym-e40', (14, 23), (9, 21))
        self.add_line('sym-e41', (9, 21), (7, 20))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
        self.add_contour('sym-c1', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29')
        self.add_contour('sym-c2', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35')
        self.add_contour('sym-c3', 'sym-e36', 'sym-e37', 'sym-e38', 'sym-e39', 'sym-e40', 'sym-e41')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
