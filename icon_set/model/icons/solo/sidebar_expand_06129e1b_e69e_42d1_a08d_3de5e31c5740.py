"""Sidebar expand (apps), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '06129e1b-e69e-42d1-a08d-3de5e31c5740'
SOURCE_PATH = 'pictographic-primitives/apps/sidebar expand_06129e1b-e69e-42d1-a08d-3de5e31c5740.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class SidebarExpand(Solo48):
    icon_id = 'sidebar-expand'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    categories = ('apps', 'primitives')
    aliases = ()
    keywords = ('sidebar', 'expand', 'apps')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (16, 42), (42, 42))
        self.add_line('e1', (42, 42), (42, 6))
        self.add_line('e2', (42, 6), (16, 6))
        self.add_line('e3', (16, 42), (16, 6))
        self.add_line('e4', (16, 42), (6, 42))
        self.add_line('e5', (6, 42), (6, 6))
        self.add_line('e6', (6, 6), (16, 6))
        self.add_line('e7', (31, 17), (24, 24))
        self.add_line('e8', (24, 24), (31, 31))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=False)
        self.add_contour('c1', 'e3', closed=False)
        self.add_contour('c2', 'e4', 'e5', 'e6', closed=False)
        self.add_contour('c3', 'e7', 'e8', closed=False)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
