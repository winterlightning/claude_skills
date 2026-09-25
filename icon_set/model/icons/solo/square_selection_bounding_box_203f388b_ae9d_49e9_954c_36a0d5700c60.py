"""A square selection frame with four corner control handles."""

from ...keyshapes import Keyshape
from ._base import Solo48


SOURCE_ICON_ID = "203f388b-ae9d-49e9-954c-36a0d5700c60"
SOURCE_PATH = "pictographic-primitives/_uncategorized_02/align to selection_203f388b-ae9d-49e9-954c-36a0d5700c60.svg"
AUTHOR = "gpt-5"


class SquareSelectionBoundingBox(Solo48):
    icon_id = "square-selection-bounding-box"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("selection-frame", "transform-bounding-box")
    keywords = ("selection", "bounding", "box", "handles", "resize")

    def build(self) -> None:
        # Plan: four identical square handle definitions occupy the corners.
        # Short centered edge runs preserve the bounding-box frame while keeping
        # the required eight-unit clearance from each handle loop.
        for name, left, top in (
            ("top-left", 6, 6),
            ("top-right", 34, 6),
            ("bottom-right", 34, 34),
            ("bottom-left", 6, 34),
        ):
            self.add_polyline(
                f"handle-{name}",
                (left, top),
                (left + 8, top),
                (left + 8, top + 8),
                (left, top + 8),
                closed=True,
            )

        self.add_line("frame-top", (22, 10), (26, 10))
        self.add_line("frame-right", (38, 22), (38, 26))
        self.add_line("frame-bottom", (26, 38), (22, 38))
        self.add_line("frame-left", (10, 26), (10, 22))
