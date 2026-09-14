"""Cough (health), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc3ea9f7-36ca-4b3a-a099-e36c89039b41'
SOURCE_PATH = 'icons-json/health/cough_bc3ea9f7-36ca-4b3a-a099-e36c89039b41.json'
AUTHOR = 'json_to_solo'

class CoughHealth(Solo48):
    icon_id = 'cough-health'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('cough', 'health')

    def build(self):
        self.add_line('e0', (35, 44), (35, 36))
        self.add_line('e1', (11, 14), (8, 27))
        self.add_line('e2', (8, 27), (12, 27))
        self.add_line('e3', (12, 27), (12, 33))
        self.add_line('e4', (16, 37), (19, 38))
        self.add_line('e5', (20, 39), (20, 44))
        self.add_bezier('e6', (35, 36), ((35, 35.191), (37.019, 31.973), (37.499, 31.027)), ((38.964, 28.073), (39.992, 24.391), (39.992, 21.018)), ((39.992, 20.911), (40, 20.803), (40, 20.696)), ((40, 20.694), (40, 20.693), (40, 20.691)), ((40, 20.355), (39.992, 20.027), (39.992, 19.691)), ((39.992, 11.618), (33.962, 4.009), (26.257, 4.009)), ((26.133, 4.009), (26, 4), (25.875, 4)), ((25.873, 4), (25.871, 4), (25.869, 4)), ((25.566, 4), (25.272, 4.009), (24.968, 4.009)), ((20.076, 4.009), (15.301, 7.118), (12.589, 11.409)), ((12.093, 12.191), (11.244, 13.082), (11, 14)))
        self.add_bezier('e7', (12, 33), ((12, 34.882), (14.501, 36.591), (16, 37)))
        self.add_bezier('e8', (19, 38), ((19.093, 38.082), (19.225, 37.727), (19.335, 37.818)), ((19.579, 38.018), (19.832, 38.755), (20, 39)))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e2', 'e3', 'e7', 'e4', 'e8', 'e5')
