"""Standard Payment Credit Card -- batch-002 r2 generation.

Subject: a landscape payment card with a magnetic stripe near the top and two
short number marks along the lower left.

Plan: one rounded-rectangle card (radius 4) owns every other part. The stripe
is a full-width chord that shares split nodes with both card sides. The two
number marks form a left-anchored series with one length and one step.
Keyshape HRECT_L; centerline box (4,8)-(44,40).
Reduction: the reference's four-sided card, stripe and two dashes are all
kept; nothing was dropped.
Construction reference: Lucide credit-card (rounded card plus one full-width
stripe chord), re-derived on the SOLO48 grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._batch_002_r2_shapes import rounded_rect

SOURCE_ICON_ID = '48208b48-931c-4607-8b76-e8e4eddfbfba'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/business/card_48208b48-931c-4607-8b76-e8e4eddfbfba.svg'
EXPORTED_REFERENCE = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-002/references/card_48208b48-931c-4607-8b76-e8e4eddfbfba.svg'
AUTHOR = 'claude-opus-5'

LEFT, TOP, RIGHT, BOTTOM, RADIUS = 4, 8, 44, 40, 4
STRIPE_Y = TOP + 8
# Marks keep 9 from the rounded card: a curved contour cannot certify exactly 8.
MARK_Y, MARK_X, MARK_LEN, MARK_STEP = BOTTOM - 9, LEFT + 9, 6, 14


class StandardPaymentCreditCardBatch002R2(Solo48):
    icon_id = 'standard-payment-credit-card-batch-002-r2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/business'
    aliases = ('credit-card', 'payment-card', 'bank-card')
    keywords = ('card', 'credit', 'debit', 'payment', 'bank', 'pay', 'stripe')

    def build(self) -> None:
        left_node, right_node = (LEFT, STRIPE_Y), (RIGHT, STRIPE_Y)
        rounded_rect(self, 'card', LEFT, TOP, RIGHT, BOTTOM, RADIUS,
                     nodes=(left_node, right_node))
        self.add_line('stripe', left_node, right_node)
        self.relate('connect', 'card', 'stripe')
        for i in range(2):
            x = MARK_X + i * MARK_STEP
            self.add_line(f'number-mark-{i + 1}', (x, MARK_Y), (x + MARK_LEN, MARK_Y))
