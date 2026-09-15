"""Ui columns (apps), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '87c9b933-0954-4c85-b549-2051219db557'
SOURCE_PATH = 'pictographic-primitives/apps/ui columns_87c9b933-0954-4c85-b549-2051219db557.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class UiColumns(Solo48):
    icon_id = 'ui-columns'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('ui', 'columns', 'apps')

    def build(self):
        self.add_line('e0', (28, 23), (44, 23))
        self.add_line('e1', (28, 23), (28, 40))
        self.add_line('e2', (28, 40), (44, 40))
        self.add_line('e3', (44, 40), (44, 23))
        self.add_line('e4', (28, 23), (28, 8))
        self.add_line('e5', (28, 8), (44, 8))
        self.add_line('e6', (44, 8), (44, 23))
        self.add_line('e7', (5, 8), (19, 8))
        self.add_line('e8', (20, 9), (20, 39))
        self.add_line('e9', (19, 40), (5, 40))
        self.add_line('e10', (4, 39), (4, 9))
        self.add_arc('e11', (4, 9), (5, 8), radius_x=1)
        self.add_arc('e12', (19, 8), (20, 9), radius_x=1)
        self.add_arc('e13', (20, 39), (19, 40), radius_x=1)
        self.add_arc('e14', (5, 40), (4, 39), radius_x=1)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3')
        self.add_contour('c2', 'e4', 'e5', 'e6')
        self.add_contour('c3', 'e11', 'e7', 'e12', 'e8', 'e13', 'e9', 'e14', 'e10', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
