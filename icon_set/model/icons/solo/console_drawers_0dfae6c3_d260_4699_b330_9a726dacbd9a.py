"""Console drawers (furnitures), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0dfae6c3-d260-4699-b330-9a726dacbd9a'
SOURCE_PATH = 'icons-json/furnitures/console drawers_0dfae6c3-d260-4699-b330-9a726dacbd9a.json'
AUTHOR = 'json_to_solo'

class ConsoleDrawers(Solo48):
    icon_id = 'console-drawers'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('console', 'drawers', 'furnitures')

    def build(self):
        self.add_line('e0', (7, 40), (7, 31))
        self.add_line('e1', (41, 40), (41, 31))
        self.add_line('e2', (29, 19), (44, 19))
        self.add_line('e3', (29, 31), (29, 8))
        self.add_line('e4', (17, 31), (17, 8))
        self.add_line('e5', (44, 31), (44, 8))
        self.add_line('e6', (44, 8), (4, 8))
        self.add_line('e7', (4, 8), (4, 31))
        self.add_line('e8', (4, 31), (44, 31))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5', 'e6', 'e7', 'e8', closed=True)
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c5')
