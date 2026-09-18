"""An app window with a right-hand sidebar panel holding three menu items.

Plan: the mirror of the left-sidebar construction about x=24: rounded-square
frame, full-height divider, and a vertical series of three short menu strokes
(count 3, step 8) 9u inside the curved frame and 8u from the divider.
Keyshape: SQUARE, centerline box (6,6)-(42,42). Three menu rows 8u apart plus
9u frame clearance need 34u of height, which only SQUARE provides.
Reduction: the menu strokes are shortened to 2u so the sidebar stays narrower
than the content pane.
Construction reference: Lucide `panel-right` and `layout-list` (menu strokes).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._batch_001_r3_shapes import rounded_rect

SOURCE_ICON_ID = "1a419240-2e4b-5412-9f3a-4f6e4f0bf430"
SOURCE_PATH = "/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/apps/sidebar line right_1a419240-2e4b-5412-9f3a-4f6e4f0bf430.svg"
EXPORTED_REFERENCE_PATH = "work/brief-exports/20260918-all-todo-batches-15/batches/batch-001/references/sidebar line right_1a419240-2e4b-5412-9f3a-4f6e4f0bf430.svg"
AUTHOR = "claude-opus-5"


class RightSidebarInterfacePanelBatch001R3(Solo48):
    icon_id = "right-sidebar-interface-panel-batch-001-r3"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "apps"
    aliases = ("sidebar-line-right", "right-panel")
    keywords = ("sidebar", "panel", "menu", "right", "layout", "interface")

    def build(self) -> None:
        left, top, right, bottom = 6, 6, 42, 42
        menu_x1, menu_len = right - 9, 2
        divider_x = menu_x1 - menu_len - 8
        frame = rounded_rect(self, "frame", left, top, right, bottom, radius=4,
                             top_nodes=(divider_x,), bottom_nodes=(divider_x,))
        self.add_line("divider", (divider_x, top), (divider_x, bottom))
        for member in frame[(divider_x, top)] + frame[(divider_x, bottom)]:
            self.relate("connect", member, "divider")
        count, step, axis_y = 3, 8, 24
        first_y = axis_y - (count - 1) * step // 2
        for index in range(count):
            y = first_y + index * step
            self.add_line(f"menu-{index + 1}", (menu_x1 - menu_len, y), (menu_x1, y))
