"""closed-fitness-band-with-two-display-marks (redraw of the new-pipeline trace).

Plan: a closed wristband seen from the front, a rounded display pod across
its middle and two stacked display marks (Lucide `watch` construction: a face
with straps above and below, here closed into loops).
- pod: rounded rectangle on the full VRECT_M width, (10,11)-(38,37), corner
  radius 6. The top and bottom edges are split at x=16 and x=32 where the
  corner arcs end, so the straps share those nodes.
- straps: one half-ellipse loop (rx 8, ry 7) above and one below, each made
  of two quarter arcs from the pod corner nodes (16,11)/(32,11) and
  (16,37)/(32,37). Their
  apexes (24,4) and (24,44) are the keyshape's top and bottom extremes. Each
  loop leaves the pod at 90 degrees.
- marks: two equal lines from x=19 to x=29 at y=20 and y=28, 8 apart and 9
  from every pod wall. At exactly 8 the arc-bearing pod contour comes back
  `review` (the exact-8 trap).
All parts mirror about x=24 and y=24.
Vertical budget: 7 strap + 9 + 8 + 9 pod interior + 7 strap = 40, the full
VRECT_M height. The pod carries the x extremes. The strap is narrower (16),
so the loops still read as a band.

Keyshape: VRECT_M, as suggested (score 0.72, tall subject).

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4 with every gap budgeted at 8.
- stroke-count (11 strokes): now 4 parts (pod, two straps, and the marks as
  two lines).
- keyshape-short-axis (x filled 47%): the pod now spans x 10-38, so all
  four extremes sit exactly on the VRECT_M box.
- clearance e0/e3, e0/e6, e3/e5, e6/e8 (pod edges 1.5-1.8 from the band
  wall): the band walls no longer run beside the pod. The straps start at
  the pod corner nodes (declared connect).
- clearance e0/e9, e0/e10, e1/e9, e2/e10, e3/e9, e4/e9, e5/e9, e6/e10,
  e7/e10, e8/e10 (marks 4-6.4 from walls): the marks are 9 from every wall.
- clearance e9/e10 (marks 4.25 apart): now 8 apart.
- narrow-join e1/e0, e2/e0, e5/e0, e8/e0 (30 degree wedges): every strap
  meets the pod at 90 degrees.
- loose-join e4/e0, e5/e0, e7/e0, e8/e0: joins share exact nodes and are
  declared with relate('connect').
- holes at (20.9,18.6), (19.9,23.8), (21.0,29.1) (1.1-2.6 wide): the pod
  corner wedges are gone. The only holes left are the two strap loops
  (centerline inscribed 7) and the pod interior.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1cd0692c-3506-4df2-80d7-66be18de3019"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1936-closed-fitness-band-with-two-display-marks/closed-fitness-band-with-two-display-marks_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24                  # mirror axis
L, R = 10, 38            # pod side walls (VRECT_M x extremes)
T, B = 11, 37            # pod top / bottom edges, 9 from the marks
CR = 6                   # pod corner radius; corners end at the strap nodes
SL, SR = L + CR, R - CR  # strap walls, x = 16 / 32
SRX = (SR - SL) // 2     # strap half-width 8
SRY = T - 4              # strap height 7; apexes at y = 4 / 44
MARK_YS = (T + 9, B - 9)  # y = 20 / 28, 8 apart
MARK_L, MARK_R = L + 9, R - 9  # x = 19 / 29


class ClosedFitnessBandWithTwoDisplayMarksRedraw(Solo48):
    icon_id = "closed-fitness-band-with-two-display-marks-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("fitness tracker", "activity band", "smart band")
    keywords = ("fitness", "band", "tracker", "wristband", "wearable", "display", "health")

    def build(self) -> None:
        self.add_arc("c-tl", (L, T + CR), (SL, T), radius_x=CR, sweep=True)
        self.add_line("top", (SL, T), (SR, T))
        self.add_arc("c-tr", (SR, T), (R, T + CR), radius_x=CR, sweep=True)
        self.add_line("right", (R, T + CR), (R, B - CR))
        self.add_arc("c-br", (R, B - CR), (SR, B), radius_x=CR, sweep=True)
        self.add_line("bottom", (SR, B), (SL, B))
        self.add_arc("c-bl", (SL, B), (L, B - CR), radius_x=CR, sweep=True)
        self.add_line("left", (L, B - CR), (L, T + CR))
        self.add_contour(
            "pod", "c-tl", "top", "c-tr", "right", "c-br", "bottom", "c-bl", "left",
            closed=True,
        )

        top_apex, bottom_apex = (AX, T - SRY), (AX, B + SRY)
        self.add_arc("strap-top-l", (SL, T), top_apex, radius_x=SRX, radius_y=SRY, sweep=True)
        self.add_arc("strap-top-r", top_apex, (SR, T), radius_x=SRX, radius_y=SRY, sweep=True)
        self.add_contour("strap-top", "strap-top-l", "strap-top-r")
        self.add_arc("strap-bottom-r", (SR, B), bottom_apex, radius_x=SRX, radius_y=SRY, sweep=True)
        self.add_arc("strap-bottom-l", bottom_apex, (SL, B), radius_x=SRX, radius_y=SRY, sweep=True)
        self.add_contour("strap-bottom", "strap-bottom-r", "strap-bottom-l")
        self.relate("connect", "strap-top", "pod")
        self.relate("connect", "strap-bottom", "pod")

        for i, y in enumerate(MARK_YS):
            self.add_line(f"mark-{i + 1}", (MARK_L, y), (MARK_R, y))
