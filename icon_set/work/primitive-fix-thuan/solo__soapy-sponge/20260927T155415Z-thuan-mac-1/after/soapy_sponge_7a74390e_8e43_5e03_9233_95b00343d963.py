"""Soapy sponge: a rectangular sponge block in oblique view resting in soap suds, authored on SOLO48.

Plan: SQUARE centerline box (6,6)-(42,42). Cuboid with front face x 15..33,
y 14..32 and a depth offset (9,-8) so the top face edges sit 8+ apart; the right
face drops to (42,24). Suds = two r5 bubbles on 3-4-5 lattice points: the outer
one spills left of the block, the inner one covers the lower-left front corner
(the left front edge ends on it), then a puddle spreads under the block: a
rounded right end leaving the front-bottom-right corner and a flat base on y=42.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7a74390e-8e43-5e03-9233-95b00343d963"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__soapy-sponge/20260927T155415Z-thuan-mac-1/reference/cleaning sponge soap_7a74390e-8e43-5e03-9233-95b00343d963.svg"
AUTHOR = "claude-opus-5-5"


class SoapySponge(Solo48):
    icon_id = "soapy-sponge"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "wayfinding"
    categories = ("wayfinding", "primitives")
    aliases = ("cleaning sponge soap",)
    keywords = ("sponge", "soap", "suds", "cleaning", "washing", "foam")

    def build(self) -> None:
        A, B = (15, 14), (33, 14)         # front top
        D, C = (24, 6), (42, 6)           # back top
        E, F = (33, 32), (42, 24)         # front bottom right, right face bottom
        G = (15, 25)                      # left front edge meets the inner bubble
        V = (15, 31)                      # valley between the two bubbles
        J = (22, 32)                      # inner bubble lands on the front bottom edge
        self.add_line("block-left", G, A)
        self.add_line("block-top-left", A, D)
        self.add_line("block-back", D, C)
        self.add_line("block-right", C, F)
        self.add_line("block-right-bottom", F, E)
        self.add_contour("block", "block-left", "block-top-left", "block-back", "block-right", "block-right-bottom")
        self.add_line("block-front-top", A, B)
        self.add_line("block-top-right", B, C)
        self.add_line("block-front-right", B, E)
        self.add_line("block-front-bottom", J, E)
        # Suds: puddle then bubbles, outer bubble centre (11,34), inner (19,28), both r5
        self.add_arc("puddle-end", E, (39, 37), radius_x=6, radius_y=5)
        self.add_arc("puddle-curve", (39, 37), (34, 42), radius_x=5)
        self.add_line("puddle-base", (34, 42), (10, 42))
        self.add_arc("puddle-corner", (10, 42), (6, 38), radius_x=4)
        self.add_line("suds-left", (6, 38), (6, 34))
        self.add_arc("bubble-outer", (6, 34), V, radius_x=5)
        self.add_arc("bubble-inner-a", V, G, radius_x=5)
        self.add_arc("bubble-inner-b", G, J, radius_x=5, large_arc=True)
        self.add_contour("suds", "puddle-end", "puddle-curve", "puddle-base", "puddle-corner", "suds-left",
                         "bubble-outer", "bubble-inner-a", "bubble-inner-b")
        self.relate("connect", "block", "block-front-top", "block-top-right", "block-front-right",
                    "block-front-bottom", "suds")
