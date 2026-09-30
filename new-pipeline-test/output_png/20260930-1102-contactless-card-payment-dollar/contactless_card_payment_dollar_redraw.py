"""contactless card payment, dollar (redraw of the new-pipeline traced SVG).

Subject: a payment card carrying a dollar sign and the contactless wave
mark, i.e. "pay by tapping this card".

Plan: HRECT_L (centerline box (4,8)-(44,40)), not the suggested HRECT_M.
The dollar sign is the tallest inner mark: an S of 12 with 1-unit stem
tabs is 14 tall, and it needs more than 8 of clearance to each card wall,
so the card must be 32 tall on centerlines; HRECT_M only offers 28.
- card: rounded rectangle (4,8)-(44,40), corner radius 4; its four walls
  are the four keyshape extremes.
- dollar: compact S about the stem axis x 15 (top run y 18, crossing node
  y 24, foot y 30, elliptical bowls rx 2 / ry 3, the house compact-currency
  construction) plus two 1-unit stem tabs sharing the S end nodes, declared
  connected. The stem is not drawn through the S: across the 6-unit bowls
  it would close them into blobs.
- waves: two right-facing arcs sharing the dollar's y 24 axis, chords
  x 25 (y 19-29, r 7) and x 34 (y 17-31, r 15), printed on the card to the
  right of the dollar. Chords and radii were searched so every pair is
  strictly over 8 apart (8.06 dollar-wave, 8.5 wave-wave, 8.1 wave-wall);
  an exact 8 between curves cannot be certified by the engine.
The trace put three waves outside the card. Outside waves cost more than 8
per wave plus 8 to the card wall, which leaves under 22 units of card width
for a 30-unit-tall card: a portrait card that reads as a phone. Moving the
waves onto the card (where the contactless mark sits on real cards) keeps
a wide card. Lucide `nfc` informed the nested wave arcs and Lucide
`dollar-sign` the S (without its through-stem, see above).

Metric issues (contactless-card-payment-dollar_metrics.json):
- stroke-width (info, trace 2.64 fitted): redrawn at stroke 4, every gap
  budgeted at more than 8 on centerlines.
- stroke-count (warn, 9 strokes vs 6): the trace's broken S fragments
  (e2-e6) are one S contour plus two tabs; waves reduced from 3 to 2.
  Six parts: card, S, two tabs, two waves.
- keyshape-short-axis (warn, HRECT_M y fill 66%): fixed by the HRECT_L
  choice above; the card walls sit exactly on all four box edges.
- clearance errors e0-e2/e3/e4/e5/e6 (card vs dollar pieces 3.2-5.0),
  e0-e7/e8 and e1-e7/e8, e7-e8 (waves 2.6-6.8 apart), e2-e5, e4-e6
  (dollar pieces 4.0 apart): all fixed; every distinct pair clears 8.
- loose-join infos e3-e6, e4-e5, e5-e6: fixed; the S is one contour and
  the tabs share its exact end nodes with relate('connect').
Not kept from the trace: the third (outermost) wave and the waves' place
outside the card, both dropped for the width budget above.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "83b7c65e-14e9-4428-b2e6-57332f20611f"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1102-contactless-card-payment-dollar/contactless-card-payment-dollar_raw.svg"
AUTHOR = "claude-opus-5-5"

CARD = (4, 8, 44, 40)          # left, top, right, bottom (centerlines)
CARD_R = 4
DOLLAR_X, DOLLAR_Y = 15, 24    # stem axis and S crossing node
BOWL_X, BOWL_Y = 2, 3         # bowl radii; S runs at y 18 / 24 / 30
TAB = 1                        # stem tab beyond the S
WAVES = ((25, 5, 7), (34, 7, 15))      # chord x, half chord, radius


class ContactlessCardPaymentDollarRedraw(Solo48):
    icon_id = "contactless-card-payment-dollar-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "payments"
    aliases = ("contactless-card-payment-dollar", "tap to pay dollar", "nfc card payment")
    keywords = ("contactless", "payment", "card", "credit card", "dollar", "nfc", "tap", "pay", "money")

    def build(self) -> None:
        self._card()
        self._dollar()
        for i, (x, h, r) in enumerate(WAVES):
            self.add_arc(f"wave-{i}", (x, DOLLAR_Y - h), (x, DOLLAR_Y + h), radius_x=r, sweep=True)

    def _card(self) -> None:
        l, t, r, b = CARD
        k = CARD_R
        self.add_line("card-top", (l + k, t), (r - k, t))
        self.add_arc("card-tr", (r - k, t), (r, t + k), radius_x=k, sweep=True)
        self.add_line("card-right", (r, t + k), (r, b - k))
        self.add_arc("card-br", (r, b - k), (r - k, b), radius_x=k, sweep=True)
        self.add_line("card-bottom", (r - k, b), (l + k, b))
        self.add_arc("card-bl", (l + k, b), (l, b - k), radius_x=k, sweep=True)
        self.add_line("card-left", (l, b - k), (l, t + k))
        self.add_arc("card-tl", (l, t + k), (l + k, t), radius_x=k, sweep=True)
        self.add_contour("card", "card-top", "card-tr", "card-right", "card-br",
                         "card-bottom", "card-bl", "card-left", "card-tl", closed=True)

    def _dollar(self) -> None:
        x, y, qx, q = DOLLAR_X, DOLLAR_Y, BOWL_X, BOWL_Y
        top, foot = (x, y - 2 * q), (x, y + 2 * q)
        self.add_line("s-top", (x + qx, y - 2 * q), top)
        self.add_arc("s-upper", top, (x, y), radius_x=qx, radius_y=q, sweep=False)
        self.add_arc("s-lower", (x, y), foot, radius_x=qx, radius_y=q, sweep=True)
        self.add_line("s-foot", foot, (x - qx, y + 2 * q))
        self.add_contour("dollar", "s-top", "s-upper", "s-lower", "s-foot")
        self.add_line("stem-top", (x, y - 2 * q - TAB), top)
        self.add_line("stem-bottom", foot, (x, y + 2 * q + TAB))
        self.relate("connect", "stem-top", "dollar")
        self.relate("connect", "stem-bottom", "dollar")
