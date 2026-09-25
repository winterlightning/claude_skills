"""A rounded square selection boundary broken into twelve dashes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "01358fdb-e97b-45c4-b36d-ff26939879f9"
SOURCE_PATH = "pictographic-primitives/other/square dashed_01358fdb-e97b-45c4-b36d-ff26939879f9.svg"
AUTHOR = "gpt-6"


class RoundedDashedSelectionBox(Solo48):
    icon_id = "rounded-dashed-selection-box"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("dashed square", "selection marquee")
    keywords = ("crop", "boundary", "outline", "dotted")

    def build(self) -> None:
        # One square definition owns all four corner units and side bars.
        lo, hi, radius = 6, 42, 3
        near, far = 12, 2 * 24 - 12
        middle_lo, middle_hi = 21, 2 * 24 - 21

        self.add_line("nw-top", (near, lo), (lo + radius, lo))
        self.add_arc("nw-arc", (lo + radius, lo), (lo, lo + radius),
                     radius_x=radius, sweep=False)
        self.add_line("nw-side", (lo, lo + radius), (lo, near))
        self.add_contour("northwest", "nw-top", "nw-arc", "nw-side")

        self.add_line("ne-top", (far, lo), (hi - radius, lo))
        self.add_arc("ne-arc", (hi - radius, lo), (hi, lo + radius),
                     radius_x=radius)
        self.add_line("ne-side", (hi, lo + radius), (hi, near))
        self.add_contour("northeast", "ne-top", "ne-arc", "ne-side")

        self.add_line("se-side", (hi, far), (hi, hi - radius))
        self.add_arc("se-arc", (hi, hi - radius), (hi - radius, hi),
                     radius_x=radius)
        self.add_line("se-bottom", (hi - radius, hi), (far, hi))
        self.add_contour("southeast", "se-side", "se-arc", "se-bottom")

        self.add_line("sw-bottom", (near, hi), (lo + radius, hi))
        self.add_arc("sw-arc", (lo + radius, hi), (lo, hi - radius),
                     radius_x=radius)
        self.add_line("sw-side", (lo, hi - radius), (lo, far))
        self.add_contour("southwest", "sw-bottom", "sw-arc", "sw-side")

        self.add_line("north-middle", (middle_lo, lo), (middle_hi, lo))
        self.add_line("east-middle", (hi, middle_lo), (hi, middle_hi))
        self.add_line("south-middle", (middle_hi, hi), (middle_lo, hi))
        self.add_line("west-middle", (lo, middle_hi), (lo, middle_lo))
