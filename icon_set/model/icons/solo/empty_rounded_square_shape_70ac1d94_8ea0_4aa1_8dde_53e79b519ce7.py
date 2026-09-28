from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "70ac1d94-8ea0-4aa1-8dde-53e79b519ce7"
SOURCE_PATH = "pictographic-primitives/_uncategorized_21/gray_70ac1d94-8ea0-4aa1-8dde-53e79b519ce7.svg"
AUTHOR = "gpt-6"

class EmptyRoundedSquareShape(Solo48):
    icon_id = "empty-rounded-square-shape"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("rounded square",)
    keywords = ("empty", "border", "frame")

    def build(self) -> None:
        # Four repeated radius-6 corners make one continuous rounded outline.
        self.add_line("top", (12, 6), (36, 6))
        self.add_arc("corner-tr", (36, 6), (42, 12), radius_x=6, sweep=True)
        self.add_line("right", (42, 12), (42, 36))
        self.add_arc("corner-br", (42, 36), (36, 42), radius_x=6, sweep=True)
        self.add_line("bottom", (36, 42), (12, 42))
        self.add_arc("corner-bl", (12, 42), (6, 36), radius_x=6, sweep=True)
        self.add_line("left", (6, 36), (6, 12))
        self.add_arc("corner-tl", (6, 12), (12, 6), radius_x=6, sweep=True)
        self.add_contour("outline", "top", "corner-tr", "right", "corner-br", "bottom", "corner-bl", "left", "corner-tl", closed=True)
