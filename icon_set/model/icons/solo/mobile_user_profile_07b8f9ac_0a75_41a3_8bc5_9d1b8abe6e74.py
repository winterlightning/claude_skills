"""A smartphone displaying a detached user head and shoulders."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "07b8f9ac-0a75-41a3-8bc5-9d1b8abe6e74"
SOURCE_PATH = "pictographic-primitives/other/mobile phone user_07b8f9ac-0a75-41a3-8bc5-9d1b8abe6e74.svg"
AUTHOR = "gpt-6"


class MobileUserProfile(Solo48):
    icon_id = "mobile-user-profile"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("phone profile", "mobile user")
    keywords = ("smartphone", "account", "avatar", "person")

    def build(self) -> None:
        # Radius-four phone envelope. The bottom divider shares the exact
        # y=36 nodes with the sides and with both shoulder endpoints.
        self.add_line("top", (12, 4), (36, 4))
        self.add_arc("ne", (36, 4), (40, 8), radius_x=4)
        self.add_line("right-screen", (40, 8), (40, 36))
        self.add_line("right-footer", (40, 36), (40, 40))
        self.add_arc("se", (40, 40), (36, 44), radius_x=4)
        self.add_line("bottom", (36, 44), (12, 44))
        self.add_arc("sw", (12, 44), (8, 40), radius_x=4)
        self.add_line("left-footer", (8, 40), (8, 36))
        self.add_line("left-screen", (8, 36), (8, 8))
        self.add_arc("nw", (8, 8), (12, 4), radius_x=4)
        self.add_contour("phone-frame", "top", "ne", "right-screen",
                         "right-footer", "se", "bottom", "sw",
                         "left-footer", "left-screen", "nw", closed=True)

        self.add_arc("head-upper", (28, 17), (20, 17), radius_x=4, sweep=False)
        self.add_arc("head-lower", (20, 17), (28, 17), radius_x=4, sweep=False)
        self.add_contour("head", "head-upper", "head-lower", closed=True)
        self.add_bezier("shoulder-left", (16, 36),
                        ((16, 32), (20, 29), (24, 29)))
        self.add_bezier("shoulder-right", (24, 29),
                        ((28, 29), (32, 32), (32, 36)))
        self.add_contour("shoulders", "shoulder-left", "shoulder-right")

        self.add_line("footer-left", (8, 36), (16, 36))
        self.add_line("footer-center", (16, 36), (32, 36))
        self.add_line("footer-right", (32, 36), (40, 36))
        self.relate("connect", "footer-left", "left-screen")
        self.relate("connect", "footer-right", "right-screen")
        self.relate("connect", "shoulder-left", "footer-left")
        self.relate("connect", "shoulder-right", "footer-right")
