"""Double arrow left (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '732ebdab-0fb0-5a73-b5de-bff0b7b443bc'
SOURCE_PATH = 'icons-json/arrows/double arrow left_732ebdab-0fb0-5a73-b5de-bff0b7b443bc.json'
AUTHOR = 'json_to_solo'

class DoubleArrowLeft(Solo48):
    icon_id = 'double-arrow-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('double', 'arrow', 'left', 'arrows')

    def build(self):
        self.add_line('sym-e0', (44, 24), (44, 37))
        self.add_arc('sym-e1', (44, 37), (44, 38), radius_x=38, sweep=False)
        self.add_line('sym-e2', (44, 38), (43, 40))
        self.add_line('sym-e3', (43, 40), (42, 40))
        self.add_line('sym-e5', (42, 40), (41, 40))
        self.add_line('sym-e6', (41, 40), (28, 30))
        self.add_line('sym-e7', (28, 30), (28, 37))
        self.add_line('sym-e8', (28, 37), (26, 40))
        self.add_arc('sym-e9', (26, 40), (25, 40), radius_x=29, sweep=False)
        self.add_arc('sym-e10', (25, 40), (24, 40), radius_x=27, sweep=False)
        self.add_line('sym-e12', (24, 40), (6, 27))
        self.add_line('sym-e13', (6, 27), (4, 25))
        self.add_line('sym-e14', (4, 25), (4, 24))
        self.add_line('sym-e19', (4, 24), (4, 23))
        self.add_line('sym-e20', (4, 23), (6, 21))
        self.add_line('sym-e21', (6, 21), (24, 8))
        self.add_arc('sym-e23', (24, 8), (25, 8), radius_x=43, sweep=False)
        self.add_arc('sym-e24', (25, 8), (26, 8), radius_x=45, sweep=False)
        self.add_line('sym-e25', (26, 8), (28, 11))
        self.add_line('sym-e26', (28, 11), (28, 18))
        self.add_line('sym-e27', (28, 18), (41, 8))
        self.add_line('sym-e28', (41, 8), (42, 8))
        self.add_line('sym-e30', (42, 8), (43, 8))
        self.add_line('sym-e31', (43, 8), (44, 10))
        self.add_arc('sym-e32', (44, 10), (44, 11), radius_x=23, sweep=False)
        self.add_line('sym-e33', (44, 11), (44, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', closed=True)
