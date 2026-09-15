"""Ui columns (apps), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '87c9b933-0954-4c85-b549-2051219db557'
SOURCE_PATH = 'pictographic-primitives/apps/ui columns_87c9b933-0954-4c85-b549-2051219db557.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class UiColumns(Solo48):
    icon_id = 'ui-columns'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('ui', 'columns', 'apps')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('e0', (28, 23), (44, 23))
        self.add_line('e1', (28, 23), (28, 40))
        self.add_line('e2', (28, 40), (44, 40))
        self.add_line('e3', (44, 40), (44, 23))
        self.add_line('e4', (28, 23), (28, 8))
        self.add_line('e5', (28, 8), (44, 8))
        self.add_line('e6', (44, 8), (44, 23))
        self.add_line('e7', (4, 8), (20, 8))
        self.add_line('e8', (20, 8), (20, 40))
        self.add_line('e9', (20, 40), (4, 40))
        self.add_line('e10', (4, 40), (4, 8))
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', 'e2', 'e3', closed=False)
        self.add_contour('c2', 'e4', 'e5', 'e6', closed=False)
        self.add_contour('c3', 'e7', 'e8', 'e9', 'e10', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
