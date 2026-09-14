"""Lab tube experiment (science), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fb52e379-0f84-4c69-a8bd-3b7fd2c8c58e'
SOURCE_PATH = 'icons-json/science/lab tube experiment_fb52e379-0f84-4c69-a8bd-3b7fd2c8c58e.json'
AUTHOR = 'json_to_solo'

class LabTubeExperimentScience(Solo48):
    icon_id = 'lab-tube-experiment-science'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('lab', 'tube', 'experiment', 'science')

    def build(self):
        self.add_line('e0', (10, 14), (38, 14))
        self.add_line('e1', (10, 14), (10, 37))
        self.add_line('e2', (38, 37), (38, 14))
        self.add_line('e3', (10, 14), (10, 7))
        self.add_line('e4', (10, 7), (8, 4))
        self.add_line('e5', (8, 4), (40, 4))
        self.add_line('e6', (38, 7), (38, 14))
        self.add_arc('e7-1', (10, 37), (23, 44), radius_x=16, sweep=False)
        self.add_line('e7-2', (23, 44), (31, 43))
        self.add_arc('e7-3', (31, 43), (35, 41), radius_x=15, sweep=False)
        self.add_arc('e7-4', (35, 41), (38, 37), radius_x=8, sweep=False)
        self.add_arc('e8', (40, 4), (38, 7), radius_x=7)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e2')
        self.add_contour('c2', 'e3', 'e4', 'e5', 'e8', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
