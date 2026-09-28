"""Airplane diagonal: an airliner seen from above, flying toward the upper right,
with a long narrow fuselage, swept wings and a small tailplane.

Symbol plan: mirror symmetry about the flight axis x+y=48, reflection
(x, y) -> (48-y, 48-x), which keeps every point on the integer grid. The fuselage
sides run on x+y=41 and x+y=55 (9.9 apart). Nose and tail are radius-5 caps whose
ends are 3-4-5 offsets from the axis centres (37,11) and (11,37), so the nose is a
smooth round dome touching the top and right edges. Only the upper-left half of
the outline (wing, tailplane) is authored; the lower-right half is its mirror.
Revision (reviewer: diagonal toward the upper right, long narrow body, smoothly
rounded nose): the stubby cross-shaped body is replaced by a slim fuselage and a
round nose cap.
Lucide construction: 'plane' - diagonal airliner with swept wings.
Keyshape SQUARE: centerline 6..42 (nose cap top/right, wing tips, tail cap).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "2ec97e18-7c91-4c51-a73f-9939c19661c8"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__airplane-diagonal/20260926T061914Z-thuan-mac/reference/airplane_2ec97e18-7c91-4c51-a73f-9939c19661c8.svg"
AUTHOR = "claude-opus-5-5"

# Upper-left half, from the nose cap end to the tail cap end (sides on x+y=41).
HALF = ((34, 7), (28, 13), (12, 6), (6, 12), (21, 20), (15, 26), (7, 26), (7, 34))


def mirror(p: tuple[int, int]) -> tuple[int, int]:
    return (48 - p[1], 48 - p[0])


class AirplaneDiagonal(Solo48):
    icon_id = "airplane-diagonal"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/air"
    aliases = ("airplane", "plane", "flight")
    keywords = ("airplane", "plane", "flight", "travel", "aircraft", "airport", "jet")

    def build(self) -> None:
        members = []
        for i, (a, b) in enumerate(zip(HALF, HALF[1:]), 1):
            self.add_line(f"upper-{i}", a, b)
            members.append(f"upper-{i}")
        self.add_arc("tail", HALF[-1], mirror(HALF[-1]), radius_x=5, sweep=False)
        members.append("tail")
        lower = [mirror(p) for p in reversed(HALF)]
        for i, (a, b) in enumerate(zip(lower, lower[1:]), 1):
            self.add_line(f"lower-{i}", a, b)
            members.append(f"lower-{i}")
        self.add_arc("nose", lower[-1], HALF[0], radius_x=5, sweep=False)
        members.append("nose")
        self.add_contour("airframe", *members, closed=True)
