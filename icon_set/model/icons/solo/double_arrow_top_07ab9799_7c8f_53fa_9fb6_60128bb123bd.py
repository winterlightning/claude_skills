"""Double arrow top (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '07ab9799-7c8f-53fa-9fb6-60128bb123bd'
SOURCE_PATH = 'icons-json/arrows/double arrow top_07ab9799-7c8f-53fa-9fb6-60128bb123bd.json'
AUTHOR = 'json_to_solo'

class DoubleArrowTop(Solo48):
    icon_id = 'double-arrow-top'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('double', 'arrow', 'top', 'arrows')

    def build(self):
        self.add_line('sym-e0', (11, 28), (8, 26))
        self.add_line('sym-e1', (8, 26), (8, 25))
        self.add_line('sym-e2', (8, 25), (8, 24))
        self.add_line('sym-e4', (8, 24), (21, 6))
        self.add_arc('sym-e5', (21, 6), (23, 4), radius_x=5)
        self.add_line('sym-e6', (23, 4), (24, 4))
        self.add_line('sym-e11', (24, 4), (25, 4))
        self.add_arc('sym-e12', (25, 4), (27, 6), radius_x=5)
        self.add_line('sym-e13', (27, 6), (40, 24))
        self.add_line('sym-e15', (40, 24), (40, 25))
        self.add_arc('sym-e16', (40, 25), (40, 26), radius_x=28, sweep=False)
        self.add_line('sym-e17', (40, 26), (37, 28))
        self.add_line('sym-e18', (37, 28), (30, 28))
        self.add_line('sym-e19', (30, 28), (40, 41))
        self.add_arc('sym-e20', (40, 41), (40, 42), radius_x=41, sweep=False)
        self.add_line('sym-e22', (40, 42), (40, 43))
        self.add_line('sym-e23', (40, 43), (38, 44))
        self.add_line('sym-e24', (38, 44), (37, 44))
        self.add_line('sym-e25', (37, 44), (24, 44))
        self.add_line('sym-e26', (24, 44), (11, 44))
        self.add_arc('sym-e27', (11, 44), (10, 44), radius_x=24, sweep=False)
        self.add_line('sym-e28', (10, 44), (8, 43))
        self.add_line('sym-e29', (8, 43), (8, 42))
        self.add_line('sym-e31', (8, 42), (8, 41))
        self.add_line('sym-e32', (8, 41), (18, 28))
        self.add_line('sym-e33', (18, 28), (11, 28))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e31', 'sym-e32', 'sym-e33', closed=True)
