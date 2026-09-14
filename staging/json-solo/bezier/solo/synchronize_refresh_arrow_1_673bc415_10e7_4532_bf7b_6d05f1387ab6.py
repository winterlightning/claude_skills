"""Synchronize refresh arrow 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '673bc415-10e7-4532-bf7b-6d05f1387ab6'
SOURCE_PATH = 'icons-json/interface-essential/synchronize refresh arrow 1_673bc415-10e7-4532-bf7b-6d05f1387ab6.json'
AUTHOR = 'json_to_solo'

class SynchronizeRefreshArrow1673bc415(Solo48):
    icon_id = 'synchronize-refresh-arrow-1-673bc415'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('synchronize', 'refresh', 'arrow', 'interface-essential')

    def build(self):
        self.add_line('e0', (4, 21), (9, 26))
        self.add_line('e1', (14, 21), (10, 24))
        self.add_line('e2', (10, 24), (9, 26))
        self.add_bezier('e3', (25, 40), ((25.282, 40), (25.473, 39.992), (25.755, 39.992)), ((26.036, 39.992), (26.318, 39.992), (26.6, 39.992)), ((26.673, 39.992), (26.745, 40), (26.809, 40)), ((27.045, 40), (27.282, 39.983), (27.518, 39.983)), ((29.055, 39.983), (30.6, 39.579), (32.036, 39.124)), ((38.536, 37.078), (43.991, 31.124), (43.991, 24.573)), ((43.991, 24.448), (44, 24.324), (44, 24.2)), ((44, 24.198), (44, 24.196), (44, 24.194)), ((44, 23.907), (43.991, 23.613), (43.991, 23.326)), ((43.991, 15.251), (35.618, 8.017), (27.009, 8.017)), ((26.839, 8.017), (26.66, 8), (26.49, 8)), ((26.487, 8), (26.485, 8), (26.482, 8)), ((26.1, 8), (25.718, 8.017), (25.336, 8.017)), ((18.718, 8.017), (12.445, 12.379), (9.973, 17.912)), ((8.855, 20.404), (9.173, 23.339), (9, 26)))
        self.add_contour('c0', 'e3')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
