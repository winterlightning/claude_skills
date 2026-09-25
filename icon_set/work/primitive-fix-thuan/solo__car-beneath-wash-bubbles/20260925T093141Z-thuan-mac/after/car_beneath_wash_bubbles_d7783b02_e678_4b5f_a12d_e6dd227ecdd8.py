"""A car wash: a front-view car under three diagonal streaks of washing spray.

Symbol plan: Lucide car-front construction on the x=24 axis -- a rounded body (r2
corners), a trapezoid cabin standing on the body's top edge, and two wheel stubs hanging
from its bottom edge, all mirrored. Above the roof, three equal parallel diagonal spray
lines on a 10-unit pitch (8.7 perpendicular) replace the source's dots, as the reviewer
asked.
Lucide construction: car-front (body rect, cabin trapezoid, wheel stubs).
Keyshape SQUARE: centerline x 6..42 (body sides), y 6..42 (spray tops, wheel stubs).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d7783b02-e678-4b5f-a12d-e6dd227ecdd8"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__car-beneath-wash-bubbles/20260925T093141Z-thuan-mac/reference/car repair wash 2_d7783b02-e678-4b5f-a12d-e6dd227ecdd8.svg"
AUTHOR = "claude-opus-5-5"


class CarBeneathWashBubbles(Solo48):
    icon_id = "car-beneath-wash-bubbles"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/service"
    aliases = ("car-wash", "car-repair-wash")
    keywords = ("car", "wash", "car-wash", "cleaning", "spray", "water", "service", "garage")

    def build(self) -> None:
        left, right, belt, floor, r = 6, 42, 30, 38, 2
        roof, roof_l, roof_r, foot_l, foot_r = 22, 14, 34, 10, 38
        wheel_l, wheel_r = 11, 37
        # body: rounded rectangle, top edge split where the cabin stands, bottom where the wheels hang
        self.add_line("body-top-l", (left + r, belt), (foot_l, belt))
        self.add_line("body-top-m", (foot_l, belt), (foot_r, belt))
        self.add_line("body-top-r", (foot_r, belt), (right - r, belt))
        self.add_arc("body-tr", (right - r, belt), (right, belt + r), radius_x=r, sweep=True)
        self.add_line("body-right", (right, belt + r), (right, floor - r))
        self.add_arc("body-br", (right, floor - r), (right - r, floor), radius_x=r, sweep=True)
        self.add_line("body-bottom-r", (right - r, floor), (wheel_r, floor))
        self.add_line("body-bottom-m", (wheel_r, floor), (wheel_l, floor))
        self.add_line("body-bottom-l", (wheel_l, floor), (left + r, floor))
        self.add_arc("body-bl", (left + r, floor), (left, floor - r), radius_x=r, sweep=True)
        self.add_line("body-left", (left, floor - r), (left, belt + r))
        self.add_arc("body-tl", (left, belt + r), (left + r, belt), radius_x=r, sweep=True)
        self.add_contour("body", "body-top-l", "body-top-m", "body-top-r", "body-tr", "body-right",
                         "body-br", "body-bottom-r", "body-bottom-m", "body-bottom-l", "body-bl",
                         "body-left", "body-tl", closed=True)
        # cabin: windscreen trapezoid standing on the body
        self.add_polyline("cabin", (foot_l, belt), (roof_l, roof), (roof_r, roof), (foot_r, belt))
        self.relate("connect", "body", "cabin")
        # wheels
        self.add_line("wheel-left", (wheel_l, floor), (wheel_l, 42))
        self.add_line("wheel-right", (wheel_r, floor), (wheel_r, 42))
        self.relate("connect", "body", "wheel-left")
        self.relate("connect", "body", "wheel-right")
        # washing spray: three parallel diagonal streaks above the roof
        for i, x in enumerate((12, 22, 32)):
            self.add_line(f"spray-{i + 1}", (x, 13), (x + 4, 6))
