"""Credit card payment: a bank card inserted into the top slot of a payment
terminal with a keypad.
Review (meaning, "machine and card"): the earlier notched shape and loose
arrow did not read as either. This revision shows both explicitly: a card
with its magnetic stripe standing in the terminal's slot, and an upright terminal
body with a 2x2 keypad.
Keyshape VRECT_M (10,4)-(38,44): an upright terminal like the reference.
Symbol plan: card sides end on nodes of the terminal's top edge (T joins,
declared); the stripe splits the card sides; keypad = four dots exactly 8 clear of
the walls (square centerline corners so the gaps certify); mirrored about x=24.
Lucide construction: credit-card (rect + stripe line) and calculator keys.
Omissions: the reference's separate card and down arrow (the insertion shows
the payment directly).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='29a5a818-9fcd-4062-843c-4ae6c6b33268'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__credit-card-payment/20260926T125430Z-thuan-mac/reference/credit card payment_29a5a818-9fcd-4062-843c-4ae6c6b33268.svg'
AUTHOR = "claude-opus-5-5"


class _Shapes:
    def circle(self, n, x, y, r):
        pts = [(x - r, y), (x, y - r), (x + r, y), (x, y + r), (x - r, y)]
        for i, (a, b) in enumerate(zip(pts, pts[1:])):
            self.add_arc(f"{n}-{i}", a, b, radius_x=r)
        self.add_contour(n, *(f"{n}-{i}" for i in range(4)), closed=True)

    def lines(self, n, *pts, closed=False):
        """Plain add_line segments grouped in one contour (members joinable by relate)."""
        seq = list(pts) + ([pts[0]] if closed else [])
        ids = []
        for i, (a, b) in enumerate(zip(seq, seq[1:])):
            self.add_line(f"{n}-{i}", a, b)
            ids.append(f"{n}-{i}")
        self.add_contour(n, *ids, closed=closed)
        return ids

class CreditCardPayment(_Shapes, Solo48):
    icon_id = 'credit-card-payment'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'finance/payment'
    categories = ('finance', 'shopping')
    aliases = ('card payment', 'card terminal', 'pos terminal')
    keywords = ('credit', 'card', 'payment', 'terminal', 'pos', 'pay', 'machine', 'reader')

    def build(self):
        L, R, top, B = 10, 38, 20, 44
        cl, cr = 14, 34
        self.lines('terminal', (cl, top), (cr, top), (R, top), (R, B), (L, B), (L, top), closed=True)
        self.lines('card', (cl, top), (cl, 12), (cl, 4), (cr, 4), (cr, 12), (cr, top))
        self.add_line('stripe', (cl, 12), (cr, 12))
        self.relate('connect', 'terminal', 'card')
        self.relate('connect', 'card', 'stripe')
        for i, (x, y) in enumerate(((18, 28), (30, 28), (18, 36), (30, 36))):
            self.add_dot(f'key-{i}', (x, y))
