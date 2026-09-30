"""combination-pliers (redraw of the new-pipeline traced SVG).

Plan: open combination pliers seen flat, jaws up, mirrored about x=24 on
VRECT_M (centerline box (10,4)-(38,44)).
- hinge: a closed r5 pin ring centred (24,22), split at the four points where
  the halves attach so every contact shares an endpoint.
- each half (one open contour): the handle rises from its tip on the box
  edge (10,44) to the ring's waist point (19,22); the jaw's outer wall is one
  cubic that bulges out to x~10 and curls in to the flat jaw tip (11,4)-(20,4);
  the inner jaw face drops straight down x=20 and lands on the ring at (20,19).
  The ring's top arc is the bottom of the notch between the jaws.
- handles are single strokes: a traced tube handle would need 10 between its
  walls and read as a fat bar at 48 px.
Traced shape: 20260930-1037-combination-pliers/combination-pliers_raw.svg,
read for proportion only (jaws ~1/3, hinge, long spreading handles).
No useful Lucide match (Lucide has no pliers).

Metric issues:
- stroke-width (info): redrawn at stroke 4 with every gap budgeted for it.
- keyshape-short-axis (warn): fixed; the handle tips sit on x=10 and x=38,
  so VRECT_M is filled on both axes.
- clearance e0/e2 3.4 apart (error): fixed; the separate notch-bottom arc is
  gone, the ring's top arc now closes the notch.
- holes 0.4 wide at the jaws (2 errors): fixed; each jaw encloses one hole
  bounded by x=20, the y=4 tip and the outer wall, 6 inscribed on the ink.
- hole 2.09 wide under the notch (error): fixed; removed, the notch is open
  and 8 wide on centerlines down to the ring.
- holes 0.28 wide in the handles (2 errors): fixed; handles are single
  strokes, so they enclose nothing.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6b9c56ef-5064-4dca-b96f-f14cdc63e5ef"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1037-combination-pliers/"
    "combination-pliers_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
HINGE_Y = 22
HINGE_R = 5
WAIST = (19, 22)       # handle and jaw wall meet the ring here
NOTCH_FOOT = (20, 19)  # inner jaw face lands on the ring here
TIP_Y = 4
HANDLE_TIP = (10, 44)


def mirror(p):
    return (2 * AXIS - p[0], p[1])


class CombinationPliersRedraw(Solo48):
    icon_id = "combination-pliers-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ("pliers", "lineman pliers")
    keywords = ("pliers", "combination", "tool", "grip", "cut", "wire", "hardware", "repair")

    def build(self) -> None:
        ring = [
            ("hinge-top", NOTCH_FOOT, mirror(NOTCH_FOOT)),
            ("hinge-r", mirror(NOTCH_FOOT), mirror(WAIST)),
            ("hinge-bottom", mirror(WAIST), WAIST),
            ("hinge-l", WAIST, NOTCH_FOOT),
        ]
        for name, a, b in ring:
            self.add_arc(name, a, b, radius_x=HINGE_R, sweep=True)
        self.add_contour("hinge", *[n for n, *_ in ring], closed=True)

        handle = ((10, 37), (14, 28), WAIST)
        slant_top = (11, TIP_Y)
        jaw_wall = ((10, 18), (9, 9), slant_top)
        inner_top = (NOTCH_FOOT[0], TIP_Y)

        # Left half, walked from the handle tip up and round the jaw.
        self.add_bezier("handle-l", HANDLE_TIP, handle)
        self.add_bezier("jaw-wall-l", WAIST, jaw_wall)
        self.add_line("jaw-tip-l", slant_top, inner_top)
        self.add_line("jaw-face-l", inner_top, NOTCH_FOOT)
        self.add_contour(
            "half-l", "handle-l", "jaw-wall-l", "jaw-tip-l", "jaw-face-l",
        )

        # Right half: exact mirror, walked in the same order.
        self.add_bezier("handle-r", mirror(HANDLE_TIP), tuple(mirror(q) for q in handle))
        self.add_bezier("jaw-wall-r", mirror(WAIST), tuple(mirror(q) for q in jaw_wall))
        self.add_line("jaw-tip-r", mirror(slant_top), mirror(inner_top))
        self.add_line("jaw-face-r", mirror(inner_top), mirror(NOTCH_FOOT))
        self.add_contour(
            "half-r", "handle-r", "jaw-wall-r", "jaw-tip-r", "jaw-face-r",
        )

        self.relate("connect", "half-l", "hinge")
        self.relate("connect", "half-r", "hinge")
