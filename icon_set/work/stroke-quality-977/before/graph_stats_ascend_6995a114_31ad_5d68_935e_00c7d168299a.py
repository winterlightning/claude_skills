"""Graph stats ascend (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6995a114-31ad-5d68-935e-00c7d168299a'
SOURCE_PATH = 'pictographic-primitives/interface-essential/graph stats ascend_6995a114-31ad-5d68-935e-00c7d168299a.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class GraphStatsAscend(Solo48):
    icon_id = 'graph-stats-ascend'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('graph', 'stats', 'ascend', 'interface-essential')

    def build(self):
        self.add_line('e0', (34, 8), (44, 8))
        self.add_line('e1', (44, 8), (29, 29))
        self.add_line('e2', (29, 29), (20, 18))
        self.add_line('e3', (20, 18), (4, 40))
        self.add_line('e4', (44, 22), (44, 8))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3')
        self.add_contour('c1', 'e4')
        self.relate('connect', 'c0', 'c1')
