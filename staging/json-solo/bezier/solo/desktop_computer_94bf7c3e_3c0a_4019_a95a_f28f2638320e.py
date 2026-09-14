"""Batch-02/desktop computer (computers), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '94bf7c3e-3c0a-4019-a95a-f28f2638320e'
SOURCE_PATH = 'icons-json/computers/batch-02/desktop computer_94bf7c3e-3c0a-4019-a95a-f28f2638320e.json'
AUTHOR = 'json_to_solo'

class Batch02DesktopComputer94bf7c3e(Solo48):
    icon_id = 'batch-02-desktop-computer-94bf7c3e'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    aliases = ()
    keywords = ('batch', 'desktop', 'computer', 'computers')

    def build(self):
        self.add_line('e0', (6, 25), (42, 25))
        self.add_line('e1', (14, 42), (34, 42))
        self.add_line('e2', (17, 33), (17, 42))
        self.add_line('e3', (31, 33), (31, 42))
        self.add_line('e4', (6, 8), (6, 31))
        self.add_line('e5', (8, 33), (40, 33))
        self.add_line('e6', (42, 31), (42, 8))
        self.add_line('e7', (40, 6), (8, 6))
        self.add_bezier('e8', (42, 25), ((41.452, 25), (40.548, 25), (40, 25)))
        self.add_bezier('e9', (8, 6), ((7.967, 6), (8.381, 6.008), (8.348, 6.008)), ((7.325, 6.008), (6.016, 7.325), (6.016, 8.348)), ((6.008, 8.381), (6.008, 7.967), (6, 8)))
        self.add_bezier('e10', (6, 31), ((6, 32.342), (6.936, 32.64), (8, 33)))
        self.add_bezier('e11', (40, 33), ((41.162, 33), (42, 32.162), (42, 31)))
        self.add_bezier('e12', (42, 8), ((41.992, 7.959), (41.992, 8.365), (41.984, 8.324)), ((41.984, 7.285), (40.998, 6), (40, 6)))
        self.add_contour('c0', 'e0', 'e8')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e9', 'e4', 'e10', 'e5', 'e11', 'e6', 'e12', 'e7', closed=True)
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c1')
