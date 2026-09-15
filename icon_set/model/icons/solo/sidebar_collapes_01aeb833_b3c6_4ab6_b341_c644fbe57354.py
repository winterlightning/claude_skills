"""Sidebar collapes (apps), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '01aeb833-b3c6-4ab6-b341-c644fbe57354'
SOURCE_PATH = 'pictographic-primitives/apps/sidebar collapes_01aeb833-b3c6-4ab6-b341-c644fbe57354.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class SidebarCollapes(Solo48):
    icon_id = 'sidebar-collapes'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('sidebar', 'collapes', 'apps')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (32, 8), (44, 8))
        self.add_line('e1', (44, 8), (44, 40))
        self.add_line('e2', (44, 40), (32, 40))
        self.add_line('e3', (32, 8), (32, 40))
        self.add_line('e4', (32, 8), (4, 8))
        self.add_line('e5', (4, 8), (4, 40))
        self.add_line('e6', (4, 40), (32, 40))
        self.add_line('e7', (17, 18), (23, 24))
        self.add_line('e8', (23, 24), (17, 30))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=False)
        self.add_contour('c1', 'e3', closed=False)
        self.add_contour('c2', 'e4', 'e5', 'e6', closed=False)
        self.add_contour('c3', 'e7', 'e8', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
