from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "74b38620-31d3-4e94-b22c-89627d614204"
SOURCE_PATH = "pictographic-primitives/_uncategorized_23/house hurricane_74b38620-31d3-4e94-b22c-89627d614204.svg"
AUTHOR = "gpt-6"

class HouseWithHurricaneStorm(Solo48):
    icon_id = "house-with-hurricane-storm"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("house tornado",)
    keywords = ("home", "hurricane", "wind")

    def build(self) -> None:
        # Small house remains lower-left; four wind strokes taper toward lower right.
        self.add_polyline("house", (6, 28), (18, 16), (30, 28), (30, 40), (28, 42), (8, 42), (6, 40), (6, 28), closed=True)
        self.add_dot("window", (18, 32))
        for y, start in ((6, 28), (14, 32), (22, 36), (30, 38)):
            self.add_line(f"storm-{y}", (start, y), (42, y))
