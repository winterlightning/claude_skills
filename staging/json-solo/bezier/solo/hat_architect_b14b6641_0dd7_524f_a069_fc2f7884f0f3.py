"""Batch-03/hat architect (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b14b6641-0dd7-524f-a069-fc2f7884f0f3'
SOURCE_PATH = 'icons-json/accessories/batch-03/hat architect_b14b6641-0dd7-524f-a069-fc2f7884f0f3.json'
AUTHOR = 'json_to_solo'

class Batch03HatArchitect(Solo48):
    icon_id = 'batch-03-hat-architect'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'hat', 'architect', 'accessories')

    def build(self):
        self.add_bezier('sym-e0', (8, 31), ((8, 31), (8, 31), (8, 31)))
        self.add_bezier('sym-e1', (8, 31), ((7.935, 31.002), (7.068, 31), (7, 31)))
        self.add_bezier('sym-e2', (7, 31), ((6.954, 31), (7.046, 31), (7, 31)))
        self.add_bezier('sym-e3', (7, 31), ((6.769, 31), (7.212, 30.934), (7, 31)))
        self.add_bezier('sym-e4', (7, 31), ((5.782, 31.382), (4, 34.277), (4, 36)))
        self.add_bezier('sym-e5', (4, 36), ((4, 36.098), (4, 35.902), (4, 36)))
        self.add_bezier('sym-e6', (4, 36), ((4, 36.098), (4, 35.902), (4, 36)))
        self.add_bezier('sym-e7', (4, 36), ((4, 37.895), (5.6, 40), (7, 40)))
        self.add_line('sym-e8', (7, 40), (24, 40))
        self.add_line('sym-e9', (24, 40), (41, 40))
        self.add_bezier('sym-e10', (41, 40), ((42.4, 40), (44, 37.895), (44, 36)))
        self.add_bezier('sym-e11', (44, 36), ((44, 35.902), (44, 36.098), (44, 36)))
        self.add_bezier('sym-e12', (44, 36), ((44, 35.902), (44, 36.098), (44, 36)))
        self.add_bezier('sym-e13', (44, 36), ((44, 34.277), (42.218, 31.382), (41, 31)))
        self.add_bezier('sym-e14', (41, 31), ((40.788, 30.934), (41.231, 31), (41, 31)))
        self.add_bezier('sym-e15', (41, 31), ((40.954, 31), (41.046, 31), (41, 31)))
        self.add_bezier('sym-e16', (41, 31), ((40.932, 31), (40.065, 31.002), (40, 31)))
        self.add_bezier('sym-e17', (40, 31), ((40, 31), (40, 31), (40, 31)))
        self.add_line('sym-e18', (40, 31), (24, 31))
        self.add_line('sym-e19', (24, 31), (8, 31))
        self.add_bezier('sym-e20', (8, 31), ((7.918, 28.772), (7.482, 27.154), (8, 25)))
        self.add_bezier('sym-e21', (8, 25), ((9.655, 18.095), (14.045, 13.797), (19, 12)))
        self.add_bezier('sym-e22', (19, 12), ((19.036, 10.511), (19.409, 8), (21, 8)))
        self.add_bezier('sym-e23', (21, 8), ((21.073, 8), (20.927, 8), (21, 8)))
        self.add_line('sym-e24', (21, 8), (24, 8))
        self.add_line('sym-e25', (24, 8), (27, 8))
        self.add_bezier('sym-e26', (27, 8), ((27.073, 8), (26.927, 8), (27, 8)))
        self.add_bezier('sym-e27', (27, 8), ((28.591, 8), (28.964, 10.511), (29, 12)))
        self.add_bezier('sym-e28', (29, 12), ((33.955, 13.797), (38.345, 18.095), (40, 25)))
        self.add_bezier('sym-e29', (40, 25), ((40.518, 27.154), (40.082, 28.772), (40, 31)))
        self.add_bezier('sym-e30', (19, 12), ((19, 12), (19, 12), (19, 12)))
        self.add_line('sym-e31', (19, 12), (19, 19))
        self.add_bezier('sym-e32', (19, 19), ((19, 21.289), (20.718, 22), (22, 22)))
        self.add_line('sym-e33', (22, 22), (24, 22))
        self.add_line('sym-e34', (24, 22), (26, 22))
        self.add_bezier('sym-e35', (26, 22), ((27.282, 22), (29, 21.289), (29, 19)))
        self.add_line('sym-e36', (29, 19), (29, 12))
        self.add_bezier('sym-e37', (29, 12), ((29, 12), (29, 12), (29, 12)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29')
        self.add_contour('sym-c1', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35', 'sym-e36', 'sym-e37')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
