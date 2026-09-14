"""Graph line spline (business), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f4acbb4-799c-5a89-97d6-f6dbcb05930f'
SOURCE_PATH = 'icons-json/business/graph line spline_8f4acbb4-799c-5a89-97d6-f6dbcb05930f.json'
AUTHOR = 'json_to_solo'

class GraphLineSpline(Solo48):
    icon_id = 'graph-line-spline'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('graph', 'line', 'spline', 'business')

    def build(self):
        self.add_line('e0', (26, 15), (29, 19))
        self.add_line('e1', (40, 19), (43, 13))
        self.add_line('e2', (44, 27), (41, 31))
        self.add_line('e3', (15, 32), (4, 40))
        self.add_line('e4', (4, 40), (4, 8))
        self.add_line('e5', (4, 40), (44, 40))
        self.add_arc('e6-1', (4, 28), (12, 24), radius_x=8, sweep=False)
        self.add_line('e6-2', (12, 24), (18, 13))
        self.add_arc('e6-3', (18, 13), (26, 15), radius_x=6)
        self.add_arc('e7', (29, 19), (40, 19), radius_x=6, sweep=False)
        self.add_arc('e8-1', (41, 31), (35, 34), radius_x=7)
        self.add_line('e8-2', (35, 34), (25, 29))
        self.add_arc('e8-3', (25, 29), (22, 29), radius_x=9, sweep=False)
        self.add_line('e8-4', (22, 29), (15, 32))
        self.add_contour('c0', 'e6-1', 'e6-2', 'e6-3', 'e0', 'e7', 'e1')
        self.add_contour('c1', 'e2', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e3', 'e4')
        self.add_contour('c2', 'e5')
        self.relate('connect', 'c0', 'c1')
