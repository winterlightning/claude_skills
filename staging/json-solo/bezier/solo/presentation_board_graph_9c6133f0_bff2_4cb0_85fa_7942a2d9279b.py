"""Presentation board graph (office), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e16', (28, 17), ((27.73, 17.27), (27.188, 16.665), (27, 17)))
        self.add_bezier('e17', (20, 15), ((19.845, 14.975), (19.696, 14.73), (19.5, 14.722)), ((19.295, 14.722), (19.147, 14.975), (19, 15)))
        self.add_bezier('e18', (6, 8), ((6.507, 6.805), (6.805, 6.515), (8, 6)))
        self.add_bezier('e19', (40, 6), ((40.049, 6), (40.454, 6.008), (40.503, 6.008)), ((41.329, 6.008), (41.738, 7.427), (42, 8)))
        self.add_bezier('e20', (42, 28), ((42, 28.025), (41.992, 28.148), (41.992, 28.173)), ((41.992, 29.024), (40.605, 29.73), (40, 30)))
        self.add_bezier('e21', (6, 28), ((6.54, 29.105), (6.895, 29.509), (8, 30)))
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
