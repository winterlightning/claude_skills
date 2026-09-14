"""T shirt (clothes), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3b53f582-4552-4079-9580-b9a0440eed2e'
SOURCE_PATH = 'icons-json/clothes/t shirt_3b53f582-4552-4079-9580-b9a0440eed2e.json'
AUTHOR = 'json_to_solo'

class TShirt3b53f582(Solo48):
    icon_id = 't-shirt-3b53f582'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('t', 'shirt', 'clothes')

    def build(self):
        self.add_line('e0', (17, 8), (4, 16))
        self.add_line('e1', (4, 16), (9, 22))
        self.add_line('e2', (9, 22), (13, 20))
        self.add_line('e3', (13, 20), (13, 40))
        self.add_line('e4', (13, 40), (35, 40))
        self.add_line('e5', (35, 40), (35, 20))
        self.add_line('e6', (35, 20), (39, 22))
        self.add_line('e7', (39, 22), (44, 16))
        self.add_line('e8', (44, 16), (31, 8))
        self.add_arc('e9', (31, 8), (17, 8), radius_x=9)
        self.add_contour('c0', 'e9', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', closed=True)
