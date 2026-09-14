"""Double arrow right (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ed70003a-c057-54c5-881a-b3ad2feedaf5'
SOURCE_PATH = 'icons-json/arrows/double arrow right_ed70003a-c057-54c5-881a-b3ad2feedaf5.json'
AUTHOR = 'json_to_solo'

class DoubleArrowRight(Solo48):
    icon_id = 'double-arrow-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('double', 'arrow', 'right', 'arrows')

    def build(self):
        self.add_line('sym-e0', (4, 24), (4, 11))
        self.add_line('sym-e1', (4, 11), (4, 10))
        self.add_line('sym-e2', (4, 10), (5, 8))
        self.add_line('sym-e3', (5, 8), (6, 8))
        self.add_arc('sym-e5', (6, 8), (7, 8), radius_x=7, sweep=False)
        self.add_line('sym-e6', (7, 8), (20, 18))
        self.add_line('sym-e7', (20, 18), (20, 11))
        self.add_line('sym-e8', (20, 11), (22, 8))
        self.add_line('sym-e9', (22, 8), (23, 8))
        self.add_line('sym-e10', (23, 8), (24, 8))
        self.add_line('sym-e12', (24, 8), (42, 21))
        self.add_line('sym-e13', (42, 21), (44, 23))
        self.add_line('sym-e14', (44, 23), (44, 24))
        self.add_line('sym-e19', (44, 24), (44, 25))
        self.add_line('sym-e20', (44, 25), (42, 27))
        self.add_line('sym-e21', (42, 27), (24, 40))
        self.add_line('sym-e23', (24, 40), (23, 40))
        self.add_arc('sym-e24', (23, 40), (22, 40), radius_x=26, sweep=False)
        self.add_line('sym-e25', (22, 40), (20, 37))
        self.add_line('sym-e26', (20, 37), (20, 30))
        self.add_line('sym-e27', (20, 30), (7, 40))
        self.add_line('sym-e28', (7, 40), (6, 40))
        self.add_arc('sym-e30', (6, 40), (5, 40), radius_x=1, sweep=False)
        self.add_line('sym-e31', (5, 40), (4, 38))
        self.add_line('sym-e32', (4, 38), (4, 37))
        self.add_line('sym-e33', (4, 37), (4, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', closed=True)
