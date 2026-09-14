"""Lab bottle experiment (science), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a333e93a-f33e-5e27-af74-1c49d54d185b'
SOURCE_PATH = 'icons-json/science/lab bottle experiment_a333e93a-f33e-5e27-af74-1c49d54d185b.json'
AUTHOR = 'json_to_solo'

class LabBottleExperimentScience(Solo48):
    icon_id = 'lab-bottle-experiment-science'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('lab', 'bottle', 'experiment', 'science')

    def build(self):
        self.add_line('e0', (34, 29), (14, 29))
        self.add_line('e1', (30, 8), (30, 19))
        self.add_line('e2', (31, 21), (39, 37))
        self.add_line('e3', (33, 44), (13, 44))
        self.add_line('e4', (9, 37), (17, 21))
        self.add_line('e5', (18, 19), (18, 8))
        self.add_line('e6', (17, 4), (29, 4))
        self.add_bezier('e7', (30, 19), ((30, 19.936), (30.57, 20.182), (31, 21)))
        self.add_bezier('e8', (39, 37), ((39.41, 37.8), (40, 38.609), (40, 39.509)), ((40, 39.51), (40, 39.511), (40, 39.513)), ((40, 39.584), (40, 39.656), (40, 39.736)), ((40, 39.809), (39.99, 39.882), (39.99, 39.955)), ((39.99, 41.682), (38.43, 43.3), (36.72, 43.864)), ((36.21, 44), (35.53, 43.982), (35.01, 43.982)), ((34.34, 43.982), (33.67, 44), (33, 44)))
        self.add_bezier('e9', (13, 44), ((12.91, 44), (12.82, 43.991), (12.74, 43.991)), ((10.76, 43.991), (9.52, 42.982), (8.62, 41.473)), ((8.31, 40.964), (8.01, 40.4), (8.01, 39.809)), ((8.01, 39.737), (8, 39.666), (8, 39.603)), ((8, 39.602), (8, 39.601), (8, 39.6)), ((8, 39.527), (8.01, 39.455), (8.01, 39.382)), ((8.01, 38.573), (8.62, 37.727), (9, 37)))
        self.add_bezier('e10', (17, 21), ((17.32, 20.373), (17.72, 19.655), (18, 19)))
        self.add_bezier('e11', (18, 8), ((17.35, 7.836), (16.61, 7.355), (16.05, 6.982)), ((15.2, 6.409), (15.12, 5.173), (15.85, 4.509)), ((16.22, 4.164), (16.56, 4.173), (17, 4)))
        self.add_bezier('e12', (29, 4), ((29.39, 4), (29.77, 4.009), (30.16, 4.009)), ((30.56, 4.009), (31.28, 4), (31.63, 4.182)), ((32.74, 4.873), (32.82, 6.991), (31.3, 7.364)), ((30.87, 7.455), (30.43, 7.909), (30, 8)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e7', 'e2', 'e8', 'e3', 'e9', 'e4', 'e10', 'e5', 'e11', 'e6', 'e12', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
