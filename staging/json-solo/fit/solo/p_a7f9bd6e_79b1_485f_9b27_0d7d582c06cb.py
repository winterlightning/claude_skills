"""P (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a7f9bd6e-79b1-485f-9b27-0d7d582c06cb'
SOURCE_PATH = 'icons-json/typeface/p_a7f9bd6e-79b1-485f-9b27-0d7d582c06cb.json'
AUTHOR = 'json_to_solo'

class P(Solo48):
    icon_id = 'p'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('p', 'typeface')

    def build(self):
        self.add_line('e0', (8, 15), (8, 44))
        self.add_arc('e1-1', (8, 29), (29, 28), radius_x=77, sweep=False)
        self.add_arc('e1-2', (29, 28), (38, 23), radius_x=16, sweep=False)
        self.add_line('e1-3', (38, 23), (40, 16))
        self.add_arc('e1-4', (40, 16), (33, 6), radius_x=12, sweep=False)
        self.add_line('e1-5', (33, 6), (22, 4))
        self.add_line('e1-6', (22, 4), (13, 6))
        self.add_arc('e1-7', (13, 6), (8, 14), radius_x=9, sweep=False)
        self.add_line('e1-8', (8, 14), (8, 15))
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8', 'e0')
