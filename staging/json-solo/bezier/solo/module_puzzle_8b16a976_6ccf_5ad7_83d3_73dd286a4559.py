"""Module puzzle (programing), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8b16a976-6ccf-5ad7-83d3-73dd286a4559'
SOURCE_PATH = 'icons-json/programing/module puzzle_8b16a976-6ccf-5ad7-83d3-73dd286a4559.json'
AUTHOR = 'json_to_solo'

class ModulePuzzlePrograming(Solo48):
    icon_id = 'module-puzzle-programing'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('module', 'puzzle', 'programing')

    def build(self):
        self.add_line('e0', (21, 13), (11, 13))
        self.add_line('e1', (8, 17), (8, 25))
        self.add_line('e2', (8, 31), (8, 42))
        self.add_line('e3', (11, 44), (21, 44))
        self.add_line('e4', (27, 44), (38, 44))
        self.add_line('e5', (40, 42), (40, 16))
        self.add_line('e6', (37, 13), (27, 13))
        self.add_bezier('e7', (27, 13), ((27.429, 12.018), (28.547, 10.918), (28.699, 9.8)), ((29.103, 6.836), (26.897, 4), (24.076, 4)), ((24.075, 4), (24.074, 4), (24.073, 4)), ((24.006, 4), (23.932, 4.009), (23.865, 4.018)), ((21.044, 4.018), (18.804, 6.9), (19.259, 9.864)), ((19.427, 10.973), (20.537, 12.027), (21, 13)))
        self.add_bezier('e8', (11, 13), ((9.829, 13), (8.017, 14.255), (8.017, 15.609)), ((8.017, 15.764), (8.008, 15.918), (8.008, 16.064)), ((8.008, 16.145), (8, 16.218), (8, 16.291)), ((8, 16.436), (8, 16.855), (8, 17)))
        self.add_bezier('e9', (8, 25), ((9.701, 24.118), (11.284, 23.1), (13.229, 23.636)), ((14.223, 23.909), (15.124, 24.618), (15.739, 25.473)), ((18.476, 29.282), (15.453, 33.764), (11.251, 33.009)), ((10.105, 32.8), (8.968, 31.6), (8, 31)))
        self.add_bezier('e10', (8, 42), ((8.699, 42.882), (9.821, 44), (11, 44)))
        self.add_bezier('e11', (21, 44), ((20.276, 42.736), (19.857, 41.527), (19.646, 40.027)), ((19.267, 37.309), (21.558, 34.945), (24.017, 34.909)), ((26.122, 34.882), (28.278, 36.636), (28.749, 38.855)), ((29.162, 40.764), (27.8, 42.4), (27, 44)))
        self.add_bezier('e12', (38, 44), ((38.168, 43.9), (38.669, 43.918), (38.821, 43.809)), ((39.503, 43.355), (39.655, 42.673), (40, 42)))
        self.add_bezier('e13', (40, 16), ((40, 15.8), (39.992, 15.418), (39.992, 15.227)), ((39.992, 13.927), (38.678, 13.109), (37.608, 13.018)), ((37.272, 12.991), (37.328, 13), (37, 13)))
        self.add_contour('c0', 'e7', 'e0', 'e8', 'e1', 'e9', 'e2', 'e10', 'e3', 'e11', 'e4', 'e12', 'e5', 'e13', 'e6', closed=True)
