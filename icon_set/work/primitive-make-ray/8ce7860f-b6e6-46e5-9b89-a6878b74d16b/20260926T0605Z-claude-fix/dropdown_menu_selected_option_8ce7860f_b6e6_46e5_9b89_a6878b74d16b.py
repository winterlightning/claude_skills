"""Dropdown menu with a selected option: a wide dropdown field at the top-left
overlapping an open option panel, with a check mark marking the selected option.

Symbol plan: two contours sharing the nodes (30,6) and (14,18). The field is a
closed box x 6..30, y 6..18 (two thirds of the width, as in the reference). The
panel is an open run from the field's top-right corner along the top, down the
right side, along the bottom and up its left side (x=14) into the field's bottom
edge, so the field reads as laid over the panel. Corners are square on the
centerline and painted round by the round joins, which keeps every clearance
straight-to-straight. The check mark sits in the panel below the field, exactly 8
from the field bottom and from the panel's left, right and bottom walls.
Omission: the reference's two option lines; the panel interior below the field is
one 8-unit band tall, which holds the check or one row, not both.
Revision: the rejected drawing shrank the field to a small tab and cramped the
check beside it.
Lucide construction: 'square-check' / 'clipboard-check' - box with an open check;
no dropdown-with-panel match.
Keyshape SQUARE: centerline 6..42 (field left/top, panel right/bottom).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "8ce7860f-b6e6-46e5-9b89-a6878b74d16b"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__dropdown-menu-selected-option/20260926T055144Z-thuan-mac/reference/web form drop down menu form_8ce7860f-b6e6-46e5-9b89-a6878b74d16b.svg"
AUTHOR = "claude-opus-5-5"


class DropdownMenuSelectedOption(Solo48):
    icon_id = "dropdown-menu-selected-option"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "websites"
    aliases = ("web-form-dropdown", "select-menu")
    keywords = ("dropdown", "menu", "selected", "check", "form", "options", "select", "interface")

    def build(self) -> None:
        left, top, right, bottom = 6, 6, 42, 42
        field_right, field_bottom, panel_left = 30, 18, 14
        self.add_polyline("field", (left, top), (field_right, top), (field_right, field_bottom),
                          (panel_left, field_bottom), (left, field_bottom), closed=True)
        self.add_polyline("panel", (field_right, top), (right, top), (right, bottom),
                          (panel_left, bottom), (panel_left, field_bottom))
        self.relate("connect", "field", "panel")
        self.add_polyline("check", (22, 30), (26, 34), (34, 26))
