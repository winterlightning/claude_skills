"""Presentation board (office), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2ca57da6-a1e1-40e2-9dd9-b25695b74495'
SOURCE_PATH = 'icons-json/office/presentation board_2ca57da6-a1e1-40e2-9dd9-b25695b74495.json'
AUTHOR = 'json_to_solo'

class PresentationBoard(Solo48):
    icon_id = 'presentation-board'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('presentation', 'board', 'office')

    def build(self):
        self.add_line('e0', (16, 42), (24, 34))
        self.add_line('e1', (24, 34), (24, 42))
        self.add_line('e2', (32, 42), (24, 33))
        self.add_line('e3', (24, 33), (24, 30))
        self.add_line('e4', (6, 12), (42, 12))
        self.add_line('e5', (6, 12), (6, 28))
        self.add_line('e6', (8, 30), (24, 30))
        self.add_line('e7', (6, 12), (6, 8))
        self.add_line('e8', (8, 6), (40, 6))
        self.add_line('e9', (42, 8), (42, 12))
        self.add_line('e10', (42, 12), (42, 28))
        self.add_line('e11', (40, 30), (24, 30))
        self.add_line('e12', (6, 28), (8, 30))
        self.add_arc('e13', (6, 8), (8, 6), radius_x=2)
        self.add_arc('e14', (40, 6), (42, 8), radius_x=2)
        self.add_line('e15', (42, 28), (40, 30))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5', 'e12', 'e6')
        self.add_contour('c4', 'e7', 'e13', 'e8', 'e14', 'e9')
        self.add_contour('c5', 'e10', 'e15', 'e11')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
