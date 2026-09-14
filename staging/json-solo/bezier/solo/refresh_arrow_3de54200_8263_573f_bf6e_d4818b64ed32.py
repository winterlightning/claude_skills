"""Refresh arrow (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3de54200-8263-573f-bf6e-d4818b64ed32'
SOURCE_PATH = 'icons-json/interface-essential/refresh arrow_3de54200-8263-573f-bf6e-d4818b64ed32.json'
AUTHOR = 'json_to_solo'

class RefreshArrowInterfaceEssential(Solo48):
    icon_id = 'refresh-arrow-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('refresh', 'arrow', 'interface-essential')

    def build(self):
        self.add_line('e0', (6, 38), (14, 38))
        self.add_line('e1', (14, 38), (14, 29))
        self.add_bezier('e2', (21, 41), ((22.309, 41.221), (24, 41.984), (25.268, 41.984)), ((25.391, 41.992), (25.514, 41.992), (25.636, 42)), ((25.638, 42), (25.64, 42), (25.642, 42)), ((25.763, 42), (25.876, 41.992), (25.996, 41.992)), ((26.929, 41.992), (27.837, 41.64), (28.737, 41.419)), ((36.142, 39.627), (41.992, 32.272), (41.992, 24.614)), ((41.992, 24.493), (42, 24.38), (42, 24.267)), ((42, 24.265), (42, 24.264), (42, 24.262)), ((42, 23.918), (41.984, 23.575), (41.984, 23.239)), ((41.984, 15.033), (35.315, 7.538), (27.289, 6.278)), ((26.561, 6.164), (25.8, 6), (25.064, 6)), ((25.062, 6), (25.061, 6), (25.059, 6)), ((24.971, 6), (24.89, 6), (24.802, 6)), ((24.548, 6), (24.295, 6.016), (24.041, 6.016)), ((12.742, 6.016), (6, 16.898), (6.892, 27.78)), ((7.849, 32.19), (9.85, 34.924), (13, 38)))
        self.add_contour('c0', 'e2')
        self.add_contour('c1', 'e0', 'e1')
        self.relate('connect', 'c0', 'c1')
