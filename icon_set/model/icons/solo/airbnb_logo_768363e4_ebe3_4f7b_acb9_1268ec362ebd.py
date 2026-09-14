"""Airbnb logo (_uncategorized_01), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '768363e4-ebe3-4f7b-acb9-1268ec362ebd'
SOURCE_PATH = 'icons-json/_uncategorized_01/airbnb logo_768363e4-ebe3-4f7b-acb9-1268ec362ebd.json'
AUTHOR = 'json_to_solo'

class AirbnbLogo(Solo48):
    icon_id = 'airbnb-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_01'
    aliases = ()
    keywords = ('airbnb', 'logo', '_uncategorized_01')

    def build(self):
        self.add_arc('sym-e1', (24, 19), (23, 19), radius_x=4)
        self.add_arc('sym-e2', (23, 19), (21, 20), radius_x=6)
        self.add_arc('sym-e3', (21, 20), (21, 33), radius_x=8, sweep=False)
        self.add_arc('sym-e4', (21, 33), (23, 36), radius_x=25, sweep=False)
        self.add_line('sym-e6', (23, 36), (24, 37))
        self.add_arc('sym-e7', (24, 37), (22, 38), radius_x=53, sweep=False)
        self.add_arc('sym-e8', (22, 38), (14, 42), radius_x=12)
        self.add_line('sym-e11-1', (14, 42), (8, 40))
        self.add_line('sym-e11-2', (8, 40), (6, 35))
        self.add_line('sym-e13', (6, 35), (6, 34))
        self.add_arc('sym-e14', (6, 34), (7, 31), radius_x=6, sweep=False)
        self.add_line('sym-e15', (7, 31), (19, 9))
        self.add_arc('sym-e16', (19, 9), (24, 6), radius_x=6)
        self.add_arc('sym-e17', (24, 6), (29, 9), radius_x=6)
        self.add_line('sym-e18', (29, 9), (41, 31))
        self.add_line('sym-e19', (41, 31), (42, 34))
        self.add_line('sym-e20', (42, 34), (42, 35))
        self.add_line('sym-e22-1', (42, 35), (40, 40))
        self.add_line('sym-e22-2', (40, 40), (34, 42))
        self.add_arc('sym-e25', (34, 42), (26, 38), radius_x=13)
        self.add_arc('sym-e26', (26, 38), (24, 37), radius_x=53, sweep=False)
        self.add_line('sym-e27', (24, 37), (25, 36))
        self.add_arc('sym-e29', (25, 36), (27, 33), radius_x=25, sweep=False)
        self.add_arc('sym-e30', (27, 33), (27, 20), radius_x=8, sweep=False)
        self.add_arc('sym-e31', (27, 20), (25, 19), radius_x=6)
        self.add_arc('sym-e32', (25, 19), (24, 19), radius_x=4)
        self.add_contour('sym-c0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e11-1', 'sym-e11-2', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e22-1', 'sym-e22-2', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', closed=True)
