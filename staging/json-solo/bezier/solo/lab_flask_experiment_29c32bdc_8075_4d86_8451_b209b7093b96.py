"""Lab flask experiment (science), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '29c32bdc-8075-4d86-8451-b209b7093b96'
SOURCE_PATH = 'icons-json/science/lab flask experiment_29c32bdc-8075-4d86-8451-b209b7093b96.json'
AUTHOR = 'json_to_solo'

class LabFlaskExperiment(Solo48):
    icon_id = 'lab-flask-experiment'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('lab', 'flask', 'experiment', 'science')

    def build(self):
        self.add_line('sym-e0', (13, 28), (35, 28))
        self.add_line('sym-e1', (35, 28), (40, 37))
        self.add_bezier('sym-e2', (40, 37), ((40, 37.445), (40, 37.564), (40, 38)))
        self.add_bezier('sym-e3', (40, 38), ((40, 38.445), (40, 38.545), (40, 39)))
        self.add_bezier('sym-e4', (40, 39), ((40, 39.045), (40, 39.945), (40, 40)))
        self.add_bezier('sym-e5', (40, 40), ((40, 40.055), (40, 39.945), (40, 40)))
        self.add_bezier('sym-e6', (40, 40), ((40, 42.127), (37.98, 43.382), (36, 44)))
        self.add_line('sym-e7', (36, 44), (24, 44))
        self.add_line('sym-e8', (24, 44), (12, 44))
        self.add_bezier('sym-e9', (12, 44), ((10.02, 43.382), (8, 42.127), (8, 40)))
        self.add_bezier('sym-e10', (8, 40), ((8, 39.945), (8, 40.055), (8, 40)))
        self.add_bezier('sym-e11', (8, 40), ((8, 39.945), (8, 39.045), (8, 39)))
        self.add_bezier('sym-e12', (8, 39), ((8, 38.545), (8, 38.445), (8, 38)))
        self.add_bezier('sym-e13', (8, 38), ((8, 37.564), (8, 37.445), (8, 37)))
        self.add_line('sym-e14', (8, 37), (13, 28))
        self.add_line('sym-e15', (13, 28), (18, 19))
        self.add_bezier('sym-e16', (18, 19), ((18, 18.7), (18, 18.3), (18, 18)))
        self.add_line('sym-e17', (18, 18), (18, 4))
        self.add_line('sym-e18', (18, 4), (24, 4))
        self.add_line('sym-e19', (24, 4), (30, 4))
        self.add_line('sym-e20', (30, 4), (30, 18))
        self.add_bezier('sym-e21', (30, 18), ((30, 18.3), (30, 18.7), (30, 19)))
        self.add_line('sym-e22', (30, 19), (35, 28))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22')
