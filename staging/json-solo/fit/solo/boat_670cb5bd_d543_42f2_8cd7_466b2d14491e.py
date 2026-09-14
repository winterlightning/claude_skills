"""Boat (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '670cb5bd-d543-42f2-8cd7-466b2d14491e'
SOURCE_PATH = 'icons-json/transportation/boat_670cb5bd-d543-42f2-8cd7-466b2d14491e.json'
AUTHOR = 'json_to_solo'

class Boat670cb5bd(Solo48):
    icon_id = 'boat-670cb5bd'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('boat', 'transportation')

    def build(self):
        self.add_line('e0', (34, 22), (30, 8))
        self.add_line('e1', (30, 8), (12, 8))
        self.add_line('e2', (12, 8), (9, 22))
        self.add_line('e3', (4, 28), (4, 22))
        self.add_line('e4', (4, 22), (44, 22))
        self.add_line('e5-1', (44, 22), (39, 39))
        self.add_line('e5-2', (39, 39), (37, 40))
        self.add_line('e5-3', (37, 40), (33, 36))
        self.add_line('e5-4', (33, 36), (29, 39))
        self.add_line('e5-5', (29, 39), (26, 40))
        self.add_arc('e5-6', (26, 40), (20, 36), radius_x=8)
        self.add_line('e5-7', (20, 36), (12, 40))
        self.add_line('e5-8', (12, 40), (7, 38))
        self.add_arc('e5-9', (7, 38), (5, 34), radius_x=12)
        self.add_arc('e5-10', (5, 34), (4, 28), radius_x=21)
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7', 'e5-8', 'e5-9', 'e5-10', 'e3', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
