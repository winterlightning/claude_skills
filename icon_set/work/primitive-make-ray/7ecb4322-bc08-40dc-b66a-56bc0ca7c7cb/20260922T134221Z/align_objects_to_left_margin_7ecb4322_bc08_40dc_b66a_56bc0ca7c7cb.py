"""Two left-aligned bars with paired arrows moving toward a margin."""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48


SOURCE_ICON_ID = "7ecb4322-bc08-40dc-b66a-56bc0ca7c7cb"
SOURCE_PATH = "pictographic-primitives/_uncategorized_01/align left move_7ecb4322-bc08-40dc-b66a-56bc0ca7c7cb.svg"
AUTHOR = "gpt-5"


class AlignObjectsToLeftMargin(Solo48):
    icon_id = "align-objects-to-left-margin"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "actions/alignment"
    aliases = ("align-left", "left-align-move")
    keywords = ("align", "left", "margin", "bars", "arrows")

    def build(self) -> None:
        # Plan: a vertical margin owns the left edge, two round-ended horizontal
        # bars share x=17, and a mirrored top/bottom arrow series points left.
        self.add_line("left-margin", (8, 4), (8, 44))
        self.add_line("bar-long", (17, 18), (40, 18))
        self.add_line("bar-short", (17, 30), (32, 30))

        for position, y, upper_y, lower_y in (
            ("top", 6, 4, 8),
            ("bottom", 42, 40, 44),
        ):
            self.add_line(f"arrow-{position}-shaft", (16, y), (32, y))
            self.add_line(f"arrow-{position}-upper-head", (20, upper_y), (16, y))
            self.add_line(f"arrow-{position}-lower-head", (16, y), (20, lower_y))
            self.add_contour(
                f"arrow-{position}-head",
                f"arrow-{position}-upper-head",
                f"arrow-{position}-lower-head",
            )
            self.relate("connect", f"arrow-{position}-shaft", f"arrow-{position}-head")
