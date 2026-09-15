"""Sign badge bubble message (maps), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '78a70699-5196-5eb3-a804-07f9a0fa90e3'
SOURCE_PATH = 'pictographic-primitives/maps/sign badge bubble message_78a70699-5196-5eb3-a804-07f9a0fa90e3.svg'
AUTHOR = 'gpt-6'

class SignBadgeBubbleMessage(Solo48):
    icon_id = 'sign-badge-bubble-message'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('sign', 'badge', 'bubble', 'message', 'maps')

    def build(self):
        self.add_line('e0', (15, 35), (10, 35))
        self.add_line('e1', (6, 29), (6, 10))
        self.add_line('e3', (42, 9), (42, 30))
        self.add_line('e4', (33, 35), (25, 42))
        self.add_line('e5-1', (10, 35), (7, 33))
        self.add_line('e5-2', (7, 33), (6, 29))
        self.add_arc('e6-1', (6, 10), (6, 9), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_arc('e6-2', (6, 9), (9, 6), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('e6-3', (9, 6), (37, 6))
        self.add_arc('e7-1', (37, 6), (40, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e7-2', (40, 7), (42, 9), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('e8-1', (42, 30), (39, 34), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('e8-2', (39, 34), (33, 35))
        self.add_arc('e9-1', (25, 42), (23, 42), radius_x=22, radius_y=22, large_arc=False, sweep=False)
        self.add_line('e9-2', (23, 42), (15, 35))
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e1', 'e6-1', 'e6-2', 'e6-3', 'e7-1', 'e7-2', 'e3', 'e8-1', 'e8-2', 'e4', 'e9-1', 'e9-2', closed=True)
