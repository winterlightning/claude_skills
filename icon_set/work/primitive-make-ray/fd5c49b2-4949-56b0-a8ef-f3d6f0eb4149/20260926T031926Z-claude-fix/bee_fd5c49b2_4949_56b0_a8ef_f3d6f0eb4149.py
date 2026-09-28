"""A bee seen from above: round head with two antennae, striped body, swept wings.

Symbol plan: mirrored about x=24. The head is an r5 circle at (24,11) touching the top edge; the
antennae leave its upper shoulders (+-4,-3) and curl outward. The body hangs from the head's lower
shoulders (+-4,+3), widens to the first stripe, narrows through the second stripe and
closes in a pointed sting at the bottom. Each wing is a lobe from the body side (K) swept
out and down to a rounded tip and back to the first stripe's end (B).
Lucide construction: 'bee' - round head, antennae curls, banded oval body, side wings.
Keyshape SQUARE: centerline x 6..42 (wing tips), y 6..42 (head top, sting).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "fd5c49b2-4949-56b0-a8ef-f3d6f0eb4149"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__bee-with-swept-wings/20260926T030905Z-thuan-mac/reference/bee_fd5c49b2-4949-56b0-a8ef-f3d6f0eb4149.svg"
AUTHOR = "claude-opus-5-5"


class BeeWithSweptWings(Solo48):
    icon_id = "bee-with-swept-wings"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/insects"
    aliases = ("bee", "honeybee", "bumblebee")
    keywords = ("bee", "honey", "insect", "bug", "wings", "stripes", "pollinator", "buzz", "hive")

    def build(self) -> None:
        m = lambda p: (48 - p[0], p[1])
        A, K, B, Cc, TIP = (20, 14), (17, 18), (15, 25), (17, 33), (24, 42)
        H = (20, 8)
        # head
        self.add_arc("head-1", H, m(H), radius_x=5, sweep=True)
        self.add_arc("head-2", m(H), m(A), radius_x=5, sweep=True)
        self.add_arc("head-3", m(A), A, radius_x=5, sweep=True)
        self.add_arc("head-4", A, H, radius_x=5, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)
        for side, f in (("left", lambda p: p), ("right", m)):
            self.add_bezier(f"antenna-{side}", f(H), (f((18.5, 6.5)), f((16, 6)), f((13, 7))))
            if side == "left":
                self.add_line("body-left-1", A, K)
                self.add_bezier("body-left-2", K, ((16, 20.5), (15, 23), B))
                self.add_bezier("body-left-3", B, ((15, 29), (16, 32), Cc))
                self.add_line("body-left-4", Cc, TIP)
            else:
                self.add_line("body-right-4", TIP, m(Cc))
                self.add_bezier("body-right-3", m(Cc), (m((16, 32)), m((15, 29)), m(B)))
                self.add_bezier("body-right-2", m(B), (m((15, 23)), m((16, 20.5)), m(K)))
                self.add_line("body-right-1", m(K), m(A))
            self.add_bezier(f"wing-{side}", f(K),
                            (f((12, 14)), f((6, 16)), f((6, 21))),
                            (f((6, 25.5)), f((11, 26.5)), f(B)))
            self.relate("connect", "head", f"antenna-{side}")
            self.relate("connect", "body", f"wing-{side}")
            self.relate("connect", "stripe-1", f"wing-{side}")
        self.add_contour("body", "body-left-1", "body-left-2", "body-left-3", "body-left-4",
                         "body-right-4", "body-right-3", "body-right-2", "body-right-1")
        self.add_line("stripe-1", B, m(B))
        self.add_line("stripe-2", Cc, m(Cc))
        self.relate("connect", "head", "body")
        self.relate("connect", "body", "stripe-1")
        self.relate("connect", "body", "stripe-2")
