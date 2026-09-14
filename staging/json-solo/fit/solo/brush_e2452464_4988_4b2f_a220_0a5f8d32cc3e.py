"""Batch-01/brush (decoration), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e2452464-4988-4b2f-a220-0a5f8d32cc3e'
SOURCE_PATH = 'icons-json/decoration/batch-01/brush_e2452464-4988-4b2f-a220-0a5f8d32cc3e.json'
AUTHOR = 'json_to_solo'

class Batch01Brush(Solo48):
    icon_id = 'batch-01-brush'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    aliases = ()
    keywords = ('batch', 'brush', 'decoration')

    def build(self):
        self.add_line('e0', (8, 37), (9, 32))
        self.add_line('e1', (22, 32), (26, 29))
        self.add_line('e2', (17, 27), (21, 22))
        self.add_line('e3', (21, 22), (38, 7))
        self.add_line('e4', (42, 10), (29, 26))
        self.add_line('e5', (29, 26), (26, 29))
        self.add_line('e6', (17, 27), (22, 32))
        self.add_arc('e7-1', (22, 32), (17, 41), radius_x=8)
        self.add_line('e7-2', (17, 41), (10, 42))
        self.add_arc('e7-3', (10, 42), (6, 41), radius_x=10)
        self.add_arc('e7-4', (6, 41), (8, 37), radius_x=7, sweep=False)
        self.add_arc('e8', (9, 32), (17, 27), radius_x=6)
        self.add_line('e9-1', (38, 7), (40, 6))
        self.add_arc('e9-2', (40, 6), (42, 8), radius_x=2)
        self.add_arc('e9-3', (42, 8), (42, 10), radius_x=22, sweep=False)
        self.add_contour('c0', 'e6')
        self.add_contour('c1', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e0', 'e8')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e2', 'e3', 'e9-1', 'e9-2', 'e9-3', 'e4', 'e5')
