"""Expand diagonal 3 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'acffab5a-172c-4c47-9753-9303f8489856'
SOURCE_PATH = 'pictographic-primitives/interface-essential/expand diagonal 3_acffab5a-172c-4c47-9753-9303f8489856.svg'
AUTHOR = 'gpt-6'

class ExpandDiagonal3(Solo48):
    icon_id = 'expand-diagonal-3'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('expand', 'diagonal', 'interface-essential')

    def build(self):
        self.add_line('e0', (30, 6), (42, 6))
        self.add_line('e2', (6, 30), (6, 42))
        self.add_line('e3', (18, 42), (6, 42))
        self.add_line('e4', (42, 18), (42, 6))
        self.add_line('e5', (42, 6), (6, 42))
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e2', closed=False)
        self.add_contour('c2', 'e3', closed=False)
        self.add_contour('c3', 'e4', closed=False)
        self.add_contour('c4', 'e5', closed=False)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
