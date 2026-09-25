"""A screen split into three horizontal bands with a pull-out drawer tab below it.

Plan: root = the screen, a rounded rectangle whose two horizontal rules form a
series of three equal 9u bands; the drawer tab is an open U attached under the
screen's bottom edge, centred on x=24 and mirrored about it.
Keyshape: SQUARE, centerline box (6,6)-(42,42).
Reduction: the small chevron inside the tab is dropped: the tab is only 9u
tall, and a chevron needs 8u clearance to both tab edges. The tab's shape and
position alone carry the drawer reading.
Construction reference: Lucide `panels-top-left` (full-width rules in a frame).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._batch_001_r3_shapes import rounded_rect

SOURCE_ICON_ID = "b791a328-23eb-4943-b1f0-55d32115fef6"
SOURCE_PATH = "/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/apps/ui screen split_b791a328-23eb-4943-b1f0-55d32115fef6.svg"
EXPORTED_REFERENCE_PATH = "work/brief-exports/20260918-all-todo-batches-15/batches/batch-001/references/ui screen split_b791a328-23eb-4943-b1f0-55d32115fef6.svg"
AUTHOR = "claude-opus-5"


class TripleHorizontalScreenSplitBatch001R3(Solo48):
    icon_id = "triple-horizontal-screen-split-batch-001-r3"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "apps"
    categories = ("apps", "primitives")
    aliases = ("ui-screen-split", "three-row-layout")
    keywords = ("screen", "split", "rows", "bands", "drawer", "tab", "layout", "interface")

    def build(self) -> None:
        left, top, right = 6, 6, 42
        band, bands = 9, 3
        screen_bottom = top + band * bands
        axis_x, tab_half, tab_radius, tab_bottom = 24, 8, 4, 42
        tab_left, tab_right = axis_x - tab_half, axis_x + tab_half
        rule_ys = [top + band * (i + 1) for i in range(bands - 1)]
        screen = rounded_rect(self, "screen", left, top, right, screen_bottom, radius=4,
                              left_nodes=rule_ys, right_nodes=rule_ys,
                              bottom_nodes=(tab_left, tab_right))
        for index, y in enumerate(rule_ys):
            rule = f"rule-{index + 1}"
            self.add_line(rule, (left, y), (right, y))
            for member in screen[(left, y)] + screen[(right, y)]:
                self.relate("connect", member, rule)
        # Drawer tab: open U hanging from the screen's bottom edge.
        wall_end = tab_bottom - tab_radius
        self.add_line("tab-left", (tab_left, screen_bottom), (tab_left, wall_end))
        self.add_arc("tab-corner-left", (tab_left, wall_end), (tab_left + tab_radius, tab_bottom),
                     radius_x=tab_radius, sweep=False)
        self.add_line("tab-bottom", (tab_left + tab_radius, tab_bottom), (tab_right - tab_radius, tab_bottom))
        self.add_arc("tab-corner-right", (tab_right - tab_radius, tab_bottom), (tab_right, wall_end),
                     radius_x=tab_radius, sweep=False)
        self.add_line("tab-right", (tab_right, wall_end), (tab_right, screen_bottom))
        self.add_contour("tab", "tab-left", "tab-corner-left", "tab-bottom",
                         "tab-corner-right", "tab-right")
        for member in screen[(tab_left, screen_bottom)]:
            self.relate("connect", member, "tab-left")
        for member in screen[(tab_right, screen_bottom)]:
            self.relate("connect", member, "tab-right")
