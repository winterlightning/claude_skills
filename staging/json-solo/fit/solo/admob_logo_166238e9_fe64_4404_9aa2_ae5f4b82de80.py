"""Admob logo (_uncategorized_01), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '166238e9-fe64-4404-9aa2-ae5f4b82de80'
SOURCE_PATH = 'icons-json/_uncategorized_01/admob logo_166238e9-fe64-4404-9aa2-ae5f4b82de80.json'
AUTHOR = 'json_to_solo'

class AdmobLogoUncategorized01(Solo48):
    icon_id = 'admob-logo-uncategorized-01'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_01'
    aliases = ()
    keywords = ('admob', 'logo', '_uncategorized_01')

    def build(self):
        self.add_line('e0', (22, 43), (14, 43))
        self.add_line('e1', (8, 37), (8, 19))
        self.add_line('e2', (40, 19), (40, 39))
        self.add_line('e3', (29, 36), (20, 36))
        self.add_line('e4', (19, 34), (19, 19))
        self.add_line('e5', (29, 19), (29, 36))
        self.add_arc('e6', (14, 43), (8, 37), radius_x=7)
        self.add_arc('e7-1', (8, 19), (24, 4), radius_x=17)
        self.add_arc('e7-2', (24, 4), (40, 19), radius_x=17)
        self.add_arc('e8-1', (40, 39), (35, 44), radius_x=5)
        self.add_line('e8-2', (35, 44), (30, 42))
        self.add_arc('e8-3', (30, 42), (29, 36), radius_x=10)
        self.add_arc('e9', (20, 36), (19, 34), radius_x=2)
        self.add_arc('e10', (19, 19), (29, 19), radius_x=5)
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e7-1', 'e7-2', 'e2', 'e8-1', 'e8-2', 'e8-3')
        self.add_contour('c1', 'e3', 'e9', 'e4', 'e10', 'e5', closed=True)
        self.relate('connect', 'c0', 'c1')
