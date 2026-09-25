"""A pointed, house-shaped badge carrying an upward chevron: an "upgrade" or "move up" mark.

Plan: root = the badge, one closed contour mirrored about x=24: a 45-degree
gable apex, vertical walls, and radius-4 bottom corners. It owns a chevron
mirrored about the same axis, whose arms run parallel to the gable 12.7u
inside it.
Keyshape: VRECT_L, centerline box (8,4)-(40,44).
Reduction: the reference's softened apex relies on the stroke's round join.
Construction reference: Lucide `square-chevron-up` (chevron in a frame); no
useful pentagon-badge match was found.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "6fc2c407-33a8-5797-8946-2a1abe058890"
SOURCE_PATH = "/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/arrows/arrow badge top_6fc2c407-33a8-5797-8946-2a1abe058890.svg"
EXPORTED_REFERENCE_PATH = "work/brief-exports/20260918-all-todo-batches-15/batches/batch-001/references/arrow badge top_6fc2c407-33a8-5797-8946-2a1abe058890.svg"
AUTHOR = "claude-opus-5"


class UpwardPointingArrowBadgeBatch001R3(Solo48):
    icon_id = "upward-pointing-arrow-badge-batch-001-r3"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "arrows"
    categories = ("arrows", "primitives")
    aliases = ("arrow-badge-top", "upgrade-badge")
    keywords = ("arrow", "up", "badge", "chevron", "upgrade", "rank", "promote")

    def build(self) -> None:
        axis_x, apex_y, half_width, bottom, radius = 24, 4, 16, 44, 4
        eave_y = apex_y + half_width  # 45-degree gable
        left, right = axis_x - half_width, axis_x + half_width
        self.add_line("gable-right", (axis_x, apex_y), (right, eave_y))
        self.add_line("wall-right", (right, eave_y), (right, bottom - radius))
        self.add_arc("corner-right", (right, bottom - radius), (right - radius, bottom), radius_x=radius)
        self.add_line("base", (right - radius, bottom), (left + radius, bottom))
        self.add_arc("corner-left", (left + radius, bottom), (left, bottom - radius), radius_x=radius)
        self.add_line("wall-left", (left, bottom - radius), (left, eave_y))
        self.add_line("gable-left", (left, eave_y), (axis_x, apex_y))
        self.add_contour("badge", "gable-right", "wall-right", "corner-right", "base",
                         "corner-left", "wall-left", "gable-left", closed=True)
        vertex_y, arm = 23, 7
        self.add_polyline("chevron", (axis_x - arm, vertex_y + arm), (axis_x, vertex_y),
                          (axis_x + arm, vertex_y + arm))
