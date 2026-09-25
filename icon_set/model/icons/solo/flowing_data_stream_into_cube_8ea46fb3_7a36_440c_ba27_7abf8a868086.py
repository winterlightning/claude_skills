"""Four converging stream lines flowing beside a lower-right isometric cube."""

from ...keyshapes import Keyshape
from ._base import Solo48


SOURCE_ICON_ID = "8ea46fb3-7a36-440c-ba27-7abf8a868086"
SOURCE_PATH = "pictographic-primitives/_uncategorized_02/amazon kinesis data stream_8ea46fb3-7a36-440c-ba27-7abf8a868086.svg"
AUTHOR = "gpt-5"


class FlowingDataStreamIntoCube(Solo48):
    icon_id = "flowing-data-stream-into-cube"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("data-stream-cube", "stream-to-storage")
    keywords = ("data", "stream", "flow", "cube", "storage", "kinesis")

    def build(self) -> None:
        # Plan: four independent quarter-ellipse streams curve toward the right.
        # The lower-right cube is a separate composite with one outer contour,
        # a shared face junction, and a center drop to its bottom vertex.
        self.add_arc("stream-upper-outer", (20, 6), (42, 12), radius_x=22, radius_y=6)
        self.add_arc("stream-upper-inner", (6, 14), (18, 22), radius_x=12, radius_y=8)
        self.add_arc("stream-lower-outer", (6, 34), (13, 29), radius_x=7, radius_y=5)
        self.add_arc("stream-lower-inner", (12, 42), (16, 37), radius_x=4, radius_y=5)

        cube_top = (34, 21)
        cube_left = (26, 26)
        cube_right = (42, 26)
        cube_center = (34, 31)
        cube_bottom = (34, 42)
        cube_left_bottom = (26, 36)
        cube_right_bottom = (42, 36)

        self.add_polyline(
            "cube-outline",
            cube_top,
            cube_right,
            cube_right_bottom,
            cube_bottom,
            cube_left_bottom,
            cube_left,
            closed=True,
        )
        self.add_polyline("cube-top-seam", cube_left, cube_center, cube_right)
        self.add_line("cube-center-drop", cube_center, cube_bottom)
        self.relate("connect", "cube-outline", "cube-top-seam")
        self.relate("connect", "cube-top-seam", "cube-center-drop")
        self.relate("connect", "cube-outline", "cube-center-drop")
