"""Smartphone in front of a tablet (iOS / iPadOS devices), authored on SOLO48.

Plan: SQUARE centerline box (6,6)-(42,42). Front phone = rounded r4 rectangle
16x23 with a chin line 8 above its base. Tablet behind = rounded r4 rectangle
(16,6)-(42,42) drawn only where it is not hidden: a top-left corner hook ending
9 above the phone, the top and right walls, and the bottom run ending 8+ right of
the phone. Tablet chin line 8 above its base leaves the right wall.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3fb51cae-d169-4028-adc1-8f278625e347"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__smartphone-and-tablet-devices-batch-006-11/20260927T155415Z-thuan-mac-1/reference/ios ipados devices_3fb51cae-d169-4028-adc1-8f278625e347.svg"
AUTHOR = "claude-opus-5-5"


class SmartphoneAndTabletDevices(Solo48):
    icon_id = "smartphone-and-tablet-devices-batch-006-11"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology"
    categories = ("technology", "primitives")
    aliases = ("ios ipados devices", "phone and tablet")
    keywords = ("smartphone", "tablet", "devices", "ios", "ipados", "mobile")

    def build(self) -> None:
        r = 4
        # Phone (front)
        L, R, T, B, chin = 6, 22, 19, 42, 34
        self.add_line("phone-top", (L + r, T), (R - r, T))
        self.add_arc("phone-tr", (R - r, T), (R, T + r), radius_x=r)
        self.add_line("phone-right-a", (R, T + r), (R, chin))
        self.add_line("phone-right-b", (R, chin), (R, B - r))
        self.add_arc("phone-br", (R, B - r), (R - r, B), radius_x=r)
        self.add_line("phone-bottom", (R - r, B), (L + r, B))
        self.add_arc("phone-bl", (L + r, B), (L, B - r), radius_x=r)
        self.add_line("phone-left-b", (L, B - r), (L, chin))
        self.add_line("phone-left-a", (L, chin), (L, T + r))
        self.add_arc("phone-tl", (L, T + r), (L + r, T), radius_x=r)
        self.add_contour("phone", "phone-top", "phone-tr", "phone-right-a", "phone-right-b", "phone-br",
                         "phone-bottom", "phone-bl", "phone-left-b", "phone-left-a", "phone-tl", closed=True)
        self.add_line("phone-chin", (L, chin), (R, chin))
        self.relate("connect", "phone", "phone-chin")
        # Tablet (behind)
        TL, TR, TT, TB = 16, 42, 6, 42
        self.add_arc("tablet-tl", (TL, TT + r), (TL + r, TT), radius_x=r)
        self.add_line("tablet-top", (TL + r, TT), (TR - r, TT))
        self.add_arc("tablet-tr", (TR - r, TT), (TR, TT + r), radius_x=r)
        self.add_line("tablet-right-a", (TR, TT + r), (TR, chin))
        self.add_line("tablet-right-b", (TR, chin), (TR, TB - r))
        self.add_arc("tablet-br", (TR, TB - r), (TR - r, TB), radius_x=r)
        self.add_line("tablet-bottom", (TR - r, TB), (30, TB))
        self.add_contour("tablet", "tablet-tl", "tablet-top", "tablet-tr", "tablet-right-a", "tablet-right-b",
                         "tablet-br", "tablet-bottom")
        self.add_line("tablet-chin", (31, chin), (TR, chin))
        self.relate("connect", "tablet", "tablet-chin")
