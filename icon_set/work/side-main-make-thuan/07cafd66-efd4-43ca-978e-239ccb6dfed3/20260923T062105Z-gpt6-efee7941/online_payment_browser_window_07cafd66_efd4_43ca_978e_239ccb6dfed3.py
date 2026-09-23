"""A browser window with a central dollar symbol."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "07cafd66-efd4-43ca-978e-239ccb6dfed3"
SOURCE_PATH = "pictographic-primitives/other/browser dollar sign_07cafd66-efd4-43ca-978e-239ccb6dfed3.svg"
AUTHOR = "gpt-6"


class OnlinePaymentBrowserWindow(Solo48):
    icon_id = "online-payment-browser-window"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/finance"
    aliases = ("browser dollar", "online payment")
    keywords = ("web", "money", "payment", "commerce")

    def build(self) -> None:
        # Browser shell and tab divider are one square composition.
        self.add_line("top", (10, 6), (38, 6))
        self.add_arc("ne", (38, 6), (42, 10), radius_x=4)
        self.add_line("right-header", (42, 10), (42, 14))
        self.add_line("right-body", (42, 14), (42, 38))
        self.add_arc("se", (42, 38), (38, 42), radius_x=4)
        self.add_line("bottom", (38, 42), (10, 42))
        self.add_arc("sw", (10, 42), (6, 38), radius_x=4)
        self.add_line("left-body", (6, 38), (6, 14))
        self.add_line("left-header", (6, 14), (6, 10))
        self.add_arc("nw", (6, 10), (10, 6), radius_x=4)
        self.add_contour("browser", "top", "ne", "right-header",
                         "right-body", "se", "bottom", "sw",
                         "left-body", "left-header", "nw", closed=True)
        self.add_line("header-divider", (6, 14), (42, 14))
        self.relate("connect", "header-divider", "left-body")
        self.relate("connect", "header-divider", "right-header")

        # The S is built as two smooth strokes meeting the vertical spine at
        # (24,28). It preserves the source's hand-drawn dollar silhouette.
        self.add_bezier("dollar-upper", (28, 23),
                        ((23, 21), (20, 23), (20, 25)),
                        ((20, 27), (22, 28), (24, 28)))
        self.add_bezier("dollar-lower", (24, 28),
                        ((27, 28), (29, 29), (28, 31)),
                        ((27, 33), (23, 34), (20, 33)))
        self.add_line("dollar-spine-upper", (24, 23), (24, 28))
        self.add_line("dollar-spine-lower", (24, 28), (24, 33))
        self.relate("connect", "dollar-spine-upper", "dollar-upper")
        self.relate("connect", "dollar-spine-lower", "dollar-lower")
