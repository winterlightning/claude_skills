"""Double arrow bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e5f5f6da-8db6-57b5-9fbb-9c29c2944a84'
SOURCE_PATH = 'icons-json/arrows/double arrow bottom_e5f5f6da-8db6-57b5-9fbb-9c29c2944a84.json'
AUTHOR = 'json_to_solo'

class DoubleArrowBottom(Solo48):
    icon_id = 'double-arrow-bottom'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('double', 'arrow', 'bottom', 'arrows')

    def build(self):
        self.add_line('sym-e0', (24, 4), (37, 4))
        self.add_line('sym-e1', (37, 4), (38, 4))
        self.add_line('sym-e2', (38, 4), (40, 5))
        self.add_arc('sym-e3', (40, 5), (40, 6), radius_x=1, sweep=False)
        self.add_line('sym-e5', (40, 6), (40, 7))
        self.add_line('sym-e6', (40, 7), (30, 20))
        self.add_line('sym-e7', (30, 20), (37, 20))
        self.add_line('sym-e8', (37, 20), (40, 22))
        self.add_line('sym-e9', (40, 22), (40, 23))
        self.add_arc('sym-e10', (40, 23), (40, 24), radius_x=26, sweep=False)
        self.add_line('sym-e12', (40, 24), (27, 42))
        self.add_line('sym-e13', (27, 42), (25, 44))
        self.add_line('sym-e14', (25, 44), (24, 44))
        self.add_line('sym-e19', (24, 44), (23, 44))
        self.add_line('sym-e20', (23, 44), (21, 42))
        self.add_line('sym-e21', (21, 42), (8, 24))
        self.add_line('sym-e23', (8, 24), (8, 23))
        self.add_line('sym-e24', (8, 23), (8, 22))
        self.add_line('sym-e25', (8, 22), (11, 20))
        self.add_line('sym-e26', (11, 20), (18, 20))
        self.add_line('sym-e27', (18, 20), (8, 7))
        self.add_line('sym-e28', (8, 7), (8, 6))
        self.add_line('sym-e30', (8, 6), (8, 5))
        self.add_line('sym-e31', (8, 5), (10, 4))
        self.add_line('sym-e32', (10, 4), (11, 4))
        self.add_line('sym-e33', (11, 4), (24, 4))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', closed=True)
