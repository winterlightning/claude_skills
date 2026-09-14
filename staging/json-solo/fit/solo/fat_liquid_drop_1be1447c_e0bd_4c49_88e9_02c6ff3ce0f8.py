"""Fat liquid drop (drinks), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1be1447c-e0bd-4c49-88e9-02c6ff3ce0f8'
SOURCE_PATH = 'icons-json/drinks/fat liquid drop_1be1447c-e0bd-4c49-88e9-02c6ff3ce0f8.json'
AUTHOR = 'json_to_solo'

class FatLiquidDrop1be1447c(Solo48):
    icon_id = 'fat-liquid-drop-1be1447c'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'drinks'
    aliases = ()
    keywords = ('fat', 'liquid', 'drop', 'drinks')

    def build(self):
        self.add_line('sym-e0', (22, 7), (14, 18))
        self.add_arc('sym-e1', (14, 18), (8, 30), radius_x=31, sweep=False)
        self.add_line('sym-e2', (8, 30), (8, 31))
        self.add_arc('sym-e4', (8, 31), (9, 35), radius_x=10, sweep=False)
        self.add_arc('sym-e5', (9, 35), (23, 44), radius_x=16, sweep=False)
        self.add_line('sym-e6', (23, 44), (24, 44))
        self.add_arc('sym-e9', (24, 44), (25, 44), radius_x=29)
        self.add_arc('sym-e10', (25, 44), (39, 35), radius_x=16, sweep=False)
        self.add_arc('sym-e11', (39, 35), (40, 31), radius_x=10, sweep=False)
        self.add_line('sym-e13', (40, 31), (40, 30))
        self.add_arc('sym-e14', (40, 30), (34, 18), radius_x=30, sweep=False)
        self.add_line('sym-e15', (34, 18), (26, 7))
        self.add_line('sym-e16', (26, 7), (24, 4))
        self.add_line('sym-e17', (24, 4), (22, 7))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
