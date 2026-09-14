"""P (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ce56e29c-a654-5258-b06d-a13207fd6905'
SOURCE_PATH = 'icons-json/typeface/P_ce56e29c-a654-5258-b06d-a13207fd6905.json'
AUTHOR = 'json_to_solo'

class PCe56e29c(Solo48):
    icon_id = 'p-ce56e29c'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('p', 'typeface')

    def build(self):
        self.add_line('e0', (8, 26), (26, 26))
        self.add_line('e1', (25, 4), (8, 4))
        self.add_line('e2', (8, 4), (8, 44))
        self.add_arc('e3-1', (26, 26), (40, 15), radius_x=13, sweep=False)
        self.add_arc('e3-2', (40, 15), (34, 6), radius_x=10, sweep=False)
        self.add_line('e3-3', (34, 6), (25, 4))
        self.add_contour('c0', 'e0', 'e3-1', 'e3-2', 'e3-3', 'e1', 'e2')
