"""Batch-02/bag handle (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e058f399-32d7-55f0-a75e-23168e8b2b79'
SOURCE_PATH = 'icons-json/accessories/batch-02/bag handle_e058f399-32d7-55f0-a75e-23168e8b2b79.json'
AUTHOR = 'json_to_solo'

class Batch02BagHandle(Solo48):
    icon_id = 'batch-02-bag-handle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'bag', 'handle', 'accessories')

    def build(self):
        self.add_line('e0', (16, 19), (16, 12))
        self.add_line('e1', (32, 12), (32, 19))
        self.add_line('e2', (37, 44), (10, 44))
        self.add_line('e3', (9, 27), (10, 15))
        self.add_line('e4', (10, 15), (38, 15))
        self.add_line('e5', (38, 15), (40, 41))
        self.add_bezier('e6', (16, 12), ((16, 7.8), (19.537, 4.009), (23.587, 4.009)), ((23.72, 4.009), (23.844, 4), (23.977, 4)), ((23.979, 4), (23.981, 4), (23.983, 4)), ((24.118, 4), (24.253, 4.009), (24.379, 4.009)), ((28.522, 4.009), (32, 7.727), (32, 12)))
        self.add_bezier('e7', (40, 41), ((40, 41.1), (40, 41.464), (39.992, 41.564)), ((39.992, 43.073), (38.501, 44), (37.221, 44)), ((37.027, 44), (37.194, 44), (37, 44)))
        self.add_bezier('e8', (10, 44), ((9.941, 44), (9.558, 44), (9.499, 44)), ((8.665, 44), (8.008, 43.136), (8.008, 42.291)), ((8.008, 42.103), (8, 41.924), (8, 41.745)), ((8, 41.742), (8, 41.739), (8, 41.736)), ((8, 41.464), (8.008, 41.2), (8.008, 40.936)), ((8.008, 39.445), (8.152, 37.936), (8.236, 36.445)), ((8.413, 33.209), (8.773, 30.236), (9, 27)))
        self.add_contour('c0', 'e0', 'e6', 'e1')
        self.add_contour('c1', 'e7', 'e2', 'e8', 'e3', 'e4', 'e5', closed=True)
