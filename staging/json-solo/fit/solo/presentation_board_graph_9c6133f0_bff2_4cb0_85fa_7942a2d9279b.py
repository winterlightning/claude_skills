"""Presentation board graph (office), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9c6133f0-bff2-4cb0-85fa-7942a2d9279b'
SOURCE_PATH = 'icons-json/office/presentation board graph_9c6133f0-bff2-4cb0-85fa-7942a2d9279b.json'
AUTHOR = 'json_to_solo'

class PresentationBoardGraphOffice(Solo48):
    icon_id = 'presentation-board-graph-office'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('presentation', 'board', 'graph', 'office')

    def build(self):
        self.add_line('e0', (34, 12), (31, 21))
        self.add_line('e1', (31, 21), (28, 17))
        self.add_line('e2', (27, 17), (24, 23))
        self.add_line('e3', (24, 23), (20, 15))
        self.add_line('e4', (19, 15), (17, 19))
        self.add_line('e5', (17, 19), (6, 19))
        self.add_line('e6', (17, 42), (24, 35))
        self.add_line('e7', (24, 42), (24, 35))
        self.add_line('e8', (31, 42), (24, 35))
        self.add_line('e9', (6, 19), (6, 8))
        self.add_line('e10', (8, 6), (40, 6))
        self.add_line('e11', (42, 8), (42, 28))
        self.add_line('e12', (40, 30), (24, 30))
        self.add_line('e13', (6, 19), (6, 28))
        self.add_line('e14', (8, 30), (24, 30))
        self.add_line('e15', (24, 30), (24, 35))
        self.add_line('e16', (28, 17), (27, 17))
        self.add_arc('e17', (20, 15), (19, 15), radius_x=1, sweep=False)
        self.add_arc('e18', (6, 8), (8, 6), radius_x=2)
        self.add_arc('e19', (40, 6), (42, 8), radius_x=2)
        self.add_arc('e20', (42, 28), (40, 30), radius_x=2)
        self.add_line('e21', (6, 28), (8, 30))
        self.add_contour('c0', 'e0', 'e1', 'e16', 'e2', 'e3', 'e17', 'e4', 'e5')
        self.add_contour('c1', 'e6')
        self.add_contour('c2', 'e7')
        self.add_contour('c3', 'e8')
        self.add_contour('c4', 'e9', 'e18', 'e10', 'e19', 'e11', 'e20', 'e12')
        self.add_contour('c5', 'e13', 'e21', 'e14')
        self.add_contour('c6', 'e15')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
