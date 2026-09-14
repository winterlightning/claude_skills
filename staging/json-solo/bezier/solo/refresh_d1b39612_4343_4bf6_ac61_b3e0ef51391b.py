"""Refresh (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd1b39612-4343-4bf6-ac61-b3e0ef51391b'
SOURCE_PATH = 'icons-json/interface-essential/refresh_d1b39612-4343-4bf6-ac61-b3e0ef51391b.json'
AUTHOR = 'json_to_solo'

class RefreshD1b39612(Solo48):
    icon_id = 'refresh-d1b39612'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('refresh', 'interface-essential')

    def build(self):
        self.add_line('e0', (37, 13), (40, 16))
        self.add_line('e1', (40, 6), (40, 16))
        self.add_line('e2', (40, 16), (31, 16))
        self.add_bezier('e3', (42, 26), ((40.977, 33.167), (35.487, 39.979), (28.295, 41.517)), ((27.412, 41.705), (26.422, 41.984), (25.514, 41.984)), ((25.244, 41.984), (24.982, 42), (24.712, 42)), ((24.707, 42), (24.702, 42), (24.696, 42)), ((24.374, 42), (24.044, 41.984), (23.722, 41.984)), ((15.851, 41.984), (8.626, 36.297), (6.622, 28.737)), ((6.295, 27.518), (6.008, 26.275), (6.008, 25.006)), ((6.008, 24.749), (6, 24.491), (6, 24.233)), ((6, 24.229), (6, 24.225), (6, 24.221)), ((6, 23.959), (6.016, 23.697), (6.016, 23.435)), ((6.016, 22.061), (6.295, 20.735), (6.646, 19.41)), ((9.044, 10.402), (18.42, 6), (27.461, 6.843)), ((31.315, 7.628), (34.259, 10.259), (37, 13)))
        self.add_contour('c0', 'e3', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
