"""Shield (protection), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e1100ca-39fe-4e71-b978-93997ec5e7d8'
SOURCE_PATH = 'icons-json/protection/shield_8e1100ca-39fe-4e71-b978-93997ec5e7d8.json'
AUTHOR = 'json_to_solo'

class Shield(Solo48):
    icon_id = 'shield'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('shield', 'protection')

    def build(self):
        self.add_line('e0', (40, 10), (34, 9))
        self.add_line('e1', (34, 9), (28, 6))
        self.add_line('e2', (28, 6), (24, 4))
        self.add_line('e3', (24, 4), (13, 9))
        self.add_line('e4', (13, 9), (8, 10))
        self.add_bezier('e5', (8, 10), ((8, 11.927), (8.017, 14.218), (8.017, 16.136)), ((8.017, 17.709), (8.202, 19.291), (8.387, 20.845)), ((9.272, 28.345), (12.017, 35.018), (17.482, 39.9)), ((18.568, 40.873), (22.678, 44), (23.949, 44)), ((23.971, 44), (23.994, 44), (24.017, 44)), ((25.457, 44), (28.902, 41.34), (30.046, 40.4)), ((35.453, 35.964), (38.408, 29.064), (39.503, 21.982)), ((39.722, 20.536), (39.992, 19.009), (39.992, 17.536)), ((39.992, 17.464), (40, 17.382), (40, 17.309)), ((40, 15.8), (40, 14.282), (40, 12.773)), ((40, 12.2), (40, 11.618), (40, 11.045)), ((40, 10.818), (40, 9.773), (40, 10)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', closed=True)
