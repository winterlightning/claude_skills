"""An app window with a left navigation sidebar holding three menu items.

Plan: root = rounded-square frame with a full-height divider. The sidebar owns
a vertical series of three short menu strokes (count 3, step 8) centred on the
frame's horizontal axis; they sit 9u inside the curved frame and 8u from the
straight divider.
Keyshape: SQUARE, centerline box (6,6)-(42,42). The landscape reference needs
three menu rows 8u apart plus 9u frame clearance (34u), which only the 36u
SQUARE height provides.
Reduction: the menu strokes are shortened to 2u so the sidebar stays narrower
than the content pane.
Construction reference: Lucide `panel-left` and `layout-list` (menu strokes).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._batch_001_r3_shapes import rounded_rect

SOURCE_ICON_ID = "779a7169-b4d5-52a9-a799-2ce7e82c5026"
SOURCE_PATH = "/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/apps/sidebar line left_779a7169-b4d5-52a9-a799-2ce7e82c5026.svg"
EXPORTED_REFERENCE_PATH = "work/brief-exports/20260918-all-todo-batches-15/batches/batch-001/references/sidebar line left_779a7169-b4d5-52a9-a799-2ce7e82c5026.svg"
AUTHOR = "claude-opus-5"


class LeftSidebarNavigationLayoutBatch001R3(Solo48):
    icon_id = "left-sidebar-navigation-layout-batch-001-r3"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "apps"
    categories = ("apps", "primitives")
    aliases = ("sidebar-line-left", "navigation-sidebar")
    keywords = ("sidebar", "navigation", "menu", "left", "layout", "panel", "interface")

    def build(self) -> None:
        left, top, right, bottom = 6, 6, 42, 42
        menu_x0, menu_len = left + 9, 2
        divider_x = menu_x0 + menu_len + 8
        frame = rounded_rect(self, "frame", left, top, right, bottom, radius=4,
                             top_nodes=(divider_x,), bottom_nodes=(divider_x,))
        self.add_line("divider", (divider_x, top), (divider_x, bottom))
        for member in frame[(divider_x, top)] + frame[(divider_x, bottom)]:
            self.relate("connect", member, "divider")
        count, step, axis_y = 3, 8, 24
        first_y = axis_y - (count - 1) * step // 2
        for index in range(count):
            y = first_y + index * step
            self.add_line(f"menu-{index + 1}", (menu_x0, y), (menu_x0 + menu_len, y))
