"""Unlock (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '90a6ff07-21bc-47ed-b588-aacc1c25c397'
SOURCE_PATH = 'icons-json/symbol/unlock_90a6ff07-21bc-47ed-b588-aacc1c25c397.json'
AUTHOR = 'json_to_solo'

class Unlock90a6ff07(Solo48):
    icon_id = 'unlock-90a6ff07'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('unlock', 'symbol')

    def build(self):
        self.add_line('e0', (14, 13), (14, 21))
        self.add_line('e1', (8, 24), (8, 40))
        self.add_line('e2', (11, 44), (37, 44))
        self.add_line('e3', (40, 40), (40, 25))
        self.add_line('e4', (37, 21), (14, 21))
        self.add_arc('e5-1', (34, 14), (24, 4), radius_x=10, sweep=False)
        self.add_arc('e5-2', (24, 4), (14, 13), radius_x=11, sweep=False)
        self.add_arc('e6', (14, 21), (8, 24), radius_x=5, sweep=False)
        self.add_line('e7-1', (8, 40), (9, 43))
        self.add_arc('e7-2', (9, 43), (11, 44), radius_x=3, sweep=False)
        self.add_arc('e8', (37, 44), (40, 40), radius_x=5, sweep=False)
        self.add_arc('e9', (40, 25), (37, 21), radius_x=5, sweep=False)
        self.add_contour('c0', 'e5-1', 'e5-2', 'e0', 'e6', 'e1', 'e7-1', 'e7-2', 'e2', 'e8', 'e3', 'e9', 'e4')
