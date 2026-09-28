"""A browser window with a central dollar symbol."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "07cafd66-efd4-43ca-978e-239ccb6dfed3"
SOURCE_PATH = "pictographic-primitives/other/browser dollar sign_07cafd66-efd4-43ca-978e-239ccb6dfed3.svg"
AUTHOR = "claude-fable-5-1"


class OnlinePaymentBrowserWindow(Solo48):
    icon_id = "online-payment-browser-window"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/finance"
    aliases = ("browser dollar", "online payment")
    keywords = ("web", "money", "payment", "commerce")

    def build(self) -> None:
        # Window: rounded 36-unit square. The header divider is dropped: with
        # it the interior band is 12 units, and the currency mark needs 18.
        self.add_line("top", (10, 6), (38, 6))
        self.add_arc("ne", (38, 6), (42, 10), radius_x=4)
        self.add_line("right", (42, 10), (42, 38))
        self.add_arc("se", (42, 38), (38, 42), radius_x=4)
        self.add_line("bottom", (38, 42), (10, 42))
        self.add_arc("sw", (10, 42), (6, 38), radius_x=4)
        self.add_line("left", (6, 38), (6, 10))
        self.add_arc("nw", (6, 10), (10, 6), radius_x=4)
        self.add_contour("browser", "top", "ne", "right", "se",
                         "bottom", "sw", "left", "nw", closed=True)
        # Currency mark: Lucide dollar-sign construction (two bows, no spine)
        # on rows y=15/24/33, nine units from each wall and from each other.
        # Each bow is one cubic with horizontal tangents, bulging 3 units.
        self.add_line("dollar-top", (28, 15), (20, 15))
        self.add_bezier("dollar-upper-bow", (20, 15), ((16, 15), (16, 24), (20, 24)))
        self.add_line("dollar-middle", (20, 24), (28, 24))
        self.add_bezier("dollar-lower-bow", (28, 24), ((32, 24), (32, 33), (28, 33)))
        self.add_line("dollar-bottom", (28, 33), (20, 33))
        self.add_contour("dollar", "dollar-top", "dollar-upper-bow", "dollar-middle",
                         "dollar-lower-bow", "dollar-bottom")
