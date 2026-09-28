"""Monitor: a desktop computer monitor - a large screen on a vertical stem with a flat
foot.

Symbol plan: mirror symmetry about x=24. The screen is a rounded rectangle (radius
4) spanning the full width, x 6..42, and 26 tall (y 6..32), its bottom edge split at
the stem. The stem drops straight from (24,32) to the foot, a flat line 16 wide on
the bottom edge, split at the stem.
Revision (reviewer: "Make the screen wider and more vertical"): the 40x20 screen
on splayed legs becomes a 36x26 screen (taller in proportion, and the full width
of its keyshape) on the reference's stem and flat foot.
Lucide construction: 'monitor' - rounded screen, stem and base line.
Keyshape SQUARE: centerline 6..42 (screen sides/top, foot).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "78e9aab1-7764-40a5-b4c1-bf8d31d6b2cb"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__batch-01-monitor-computers/20260926T073832Z-thuan-mac/reference/monitor_78e9aab1-7764-40a5-b4c1-bf8d31d6b2cb.svg"
AUTHOR = "claude-opus-5-5"


class MonitorComputers(Solo48):
    icon_id = "batch-01-monitor-computers-solo"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology/computers"
    aliases = ("monitor", "desktop-screen")
    keywords = ("monitor", "screen", "display", "computer", "desktop", "pc")

    def build(self) -> None:
        left, top, right, bottom, r = 6, 6, 42, 32, 4
        self.add_line("screen-top", (left + r, top), (right - r, top))
        self.add_arc("screen-tr", (right - r, top), (right, top + r), radius_x=r)
        self.add_line("screen-right", (right, top + r), (right, bottom - r))
        self.add_arc("screen-br", (right, bottom - r), (right - r, bottom), radius_x=r)
        self.add_line("screen-bottom-right", (right - r, bottom), (24, bottom))
        self.add_line("screen-bottom-left", (24, bottom), (left + r, bottom))
        self.add_arc("screen-bl", (left + r, bottom), (left, bottom - r), radius_x=r)
        self.add_line("screen-left", (left, bottom - r), (left, top + r))
        self.add_arc("screen-tl", (left, top + r), (left + r, top), radius_x=r)
        self.add_contour("screen", "screen-top", "screen-tr", "screen-right", "screen-br",
                         "screen-bottom-right", "screen-bottom-left", "screen-bl", "screen-left",
                         "screen-tl", closed=True)
        self.add_line("stem", (24, bottom), (24, 42))
        self.add_polyline("foot", (16, 42), (24, 42), (32, 42))
        self.relate("connect", "screen", "stem")
        self.relate("connect", "stem", "foot")
