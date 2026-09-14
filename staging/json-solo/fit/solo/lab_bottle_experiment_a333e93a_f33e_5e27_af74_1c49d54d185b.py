"""Lab bottle experiment (science), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_line('e7', (30, 19), (31, 21))
        self.add_line('e8-1', (39, 37), (40, 40))
        self.add_arc('e8-2', (40, 40), (36, 44), radius_x=4)
        self.add_line('e8-3', (36, 44), (33, 44))
        self.add_arc('e9-1', (13, 44), (10, 43), radius_x=5)
        self.add_line('e9-2', (10, 43), (8, 40))
        self.add_line('e9-3', (8, 40), (9, 37))
        self.add_arc('e10', (17, 21), (18, 19), radius_x=15)
        self.add_line('e11-1', (18, 8), (16, 7))
        self.add_arc('e11-2', (16, 7), (17, 4), radius_x=2)
        self.add_line('e12-1', (29, 4), (32, 5))
        self.add_arc('e12-2', (32, 5), (32, 7), radius_x=2)
        self.add_line('e12-3', (32, 7), (30, 8))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e7', 'e2', 'e8-1', 'e8-2', 'e8-3', 'e3', 'e9-1', 'e9-2', 'e9-3', 'e4', 'e10', 'e5', 'e11-1', 'e11-2', 'e6', 'e12-1', 'e12-2', 'e12-3', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
