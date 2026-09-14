"""N (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c93adf0c-a051-45cd-bf10-f241e47b2183'
SOURCE_PATH = 'icons-json/typeface/N_c93adf0c-a051-45cd-bf10-f241e47b2183.json'
AUTHOR = 'json_to_solo'

class NC93adf0c(Solo48):
    icon_id = 'n-c93adf0c'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('n', 'typeface')

    def build(self):
        self.add_line('e0', (8, 44), (8, 5))
        self.add_line('e1', (10, 4), (38, 44))
        self.add_line('e2', (40, 43), (40, 4))
        self.add_bezier('e3', (8, 5), ((8, 4.909), (8, 4.736), (8, 4.645)), ((8, 4.545), (8.14, 4.018), (8.31, 4.018)), ((8.38, 4.009), (8.44, 4.009), (8.51, 4)), ((8.67, 4), (8.83, 4), (8.99, 4)), ((9.17, 4), (9.34, 4), (9.52, 4)), ((9.68, 4), (9.84, 4), (10, 4)))
        self.add_bezier('e4', (38, 44), ((38.13, 44), (38.27, 44), (38.4, 44)), ((38.71, 44), (38.98, 44), (39.28, 44)), ((39.4, 44), (39.53, 44), (39.65, 44)), ((39.87, 44), (40, 43.445), (40, 43.309)), ((40, 43.236), (40, 43.073), (40, 43)))
        self.add_contour('c0', 'e0', 'e3', 'e1', 'e4', 'e2')
