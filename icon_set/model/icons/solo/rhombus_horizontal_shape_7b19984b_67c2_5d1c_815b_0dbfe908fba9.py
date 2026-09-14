"""Rhombus horizontal shape (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7b19984b-67c2-5d1c-815b-0dbfe908fba9'
SOURCE_PATH = 'icons-json/design/rhombus horizontal shape_7b19984b-67c2-5d1c-815b-0dbfe908fba9.json'
AUTHOR = 'json_to_solo'

class RhombusHorizontalShape(Solo48):
    icon_id = 'rhombus-horizontal-shape'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('rhombus', 'horizontal', 'shape', 'design')

    def build(self):
        self.add_line('e0', (8, 20), (22, 9))
        self.add_line('e1', (25, 8), (43, 22))
        self.add_line('e2', (42, 27), (26, 39))
        self.add_line('e3', (21, 38), (4, 25))
        self.add_line('e4-1', (22, 9), (24, 8))
        self.add_arc('e4-2', (24, 8), (25, 8), radius_x=41, sweep=False)
        self.add_line('e5-1', (43, 22), (44, 24))
        self.add_arc('e5-2', (44, 24), (42, 27), radius_x=4)
        self.add_line('e6-1', (26, 39), (24, 40))
        self.add_line('e6-2', (24, 40), (21, 38))
        self.add_arc('e7', (4, 25), (8, 20), radius_x=6)
        self.add_contour('c0', 'e0', 'e4-1', 'e4-2', 'e1', 'e5-1', 'e5-2', 'e2', 'e6-1', 'e6-2', 'e3', 'e7', closed=True)
