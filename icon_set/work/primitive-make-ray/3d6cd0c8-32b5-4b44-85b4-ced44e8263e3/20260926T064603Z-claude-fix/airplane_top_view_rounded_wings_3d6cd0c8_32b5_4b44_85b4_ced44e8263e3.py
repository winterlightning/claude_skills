"""An airplane seen from above, nose up, with wide round-tipped wings and a small tailplane.

Symbol plan: mirror-symmetric about x = 24 (m(x) = 48 - x); one closed outline. The
fuselage walls are x 20 and 28 under an r4 round nose (top (24, 6)). Each wing is a swept
tube along the 3-4-5 direction (-4, 3): its leading edge runs from the wall (20, 14) to
(8, 23), an r5 cap about (11, 27) rounds the tip (outermost x 6), and the parallel
trailing edge returns 10 behind it to (18, 28) and steps onto the wall at (20, 28). The
wall continues to (20, 37); the tailplane flares out at 45 degrees to a point (15, 42)
and returns along the tail end y 42. The flare stays 8+ from the wing's trailing edge.
Earlier attempts: widening wings hid the fuselage (attempts/v1-diverging-wings.svg); a
narrow VRECT_L version and a version with the wings starting at the nose read as an up
arrow (attempts/v2-*, v3-*).
Lucide construction: 'plane' top view; round tips as Lucide semicircle caps.
Keyshape SQUARE: centerline x 6..42 (wing tips), y 6..42 (nose, tail).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3d6cd0c8-32b5-4b44-85b4-ced44e8263e3"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__airplane-top-view-rounded-wings/20260926T064521Z-thuan-mac/reference/plane_3d6cd0c8-32b5-4b44-85b4-ced44e8263e3.svg"
AUTHOR = "claude-opus-5-5"


def _m(p):
    return (48 - p[0], p[1])


class AirplaneTopViewRoundedWings(Solo48):
    icon_id = "airplane-top-view-rounded-wings"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transport"
    aliases = ("plane", "airplane", "aeroplane")
    keywords = ("airplane", "plane", "flight", "travel", "airport", "aviation", "jet", "trip")

    def build(self) -> None:
        # left half from the nose down to the tail centre: (kind, end, radius, sweep)
        left = [("L", (20, 14), 0, 0), ("L", (8, 23), 0, 0), ("A", (14, 31), 5, False),
                ("L", (18, 28), 0, 0), ("L", (20, 28), 0, 0), ("L", (20, 37), 0, 0),
                ("L", (15, 42), 0, 0), ("L", (20, 42), 0, 0)]
        names = []
        self.add_arc("nose", (20, 10), (28, 10), radius_x=4)
        # right half: nose right end down to the tail (mirrored, reversed sweep)
        here = (28, 10)
        for i, (kind, end, r, sweep) in enumerate(left):
            end = _m(end)
            n = f"right-{i + 1}"
            if kind == "L":
                self.add_line(n, here, end)
            else:
                self.add_arc(n, here, end, radius_x=r, sweep=not sweep)
            names.append(n)
            here = end
        self.add_line("tail-end", here, (20, 42))
        # left half back up to the nose
        pts = [(20, 10)] + [e for _, e, _, _ in left]
        back = []
        for i in range(len(left) - 1, -1, -1):
            kind, end, r, sweep = left[i]
            start = pts[i]
            n = f"left-{i + 1}"
            if kind == "L":
                self.add_line(n, end, start)
            else:
                self.add_arc(n, end, start, radius_x=r, sweep=not sweep)
            back.append(n)
        self.add_contour("airplane", "nose", *names, "tail-end", *back, closed=True)
