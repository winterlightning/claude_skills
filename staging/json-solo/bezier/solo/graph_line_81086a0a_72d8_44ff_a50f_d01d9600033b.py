"""Graph line (business), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81086a0a-72d8-44ff-a50f-d01d9600033b'
SOURCE_PATH = 'icons-json/business/graph line_81086a0a-72d8-44ff-a50f-d01d9600033b.json'
AUTHOR = 'json_to_solo'

class GraphLineBusiness(Solo48):
    icon_id = 'graph-line-business'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('graph', 'line', 'business')

    def build(self):
        self.add_line('e0', (34, 8), (44, 8))
        self.add_line('e1', (44, 8), (29, 29))
        self.add_line('e2', (28, 29), (20, 18))
        self.add_line('e3', (20, 18), (4, 40))
        self.add_line('e4', (44, 8), (44, 22))
        self.add_bezier('e5', (29, 29), ((28.7, 29), (28.3, 29), (28, 29)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e5', 'e2', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
