"""Hearts card (entertainment), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '482ffc65-627d-4af6-ae76-33f5ef43b659'
SOURCE_PATH = 'icons-json/entertainment/hearts card_482ffc65-627d-4af6-ae76-33f5ef43b659.json'
AUTHOR = 'json_to_solo'

class HeartsCard(Solo48):
    icon_id = 'hearts-card'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    aliases = ()
    keywords = ('hearts', 'card', 'entertainment')

    def build(self):
        self.add_line('sym-e0', (24, 39), (24, 40))
        self.add_line('sym-e1', (24, 40), (41, 24))
        self.add_arc('sym-e2', (41, 24), (44, 18), radius_x=9, sweep=False)
        self.add_line('sym-e4', (44, 18), (44, 17))
        self.add_arc('sym-e5', (44, 17), (34, 8), radius_x=11, sweep=False)
        self.add_arc('sym-e6', (34, 8), (33, 8), radius_x=75)
        self.add_arc('sym-e8', (33, 8), (26, 11), radius_x=11, sweep=False)
        self.add_arc('sym-e9', (26, 11), (24, 12), radius_x=16)
        self.add_arc('sym-e12', (24, 12), (22, 11), radius_x=17, sweep=False)
        self.add_arc('sym-e13', (22, 11), (15, 8), radius_x=11, sweep=False)
        self.add_arc('sym-e15', (15, 8), (14, 8), radius_x=17)
        self.add_arc('sym-e16', (14, 8), (4, 17), radius_x=11, sweep=False)
        self.add_line('sym-e17', (4, 17), (4, 18))
        self.add_arc('sym-e19', (4, 18), (7, 24), radius_x=9, sweep=False)
        self.add_line('sym-e20', (7, 24), (24, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e12', 'sym-e13', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e19', 'sym-e20')
