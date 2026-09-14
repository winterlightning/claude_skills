"""Cloud (internet), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '75d3488a-6912-4de5-b1c9-1505730ec0ac'
SOURCE_PATH = 'icons-json/internet/cloud_75d3488a-6912-4de5-b1c9-1505730ec0ac.json'
AUTHOR = 'json_to_solo'

class Cloud75d3488a(Solo48):
    icon_id = 'cloud-75d3488a'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'internet'
    aliases = ()
    keywords = ('cloud', 'internet')

    def build(self):
        self.add_line('e0', (37, 40), (12, 40))
        self.add_arc('e1-1', (13, 19), (23, 8), radius_x=12)
        self.add_line('e1-2', (23, 8), (28, 9))
        self.add_arc('e1-3', (28, 9), (31, 11), radius_x=11)
        self.add_arc('e1-4', (31, 11), (35, 20), radius_x=15)
        self.add_line('e1-5', (35, 20), (39, 21))
        self.add_arc('e1-6', (39, 21), (44, 30), radius_x=11)
        self.add_line('e1-7', (44, 30), (43, 35))
        self.add_arc('e1-8', (43, 35), (37, 40), radius_x=9)
        self.add_arc('e2-1', (12, 40), (9, 39), radius_x=5)
        self.add_arc('e2-2', (9, 39), (4, 30), radius_x=11)
        self.add_line('e2-3', (4, 30), (6, 23))
        self.add_arc('e2-4', (6, 23), (13, 19), radius_x=8)
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e0', 'e2-1', 'e2-2', 'e2-3', 'e2-4')
