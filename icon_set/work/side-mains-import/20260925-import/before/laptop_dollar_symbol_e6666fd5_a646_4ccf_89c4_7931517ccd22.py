"""A laptop displaying a dollar sign."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "e6666fd5-a646-4ccf-89c4-7931517ccd22"
SOURCE_PATH = "pictographic-primitives/other/laptop dollar sign_e6666fd5-a646-4ccf-89c4-7931517ccd22.svg"
AUTHOR = "claude-fable-5-1"


class LaptopDollarSymbol(Solo48):
    icon_id = "laptop-dollar-symbol"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("payment laptop", "ecommerce laptop")
    keywords = ("computer", "dollar", "money", "online shopping")

    def build(self) -> None:
        # Laptop: Lucide laptop silhouette (screen shoulders, flared base).
        # The screen/base divider is dropped so the 18-unit currency mark fits.
        axis_x = 24
        left, right = 8, 2 * axis_x - 8
        self.add_line("screen-top", (11, 6), (37, 6))
        self.add_arc("screen-ne", (37, 6), (right, 9), radius_x=3)
        self.add_line("screen-right", (right, 9), (right, 34))
        self.add_line("base-right", (right, 34), (42, 42))
        self.add_line("base-bottom", (42, 42), (6, 42))
        self.add_line("base-left", (6, 42), (left, 34))
        self.add_line("screen-left", (left, 34), (left, 9))
        self.add_arc("screen-nw", (left, 9), (11, 6), radius_x=3)
        self.add_contour("laptop-outline", "screen-top", "screen-ne", "screen-right",
                         "base-right", "base-bottom", "base-left", "screen-left",
                         "screen-nw", closed=True)
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
