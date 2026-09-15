"""Right reverse turn ahead (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '182f0248-c380-4521-a855-6c9c834f593d'
SOURCE_PATH = 'pictographic-primitives/transportation/right reverse turn ahead_182f0248-c380-4521-a855-6c9c834f593d.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class RightReverseTurnAhead(Solo48):
    icon_id = 'right-reverse-turn-ahead'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('right', 'reverse', 'turn', 'ahead', 'transportation')

    def build(self):
        self.add_line('e0', (8, 44), (8, 24))
        self.add_line('e1', (10, 23), (29, 23))
        self.add_line('e2', (30, 22), (30, 4))
        self.add_line('e3', (30, 4), (21, 12))
        self.add_line('e4', (30, 4), (40, 12))
        self.add_arc('e5', (8, 24), (10, 23), radius_x=2)
        self.add_arc('e6', (29, 23), (30, 22), radius_x=1, sweep=False)
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2', 'e3')
        self.add_contour('c1', 'e4')
        self.relate('connect', 'c0', 'c1')
