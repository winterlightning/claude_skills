"""Synchronize refresh arrow 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a62fd369-1873-5c25-af42-83eb6dd463a0'
SOURCE_PATH = 'icons-json/interface-essential/synchronize refresh arrow 1_a62fd369-1873-5c25-af42-83eb6dd463a0.json'
AUTHOR = 'json_to_solo'

class SynchronizeRefreshArrow1A62fd369(Solo48):
    icon_id = 'synchronize-refresh-arrow-1-a62fd369'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('synchronize', 'refresh', 'arrow', 'interface-essential')

    def build(self):
        self.add_line('e0', (9, 26), (4, 22))
        self.add_line('e1', (14, 21), (9, 26))
        self.add_bezier('e2', (10, 32), ((12.573, 35.672), (15.782, 37.735), (20.327, 39.175)), ((21.764, 39.629), (23.436, 40), (24.964, 40)), ((24.966, 40), (24.968, 40), (24.97, 40)), ((25.114, 40), (25.266, 40), (25.409, 40)), ((25.791, 40), (26.164, 39.983), (26.536, 39.983)), ((35.573, 39.983), (43.991, 32.749), (43.991, 24.244)), ((43.991, 24.178), (44, 24.112), (44, 24.045)), ((44, 24.044), (44, 24.043), (44, 24.042)), ((43.991, 23.916), (43.991, 23.789), (43.982, 23.663)), ((43.982, 15.149), (35.427, 8.008), (26.445, 8.008)), ((26.15, 8.008), (25.846, 8), (25.55, 8)), ((25.546, 8), (25.541, 8), (25.536, 8)), ((25.245, 8), (24.955, 8.008), (24.664, 8.008)), ((22.445, 8.008), (19.964, 8.775), (17.991, 9.676)), ((10.945, 12.876), (8.318, 18.884), (9, 26)))
        self.add_contour('c0', 'e2', 'e0')
        self.add_contour('c1', 'e1')
