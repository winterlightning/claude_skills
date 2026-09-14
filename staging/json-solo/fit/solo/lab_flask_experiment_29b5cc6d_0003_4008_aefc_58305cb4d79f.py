"""Lab flask experiment (science), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '29b5cc6d-0003-4008-aefc-58305cb4d79f'
SOURCE_PATH = 'icons-json/science/lab flask experiment_29b5cc6d-0003-4008-aefc-58305cb4d79f.json'
AUTHOR = 'json_to_solo'

class LabFlaskExperiment29b5cc6d(Solo48):
    icon_id = 'lab-flask-experiment-29b5cc6d'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('lab', 'flask', 'experiment', 'science')

    def build(self):
        self.add_line('sym-e0', (13, 28), (35, 28))
        self.add_line('sym-e1', (35, 28), (40, 37))
        self.add_line('sym-e2', (40, 37), (40, 38))
        self.add_line('sym-e3', (40, 38), (40, 39))
        self.add_arc('sym-e4', (40, 39), (40, 40), radius_x=39, sweep=False)
        self.add_arc('sym-e6', (40, 40), (36, 44), radius_x=5)
        self.add_line('sym-e7', (36, 44), (24, 44))
        self.add_line('sym-e8', (24, 44), (12, 44))
        self.add_arc('sym-e9', (12, 44), (8, 40), radius_x=5)
        self.add_line('sym-e11', (8, 40), (8, 39))
        self.add_line('sym-e12', (8, 39), (8, 38))
        self.add_line('sym-e13', (8, 38), (8, 37))
        self.add_line('sym-e14', (8, 37), (13, 28))
        self.add_line('sym-e15', (13, 28), (18, 19))
        self.add_arc('sym-e16', (18, 19), (18, 18), radius_x=18)
        self.add_line('sym-e17', (18, 18), (18, 4))
        self.add_line('sym-e18', (18, 4), (24, 4))
        self.add_line('sym-e19', (24, 4), (30, 4))
        self.add_line('sym-e20', (30, 4), (30, 18))
        self.add_arc('sym-e21', (30, 18), (30, 19), radius_x=20, sweep=False)
        self.add_line('sym-e22', (30, 19), (35, 28))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22')
