"""A car exploding: a side-view car split in two by a zigzag crack under a spiky blast.

Symbol plan: one car silhouette (sloped rear window, flat roof, sloped windshield,
flat underside with r3 semicircular wheel bumps) mirrored about x=24,
then cut by a steep zigzag crack. The two halves are separate closed contours; the right
crack edge is the left crack edge shifted 10 right so every facing crack segment keeps a
full clearance gap. Above the crack, a seven-point starburst is the blast.
Lucide construction: car (side profile with wheels on the underside) and 'zap'/'sparkles'
style straight spike runs for the burst.
Keyshape SQUARE: centerline x 6..42 (rear and front of the car), y 6..42 (burst top spike,
wheel bottoms).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "757187c1-fd16-4577-8bb6-b25ad4df2330"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__car-broken-beneath-impact-burst/20260925T093141Z-thuan-mac/reference/car explode_757187c1-fd16-4577-8bb6-b25ad4df2330.svg"
AUTHOR = "claude-opus-5-5"


class CarBrokenBeneathImpactBurst(Solo48):
    icon_id = "car-broken-beneath-impact-burst"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/vehicle"
    aliases = ("car-explode", "car-explosion", "car-crash")
    keywords = ("car", "explode", "explosion", "crash", "accident", "broken", "blast", "wreck")

    def build(self) -> None:
        roof, belt, floor, wheel_r = 30, 34, 39, 3
        crack = [(19, roof), (21, 33), (19, 36), (21, floor)]
        shift = 10
        n = len(crack) - 1
        # rear half: tail -> sloped rear window -> roof -> crack -> underside with wheel
        self.add_line("rear-tail", (6, floor), (6, belt))
        self.add_line("rear-window", (6, belt), (10, roof))
        self.add_line("rear-roof", (10, roof), crack[0])
        for i in range(n):
            self.add_line(f"rear-crack-{i}", crack[i], crack[i + 1])
        self.add_line("rear-floor", crack[n], (15, floor))
        self.add_arc("rear-wheel", (15, floor), (9, floor), radius_x=wheel_r, sweep=True)
        self.add_line("rear-sill", (9, floor), (6, floor))
        self.add_contour("rear-half", "rear-tail", "rear-window", "rear-roof",
                         *[f"rear-crack-{i}" for i in range(n)], "rear-floor",
                         "rear-wheel", "rear-sill", closed=True)

        # front half: mirror of the rear silhouette about x=24, cut by the shifted crack
        fc = [(x + shift, y) for x, y in crack]
        self.add_line("front-roof", fc[0], (38, roof))
        self.add_line("front-window", (38, roof), (42, belt))
        self.add_line("front-nose", (42, belt), (42, floor))
        self.add_line("front-sill", (42, floor), (39, floor))
        self.add_arc("front-wheel", (39, floor), (33, floor), radius_x=wheel_r, sweep=True)
        self.add_line("front-floor", (33, floor), fc[n])
        for i in range(n, 0, -1):
            self.add_line(f"front-crack-{i}", fc[i], fc[i - 1])
        self.add_contour("front-half", "front-roof", "front-window", "front-nose",
                         "front-sill", "front-wheel", "front-floor",
                         *[f"front-crack-{i}" for i in range(n, 0, -1)], closed=True)

        # blast: seven-point starburst above the crack
        self.add_polyline("burst", *BURST, closed=True)


# seven-point starburst above the crack: outer spikes alternate with inner valleys, clockwise from the top
BURST = ((24, 6), (28, 9), (35, 9), (34, 13), (38, 16), (32, 18), (30, 21), (24, 20),
         (18, 21), (16, 18), (10, 16), (14, 13), (13, 9), (20, 9))
