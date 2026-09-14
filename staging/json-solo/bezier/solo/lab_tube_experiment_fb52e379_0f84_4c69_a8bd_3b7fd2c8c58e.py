"""Lab tube experiment (science), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e7', (10, 37), ((10, 37.482), (10.112, 37.909), (10.432, 38.373)), ((12.368, 41.227), (17.36, 43.991), (23.072, 43.991)), ((23.198, 43.991), (23.34, 44), (23.466, 44)), ((23.468, 44), (23.47, 44), (23.472, 44)), ((23.936, 44), (24.384, 43.991), (24.848, 43.991)), ((30.848, 43.991), (36.112, 41.327), (37.792, 38.173)), ((38.016, 37.755), (38, 37.427), (38, 37)))
        self.add_bezier('e8', (40, 4), ((39.584, 4.609), (38, 6.218), (38, 7)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e7', 'e2')
        self.add_contour('c2', 'e3', 'e4', 'e5', 'e8', 'e6')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
