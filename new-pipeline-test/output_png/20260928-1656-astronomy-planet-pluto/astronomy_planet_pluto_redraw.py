"""astronomy-planet-pluto (redraw of the new-pipeline traced SVG).

Plan: the dwarf planet Pluto on CIRCLE (centerline radius 20 about (24,24)).
- disk: one closed circle of two r20 half arcs, ink reaching radius 22.
- heart (Tombaugh Regio): a mirrored heart about x=28 in the lower right,
  two cubic lobes per side, tangent-continuous at the lobe tops and the
  widest points, a shallow notch at (28,23) and tip at (28,35). Every
  point stays within radius 12 of the centre, so 8+ from the disk.
- crater: a single dot in the upper left, 8+ from the disk and the heart.
Traced shape: 20260928-1656-astronomy-planet-pluto/astronomy-planet-pluto_raw.svg
(read for the subject only; nothing copied from its coordinates).
No useful Lucide match: lucide has `earth`/`orbit`, no Pluto; the heart
follows lucide/heart's lobe-and-tip construction at a smaller size.

Metric issues:
- clearance e0/e1 (crater ring 5.19 from the disk): fixed, the crater moves
  inward and sits >= 8 from the disk.
- clearance e0/e2 (heart 2.72 from the disk): fixed, the heart is rebuilt
  inside radius 12 so its outer flank is >= 8 from the disk.
- hole at the crater (2.4 inscribed, need 6): fixed by drawing the crater as
  a dot. A ring with a 6-wide hole needs r5 (10 across plus 8 clearance on
  every side), which leaves no room for a readable heart inside radius 12.
- stroke-width (info): drawn at stroke 4; all gaps budgeted for 4.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "538b81e2-4f12-5deb-8847-decaad176f32"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1656-astronomy-planet-pluto/"
    "astronomy-planet-pluto_raw.svg"
)
AUTHOR = "claude-opus-5-5"

C = 24           # disk centre
R = 20           # disk centerline radius
HEART_AX = 28    # heart mirror axis
NOTCH = (28, 23)
TIP = (28, 35)
CRATER = (15, 17)


def mirror(p):
    return (2 * HEART_AX - p[0], p[1])


class AstronomyPlanetPlutoRedraw(Solo48):
    icon_id = "astronomy-planet-pluto-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science/astronomy"
    aliases = ("pluto", "dwarf-planet")
    keywords = ("pluto", "planet", "dwarf planet", "astronomy", "space", "heart", "solar system")

    def build(self) -> None:
        self.add_arc("disk-top", (C - R, C), (C + R, C), radius_x=R, sweep=True)
        self.add_arc("disk-bottom", (C + R, C), (C - R, C), radius_x=R, sweep=True)
        self.add_contour("disk", "disk-top", "disk-bottom", closed=True)

        # Right half of the heart, notch -> lobe top -> widest -> tip.
        right = [
            ("heart-r1", NOTCH, ((29, 21.3), (30.4, 20), (32, 20))),
            ("heart-r2", (32, 20), ((34, 20), (35, 22.3), (35, 25))),
            ("heart-r3", (35, 25), ((35, 29), (31.5, 32), TIP)),
        ]
        for name, start, seg in right:
            self.add_bezier(name, start, seg)
        # Left half: mirrored, walked from the tip back up to the notch.
        left = []
        for name, start, (c1, c2, end) in reversed(right):
            lname = name.replace("-r", "-l")
            self.add_bezier(lname, mirror(end), (mirror(c2), mirror(c1), mirror(start)))
            left.append(lname)
        self.add_contour("heart", *[n for n, *_ in right], *left, closed=True)

        self.add_dot("crater", CRATER)
