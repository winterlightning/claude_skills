"""Smile (chat), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5b89f261-bd85-4abc-8e75-64ff35cd7b4f'
SOURCE_PATH = 'pictographic-primitives/chat/smile_5b89f261-bd85-4abc-8e75-64ff35cd7b4f.svg'
AUTHOR = 'gpt-6'

class Smile(Solo48):
    icon_id = 'smile'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'chat'
    aliases = ()
    keywords = ('smile', 'chat')

    def build(self):
        self.add_line('e0', (33, 21), (39, 16))
        self.add_line('e2', (44, 32), (43, 34))
        self.add_line('e3', (43, 34), (33, 28))
        self.add_line('e4', (4, 33), (4, 13))
        self.add_line('e5', (9, 8), (29, 8))
        self.add_line('e6', (33, 14), (33, 34))
        self.add_line('e7', (28, 40), (9, 40))
        self.add_line('e8-1', (39, 16), (43, 14))
        self.add_arc('e8-2', (43, 14), (44, 14), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_line('e8-3', (44, 14), (44, 32))
        self.add_line('e9-1', (9, 40), (5, 38))
        self.add_line('e9-2', (5, 38), (4, 33))
        self.add_arc('e10', (4, 13), (9, 8), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e11', (29, 8), (33, 14), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('e12-1', (33, 34), (31, 39), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('e12-2', (31, 39), (28, 40))
        self.add_contour('c0', 'e0', 'e8-1', 'e8-2', 'e8-3', 'e2', 'e3', closed=False)
        self.add_contour('c1', 'e9-1', 'e9-2', 'e4', 'e10', 'e5', 'e11', 'e6', 'e12-1', 'e12-2', 'e7', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
