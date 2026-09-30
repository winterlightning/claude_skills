"""hands-supporting-child (redraw of the new-pipeline traced SVG).

Subject: a small child bust (detached ring head over rounded shoulders) held
between two mirrored cupped hands that rise on either side and curl in
beneath it (child care, child protection, family support).

Plan: SQUARE (the suggested keyshape; centerline box (6,6)-(42,42)).
- head: ring of four cardinal r5 arcs about (24,11); top y=6.
- shoulders: user.svg bust, one open contour about x=24. Short sides at
  x=16 / x=32 rise from y=30 into r4 corner arcs and a flat top line at
  y=24 = head_cy + r + stroke + 4 (exact 4-unit ink gap to the head).
- hands: one open stroke each, mirrored about x=24. Fingers rise straight
  on x=6 / x=42 (tips y=20), the palm cups in under the child (one cubic,
  tangent-continuous at both ends, lowest at y=39) and an r3 wrist arc drops
  to the stroke end at y=42.
Extremes: x=6 / x=42 finger strokes, y=6 head top, y=42 wrist ends.
References: the generated PNG (head over an open shoulder arc between two
cupped hands) and the choice brief ("single-line forearms curving inward
and upward underneath the child ... cupped palms without fingers");
human_ref/user.svg for the bust proportions (head r5 : shoulders 16 wide,
like Lucide user r4 : 14); Lucide hand-heart / hand-helping have no
front-facing cupped pair, so no Lucide construction was reused.

Metric issues (svg_metrics) and what happened to them:
- stroke-width (info): fixed, redrawn at stroke 4; every gap between
  distinct parts is budgeted at >= 8 on centerlines.
- keyshape-short-axis (SQUARE y fill 87%): fixed, the head top sits on y=6
  and the wrist ends on y=42, x extremes on 6 / 42 (exact SQUARE fit).
- clearance e0/e1 (head 2.54 from shoulders): fixed, exact 8 centerline gap
  (head bottom y=16, shoulder line y=24), flagged with mark_human_figure.
- clearance e1/e2, e1/e3 (shoulders 5.13 from the hands): fixed, the shoulder
  ends are 10 from the finger strokes and 9+ above the palm cups.
- clearance e2/e3 (wrists 7.08 apart): fixed, the wrist ends sit on x=19 /
  x=29, 10 apart.
- hole (head 4.66 inscribed): fixed, the r5 ring leaves a 6-unit hole.
- no-head (warn): fixed, the head is a true circle of cardinal arcs.
Deliberate change: the traced hands were closed outlines (finger band +
inner palm edge). An 8-wide finger band plus the 8 gap on each side leaves
<= 4 units for the child's shoulders on a 36-unit box (8 on HRECT_L), so the
hands became single cupping strokes, as the brief itself describes. Tried and
rejected: the bust resting on outlined fingertips (read as a crown / crab)
and short outlined hands under a floating child (read as "?" hooks).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "de2a447f-9464-4dd2-8a82-6bf0842bf389"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1518-hands-supporting-child/hands-supporting-child_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
HEAD_C, HEAD_R = (24, 11), 5
BODY_TOP = HEAD_C[1] + HEAD_R + 8          # 24: exact 4-unit ink gap
SHOULDER_HALF, CORNER_R, SIDE = 8, 4, 2    # bust x=16..32, sides down to y=30

FINGER_X, FINGER_TOP = 6, 20               # |x| extreme of the hands
PALM_Y = 39                                # lowest point of the palm cup
WRIST_R, WRIST_END = 3, 42


class HandsSupportingChildRedraw(Solo48):
    icon_id = "hands-supporting-child-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/family"
    aliases = ("child care", "child protection", "childcare", "caring hands")
    keywords = ("hands", "supporting", "child", "kid", "care", "protect",
                "family", "support", "cradle", "safety")

    def build(self) -> None:
        # Head: detached ring of four cardinal arcs.
        cx, cy = HEAD_C
        r = HEAD_R
        ring = ((cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy))
        for i in range(4):
            self.add_arc(f"head-{i + 1}", ring[i], ring[(i + 1) % 4], radius_x=r)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        # Shoulders: user.svg bust, open at the bottom.
        left, right = AXIS - SHOULDER_HALF, AXIS + SHOULDER_HALF
        corner_y = BODY_TOP + CORNER_R
        self.add_line("shoulder-side-l", (left, corner_y + SIDE), (left, corner_y))
        self.add_arc("shoulder-l", (left, corner_y), (left + CORNER_R, BODY_TOP),
                     radius_x=CORNER_R)
        self.add_line("shoulder-top", (left + CORNER_R, BODY_TOP),
                      (right - CORNER_R, BODY_TOP))
        self.add_arc("shoulder-r", (right - CORNER_R, BODY_TOP), (right, corner_y),
                     radius_x=CORNER_R)
        self.add_line("shoulder-side-r", (right, corner_y), (right, corner_y + SIDE))
        self.add_contour("shoulders", "shoulder-side-l", "shoulder-l", "shoulder-top",
                         "shoulder-r", "shoulder-side-r")
        self.mark_human_figure("child", head="head", torso="shoulder-top",
                               torso_junction="start")

        # Hands: mirrored cupping strokes, fingertip -> palm cup -> wrist.
        for side, name in ((-1, "left"), (1, "right")):
            def p(x, y):
                return (x, y) if side < 0 else (2 * AXIS - x, y)
            finger_foot = (FINGER_X, 29)
            palm_end = (19 - WRIST_R, PALM_Y)
            self.add_line(f"{name}-fingers", p(FINGER_X, FINGER_TOP), p(*finger_foot))
            self.add_bezier(f"{name}-palm", p(*finger_foot),
                            (p(FINGER_X, 36), p(10, PALM_Y), p(*palm_end)))
            self.add_arc(f"{name}-wrist", p(*palm_end), p(19, WRIST_END),
                         radius_x=WRIST_R, sweep=side < 0)
            self.add_contour(f"{name}-hand", f"{name}-fingers", f"{name}-palm",
                             f"{name}-wrist")
