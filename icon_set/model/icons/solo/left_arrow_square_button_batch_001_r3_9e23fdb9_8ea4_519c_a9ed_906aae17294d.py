"""A square button whose left-pointing chevron makes it a "go back" control.

Plan: one rounded-square frame owns a centred chevron. The chevron mirrors
about the horizontal axis y=24; its vertex and arm ends are derived from one
arm length so all three square-chevron icons in this batch share proportions.
Keyshape: SQUARE, centerline box (6,6)-(42,42).
Reduction: the reference's slightly softened corners become radius-4 corners.
Construction reference: Lucide `square-chevron-left` (rx-2 frame, 90-degree
chevron centred optically).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._batch_001_r3_shapes import rounded_rect

SOURCE_ICON_ID = "9e23fdb9-8ea4-519c-a9ed-906aae17294d"
SOURCE_PATH = "/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/arrows/arrow rectangle left svg360_9e23fdb9-8ea4-519c-a9ed-906aae17294d.svg"
EXPORTED_REFERENCE_PATH = "work/brief-exports/20260918-all-todo-batches-15/batches/batch-001/references/arrow rectangle left svg360_9e23fdb9-8ea4-519c-a9ed-906aae17294d.svg"
AUTHOR = "claude-opus-5"


class LeftArrowSquareButtonBatch001R3(Solo48):
    icon_id = "left-arrow-square-button-batch-001-r3"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "arrows"
    categories = ("arrows", "primitives")
    aliases = ("square-chevron-left", "back-button")
    keywords = ("arrow", "left", "chevron", "back", "previous", "button", "square")

    def build(self) -> None:
        rounded_rect(self, "button", 6, 6, 42, 42, radius=4)
        axis_y, arm = 24, 9
        vertex_x = 19  # optical centre: the open side reads lighter
        self.add_polyline(
            "chevron",
            (vertex_x + arm, axis_y - arm), (vertex_x, axis_y), (vertex_x + arm, axis_y + arm),
        )
