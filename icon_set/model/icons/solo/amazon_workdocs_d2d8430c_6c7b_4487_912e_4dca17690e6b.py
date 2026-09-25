"""Amazon workdocs (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd2d8430c-6c7b-4487-912e-4dca17690e6b'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/amazon workdocs_d2d8430c-6c7b-4487-912e-4dca17690e6b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class AmazonWorkdocs(Solo48):
    icon_id = 'amazon-workdocs'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('amazon', 'workdocs', '_uncategorized_03')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (25, 31), (25, 42))
        self.add_line('e1', (27, 6), (42, 21))
        self.add_line('e2', (27, 6), (27, 21))
        self.add_line('e3', (27, 21), (42, 21))
        self.add_line('e4', (27, 6), (6, 6))
        self.add_line('e5', (6, 6), (6, 42))
        self.add_line('e6', (6, 42), (25, 42))
        self.add_line('e7', (42, 21), (42, 42))
        self.add_line('e8', (42, 42), (25, 42))
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', closed=False)
        self.add_contour('c2', 'e2', 'e3', closed=False)
        self.add_contour('c3', 'e4', 'e5', 'e6', closed=False)
        self.add_contour('c4', 'e7', 'e8', closed=False)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
