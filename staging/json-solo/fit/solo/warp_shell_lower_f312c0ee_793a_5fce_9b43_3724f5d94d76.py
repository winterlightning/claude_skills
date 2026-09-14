"""Warp shell lower (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f312c0ee-793a-5fce-9b43-3724f5d94d76'
SOURCE_PATH = 'icons-json/design/warp shell lower_f312c0ee-793a-5fce-9b43-3724f5d94d76.json'
AUTHOR = 'json_to_solo'

class WarpShellLowerDesign(Solo48):
    icon_id = 'warp-shell-lower-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'shell', 'lower', 'design')

    def build(self):
        self.add_arc('sym-e0', (44, 21), (34, 17), radius_x=10)
        self.add_line('sym-e1', (34, 17), (33, 14))
        self.add_line('sym-e2', (33, 14), (33, 8))
        self.add_line('sym-e3', (33, 8), (24, 8))
        self.add_line('sym-e4', (24, 8), (15, 8))
        self.add_line('sym-e5', (15, 8), (15, 14))
        self.add_line('sym-e6', (15, 14), (14, 17))
        self.add_arc('sym-e7', (14, 17), (4, 21), radius_x=10)
        self.add_line('sym-e8', (4, 21), (4, 24))
        self.add_arc('sym-e9', (4, 24), (5, 28), radius_x=12)
        self.add_arc('sym-e10', (5, 28), (23, 40), radius_x=20, sweep=False)
        self.add_arc('sym-e11', (23, 40), (24, 40), radius_x=1)
        self.add_arc('sym-e14', (24, 40), (25, 40), radius_x=1)
        self.add_arc('sym-e15', (25, 40), (43, 28), radius_x=20, sweep=False)
        self.add_line('sym-e16', (43, 28), (44, 24))
        self.add_line('sym-e17', (44, 24), (44, 21))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
