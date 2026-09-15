"""Batch-02/desktop computer (computers), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '94bf7c3e-3c0a-4019-a95a-f28f2638320e'
SOURCE_PATH = 'pictographic-primitives/computers/batch-02/desktop computer_94bf7c3e-3c0a-4019-a95a-f28f2638320e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Batch02DesktopComputerComputers(Solo48):
    icon_id = 'batch-02-desktop-computer-computers'
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
        self.add_arc('e8', (42, 25), (40, 25), radius_x=47)
        self.add_line('e9', (8, 6), (6, 8))
        self.add_line('e10', (6, 31), (8, 33))
        self.add_line('e11', (40, 33), (42, 31))
        self.add_line('e12', (42, 8), (40, 6))
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
