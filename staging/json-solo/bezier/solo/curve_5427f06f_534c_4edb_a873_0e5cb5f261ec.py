"""Curve (diagrams), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5427f06f-534c-4edb-a873-0e5cb5f261ec'
SOURCE_PATH = 'icons-json/diagrams/curve_5427f06f-534c-4edb-a873-0e5cb5f261ec.json'
AUTHOR = 'json_to_solo'

class CurveDiagrams(Solo48):
    icon_id = 'curve-diagrams'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    aliases = ()
    keywords = ('curve', 'diagrams')

    def build(self):
        self.add_bezier('sym-e0', (6, 42), ((6, 41.615), (6, 41.385), (6, 41)))
        self.add_bezier('sym-e1', (6, 41), ((6, 31.693), (10.521, 23.298), (17, 17)))
        self.add_bezier('sym-e2', (17, 17), ((23.298, 10.521), (31.693, 6), (41, 6)))
        self.add_bezier('sym-e3', (41, 6), ((41.385, 6), (41.615, 6), (42, 6)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3')
