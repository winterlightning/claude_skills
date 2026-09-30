"""Contactless digital wallet (redraw of the new-pipeline traced SVG).

Plan: a wide wallet body below with a strap clasp entering from its right
wall (the Lucide `wallet` tab cue), and two nested right-facing contactless
arcs floating above it.

Keyshape VRECT_L, centerline box (8,4)-(40,44). The metrics suggested
SQUARE (x fill 0.87, stretch 1.15). VRECT_L needs less stretch (1.08), and
its 40-unit height leaves the arcs 15 units above the body. SQUARE leaves
only 12, which forces the outer arc nearly flat.

- Body: rounded rectangle (8,28)-(40,44), corner radius 4, 2:1 like a
  wallet. Its right wall is split at the strap joint (40,36).
- Clasp: a strap line (40,36)-(32,36) from the wall into the body, 8 from
  the top and bottom edges.
- Signal: inner arc r5 about (14,11), (18,8)-(18,14); outer arc r13
  through (26,4)-(26,18) (centre (15.05,11)). Both sweep about +-35 degrees;
  the outer top is the box top.

Metric issues:
- stroke-width (info): redrawn at stroke 4 with every gap budgeted for it.
- keyshape-short-axis (warn): fixed. VRECT_L instead of a 1.15 stretch;
  the extremes sit on the box (x 8/40, y 4/44).
- clearance e0-e1: fixed. The arcs are now >= 8.9 apart on centerlines
  (was 4.01).
- clearance e0-e3 / e1-e3: fixed. The lowest arc point is y=18, 10 above
  the body top (was 3.89 / 6.45).
- hole at (34.4,33.3), 2.4 wide: fixed by redesign. The clasp is now a
  strap line with no enclosed hole. A hollow clasp cannot fit: inside the
  body it needs a 26-tall body (8 + 10 + 8), which leaves no room for the
  arcs. Outside the right wall, the 10x10 tab it needs reads as a mug
  handle (tried and rejected).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "adaa1f2f-b19e-47ce-a02c-05816f5de17d"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1105-contactless-digital-wallet-solo/contactless-digital-wallet-solo_raw.svg"
AUTHOR = "claude-opus-5-5"

# Wallet body and the strap joint on its right wall.
LEFT, RIGHT, TOP, BOTTOM, R = 8, 40, 28, 44, 4
STRAP_Y = (TOP + BOTTOM) // 2
STRAP_LEN = 8
# Contactless arcs, symmetric about y=SIG_Y: (start, end, radius).
SIG_Y = 11
INNER = ((18, SIG_Y - 3), (18, SIG_Y + 3), 5)
OUTER = ((26, SIG_Y - 7), (26, SIG_Y + 7), 13)


class ContactlessDigitalWalletSoloRedraw(Solo48):
    icon_id = "contactless-digital-wallet-solo-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/finance"
    aliases = ("nfc-wallet", "tap-to-pay-wallet")
    keywords = ("contactless", "wallet", "payment", "nfc", "tap", "digital wallet")

    def build(self) -> None:
        joint = (RIGHT, STRAP_Y)

        # Body, clockwise from the top edge.
        self.add_line("body-top", (LEFT + R, TOP), (RIGHT - R, TOP))
        self.add_arc("body-tr", (RIGHT - R, TOP), (RIGHT, TOP + R), radius_x=R)
        self.add_line("body-wall-hi", (RIGHT, TOP + R), joint)
        self.add_line("body-wall-lo", joint, (RIGHT, BOTTOM - R))
        self.add_arc("body-br", (RIGHT, BOTTOM - R), (RIGHT - R, BOTTOM), radius_x=R)
        self.add_line("body-bottom", (RIGHT - R, BOTTOM), (LEFT + R, BOTTOM))
        self.add_arc("body-bl", (LEFT + R, BOTTOM), (LEFT, BOTTOM - R), radius_x=R)
        self.add_line("body-left", (LEFT, BOTTOM - R), (LEFT, TOP + R))
        self.add_arc("body-tl", (LEFT, TOP + R), (LEFT + R, TOP), radius_x=R)
        self.add_contour(
            "body", "body-top", "body-tr", "body-wall-hi", "body-wall-lo",
            "body-br", "body-bottom", "body-bl", "body-left", "body-tl",
            closed=True,
        )

        # Clasp strap entering from the wall.
        self.add_line("clasp", joint, (RIGHT - STRAP_LEN, STRAP_Y))
        self.relate("connect", "clasp", "body")

        # Contactless waves.
        for name, (start, end, radius) in (("wave-inner", INNER), ("wave-outer", OUTER)):
            self.add_arc(name, start, end, radius_x=radius)
