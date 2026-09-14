"""Workflow compare (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '35bdab51-2134-4b2d-a32e-602ef33b7d47'
SOURCE_PATH = 'icons-json/interface-essential/workflow compare_35bdab51-2134-4b2d-a32e-602ef33b7d47.json'
AUTHOR = 'json_to_solo'

class WorkflowCompareInterfaceEssential(Solo48):
    icon_id = 'workflow-compare-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('workflow', 'compare', 'interface-essential')

    def build(self):
        self.add_line('e0', (11, 32), (11, 17))
        self.add_line('e1', (28, 6), (24, 10))
        self.add_line('e2', (28, 14), (24, 10))
        self.add_line('e3', (37, 32), (37, 17))
        self.add_line('e4', (31, 10), (24, 10))
        self.add_arc('e5-top', (6, 37), (16, 37), radius_x=5)
        self.add_arc('e5-bottom', (16, 37), (6, 37), radius_x=5)
        self.add_arc('e6-top', (6, 11), (16, 11), radius_x=5)
        self.add_arc('e6-bottom', (16, 11), (6, 11), radius_x=5)
        self.add_arc('e7-top', (32, 37), (42, 37), radius_x=5)
        self.add_arc('e7-bottom', (42, 37), (32, 37), radius_x=5)
        self.add_bezier('e8', (11, 17), ((11, 16.73), (11, 16.27), (11, 16)))
        self.add_bezier('e9', (37, 17), ((37, 16.566), (36.911, 15.695), (36.796, 15.278)), ((36.158, 12.987), (34.53, 10.983), (32.198, 10.304)), ((31.969, 10.238), (31.221, 10), (31, 10)))
        self.add_contour('c0', 'e0', 'e8')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e9', 'e4')
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.add_contour('e7', 'e7-top', 'e7-bottom', closed=True)
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c0', 'e5')
        self.relate('connect', 'c0', 'e6')
        self.relate('connect', 'c3', 'e7')
