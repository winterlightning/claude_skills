"""Graph line (health), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2a9d95b0-3301-4030-a069-703a97ff8a06'
SOURCE_PATH = 'icons-json/health/graph line_2a9d95b0-3301-4030-a069-703a97ff8a06.json'
AUTHOR = 'json_to_solo'

class GraphLine2a9d95b0(Solo48):
    icon_id = 'graph-line-2a9d95b0'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('graph', 'line', 'health')

    def build(self):
        self.add_line('e0', (35, 20), (36, 24))
        self.add_line('e1', (37, 26), (44, 27))
        self.add_line('e2', (4, 27), (12, 27))
        self.add_line('e3', (17, 22), (20, 8))
        self.add_line('e4', (20, 8), (28, 40))
        self.add_line('e5', (28, 40), (35, 20))
        self.add_line('e6', (36, 24), (37, 26))
        self.add_arc('e7', (12, 27), (17, 22), radius_x=5, sweep=False)
        self.add_contour('c0', 'e0', 'e6', 'e1')
        self.add_contour('c1', 'e2', 'e7', 'e3')
        self.add_contour('c2', 'e4', 'e5')
