"""Protection helmet (protection), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '57952e22-e183-5dd9-872b-5214ae9a25fc'
SOURCE_PATH = 'icons-json/protection/protection helmet_57952e22-e183-5dd9-872b-5214ae9a25fc.json'
AUTHOR = 'json_to_solo'

class ProtectionHelmetProtection(Solo48):
    icon_id = 'protection-helmet-protection'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('protection', 'helmet')

    def build(self):
        self.add_bezier('sym-e0', (41, 32), ((42.418, 32.75), (44, 34.08), (44, 36)))
        self.add_bezier('sym-e1', (44, 36), ((44, 36.08), (44, 35.92), (44, 36)))
        self.add_bezier('sym-e2', (44, 36), ((44, 36.08), (44, 35.92), (44, 36)))
        self.add_bezier('sym-e3', (44, 36), ((44, 36.35), (44, 36.71), (44, 37)))
        self.add_bezier('sym-e4', (44, 37), ((43.173, 38.41), (41.4, 38.86), (40, 39)))
        self.add_bezier('sym-e5', (40, 39), ((35.436, 39.45), (30.591, 40), (26, 40)))
        self.add_bezier('sym-e6', (26, 40), ((25.273, 40), (24.727, 40), (24, 40)))
        self.add_bezier('sym-e7', (24, 40), ((23.939, 40), (24.061, 40), (24, 40)))
        self.add_bezier('sym-e8', (24, 40), ((23.939, 40), (24.061, 40), (24, 40)))
        self.add_bezier('sym-e9', (24, 40), ((23.273, 40), (22.727, 40), (22, 40)))
        self.add_bezier('sym-e10', (22, 40), ((17.409, 40), (12.564, 39.45), (8, 39)))
        self.add_bezier('sym-e11', (8, 39), ((6.6, 38.86), (4.827, 38.41), (4, 37)))
        self.add_bezier('sym-e12', (4, 37), ((4, 36.71), (4, 36.35), (4, 36)))
        self.add_bezier('sym-e13', (4, 36), ((4, 35.92), (4, 36.08), (4, 36)))
        self.add_bezier('sym-e14', (4, 36), ((4, 35.92), (4, 36.08), (4, 36)))
        self.add_bezier('sym-e15', (4, 36), ((4, 34.08), (5.582, 32.75), (7, 32)))
        self.add_line('sym-e16', (7, 32), (24, 32))
        self.add_line('sym-e17', (24, 32), (41, 32))
        self.add_bezier('sym-e18', (41, 32), ((41.073, 29.07), (41.691, 25.85), (41, 23)))
        self.add_bezier('sym-e19', (41, 23), ((39.5, 16.82), (34.445, 11.11), (29, 9)))
        self.add_bezier('sym-e20', (29, 9), ((29, 9.33), (29, 9.67), (29, 10)))
        self.add_line('sym-e21', (29, 10), (29, 24))
        self.add_bezier('sym-e22', (29, 9), ((28.982, 8.89), (27.191, 8), (27, 8)))
        self.add_bezier('sym-e23', (27, 8), ((26.4, 8), (25.6, 8), (25, 8)))
        self.add_bezier('sym-e24', (25, 8), ((24.518, 8), (24.482, 8), (24, 8)))
        self.add_bezier('sym-e25', (24, 8), ((23.518, 8), (23.482, 8), (23, 8)))
        self.add_bezier('sym-e26', (23, 8), ((22.4, 8), (21.6, 8), (21, 8)))
        self.add_bezier('sym-e27', (21, 8), ((20.809, 8), (19.018, 8.89), (19, 9)))
        self.add_bezier('sym-e28', (19, 9), ((13.555, 11.11), (8.5, 16.82), (7, 23)))
        self.add_bezier('sym-e29', (7, 23), ((6.309, 25.85), (6.927, 29.07), (7, 32)))
        self.add_line('sym-e30', (19, 24), (19, 10))
        self.add_bezier('sym-e31', (19, 10), ((19, 9.67), (19, 9.33), (19, 9)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21')
        self.add_contour('sym-c1', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29')
        self.add_contour('sym-c2', 'sym-e30', 'sym-e31')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
