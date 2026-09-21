"""A5 (state), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '970a6cde-a55d-4c40-bc6d-1f90c47200b1'
SOURCE_PATH = 'icons-json/state/A5_970a6cde-a55d-4c40-bc6d-1f90c47200b1.json'
AUTHOR = 'json_to_solo'

class A5(Solo48):
    icon_id = 'a5'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('a5', 'state')

    def build(self):
        self.add_line('e0', (21, 40), (15, 10))
        self.add_line('e1', (11, 9), (4, 40))
        self.add_line('e2', (7, 29), (19, 29))
        self.add_line('e3', (43, 8), (33, 8))
        self.add_line('e4', (33, 8), (31, 23))
        self.add_line('e5-1', (15, 10), (13, 8))
        self.add_line('e5-2', (13, 8), (11, 9))
        self.add_arc('e6-1', (31, 23), (36, 20), radius_x=9)
        self.add_arc('e6-2', (36, 20), (42, 22), radius_x=7)
        self.add_line('e6-3', (42, 22), (44, 29))
        self.add_line('e6-4', (44, 29), (42, 37))
        self.add_arc('e6-5', (42, 37), (37, 40), radius_x=6)
        self.add_line('e6-6', (37, 40), (34, 39))
        self.add_arc('e6-7', (34, 39), (31, 35), radius_x=7)
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e4', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5', 'e6-6', 'e6-7')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
