"""Responsive design: a browser window with a phone in front of its top-right corner.

Symbol plan: the phone is a rounded rectangle (r3) x 30..42, y 6..26 with a home-bar line
at y=18 leaving 8 below it. The browser window is a rounded rectangle (r3) x 6..42,
y 12..42 whose top edge, title-bar line (y=20) and right side stop short of the phone,
9 clear of it, so the phone reads as sitting in front of the window's corner.
Lucide construction: 'app-window' (rounded window with a title-bar line) and
'smartphone' (rounded tall rectangle with a bottom bar).
Keyshape SQUARE: centerline x 6..42 (window left, phone right), y 6..42 (phone top, window base).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ec576c6c-24a9-4446-afbc-2928327fc9cb"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__browser-window-and-phone/20260926T030905Z-thuan-mac/reference/responsive design image_ec576c6c-24a9-4446-afbc-2928327fc9cb.svg"
AUTHOR = "claude-opus-5-5"


class BrowserWindowAndPhone(Solo48):
    icon_id = "browser-window-and-phone"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology/devices"
    aliases = ("responsive-design", "responsive-design-image", "desktop-and-mobile")
    keywords = ("responsive", "design", "browser", "window", "phone", "mobile", "desktop", "web", "devices")

    def build(self) -> None:
        # phone
        px0, px1, py0, py1, bar, r = 30, 42, 6, 26, 18, 3
        self.add_line("phone-top", (px0 + r, py0), (px1 - r, py0))
        self.add_arc("phone-corner-tr", (px1 - r, py0), (px1, py0 + r), radius_x=r, sweep=True)
        self.add_line("phone-right-upper", (px1, py0 + r), (px1, bar))
        self.add_line("phone-right-lower", (px1, bar), (px1, py1 - r))
        self.add_arc("phone-corner-br", (px1, py1 - r), (px1 - r, py1), radius_x=r, sweep=True)
        self.add_line("phone-bottom", (px1 - r, py1), (px0 + r, py1))
        self.add_arc("phone-corner-bl", (px0 + r, py1), (px0, py1 - r), radius_x=r, sweep=True)
        self.add_line("phone-left-lower", (px0, py1 - r), (px0, bar))
        self.add_line("phone-left-upper", (px0, bar), (px0, py0 + r))
        self.add_arc("phone-corner-tl", (px0, py0 + r), (px0 + r, py0), radius_x=r, sweep=True)
        self.add_contour("phone", "phone-top", "phone-corner-tr", "phone-right-upper", "phone-right-lower",
                         "phone-corner-br", "phone-bottom", "phone-corner-bl", "phone-left-lower",
                         "phone-left-upper", "phone-corner-tl", closed=True)
        self.add_line("phone-home-bar", (px0, bar), (px1, bar))
        self.relate("connect", "phone", "phone-home-bar")
        # browser window, open where the phone sits in front
        wx0, wx1, wy0, wy1, title, stop = 6, 42, 12, 42, 20, 21
        self.add_line("window-top", (stop, wy0), (wx0 + r, wy0))
        self.add_arc("window-corner-tl", (wx0 + r, wy0), (wx0, wy0 + r), radius_x=r, sweep=False)
        self.add_line("window-left-upper", (wx0, wy0 + r), (wx0, title))
        self.add_line("window-left-lower", (wx0, title), (wx0, wy1 - r))
        self.add_arc("window-corner-bl", (wx0, wy1 - r), (wx0 + r, wy1), radius_x=r, sweep=False)
        self.add_line("window-bottom", (wx0 + r, wy1), (wx1 - r, wy1))
        self.add_arc("window-corner-br", (wx1 - r, wy1), (wx1, wy1 - r), radius_x=r, sweep=False)
        self.add_line("window-right", (wx1, wy1 - r), (wx1, py1 + 9))
        self.add_contour("window", "window-top", "window-corner-tl", "window-left-upper", "window-left-lower",
                         "window-corner-bl", "window-bottom", "window-corner-br", "window-right")
        self.add_line("window-title-bar", (wx0, title), (stop, title))
        self.relate("connect", "window", "window-title-bar")
