"""A laptop displaying a dollar sign."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e6666fd5-a646-4ccf-89c4-7931517ccd22"
SOURCE_PATH = "pictographic-primitives/other/laptop dollar sign_e6666fd5-a646-4ccf-89c4-7931517ccd22.svg"
AUTHOR = "gpt-6"


class LaptopDollarSymbol(Solo48):
    icon_id = "laptop-dollar-symbol"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("payment laptop", "ecommerce laptop")
    keywords = ("computer", "dollar", "money", "online shopping")

    def build(self) -> None:
        # Laptop: mirrored screen shoulders, inclined base, and one divider.
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
        self.add_line("screen-divider", (left, 34), (right, 34))
        self.relate("connect", "screen-divider", "screen-left")
        self.relate("connect", "screen-divider", "screen-right")

        # A single currency stroke keeps the top and bottom stems joined.
        self.add_polyline("dollar", (24, 15), (24, 16), (29, 17),
                          (20, 21), (28, 23), (24, 24), (24, 25))
