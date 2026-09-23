"""A right arrow above two right-aligned bars of unequal length."""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48


SOURCE_ICON_ID = "bc08c07e-fd43-4866-85c6-472f38121c0c"
SOURCE_PATH = "pictographic-primitives/_uncategorized_02/align right move_bc08c07e-fd43-4866-85c6-472f38121c0c.svg"
AUTHOR = "gpt-5"


class RightIndentationAction(Solo48):
    icon_id = "right-indentation-action"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "actions/alignment"
    aliases = ("rightward-object-indentation", "indent-right")
    keywords = ("indent", "align", "right", "arrow", "bars", "layout")

    def build(self) -> None:
        # Plan: two round-ended bars share right_x=36 while their left ends
        # encode the indentation. A detached right arrow occupies the upper band.
        right_x = 36
        self.add_line("bar-long", (4, 24), (right_x, 24))
        self.add_line("bar-short", (16, 38), (right_x, 38))

        self.add_line("arrow-shaft", (28, 12), (44, 12))
        self.add_line("arrow-upper-head", (40, 10), (44, 12))
        self.add_line("arrow-lower-head", (44, 12), (40, 14))
        self.add_contour("arrow-head", "arrow-upper-head", "arrow-lower-head")
        self.relate("connect", "arrow-shaft", "arrow-head")
