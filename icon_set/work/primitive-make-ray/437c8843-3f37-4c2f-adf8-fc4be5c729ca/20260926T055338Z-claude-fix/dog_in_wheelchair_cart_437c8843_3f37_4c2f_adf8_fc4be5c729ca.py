"""A dog standing on its front leg with its hindquarters carried by a wheeled pet cart.

Symbol plan: the dog faces right. Its body is one closed outline: back y 12 from the
rump to the neck (26, 12), the neck up to the head top (30, 6)-(35, 6), an r7 round snout
to (42, 13), the jaw back to the chest (36, 17), the chest down to (36, 20), the belly y 20
back to the rump and an r4 semicircular rump. The tail flicks up-left from the rump top to
(6, 6). Two front legs drop straight to the ground at x 28 and 36 (8 apart). The cart is an
r7 wheel about (13, 35) under the hindquarters, hung from the rump's lower point by a
vertical strut (shared end points, declared); the wheel top is 8 below the belly and its
right side 8 from the rear leg. A one-legged first attempt (attempts/v1-one-leg.svg) read
as furniture.
Lucide construction: 'dog' side-profile body; 'circle' wheel on a strut as in Lucide's
cart/wheel icons.
Keyshape SQUARE: centerline x 6..42 (tail tip and wheel, snout), y 6..42 (head top, wheel and feet).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "437c8843-3f37-4c2f-adf8-fc4be5c729ca"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__dog-in-wheelchair-cart/20260926T055140Z-thuan-mac/reference/disabled pet_437c8843-3f37-4c2f-adf8-fc4be5c729ca.svg"
AUTHOR = "claude-opus-5-5"


class DogInWheelchairCart(Solo48):
    icon_id = "dog-in-wheelchair-cart"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/dog"
    aliases = ("disabled pet", "dog wheelchair", "pet mobility cart")
    keywords = ("dog", "pet", "wheelchair", "disabled", "cart", "mobility", "accessibility", "vet", "wheel")

    def build(self) -> None:
        back, belly, rump_x = 12, 20, 13
        self.add_line("back", (rump_x, back), (26, back))
        self.add_line("neck", (26, back), (30, 6))
        self.add_line("head-top", (30, 6), (35, 6))
        self.add_arc("snout", (35, 6), (42, 13), radius_x=7)
        self.add_line("jaw", (42, 13), (36, 17))
        self.add_line("chest", (36, 17), (36, belly))
        self.add_line("belly-front", (36, belly), (28, belly))
        self.add_line("belly-rear", (28, belly), (rump_x, belly))
        self.add_arc("rump", (rump_x, belly), (rump_x, back), radius_x=4)
        self.add_contour("body", "back", "neck", "head-top", "snout", "jaw", "chest", "belly-front",
                         "belly-rear", "rump", closed=True)
        self.add_line("tail", (rump_x, back), (6, 6))
        self.relate("connect", "body", "tail")
        for x in (28, 36):
            self.add_line(f"leg-{x}", (x, belly), (x, 42))
            self.relate("connect", "body", f"leg-{x}")
        # cart
        cx, cy, r = rump_x, 35, 7
        self.add_line("strut", (cx, belly), (cx, cy - r))
        pts = [(cx - r, cy), (cx, cy - r), (cx + r, cy), (cx, cy + r)]
        names = ("wheel-nw", "wheel-ne", "wheel-se", "wheel-sw")
        for i, n in enumerate(names):
            self.add_arc(n, pts[i], pts[(i + 1) % 4], radius_x=r)
        self.add_contour("wheel", *names, closed=True)
        self.relate("connect", "body", "strut")
        self.relate("connect", "strut", "wheel")
