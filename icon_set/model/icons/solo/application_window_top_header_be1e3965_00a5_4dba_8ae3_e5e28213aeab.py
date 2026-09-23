"""Application Window with Top Header.

Plan: one rounded frame owns the reference's connected dividers; repeated
lines share exact series coordinates. Lucide layout-panel-left informed the
framed panel proportions and single-weight partitions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'be1e3965-00a5-4dba-8ae3-e5e28213aeab'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_25/layout 2_be1e3965-00a5-4dba-8ae3-e5e28213aeab.svg'
AUTHOR = "gpt-6"

class ApplicationWindowTopHeader(Solo48):
    icon_id = 'application-window-top-header'
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
        self.add_line("divider-0", (6,20), (42,20))
        self.relate("connect", "divider-0", "frame")
