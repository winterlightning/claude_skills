"""Rhombus vertical shape (design), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '36f9de4e-504c-5766-aa5a-8f53dfc7eb8b'
SOURCE_PATH = 'icons-json/design/rhombus vertical shape_36f9de4e-504c-5766-aa5a-8f53dfc7eb8b.json'
AUTHOR = 'json_to_solo'

class RhombusVerticalShapeDesign(Solo48):
    icon_id = 'rhombus-vertical-shape-design'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('rhombus', 'vertical', 'shape', 'design')

    def build(self):
        self.add_line('e0', (22, 42), (10, 28))
        self.add_line('e1', (8, 23), (20, 8))
        self.add_line('e2', (26, 7), (40, 23))
        self.add_line('e3', (40, 25), (25, 44))
        self.add_line('e4', (25, 44), (22, 42))
        self.add_line('e5-1', (10, 28), (8, 25))
        self.add_line('e5-2', (8, 25), (8, 23))
        self.add_arc('e6-1', (20, 8), (24, 4), radius_x=23)
        self.add_line('e6-2', (24, 4), (26, 7))
        self.add_arc('e7', (40, 23), (40, 25), radius_x=21, sweep=False)
        self.add_contour('c0', 'e4', 'e0', 'e5-1', 'e5-2', 'e1', 'e6-1', 'e6-2', 'e2', 'e7', 'e3', closed=True)
