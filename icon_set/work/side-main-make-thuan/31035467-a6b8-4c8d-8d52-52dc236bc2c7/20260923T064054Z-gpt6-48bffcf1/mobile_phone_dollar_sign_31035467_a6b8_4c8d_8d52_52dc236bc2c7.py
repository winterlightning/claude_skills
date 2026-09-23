"""A mobile phone displaying a dollar sign."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "31035467-a6b8-4c8d-8d52-52dc236bc2c7"
SOURCE_PATH = "pictographic-primitives/other/mobile phone dollar sign_31035467-a6b8-4c8d-8d52-52dc236bc2c7.svg"
AUTHOR = "gpt-6"


class MobilePhoneDollarSign(Solo48):
    icon_id = "mobile-phone-dollar-sign"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("payment phone", "dollar smartphone")
    keywords = ("mobile", "money", "commerce", "payment")

    def build(self) -> None:
        # The phone is a rounded vertical frame with a separate lower bar.
        axis_x = 24
        left, right = 8, 2 * axis_x - 8
        radius = 4
        self.add_line("top", (12, 4), (36, 4))
        self.add_arc("ne", (36, 4), (right, 8), radius_x=radius)
        self.add_line("right-screen", (right, 8), (right, 36))
        self.add_line("right-footer", (right, 36), (right, 40))
        self.add_arc("se", (right, 40), (36, 44), radius_x=radius)
        self.add_line("bottom", (36, 44), (12, 44))
        self.add_arc("sw", (12, 44), (left, 40), radius_x=radius)
        self.add_line("left-footer", (left, 40), (left, 36))
        self.add_line("left-screen", (left, 36), (left, 8))
        self.add_arc("nw", (left, 8), (12, 4), radius_x=radius)
        self.add_contour("phone-frame", "top", "ne", "right-screen",
                         "right-footer", "se", "bottom", "sw",
                         "left-footer", "left-screen", "nw", closed=True)
        self.add_line("footer-divider", (left, 36), (right, 36))
        self.relate("connect", "footer-divider", "left-screen")
        self.relate("connect", "footer-divider", "right-screen")

        # The flowing currency stroke is deliberately centered on the screen.
        self.add_polyline("dollar", (24, 14), (24, 16), (29, 16),
                          (20, 20), (19, 22), (28, 24), (27, 26),
                          (24, 27), (24, 28))
