"""Shield (protection), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd8e95c74-2bc0-454c-bd2c-1f55b945beca'
SOURCE_PATH = 'icons-json/protection/shield_d8e95c74-2bc0-454c-bd2c-1f55b945beca.json'
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
        self.add_line('e0', (15, 9), (24, 4))
        self.add_line('e1', (24, 4), (33, 9))
        self.add_line('e2', (37, 9), (40, 8))
        self.add_line('e3', (8, 24), (8, 8))
        self.add_line('e4', (40, 21), (8, 21))
        self.add_bezier('e5', (8, 8), ((9.524, 8.882), (13.232, 10.045), (15, 9)))
        self.add_bezier('e6', (33, 9), ((34.389, 9.818), (35.594, 9.755), (37, 9)))
        self.add_bezier('e7', (40, 8), ((39.966, 12.545), (40, 16.727), (40, 21.273)), ((40, 21.555), (39.983, 21.827), (39.983, 22.109)), ((39.983, 23.255), (40, 24.609), (39.798, 25.736)), ((38.467, 31.682), (34.316, 36.2), (30.063, 39.945)), ((29.078, 40.818), (25.12, 44), (24.042, 44)), ((24.041, 44), (24.041, 44), (24.04, 44)), ((23.99, 44), (23.94, 43.991), (23.891, 43.991)), ((22.728, 43.991), (19.495, 41.227), (18.509, 40.4)), ((14.232, 36.809), (9.853, 32.491), (8.438, 26.645)), ((8.236, 25.809), (8, 24.864), (8, 24)))
        self.add_contour('c0', 'e5', 'e0', 'e1', 'e6', 'e2', 'e7', 'e3')
        self.add_contour('c1', 'e4')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
