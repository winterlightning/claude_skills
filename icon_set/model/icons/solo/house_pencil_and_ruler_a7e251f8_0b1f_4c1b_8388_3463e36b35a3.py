from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "a7e251f8-0b1f-4c1b-8388-3463e36b35a3"
SOURCE_PATH = "pictographic-primitives/_uncategorized_22/home improvement 3_a7e251f8-0b1f-4c1b-8388-3463e36b35a3.svg"
AUTHOR = "gpt-6"

class HousePencilAndRuler(Solo48):
    icon_id = "house-pencil-and-ruler"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("home design tools",)
    keywords = ("house", "pencil", "ruler")

    def build(self) -> None:
        # House upper-left, upright pencil right, marked ruler along bottom.
        self.add_polyline("house", (4, 18), (16, 8), (28, 18), (28, 24), (20, 24), (20, 16), (12, 16), (12, 24), (4, 24), (4, 18), closed=True)
        self.add_polyline("pencil", (36, 18), (40, 8), (44, 18), (44, 36), (40, 40), (36, 36), (36, 18), closed=True)
        self.add_line("ruler", (4, 36), (28, 36))
        for x in (10, 18, 26):
            self.add_line(f"tick-{x}", (x, 32), (x, 36))
            self.relate("connect", "ruler", f"tick-{x}")
