"""Header and Sidebar Website Layout.

Plan: one rounded frame owns the reference's connected dividers; repeated
lines share exact series coordinates. Lucide layout-panel-left informed the
framed panel proportions and single-weight partitions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ff1e1607-39c3-43d1-9b15-1bbdc71b1d27'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_25/layout 18_ff1e1607-39c3-43d1-9b15-1bbdc71b1d27.svg'
AUTHOR = "gpt-6"

class HeaderSidebarWebsiteLayout(Solo48):
    icon_id = 'header-sidebar-website-layout'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "websites"
    categories = ("websites", "primitive", "primitives")
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
        self.add_line("divider-0", (6,16), (42,16))
        self.relate("connect", "divider-0", "frame")
        self.add_line("divider-1", (18,16), (18,42))
        self.relate("connect", "divider-1", "frame")
        self.add_line("divider-2", (18,29), (42,29))
        self.relate("connect", "divider-2", "frame")
        self.relate("connect", "divider-0", "divider-1")
        self.relate("connect", "divider-1", "divider-2")
