"""A landscape app window divided by a dashed line into a narrow left sidebar and a main pane.

Plan: root = rounded landscape frame. The dashed divider is one series along
x=16: a stub attached to each frame edge plus two free dashes, all separated by
equal 8u gaps, so the line reads as dashed and crosses the frame as in the
reference.
Keyshape: HRECT_L, centerline box (4,8)-(44,40).
Reduction: the reference's four dashes become two dashes and two edge stubs.
Construction reference: Lucide `panel-left` (frame and divider placement).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._batch_001_r3_shapes import rounded_rect

SOURCE_ICON_ID = "8b3c753d-e676-4e1a-811c-69448f6e158f"
SOURCE_PATH = "/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/apps/sidebar dots left_8b3c753d-e676-4e1a-811c-69448f6e158f.svg"
EXPORTED_REFERENCE_PATH = "work/brief-exports/20260918-all-todo-batches-15/batches/batch-001/references/sidebar dots left_8b3c753d-e676-4e1a-811c-69448f6e158f.svg"
AUTHOR = "claude-opus-5"


class LayoutWithLeftSidebarBatch001R3(Solo48):
    icon_id = "layout-with-left-sidebar-batch-001-r3"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "apps"
    aliases = ("sidebar-dots-left", "dashed-sidebar-layout")
    keywords = ("sidebar", "layout", "left", "dashed", "panel", "window", "interface")

    def build(self) -> None:
        left, top, right, bottom = 4, 8, 44, 40
        divider_x, dash, gap = 16, 2, 8
        frame = rounded_rect(self, "frame", left, top, right, bottom, radius=4,
                             top_nodes=(divider_x,), bottom_nodes=(divider_x,))
        # Series along the divider: stub, dash, dash, stub with equal gaps.
        self.add_line("stub-top", (divider_x, top), (divider_x, top + dash))
        y = top + dash + gap
        for index in range(2):
            self.add_line(f"dash-{index + 1}", (divider_x, y), (divider_x, y + dash))
            y += dash + gap
        assert y + dash == bottom
        self.add_line("stub-bottom", (divider_x, y), (divider_x, bottom))
        for member in frame[(divider_x, top)]:
            self.relate("connect", member, "stub-top")
        for member in frame[(divider_x, bottom)]:
            self.relate("connect", member, "stub-bottom")
