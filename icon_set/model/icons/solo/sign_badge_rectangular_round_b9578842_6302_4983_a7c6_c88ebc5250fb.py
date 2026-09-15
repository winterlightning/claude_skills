"""Sign badge rectangular round (maps), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b9578842-6302-4983-a7c6-c88ebc5250fb'
SOURCE_PATH = 'icons-json/maps/sign badge rectangular round_b9578842-6302-4983-a7c6-c88ebc5250fb.json'
AUTHOR = 'gpt-6'

class SignBadgeRectangularRound(Solo48):
    icon_id = 'sign-badge-rectangular-round'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('sign', 'badge', 'rectangular', 'round', 'maps')

    def build(self):
        self.add_line('sym-e0', (24, 6), (40, 6))
        self.add_arc('sym-e2', (40, 6), (42, 9), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e4', (42, 9), (42, 39))
        self.add_arc('sym-e7', (42, 39), (40, 42), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e9', (40, 42), (8, 42))
        self.add_arc('sym-e12', (8, 42), (6, 39), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e14', (6, 39), (6, 9))
        self.add_arc('sym-e17', (6, 9), (8, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e19', (8, 6), (24, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e4', 'sym-e7', 'sym-e9', 'sym-e12', 'sym-e14', 'sym-e17', 'sym-e19', closed=True)
