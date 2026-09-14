"""Lab flask experiment (science), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('sym-e3-1', (13, 44), (10, 43), radius_x=5)
        self.add_arc('sym-e3-2', (10, 43), (8, 40), radius_x=4)
        self.add_line('sym-e4', (8, 40), (8, 39))
        self.add_arc('sym-e6', (8, 39), (10, 34), radius_x=9)
        self.add_line('sym-e7', (10, 34), (18, 20))
        self.add_line('sym-e8', (18, 20), (18, 19))
        self.add_line('sym-e9', (18, 19), (18, 8))
        self.add_line('sym-e10', (18, 8), (16, 7))
        self.add_arc('sym-e11', (16, 7), (16, 5), radius_x=2)
        self.add_arc('sym-e12', (16, 5), (18, 4), radius_x=3)
        self.add_line('sym-e13', (18, 4), (24, 4))
        self.add_line('sym-e14', (24, 4), (30, 4))
        self.add_arc('sym-e15', (30, 4), (32, 5), radius_x=3)
        self.add_arc('sym-e16', (32, 5), (32, 7), radius_x=2)
        self.add_line('sym-e17', (32, 7), (30, 8))
        self.add_line('sym-e18', (30, 8), (30, 19))
        self.add_arc('sym-e19', (30, 19), (30, 20), radius_x=22, sweep=False)
        self.add_line('sym-e20', (30, 20), (38, 34))
        self.add_arc('sym-e21', (38, 34), (40, 39), radius_x=9)
        self.add_arc('sym-e23', (40, 39), (40, 40), radius_x=39, sweep=False)
        self.add_arc('sym-e24-1', (40, 40), (38, 43), radius_x=4)
        self.add_arc('sym-e24-2', (38, 43), (35, 44), radius_x=5)
        self.add_line('sym-e26', (35, 44), (24, 44))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e3-1', 'sym-e3-2', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e23', 'sym-e24-1', 'sym-e24-2', 'sym-e26', closed=True)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
