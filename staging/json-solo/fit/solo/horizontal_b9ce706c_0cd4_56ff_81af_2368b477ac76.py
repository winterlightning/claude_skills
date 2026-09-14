"""Horizontal (photography), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b9ce706c-0cd4-56ff-81af-2368b477ac76'
SOURCE_PATH = 'icons-json/photography/horizontal_b9ce706c-0cd4-56ff-81af-2368b477ac76.json'
AUTHOR = 'json_to_solo'

class HorizontalPhotography(Solo48):
    icon_id = 'horizontal-photography'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    aliases = ()
    keywords = ('horizontal', 'photography')

    def build(self):
        self.add_line('e0', (8, 9), (4, 8))
        self.add_line('e1', (4, 8), (4, 40))
        self.add_line('e2', (4, 40), (10, 38))
        self.add_line('e3', (38, 38), (44, 40))
        self.add_line('e4', (44, 40), (44, 8))
        self.add_arc('e5', (44, 8), (8, 9), radius_x=41)
        self.add_arc('e6', (10, 38), (38, 38), radius_x=44)
        self.add_contour('c0', 'e5', 'e0', 'e1', 'e2', 'e6', 'e3', 'e4', closed=True)
