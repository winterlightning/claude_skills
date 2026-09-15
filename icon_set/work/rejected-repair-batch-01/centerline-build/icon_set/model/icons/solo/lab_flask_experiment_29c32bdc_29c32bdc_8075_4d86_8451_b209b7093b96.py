"""Lab flask experiment (science), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '29c32bdc-8075-4d86-8451-b209b7093b96'
SOURCE_PATH = 'pictographic-primitives/science/lab flask experiment_29c32bdc-8075-4d86-8451-b209b7093b96.svg'
AUTHOR = 'gpt-6'

class LabFlaskExperiment29c32bdc(Solo48):
    icon_id = 'lab-flask-experiment-29c32bdc'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('lab', 'flask', 'experiment', 'science')

    def build(self):
        self.add_line('sym-e0', (13, 28), (35, 28))
        self.add_line('sym-e1', (35, 28), (40, 37))
        self.add_line('sym-e2', (40, 37), (40, 39))
        self.add_arc('sym-e4', (40, 39), (40, 40), radius_x=39, radius_y=39, large_arc=False, sweep=False)
        self.add_arc('sym-e6', (40, 40), (36, 44), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('sym-e7', (36, 44), (12, 44))
        self.add_arc('sym-e9', (12, 44), (8, 40), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('sym-e11', (8, 40), (8, 37))
        self.add_line('sym-e14', (8, 37), (18, 19))
        self.add_arc('sym-e16', (18, 19), (18, 18), radius_x=18, radius_y=18, large_arc=False, sweep=True)
        self.add_line('sym-e17', (18, 18), (18, 4))
        self.add_line('sym-e18', (18, 4), (30, 4))
        self.add_line('sym-e20', (30, 4), (30, 18))
        self.add_arc('sym-e21', (30, 18), (30, 19), radius_x=20, radius_y=20, large_arc=False, sweep=False)
        self.add_line('sym-e22', (30, 19), (35, 28))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e9', 'sym-e11', 'sym-e14', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e20', 'sym-e21', 'sym-e22', closed=False)
