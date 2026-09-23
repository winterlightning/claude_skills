"""Left Sidebar with Right Stacked Rows.

Plan: one rounded frame owns the reference's connected dividers; repeated
lines share exact series coordinates. Lucide layout-panel-left informed the
framed panel proportions and single-weight partitions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cf641002-2c62-4330-aa21-85ea323db448'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_25/layout 14_cf641002-2c62-4330-aa21-85ea323db448.svg'
AUTHOR = "gpt-6"

class LeftSidebarRightStackedRows(Solo48):
    icon_id = 'left-sidebar-right-stacked-rows'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/layout"
    aliases = ()
    keywords = ("layout", "grid", "interface", "panels")

    def build(self) -> None:
        # The square ink envelope is (4,4)-(44,44), centered on 24.
        self.add_line("top", (10,6), (38,6))
        self.add_arc("top-right", (38,6), (42,10), radius_x=4, sweep=True)
        self.add_line("right", (42,10), (42,38))
        self.add_arc("bottom-right", (42,38), (38,42), radius_x=4, sweep=True)
        self.add_line("bottom", (38,42), (10,42))
        self.add_arc("bottom-left", (10,42), (6,38), radius_x=4, sweep=True)
        self.add_line("left", (6,38), (6,10))
        self.add_arc("top-left", (6,10), (10,6), radius_x=4, sweep=True)
        self.add_contour("frame", "top", "top-right", "right", "bottom-right", "bottom", "bottom-left", "left", "top-left", closed=True)
        self.add_line("divider-0", (24,6), (24,42))
        self.relate("connect", "divider-0", "frame")
        self.add_line("divider-1", (24,15), (42,15))
        self.relate("connect", "divider-1", "frame")
        self.add_line("divider-2", (24,24), (42,24))
        self.relate("connect", "divider-2", "frame")
        self.add_line("divider-3", (24,33), (42,33))
        self.relate("connect", "divider-3", "frame")
        self.relate("connect", "divider-0", "divider-1")
        self.relate("connect", "divider-0", "divider-2")
        self.relate("connect", "divider-0", "divider-3")
