"""Workflow pull request (business), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7f33bea2-e600-4c2f-86b8-178bc5495a2d'
SOURCE_PATH = 'icons-json/business/workflow pull request_7f33bea2-e600-4c2f-86b8-178bc5495a2d.json'
AUTHOR = 'json_to_solo'

class WorkflowPullRequestBusiness(Solo48):
    icon_id = 'workflow-pull-request-business'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('workflow', 'pull', 'request', 'business')

    def build(self):
        self.add_line('e0', (21, 38), (25, 35))
        self.add_line('e1', (21, 32), (25, 35))
        self.add_line('e2', (9, 18), (9, 29))
        self.add_line('e3', (17, 35), (25, 35))
        self.add_line('e4', (27, 9), (23, 12))
        self.add_line('e5', (27, 16), (23, 12))
        self.add_line('e6', (39, 30), (39, 19))
        self.add_line('e7', (31, 12), (23, 12))
        self.add_arc('e8-top', (4, 13), (14, 13), radius_x=5)
        self.add_arc('e8-bottom', (14, 13), (4, 13), radius_x=5)
        self.add_arc('e9-top', (34, 35), (44, 35), radius_x=5)
        self.add_arc('e9-bottom', (44, 35), (34, 35), radius_x=5)
        self.add_bezier('e10', (9, 29), ((9, 29.413), (9.691, 29.954), (9.855, 30.333)), ((10.9, 32.783), (14.073, 35), (17, 35)))
        self.add_bezier('e11', (39, 19), ((39, 15.901), (34.345, 12), (31, 12)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e10', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e6', 'e11', 'e7')
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.add_contour('e9', 'e9-top', 'e9-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c2', 'e8')
        self.relate('connect', 'c5', 'e9')
