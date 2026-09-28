"""An app window with a category sidebar on the left and stacked content tiles on the right.

Plan: root = rounded-square frame. A full-height divider splits it; the
sidebar owns a series of two category marks, and the content pane is split by
one horizontal rule into two stacked tiles that share the pane's edges.
Keyshape: SQUARE, centerline box (6,6)-(42,42).
Reduction: the two inset tile rectangles cannot fit at 48 with 8u clearance
around each, so the tiles become the pane's two stacked cells; the sidebar's
short menu strokes become two dots (a 2u stroke would crowd the divider).
Construction reference: Lucide `layout-panel-left` (sidebar + two stacked
tiles) and `panel-left` (frame with a full-height divider).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._batch_001_r3_shapes import rounded_rect

SOURCE_ICON_ID = "1b1a16b4-9e7f-486d-9436-8970f83666d9"
SOURCE_PATH = "/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/apps/categorization list_1b1a16b4-9e7f-486d-9436-8970f83666d9.svg"
EXPORTED_REFERENCE_PATH = "work/brief-exports/20260918-all-todo-batches-15/batches/batch-001/references/categorization list_1b1a16b4-9e7f-486d-9436-8970f83666d9.svg"
AUTHOR = "claude-opus-5"


class CategorizedSidebarLayoutBatch001R3(Solo48):
    icon_id = "categorized-sidebar-layout-batch-001-r3"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "apps"
    categories = ("apps", "primitives")
    aliases = ("categorization-list", "sidebar-tiles-layout")
    keywords = ("sidebar", "layout", "categories", "tiles", "dashboard", "window", "interface")

    def build(self) -> None:
        left, top, right, bottom = 6, 6, 42, 42
        divider_x, split_y = 23, 24
        frame = rounded_rect(self, "frame", left, top, right, bottom, radius=4,
                             top_nodes=(divider_x,), bottom_nodes=(divider_x,), right_nodes=(split_y,))
        self.add_line("divider-upper", (divider_x, top), (divider_x, split_y))
        self.add_line("divider-lower", (divider_x, split_y), (divider_x, bottom))
        self.add_line("tile-split", (divider_x, split_y), (right, split_y))
        for member in frame[(divider_x, top)]:
            self.relate("connect", member, "divider-upper")
        for member in frame[(divider_x, bottom)]:
            self.relate("connect", member, "divider-lower")
        for member in frame[(right, split_y)]:
            self.relate("connect", member, "tile-split")
        self.relate("connect", "divider-upper", "divider-lower")
        self.relate("connect", "divider-upper", "tile-split")
        self.relate("connect", "divider-lower", "tile-split")
        # Category marks: a series of two, 9u inside the curved frame and 8u from the divider.
        mark_x, first_y, step = 15, 16, 8
        for index in range(2):
            self.add_dot(f"category-{index + 1}", (mark_x, first_y + index * step))
