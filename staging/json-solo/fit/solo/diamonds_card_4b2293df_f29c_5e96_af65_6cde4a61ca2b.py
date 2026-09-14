"""Diamonds card (entertainment), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b2293df-f29c-5e96-af65-6cde4a61ca2b'
SOURCE_PATH = 'icons-json/entertainment/diamonds card_4b2293df-f29c-5e96-af65-6cde4a61ca2b.json'
AUTHOR = 'json_to_solo'

class DiamondsCardEntertainment(Solo48):
    icon_id = 'diamonds-card-entertainment'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    aliases = ()
    keywords = ('diamonds', 'card', 'entertainment')

    def build(self):
        self.add_line('sym-e0', (40, 24), (35, 18))
        self.add_line('sym-e1', (35, 18), (27, 8))
        self.add_arc('sym-e2', (27, 8), (24, 4), radius_x=11, sweep=False)
        self.add_line('sym-e3', (24, 4), (12, 19))
        self.add_line('sym-e4', (12, 19), (8, 24))
        self.add_arc('sym-e5', (8, 24), (12, 29), radius_x=29, sweep=False)
        self.add_line('sym-e6', (12, 29), (24, 44))
        self.add_line('sym-e7', (24, 44), (27, 40))
        self.add_line('sym-e8', (27, 40), (35, 30))
        self.add_line('sym-e9', (35, 30), (40, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', closed=True)
