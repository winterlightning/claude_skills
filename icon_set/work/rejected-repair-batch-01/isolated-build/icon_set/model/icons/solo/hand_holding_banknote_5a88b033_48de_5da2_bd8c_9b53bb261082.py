"""A left-entering hand grips an upright banknote. SQUARE centerline extremes (6,6)-(42,42). Lucide hand-coins informs a single open palm contour and credit-card the rounded note. Omit cuff and finger creases; retain the six-unit circular denomination. Deliberate asymmetry preserves the grasp direction."""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import rounded_rect, circle, dollar

SOURCE_ICON_ID = '5a88b033-48de-5da2-bd8c-9b53bb261082'
SOURCE_PATH = 'pictographic-primitives/payments/cash payment bills_5a88b033-48de-5da2-bd8c-9b53bb261082.svg'
AUTHOR = 'gpt-6'

class HandHoldingBanknote(Solo48):
    icon_id = 'hand-holding-banknote'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/payments'
    aliases = ()
    keywords = ('cash', 'banknote', 'money', 'hand', 'payment', 'bill', 'holding', 'currency')

    def build(self):
        # Upright note, circular denomination, and a left-entering grasp.
        self.add_line('note-left-top', (18, 24), (18, 10))
        self.add_arc('note-tl', (18, 10), (22, 6), radius_x=4)
        self.add_line('note-top', (22, 6), (38, 6))
        self.add_arc('note-tr', (38, 6), (42, 10), radius_x=4)
        self.add_line('note-right', (42, 10), (42, 26))
        self.add_arc('note-br', (42, 26), (38, 30), radius_x=4)
        self.add_line('note-bottom', (38, 30), (18, 30))
        self.add_line('note-left-bottom', (18, 30), (18, 24))
        self.add_contour('note', 'note-left-top', 'note-tl', 'note-top', 'note-tr', 'note-right', 'note-br', 'note-bottom', 'note-left-bottom', closed=True)
        circle(self, 'denomination', 30, 18, 3)
        self.add_polyline('hand-top', (6, 30), (14, 30), (18, 24))
        self.add_line('hand-right', (38, 30), (38, 34))
        self.add_arc('hand-curve', (38, 34), (30, 42), radius_x=8)
        self.add_line('hand-bottom-1', (30, 42), (14, 42))
        self.add_line('hand-bottom-2', (14, 42), (6, 38))
        self.add_contour('palm', 'hand-right', 'hand-curve', 'hand-bottom-1', 'hand-bottom-2')
        self.relate('connect', 'note', 'hand-top')
        self.relate('connect', 'note', 'palm')
