"""Trekking shelter (outdoors), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '88470bfe-b79f-53bc-a66c-39911133467b'
SOURCE_PATH = 'icons-json/outdoors/trekking shelter_88470bfe-b79f-53bc-a66c-39911133467b.json'
AUTHOR = 'json_to_solo'

class TrekkingShelter(Solo48):
    icon_id = 'trekking-shelter'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('trekking', 'shelter', 'outdoors')

    def build(self):
        self.add_line('e0', (35, 42), (38, 42))
        self.add_line('e1', (38, 42), (38, 19))
        self.add_line('e2', (35, 42), (34, 40))
        self.add_line('e3', (34, 40), (26, 25))
        self.add_line('e4', (26, 25), (24, 22))
        self.add_line('e5', (24, 22), (22, 25))
        self.add_line('e6', (22, 25), (14, 40))
        self.add_line('e7', (14, 40), (13, 42))
        self.add_line('e8', (35, 42), (13, 42))
        self.add_line('e9', (6, 24), (10, 20))
        self.add_line('e10', (10, 20), (10, 22))
        self.add_line('e11', (42, 23), (38, 19))
        self.add_line('e12', (38, 19), (25, 6))
        self.add_line('e13', (23, 6), (10, 20))
        self.add_line('e14-1', (10, 22), (10, 41))
        self.add_arc('e14-2', (10, 41), (10, 42), radius_x=1, sweep=False)
        self.add_arc('e14-3', (10, 42), (12, 42), radius_x=7)
        self.add_arc('e14-4', (12, 42), (13, 42), radius_x=22)
        self.add_line('e15', (25, 6), (23, 6))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7')
        self.add_contour('c2', 'e8')
        self.add_contour('c3', 'e9', 'e10', 'e14-1', 'e14-2', 'e14-3', 'e14-4')
        self.add_contour('c4', 'e11')
        self.add_contour('c5', 'e12', 'e15', 'e13')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
