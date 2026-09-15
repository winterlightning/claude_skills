"""Align all four barcode bars to the same top baseline. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7283882e-90f2-40c7-9b79-4b6a6ff8d3b2'
SOURCE_PATH = 'pictographic-primitives/shopping/barcode_7283882e-90f2-40c7-9b79-4b6a6ff8d3b2.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class Barcode7283882e(Solo48):
    icon_id = 'barcode-7283882e'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shopping'
    aliases = ()
    keywords = ('barcode', 'shopping')

    def build(self):
        """Symbol plan: Align all four barcode bars to the same top baseline. Reference: inspected current parent; no useful exact Lucide match selected."""
        self.add_line('e0', (4, 40), (4, 8))
        self.add_line('e1', (31, 40), (31, 8))
        self.add_line('e2', (18, 40), (18, 8))
        self.add_line('e3', (44, 40), (44, 8))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
