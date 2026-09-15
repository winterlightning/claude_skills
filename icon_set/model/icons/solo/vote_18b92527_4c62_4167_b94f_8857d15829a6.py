"""Vote (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '18b92527-4c62-4167-b94f-8857d15829a6'
SOURCE_PATH = 'icons-json/symbol/vote_18b92527-4c62-4167-b94f-8857d15829a6.json'
AUTHOR = 'gpt-6'

class Vote(Solo48):
    icon_id = 'vote'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('vote', 'symbol')

    def build(self):
        self.add_line('sym-e0', (24, 23), (15, 14))
        self.add_line('sym-e1', (15, 14), (24, 4))
        self.add_line('sym-e2', (24, 4), (33, 14))
        self.add_line('sym-e3', (33, 14), (24, 23))
        self.add_line('sym-e4', (24, 23), (10, 23))
        self.add_arc('sym-e6', (10, 23), (8, 26), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e7', (8, 26), (8, 41))
        self.add_arc('sym-e10', (8, 41), (11, 44), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e12', (11, 44), (37, 44))
        self.add_arc('sym-e15', (37, 44), (40, 41), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_arc('sym-e16', (40, 41), (40, 40), radius_x=41, radius_y=41, large_arc=False, sweep=True)
        self.add_line('sym-e17', (40, 40), (40, 26))
        self.add_arc('sym-e19', (40, 26), (38, 23), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e20', (38, 23), (24, 23))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e10', 'sym-e12', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e19', 'sym-e20', closed=True)
