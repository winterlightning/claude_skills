"""Flag 1 (social), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eb4576b3-c5b1-4d1c-8e23-fbb925182d9a'
SOURCE_PATH = 'icons-json/social/flag 1_eb4576b3-c5b1-4d1c-8e23-fbb925182d9a.json'
AUTHOR = 'json_to_solo'

class Flag1Social(Solo48):
    icon_id = 'flag-1-social'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'social'
    aliases = ()
    keywords = ('flag', 'social')

    def build(self):
        self.add_line('e0', (4, 40), (4, 10))
        self.add_line('e1', (4, 10), (10, 8))
        self.add_line('e2', (44, 11), (44, 37))
        self.add_line('e3', (30, 39), (17, 36))
        self.add_bezier('e4', (10, 8), ((10.518, 8), (11.391, 8), (11.909, 8)), ((12.545, 8), (13.182, 8.01), (13.818, 8.01)), ((13.891, 8.01), (13.973, 8), (14.045, 8)), ((14.191, 8), (14.336, 8.01), (14.482, 8.01)), ((20.964, 8.01), (27.045, 11.68), (33.564, 11.4)), ((35.464, 11.32), (37.464, 11.01), (39.327, 10.57)), ((40.036, 10.4), (41.827, 9.76), (42.564, 9.99)), ((43.209, 10.2), (43.491, 10.55), (44, 11)))
        self.add_bezier('e5', (44, 37), ((43.909, 37.11), (43.818, 37.21), (43.727, 37.32)), ((40.936, 39.22), (33.173, 39.7), (30, 39)))
        self.add_bezier('e6', (17, 36), ((16.373, 35.86), (15.373, 35.92), (14.727, 35.92)), ((11.064, 35.89), (7.482, 36.84), (4, 38)))
        self.add_contour('c0', 'e0', 'e1', 'e4', 'e2', 'e5', 'e3', 'e6')
