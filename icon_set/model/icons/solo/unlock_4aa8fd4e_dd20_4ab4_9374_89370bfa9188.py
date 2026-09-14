"""Unlock (state), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4aa8fd4e-dd20-4ab4-9374-89370bfa9188'
SOURCE_PATH = 'icons-json/state/unlock_4aa8fd4e-dd20-4ab4-9374-89370bfa9188.json'
AUTHOR = 'json_to_solo'

class Unlock(Solo48):
    icon_id = 'unlock'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('unlock', 'state')

    def build(self):
        self.add_line('e0', (14, 13), (14, 21))
        self.add_line('e1', (8, 24), (8, 40))
        self.add_line('e2', (11, 44), (37, 44))
        self.add_line('e3', (40, 40), (40, 25))
        self.add_line('e4', (37, 21), (14, 21))
        self.add_arc('e5-1', (34, 14), (24, 4), radius_x=10, sweep=False)
        self.add_arc('e5-2', (24, 4), (14, 13), radius_x=11, sweep=False)
        self.add_arc('e6', (14, 21), (8, 24), radius_x=5, sweep=False)
        self.add_arc('e7', (8, 40), (11, 44), radius_x=5, sweep=False)
        self.add_arc('e8', (37, 44), (40, 40), radius_x=5, sweep=False)
        self.add_arc('e9', (40, 25), (37, 21), radius_x=5, sweep=False)
        self.add_contour('c0', 'e5-1', 'e5-2', 'e0', 'e6', 'e1', 'e7', 'e2', 'e8', 'e3', 'e9', 'e4')
