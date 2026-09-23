from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "629f3d9a-d833-4dac-8eb4-beb66dd336ff"
SOURCE_PATH = "pictographic-primitives/_uncategorized_21/grid_629f3d9a-d833-4dac-8eb4-beb66dd336ff.svg"
AUTHOR = "gpt-6"

class NineSquareGridLayout(Solo48):
    icon_id = "nine-square-grid-layout"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface/layout"
    aliases = ("three by three grid",)
    keywords = ("nine", "cells", "layout")

    def build(self) -> None:
        # Equal columns and rows repeat at x/y 18 and 30 within one frame.
        self.add_polyline("outer", (10, 6), (38, 6), (42, 10), (42, 38), (38, 42), (10, 42), (6, 38), (6, 10), (10, 6), closed=True)
        for x in (18, 30):
            self.add_line(f"vertical-{x}", (x, 6), (x, 42))
            self.relate("connect", "outer", f"vertical-{x}")
        for y in (18, 30):
            self.add_line(f"horizontal-{y}", (6, y), (42, y))
            self.relate("connect", "outer", f"horizontal-{y}")
        for x in (18, 30):
            for y in (18, 30):
                self.relate("connect", f"vertical-{x}", f"horizontal-{y}")
