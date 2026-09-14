"""Canoe (outdoors), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2f08daf6-071b-5ac7-9717-2239ffbb2925'
SOURCE_PATH = 'icons-json/outdoors/canoe_2f08daf6-071b-5ac7-9717-2239ffbb2925.json'
AUTHOR = 'json_to_solo'

class CanoeOutdoors(Solo48):
    icon_id = 'canoe-outdoors'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('canoe', 'outdoors')

    def build(self):
        self.add_line('e0', (15, 40), (20, 40))
        self.add_line('e1-1', (20, 40), (33, 39))
        self.add_arc('e1-2', (33, 39), (40, 35), radius_x=13, sweep=False)
        self.add_line('e1-3', (40, 35), (43, 30))
        self.add_line('e1-4', (43, 30), (44, 19))
        self.add_arc('e1-5', (44, 19), (43, 8), radius_x=68, sweep=False)
        self.add_arc('e1-6', (43, 8), (24, 21), radius_x=22)
        self.add_arc('e1-7', (24, 21), (5, 8), radius_x=23)
        self.add_line('e1-8', (5, 8), (4, 21))
        self.add_arc('e1-9', (4, 21), (5, 28), radius_x=31, sweep=False)
        self.add_arc('e1-10', (5, 28), (7, 34), radius_x=20, sweep=False)
        self.add_arc('e1-11', (7, 34), (15, 40), radius_x=12, sweep=False)
        self.add_contour('c0', 'e0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e1-9', 'e1-10', 'e1-11', closed=True)
