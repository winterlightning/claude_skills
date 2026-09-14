"""Circle messages bubble (other), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f97107e-f15e-42cb-ae76-2769af6c5f64'
SOURCE_PATH = 'icons-json/other/circle messages bubble_5f97107e-f15e-42cb-ae76-2769af6c5f64.json'
AUTHOR = 'json_to_solo'

class CircleMessagesBubbleOther(Solo48):
    icon_id = 'circle-messages-bubble-other'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('circle', 'messages', 'bubble', 'other')

    def build(self):
        self.add_line('e0-1', (5, 40), (8, 37))
        self.add_arc('e0-2', (8, 37), (9, 33), radius_x=3, sweep=False)
        self.add_arc('e0-3', (9, 33), (4, 23), radius_x=13)
        self.add_arc('e0-4', (4, 23), (8, 14), radius_x=13)
        self.add_arc('e0-5', (8, 14), (23, 8), radius_x=22)
        self.add_line('e0-6', (23, 8), (32, 9))
        self.add_arc('e0-7', (32, 9), (40, 14), radius_x=21)
        self.add_arc('e0-8', (40, 14), (44, 23), radius_x=13)
        self.add_arc('e0-9', (44, 23), (38, 34), radius_x=14)
        self.add_arc('e0-10', (38, 34), (28, 38), radius_x=23)
        self.add_arc('e0-11', (28, 38), (16, 37), radius_x=24)
        self.add_line('e0-12', (16, 37), (6, 40))
        self.add_line('e0-13', (6, 40), (5, 40))
        self.add_contour('c0', 'e0-1', 'e0-2', 'e0-3', 'e0-4', 'e0-5', 'e0-6', 'e0-7', 'e0-8', 'e0-9', 'e0-10', 'e0-11', 'e0-12', 'e0-13', closed=True)
