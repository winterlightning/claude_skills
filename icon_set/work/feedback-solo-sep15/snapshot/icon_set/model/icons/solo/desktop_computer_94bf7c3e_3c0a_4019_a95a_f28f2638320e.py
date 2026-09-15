"""Batch-02/desktop computer (computers), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '94bf7c3e-3c0a-4019-a95a-f28f2638320e'
SOURCE_PATH = 'pictographic-primitives/computers/batch-02/desktop computer_94bf7c3e-3c0a-4019-a95a-f28f2638320e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Batch02DesktopComputerComputers(Solo48):
    icon_id = 'batch-02-desktop-computer-computers'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    aliases = ()
    keywords = ('batch', 'desktop', 'computer', 'computers')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (6, 25), (42, 25))
        self.add_line('e1', (14, 42), (34, 42))
        self.add_line('e2', (17, 33), (17, 42))
        self.add_line('e3', (31, 33), (31, 42))
        self.add_line('e4', (6, 6), (6, 33))
        self.add_line('e5', (6, 33), (42, 33))
        self.add_line('e6', (42, 33), (42, 6))
        self.add_line('e7', (42, 6), (6, 6))
        self.add_arc('e8', (42, 25), (40, 25), radius_x=47, radius_y=47, large_arc=False, sweep=True)
        self.add_contour('c0', 'e0', 'e8', closed=False)
        self.add_contour('c1', 'e1', closed=False)
        self.add_contour('c2', 'e2', closed=False)
        self.add_contour('c3', 'e3', closed=False)
        self.add_contour('c4', 'e4', 'e5', 'e6', 'e7', closed=True)
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c1')
