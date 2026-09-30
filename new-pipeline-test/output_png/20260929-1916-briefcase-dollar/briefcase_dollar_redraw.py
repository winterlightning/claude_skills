"""briefcase-dollar (redraw of the new-pipeline traced SVG).

Plan: a wide rounded briefcase body with a centred carry handle on top and a
dollar sign centred inside, mirrored about x=24 on SQUARE (centerline box
(6,6)-(42,42)).
- body: rounded rectangle (6,16)-(42,42), corner radius 4, 36x26 so it reads
  wide like the generated image. Its sides are the x=6 / x=42 extremes and its
  base the y=42 extreme. The top edge is three standalone lines split at the
  handle feet, the base one standalone line, the sides two corner contours;
  every neighbour pair shares an endpoint and is declared `connect`. The top
  and base are standalone lines so the dollar can sit exactly 8 from them
  (an exact-8 gap only certifies against a standalone straight line).
- handle: inverted U, legs at x=17/31, r3 shoulders, top on y=6 (the top
  extreme); its hole is 14x10 on centerlines = 10x6 ink, so 6 inscribed.
- dollar: an S spine of two half-ellipses (rx 5, ry 2) stacked on the axis
  from y=25 to y=33, the upper bulging left and the lower right, with the bar
  shown as two stubs (24-25, 33-34) where it leaves the S. The stubs end
  exactly 8 below the body top and 8 above the base.
Lucide `briefcase` (rounded body + small U handle) and `dollar-sign` (axis
bar leaving an S) informed the construction; both are rebuilt on this grid.

Metric issues (briefcase-dollar_metrics.json) and how they were handled:
- stroke-width (info): redrawn at stroke 4; every gap is budgeted for it.
- stroke-count (9 strokes, budget 6): now 4 visual parts (body, handle, S,
  bar stubs).
- keyshape-short-axis (HRECT_L fills 92% of x): not fixed on HRECT_L, the
  keyshape was changed instead. HRECT_L's 32-unit height must hold the handle
  hole (10 on centerlines for 6 inscribed) + 8 + dollar + 8, which leaves a
  4-unit dollar. VRECT_L fits a 14-unit dollar but forces a 32x30 body that
  reads as a padlock; a merged handle tab on HRECT_L reads as a camera.
  SQUARE (third candidate, fill 1.0 x 0.87) keeps a wide 36x26 body and a
  10-unit dollar; all four extremes are touched exactly.
- clearance e0 vs e2..e8 (dollar parts 3.6-6.6 from the body walls): the
  dollar now ends exactly 8 from the body top and base, 13 from the sides.
- clearance e2/e3, e3/e7, e4/e5, e4/e6, e5/e8, e6/e8 (S hooks and bar
  fragments crowding each other): the S is one contour and the bar two stubs
  sharing its end points; no hook terminals, so no near-miss pairs remain.
- hole at (20.2, 11.5) 3.2 wide: the handle hole is now 6 inscribed.
Not kept from the trace: the S terminal hooks and the bar running through the
S. Both need a dollar about 16 tall (bowls 8 apart), which the body cannot
hold under the handle; the S is therefore a two-bulge spine with short stubs.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "07459f9b-1db4-4f1f-aeee-4e5113b2f2f4"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1916-briefcase-dollar/briefcase-dollar_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24                              # mirror axis
BODY_L, BODY_R, BODY_T, BODY_B, BODY_Q = 6, 42, 16, 42, 4
HANDLE_HALF, HANDLE_TOP, HANDLE_Q = 7, 6, 3
BAR_T, S_T, S_B, BAR_B = 24, 25, 33, 34
S_RX = 5


class BriefcaseDollarRedraw(Solo48):
    icon_id = "briefcase-dollar-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/finance"
    aliases = ("money briefcase", "business finance")
    keywords = ("briefcase", "dollar", "money", "business", "salary", "finance", "cash")

    def build(self) -> None:
        l, r, t, b, q = BODY_L, BODY_R, BODY_T, BODY_B, BODY_Q
        hl, hr = AX - HANDLE_HALF, AX + HANDLE_HALF

        # Body: standalone top (split at the handle feet) and base lines,
        # side contours carrying the corner arcs.
        self.add_line("body-top-l", (l + q, t), (hl, t))
        self.add_line("body-top-mid", (hl, t), (hr, t))
        self.add_line("body-top-r", (hr, t), (r - q, t))
        self.add_arc("body-tr", (r - q, t), (r, t + q), radius_x=q, sweep=True)
        self.add_line("body-right-wall", (r, t + q), (r, b - q))
        self.add_arc("body-br", (r, b - q), (r - q, b), radius_x=q, sweep=True)
        self.add_contour("body-right", "body-tr", "body-right-wall", "body-br")
        self.add_line("body-base", (r - q, b), (l + q, b))
        self.add_arc("body-bl", (l + q, b), (l, b - q), radius_x=q, sweep=True)
        self.add_line("body-left-wall", (l, b - q), (l, t + q))
        self.add_arc("body-tl", (l, t + q), (l + q, t), radius_x=q, sweep=True)
        self.add_contour("body-left", "body-bl", "body-left-wall", "body-tl")
        ring = ("body-top-l", "body-top-mid", "body-top-r", "body-right", "body-base", "body-left")
        for a, c in zip(ring, ring[1:] + ring[:1]):
            self.relate("connect", a, c)

        # Handle: inverted U standing on the body top at the split points.
        hq, ht = HANDLE_Q, HANDLE_TOP
        self.add_line("handle-left", (hl, t), (hl, ht + hq))
        self.add_arc("handle-tl", (hl, ht + hq), (hl + hq, ht), radius_x=hq, sweep=True)
        self.add_line("handle-top", (hl + hq, ht), (hr - hq, ht))
        self.add_arc("handle-tr", (hr - hq, ht), (hr, ht + hq), radius_x=hq, sweep=True)
        self.add_line("handle-right", (hr, ht + hq), (hr, t))
        self.add_contour("handle", "handle-left", "handle-tl", "handle-top", "handle-tr", "handle-right")
        for part in ("body-top-l", "body-top-mid", "body-top-r"):
            self.relate("connect", "handle", part)

        # Dollar: S spine of two half-ellipses on the axis, bar stubs at its ends.
        mid = (S_T + S_B) // 2
        ry = (S_B - S_T) // 4
        self.add_arc("s-upper", (AX, S_T), (AX, mid), radius_x=S_RX, radius_y=ry, sweep=False)
        self.add_arc("s-lower", (AX, mid), (AX, S_B), radius_x=S_RX, radius_y=ry, sweep=True)
        self.add_contour("s", "s-upper", "s-lower")
        self.add_line("bar-top", (AX, BAR_T), (AX, S_T))
        self.add_line("bar-bottom", (AX, S_B), (AX, BAR_B))
        self.relate("connect", "bar-top", "s")
        self.relate("connect", "bar-bottom", "s")
