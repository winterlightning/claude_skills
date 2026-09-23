from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "a80c4976-31bf-47f2-b198-dfc75df4dc14"
SOURCE_PATH = "pictographic-primitives/_uncategorized_19/framework_a80c4976-31bf-47f2-b198-dfc75df4dc14.svg"
AUTHOR = "gpt-6"

class SquareGridLayoutStructure(Solo48):
    icon_id = "square-grid-layout-structure"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface/layout"
    aliases = ("framework", "grid layout")
    keywords = ("square", "four panels", "center")

    def build(self) -> None:
        # Four equal quadrants meet a compact central square on shared axes.
        self.add_polyline("outer-frame", (10, 6), (38, 6), (42, 10), (42, 38), (38, 42), (10, 42), (6, 38), (6, 10), (10, 6), closed=True)
        self.add_polyline("center-box", (20, 20), (28, 20), (28, 28), (20, 28), (20, 20), closed=True)
        for name, a, b in (("north", (24, 6), (24, 20)), ("east", (28, 24), (42, 24)), ("south", (24, 28), (24, 42)), ("west", (6, 24), (20, 24))):
            self.add_line(name, a, b)
            self.relate("connect", name, "outer-frame")
            self.relate("connect", name, "center-box")
