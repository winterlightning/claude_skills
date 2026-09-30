"""canoe (redraw of the new-pipeline traced SVG).

Subject: an open canoe in side view -- a long shallow hull with a flat
bottom and two upturned pointed ends joined by a dipping gunwale -- with one
single-bladed paddle floating diagonally above it (T grip, straight shaft,
hollow rounded blade).

Plan: HRECT_L, centerline box (4,8)-(44,40).
Extremes: x=4 / x=44 the two hull tips, y=40 the keel line, y=8 the top of
the paddle's T grip.
- hull: one closed contour mirrored about x=24. Tips (4,27)/(44,27); the
  gunwale is two mirrored cubics dipping to (24,31) with a level tangent at
  the centre, so the ends sweep up into the tips; each end drops as a cubic
  that leaves the tip vertically and lands level on the keel line y=40 at
  x=14/34; a straight keel joins them.
  Keel to gunwale is 9 on centerlines, so the hull's inside is a real hole.
- paddle: one axis on slope 1:3 (direction (3,1)), every knot on it.
  Grip bar (13,8)-(11,14) is perpendicular to the axis and split at the
  shaft end G=(12,11); shaft G->N=(24,15); blade N->T=(36,19) is an egg of
  two cubics mirrored about the axis (controls reflected through the axis),
  pointed at the neck where the shaft joins and round at the tip.
References: generated PNG read for the subject only (upturned ends,
dipping rim, flat keel, diagonal paddle with T grip and hollow blade). No
useful Lucide canoe exists; Lucide `sailboat` hull for the level keel with
curved ends. No trace coordinates copied.

Keyshape: the metrics suggested HRECT_M (score 1.10, y fill 85%) with
HRECT_L close behind (0.99). At stroke 4 the vertical stack does not fit
HRECT_M's 28 units: hull 13 + 8-9 clearance (curve to curve) + a hollow
blade and the grip rise need 32, which is exactly HRECT_L's centerline
height. The hull outline is 13 tall, the paddle 14; tried and rejected:
deeper tips (25) read as a tub rather than a canoe.

Metric issues:
- stroke-width (info): redrawn at stroke 4; every gap budgeted for it.
- keyshape-short-axis (y fill 85% on HRECT_M): fixed; on HRECT_L x runs
  exactly 4..44 (hull tips) and y exactly 8..40 (grip top, keel).
- clearance e1/e2 (blade vs hull bow, 7.55): fixed; the blade tip sits
  above the low middle of the gunwale; blade to hull is 8.7.
- clearance e1/e3 (blade overlapping the gunwale, 3.22): fixed; the whole
  paddle stays at least 8.7 above the gunwale.
- clearance e2/e3 (gunwale vs keel, 4.56): fixed; they are 9 apart.
- hole [30.9,23.6] (0.28, the blade/rim pinch): fixed; the pinch is gone
  and the blade is its own hole, about 9.5 across on centerlines.
- hole [10.2,32.7] (1.4, the thin hull interior): fixed; the hull interior
  is 9 tall at the centre.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "2f08daf6-071b-5ac7-9717-2239ffbb2925"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1945-canoe/canoe_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24                 # hull mirror axis
TIP_Y = 27              # hull tips at (4,27) / (44,27)
RIM_Y = 31              # gunwale low point at the centre
KEEL_Y, KEEL_DX = 40, 10  # keel line y=40, x 14..34

G, N, T = (12, 11), (24, 15), (36, 19)   # paddle axis: grip, neck, blade tip
BAR = (1, -3)                            # grip half-bar, perpendicular to (3,1)


def _mirror(x: float) -> float:
    return 2 * AX - x


def _reflect(p, origin=N, d=(3, 1)):
    """Reflect point p through the paddle axis (line through origin along d)."""
    vx, vy = p[0] - origin[0], p[1] - origin[1]
    k = 2 * (vx * d[0] + vy * d[1]) / (d[0] ** 2 + d[1] ** 2)
    return (origin[0] + k * d[0] - vx, origin[1] + k * d[1] - vy)


class CanoeRedraw(Solo48):
    icon_id = "canoe-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "outdoors"
    aliases = ("canoe and paddle", "open canoe")
    keywords = ("canoe", "paddle", "boat", "canoeing", "rowing", "water", "outdoors", "lake")

    def build(self) -> None:
        # Hull: gunwale (two mirrored cubics), ends and keel, one contour.
        lt, rt = (AX - 20, TIP_Y), (AX + 20, TIP_Y)
        mid = (AX, RIM_Y)
        kl, kr = (AX - KEEL_DX, KEEL_Y), (AX + KEEL_DX, KEEL_Y)
        rim_c1, rim_c2 = (9, 31), (15, RIM_Y)
        end_c1, end_c2 = (44, 35), (40, KEEL_Y)
        self.add_bezier("rim-l", lt, (rim_c1, rim_c2, mid))
        self.add_bezier("rim-r", mid, ((_mirror(rim_c2[0]), rim_c2[1]), (_mirror(rim_c1[0]), rim_c1[1]), rt))
        self.add_bezier("stern", rt, (end_c1, end_c2, kr))
        self.add_line("keel", kr, kl)
        self.add_bezier("bow", kl, ((_mirror(end_c2[0]), end_c2[1]), (_mirror(end_c1[0]), end_c1[1]), lt))
        self.add_contour("hull", "rim-l", "rim-r", "stern", "keel", "bow", closed=True)

        # Paddle: grip bar split at G, shaft, egg-shaped blade on one axis.
        self.add_polyline("grip", (G[0] + BAR[0], G[1] + BAR[1]), G, (G[0] - BAR[0], G[1] - BAR[1]))
        self.add_line("shaft", G, N)
        self.relate("connect", "shaft", "grip-1")
        self.relate("connect", "shaft", "grip-2")
        up_c1, up_c2 = (26, 10), (38, 12)
        self.add_bezier("blade-upper", N, (up_c1, up_c2, T))
        self.add_bezier("blade-lower", T, (_reflect(up_c2), _reflect(up_c1), N))
        self.add_contour("blade", "blade-upper", "blade-lower", closed=True)
        self.relate("connect", "shaft", "blade-upper")
        self.relate("connect", "shaft", "blade-lower")
