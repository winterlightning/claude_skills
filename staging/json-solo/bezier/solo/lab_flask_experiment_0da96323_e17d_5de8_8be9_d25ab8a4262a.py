"""Lab flask experiment (science), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0da96323-e17d-5de8-8be9-d25ab8a4262a'
SOURCE_PATH = 'icons-json/science/lab flask experiment_0da96323-e17d-5de8-8be9-d25ab8a4262a.json'
AUTHOR = 'json_to_solo'

class LabFlaskExperiment0da96323(Solo48):
    icon_id = 'lab-flask-experiment-0da96323'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('lab', 'flask', 'experiment', 'science')

    def build(self):
        self.add_line('sym-e0', (34, 29), (14, 29))
        self.add_line('sym-e1', (24, 44), (13, 44))
        self.add_bezier('sym-e2', (13, 44), ((12.91, 44), (13.08, 44), (13, 44)))
        self.add_bezier('sym-e3', (13, 44), ((10.63, 44), (8, 42.164), (8, 40)))
        self.add_bezier('sym-e4', (8, 40), ((8, 39.836), (8, 39.155), (8, 39)))
        self.add_bezier('sym-e5', (8, 39), ((8, 38.845), (8, 39.155), (8, 39)))
        self.add_bezier('sym-e6', (8, 39), ((8, 37.3), (9.16, 35.436), (10, 34)))
        self.add_line('sym-e7', (10, 34), (18, 20))
        self.add_bezier('sym-e8', (18, 20), ((18.04, 19.382), (18, 19.609), (18, 19)))
        self.add_line('sym-e9', (18, 19), (18, 8))
        self.add_bezier('sym-e10', (18, 8), ((16.96, 7.855), (16.64, 7.536), (16, 7)))
        self.add_bezier('sym-e11', (16, 7), ((15.58, 6.655), (15.65, 5.409), (16, 5)))
        self.add_bezier('sym-e12', (16, 5), ((16.49, 4.418), (17.17, 4), (18, 4)))
        self.add_line('sym-e13', (18, 4), (24, 4))
        self.add_line('sym-e14', (24, 4), (30, 4))
        self.add_bezier('sym-e15', (30, 4), ((30.83, 4), (31.51, 4.418), (32, 5)))
        self.add_bezier('sym-e16', (32, 5), ((32.35, 5.409), (32.42, 6.655), (32, 7)))
        self.add_bezier('sym-e17', (32, 7), ((31.36, 7.536), (31.04, 7.855), (30, 8)))
        self.add_line('sym-e18', (30, 8), (30, 19))
        self.add_bezier('sym-e19', (30, 19), ((30, 19.609), (29.96, 19.382), (30, 20)))
        self.add_line('sym-e20', (30, 20), (38, 34))
        self.add_bezier('sym-e21', (38, 34), ((38.84, 35.436), (40, 37.3), (40, 39)))
        self.add_bezier('sym-e22', (40, 39), ((40, 39.155), (40, 38.845), (40, 39)))
        self.add_bezier('sym-e23', (40, 39), ((40, 39.155), (40, 39.836), (40, 40)))
        self.add_bezier('sym-e24', (40, 40), ((40, 42.164), (37.37, 44), (35, 44)))
        self.add_bezier('sym-e25', (35, 44), ((34.92, 44), (35.09, 44), (35, 44)))
        self.add_line('sym-e26', (35, 44), (24, 44))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
