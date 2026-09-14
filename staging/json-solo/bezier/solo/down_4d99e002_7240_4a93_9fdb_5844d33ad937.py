"""Down (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4d99e002-7240-4a93-9fdb-5844d33ad937'
SOURCE_PATH = 'icons-json/arrows/down_4d99e002-7240-4a93-9fdb-5844d33ad937.json'
AUTHOR = 'json_to_solo'

class Down(Solo48):
    icon_id = 'down'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('down', 'arrows')

    def build(self):
        self.add_line('e0', (4, 8), (24, 27))
        self.add_line('e1', (24, 27), (44, 8))
        self.add_line('e2', (44, 8), (44, 21))
        self.add_line('e3', (43, 23), (26, 39))
        self.add_line('e4', (23, 39), (5, 23))
        self.add_line('e5', (5, 23), (4, 21))
        self.add_line('e6', (4, 21), (4, 8))
        self.add_bezier('e7', (44, 21), ((44, 21.564), (43.418, 22.613), (43, 23)))
        self.add_bezier('e8', (26, 39), ((25.773, 39.211), (24.873, 40), (24.545, 40)), ((24.539, 40), (24.532, 40), (24.525, 40)), ((24.093, 40), (23.304, 39.265), (23, 39)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e7', 'e3', 'e8', 'e4', 'e5', 'e6', closed=True)
