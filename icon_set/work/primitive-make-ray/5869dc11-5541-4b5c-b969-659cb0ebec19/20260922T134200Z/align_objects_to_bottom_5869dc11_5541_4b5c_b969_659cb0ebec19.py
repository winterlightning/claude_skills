"""Two unequal bars and flanking arrows aligned to a lower baseline."""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48


SOURCE_ICON_ID = "5869dc11-5541-4b5c-b969-659cb0ebec19"
SOURCE_PATH = "pictographic-primitives/_uncategorized_01/align bottom move_5869dc11-5541-4b5c-b969-659cb0ebec19.svg"
AUTHOR = "gpt-5"


class AlignObjectsToBottom(Solo48):
    icon_id = "align-objects-to-bottom"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "actions/alignment"
    aliases = ("align-bottom", "bottom-align-move")
    keywords = ("align", "bottom", "bars", "arrows", "baseline")

    def build(self) -> None:
        # Plan: two round-ended vertical bar strokes share one lower y value;
        # mirrored arrow definitions flank them, and one baseline owns the
        # horizontal envelope. The reference's narrow outlined bars reduce to
        # single coherent strokes so their openings do not collapse at 48 px.
        bar_bottom = 31
        self.add_line("bar-short", (18, 18), (18, bar_bottom))
        self.add_line("bar-tall", (30, 8), (30, bar_bottom))

        for side, axis_x, outward_x, inward_x in (
            ("left", 6, 4, 8),
            ("right", 42, 44, 40),
        ):
            self.add_line(f"arrow-{side}-shaft", (axis_x, 21), (axis_x, 31))
            self.add_line(f"arrow-{side}-outer-head", (outward_x, 29), (axis_x, 31))
            self.add_line(f"arrow-{side}-inner-head", (axis_x, 31), (inward_x, 29))
            self.add_contour(
                f"arrow-{side}-head",
                f"arrow-{side}-outer-head",
                f"arrow-{side}-inner-head",
            )
            self.relate("connect", f"arrow-{side}-shaft", f"arrow-{side}-head")

        self.add_line("baseline", (4, 40), (44, 40))
