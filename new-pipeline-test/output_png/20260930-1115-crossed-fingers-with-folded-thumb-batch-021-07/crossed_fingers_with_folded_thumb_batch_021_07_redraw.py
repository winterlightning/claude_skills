"""Crossed fingers with folded thumb (redraw of the new-pipeline traced SVG).

Plan: VRECT_L, centerline box (8,4)-(40,44). An isolated hand, so the human
head-gap rule does not apply. Four parts:
- Two finger tubes crossing at 45 degrees. Each is 9.9 wide (edges 14 apart
  in x+y or x-y) with an r5 3-4-5 tip: ends at centre+(-3,-4)/(4,3) for the
  front finger, mirrored for the back one, so both tip tops, (13,4) and
  (33,4), sit exactly on y = 4. The tip centres BACK_TIP and FRONT_TIP are
  20 apart, which puts the crossing low enough that the fingers stay long.
  - front finger (leaning right, drawn over): its left edge x+y = 35 runs
    from the palm corner C (8,27) to the tip. Its right edge x+y = 49 runs
    down to V (30,19), where the back finger comes out, and continues as
    the separate line `front-edge` to B (23,26) on the thumb.
  - back finger (leaning left, drawn behind): the tip piece `back-tip` ends
    on the front finger's left edge at G (16,19) and N (23,12): the
    over-under interruption. Below the crossing its right edge x-y = 11
    leaves V and becomes the fist's upper right corner.
- Fist: one closed `hand` contour. The back finger's edge rounds into the
  right side x = 40, a rounded palm bottom at y = 44, and the left side x = 8.
- Folded thumb: one open `thumb` contour. Its top edge rises from the left
  side J (8,30) through B, where the back finger's left edge would come out,
  so the thumb covers the base of the cross. A rounded tip, then a bottom
  edge about 8 below it that ends free inside the palm (the crease).
All joins are shared integer nodes declared with connect.

Keyshape: VRECT_L, not the suggested VRECT_M. At stroke 4 the 45-degree
cross needs tips 20 apart (X width 30), and the thumb tip must clear the
fist's corner by 8. That takes 32 units of width; VRECT_M has 28. The
metrics score VRECT_L 0.82 on the trace's aspect alone, and that trace had
2.6-wide strokes.
Dropped: the two separate curled-finger knuckles. With the thumb tip 8 from
the back finger's edge there is no room for another part that clears both.
The fist's corner stands in for them. The wrist is also dropped: a wrist
notch would come within 6 of the thumb's crease.
Changed: the cross is 45 degrees instead of the trace's steep (about 1:2)
fingers. At 1:2, the point below the crossing where the back finger comes
out falls at y = 33. That leaves no room for the thumb and palm, and the
back finger's lower half disappears; the cross then reads as a V sign.
Lucide `hand` / `hand-fist` (icon_set/references/lucide/original) gave the
rounded tube fingertips and a line that ends free inside the palm; the pose
comes from the generated image.

Metric issues (crossed-fingers-with-folded-thumb-batch-021-07_metrics.json):
- stroke-width (info, 2.63 fitted): redrawn at stroke 4 with every gap
  sized for it.
- keyshape-short-axis (warn, x fill 66% on VRECT_M): now on VRECT_L; the
  back tip's leftmost point (8,9), both tip tops at y = 4, the fist side
  x = 40 and the palm bottom y = 44 sit exactly on the box.
- clearance e1/e2, e1/e3, e1/e4, e1/e5, e2/e5 (error, 1.5-7.2): the knuckle
  capsules, thumb crease and front finger stub that crowded each other are
  gone. The thumb tip is 8.9 from the back finger's edge and 13 from the
  right side. The crease ends 9 from the left side and 8 from the palm
  bottom. The back-finger joint G is 8.6 from the thumb.
- loose-join e0/e2, e2/e3 (info): every contact is now a shared node with
  relate("connect").
- holes at (20.6,21.4), (20.8,7.1), (30.7,24.2), (22.8,26.8) (error,
  0.4-1.1): the only enclosed holes now are the two finger tubes (9.9 wide
  on centerlines). The palm stays open around the thumb's free crease.
Re-measured with svg_metrics.py (--keyshape VRECT_L) on the redraw, one
item is left: e0/e3 6.26 at (12,23)-(16,28). That is the narrow corner
where the front finger's left edge meets the thumb top. The two strokes
share the node, and any band cut obliquely by a straight line narrows this
way. validate_icon() and build_gate.py both pass it.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "05f00c7f-9195-41aa-b8b1-c15ae7c59bd3"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1115-crossed-fingers-with-folded-thumb-batch-021-07/crossed-fingers-with-folded-thumb-batch-021-07_raw.svg"
AUTHOR = "claude-opus-5-5"

TIP_R = 5
BACK_TIP = (13, 9)      # back finger tip centre: top (13,4), leftmost (8,9)
FRONT_TIP = (33, 9)     # front finger tip centre: top (33,4)

# Crossing nodes (front edges x+y = 35 / 49, back edges x-y = -3 / 11).
C = (8, 27)             # front finger's left edge meets the palm side
G = (16, 19)            # back finger's left edge meets it (under-crossing)
N = (23, 12)            # back finger's right edge meets it (notch)
V = (30, 19)            # back finger's right edge comes out from the front
B = (23, 26)            # front finger's right edge ends on the thumb
# Thumb.
J = (8, 30)             # thumb base on the palm side
T = (25, 34)            # bottom of the thumb tip
F = (17, 36)            # free end of the thumb crease


def _off(c, d):
    return (c[0] + d[0], c[1] + d[1])


class CrossedFingersWithFoldedThumbRedraw(Solo48):
    icon_id = "crossed-fingers-with-folded-thumb-batch-021-07-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/gestures"
    aliases = ("fingers crossed", "good luck")
    keywords = ("crossed", "fingers", "hand", "gesture", "luck", "hope", "wish", "thumb")

    def _run(self, name, start, *steps, closed=False):
        """One contour from L (line), A (arc: radius, sweep) and C (cubic) steps."""
        point, members = start, []
        for i, step in enumerate(steps):
            eid = f"{name}-{i}"
            kind, end = step[0], step[-1]
            if kind == "L":
                self.add_line(eid, point, end)
            elif kind == "A":
                self.add_arc(eid, point, end, radius_x=step[1], sweep=step[2])
            else:
                self.add_bezier(eid, point, (step[1], step[2], end))
            members.append(eid)
            point = end
        self.add_contour(name, *members, closed=closed)

    def build(self) -> None:
        # Front tip ends: centre+(-3,-4) on x+y = 35, centre+(4,3) on x+y = 49.
        front_l, front_r = _off(FRONT_TIP, (-3, -4)), _off(FRONT_TIP, (4, 3))
        # Back tip ends (mirrored): centre+(-4,3) on x-y = -3, centre+(3,-4) on x-y = 11.
        back_l, back_r = _off(BACK_TIP, (-4, 3)), _off(BACK_TIP, (3, -4))

        self._run(
            "hand", C,
            ("L", G), ("L", N), ("L", front_l),
            ("A", TIP_R, True, front_r),
            ("L", V),
            ("L", (35, 24)),                              # back finger, x-y = 11
            ("C", (37, 26), (40, 27), (40, 31)),          # fist corner
            ("L", (40, 33)),
            ("C", (40, 39), (36, 44), (30, 44)),
            ("L", (20, 44)),
            ("C", (13, 44), (8, 40), (8, 34)),
            ("L", J), ("L", C),
            closed=True,
        )
        self._run("back-tip", G, ("L", back_l), ("A", TIP_R, True, back_r), ("L", N))
        self.add_line("front-edge", V, B)
        self._run(
            "thumb", J,
            ("L", B),
            ("C", (26.4, 25.2), (28.4, 33.2), T),         # rounded thumb tip
            ("L", F),
        )
        for part in ("back-tip", "thumb", "front-edge"):
            self.relate("connect", "hand", part)
        self.relate("connect", "front-edge", "thumb")
