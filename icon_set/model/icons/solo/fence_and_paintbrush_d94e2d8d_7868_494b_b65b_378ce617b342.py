from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "d94e2d8d-7868-494b-b65b-378ce617b342"
SOURCE_PATH = "pictographic-primitives/_uncategorized_22/home improvement 2_d94e2d8d-7868-494b-b65b-378ce617b342.svg"
AUTHOR = "gpt-6"

class FenceAndPaintbrush(Solo48):
    icon_id = "fence-and-paintbrush"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/home-improvement"
    aliases = ("paint fence",)
    keywords = ("pickets", "rails", "brush")

    def build(self) -> None:
        # Two repeated pointed pickets and rails occupy the left; brush is upright at right.
        for name, left in (("left", 4), ("right", 20)):
            self.add_polyline(name + "-picket", (left, 40), (left, 16), (left + 4, 8), (left + 8, 16), (left + 8, 40), (left, 40), closed=True)
        for y in (22, 32):
            self.add_line(f"rail-{y}", (12, y), (20, y))
            self.relate("connect", f"rail-{y}", "left-picket")
            self.relate("connect", f"rail-{y}", "right-picket")
        self.add_polyline("brush-head", (36, 14), (44, 14), (44, 26), (36, 26), (36, 14), closed=True)
        self.add_line("brush-handle", (40, 26), (40, 40))
        self.relate("connect", "brush-head", "brush-handle")
