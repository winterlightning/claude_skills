"""decorative theater stage with audience: a scalloped stage valance with two
swept-open curtains, and two audience busts below it (redraw of the
new-pipeline traced SVG).

PLAN
- Keyshape HRECT_L, centerline box (4,8)-(44,40), mirrored about x=24. The
  metrics suggested HRECT_M (28 tall); the stage header and the busts need
  the full 32. The traced stacking (closed proscenium above the busts)
  cannot fit any SOLO48 keyshape: a detached bust is head 8 + gap 8 +
  shoulders 3 = 19 tall, plus 8 clearance under a stage floor, which leaves
  a 5-unit stage. Busts inside a closed frame were tried and read as a face
  (two ring eyes over a mouth), so the stage is drawn as its header only.
- Stage header, one open contour: short posts x=4/x=44 from y=16 up to the
  top edge y=8, flat top over each curtain, two r=4 scallops hung between
  the curtains (cusps on y=8 at x=16,24,32).
- Curtains: one Bezier each from the scallop's outer cusp (16,8) to the post
  foot (4,16), bowed 1.5 toward the stage like the reference; the shared
  endpoints join them to the header (scoped `connect`).
- Audience: two Lucide-user busts at x=24 -/+ 10 (the shared human
  reference, user.svg): r=4 hollow head (four cardinal quarter arcs), flat
  shoulder top on y=37 as a standalone line 8 below the head outline, r=3
  shoulder corners down to y=40. Each is flagged with mark_human_figure.

METRIC ISSUES
- clearance e0/e1/e2 vs e3 (curtains and valance 2-4 units under the frame
  top): fixed, the scallops are the header's own top edge and the curtains
  meet it only at shared endpoints.
- hole at (8.3,17.8) / (39.6,17.7) 3.8 wide: fixed, each curtain pocket is
  a 12 x 8 corner bowed outward; build gate hole check passes.
- clearance e3 vs e4..e7 (busts against the stage floor): fixed by dropping
  the floor and the lower proscenium (see PLAN); every head clears the
  curtains and scallops by 8 or more.
- clearance e4/e6, e5/e7 (heads fused to shoulders): fixed, head-to-shoulder
  gap is exactly 8 on centerlines / 4 ink, arc over a straight line.
- clearance e6/e7 (shoulders touching): fixed, shoulders end 8 apart.
- no-head (heads traced as dots): fixed, heads are r=4 rings.
- keyshape-short-axis (x fills 98%): fixed, posts on x=4 and x=44, top on
  y=8, shoulders on y=40.
- stroke-count 8 > 6: 5 connected parts (header with curtains, two heads,
  two shoulder arcs).
- stroke-width 2.55: redrawn at stroke 4.
NOT FIXED
- The traced proscenium sides and stage floor are omitted; they cannot sit
  8 units from the busts inside the 32-unit box.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ab781f1d-3fa8-44c5-ba49-25fd9a1a8848"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1154-decorative-theater-stage-with-audience/decorative-theater-stage-with-audience_raw.svg"
AUTHOR = "claude-opus-5-5"

MID_X = 24
LEFT, TOP, BOTTOM = 4, 8, 40
SCALLOP_R = 4
SCALLOPS = 2
CURTAIN_TOP = (MID_X - SCALLOPS * SCALLOP_R, TOP)     # (16,8), outer scallop cusp
CURTAIN_FOOT = (LEFT, 16)                             # post foot
CURTAIN_BOW = 1.5                                     # toward the stage
BUST_X = 14                                           # busts at 24 -/+ 10
SHOULDER_HALF = 6
SHOULDER_R = 3
SHOULDER_TOP = BOTTOM - SHOULDER_R                    # y=37
HEAD_R = 4
HEAD_GAP = 8                                          # head outline to shoulder top


def mirror(point: tuple[float, float]) -> tuple[float, float]:
    return (2 * MID_X - point[0], point[1])


def bowed_controls(start, end, bow):
    """Cubic controls at thirds of the chord, pushed ``bow`` along its downward normal."""
    dx, dy = end[0] - start[0], end[1] - start[1]
    length = (dx * dx + dy * dy) ** 0.5
    nx, ny = -dy / length, dx / length
    if ny < 0:
        nx, ny = -nx, -ny
    return tuple(
        (round(start[0] + dx * t + nx * bow, 2), round(start[1] + dy * t + ny * bow, 2))
        for t in (1 / 3, 2 / 3)
    )


class DecorativeTheaterStageWithAudienceRedraw(Solo48):
    icon_id = "decorative-theater-stage-with-audience-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/entertainment"
    aliases = ("theater stage", "theatre audience", "stage show")
    keywords = ("theater", "theatre", "stage", "curtain", "audience", "show",
                "performance", "play", "spectators")

    def build(self) -> None:
        right = 2 * MID_X - LEFT
        header = []
        self.add_line("post-left", CURTAIN_FOOT, (LEFT, TOP))
        self.add_line("top-left", (LEFT, TOP), CURTAIN_TOP)
        header += ["post-left", "top-left"]
        for index in range(SCALLOPS):
            x0 = CURTAIN_TOP[0] + index * 2 * SCALLOP_R
            apex = (x0 + SCALLOP_R, TOP + SCALLOP_R)
            self.add_arc(f"scallop-{index}-a", (x0, TOP), apex, radius_x=SCALLOP_R, sweep=False)
            self.add_arc(f"scallop-{index}-b", apex, (x0 + 2 * SCALLOP_R, TOP),
                         radius_x=SCALLOP_R, sweep=False)
            header += [f"scallop-{index}-a", f"scallop-{index}-b"]
        self.add_line("top-right", mirror(CURTAIN_TOP), (right, TOP))
        self.add_line("post-right", (right, TOP), mirror(CURTAIN_FOOT))
        header += ["top-right", "post-right"]
        self.add_contour("header", *header)

        c1, c2 = bowed_controls(CURTAIN_TOP, CURTAIN_FOOT, CURTAIN_BOW)
        self.add_bezier("curtain-left", CURTAIN_TOP, (c1, c2, CURTAIN_FOOT))
        self.add_bezier("curtain-right", mirror(CURTAIN_TOP),
                        (mirror(c1), mirror(c2), mirror(CURTAIN_FOOT)))
        self.relate("connect", "header", "curtain-left")
        self.relate("connect", "header", "curtain-right")

        head_y = SHOULDER_TOP - HEAD_GAP - HEAD_R
        for side, cx in (("left", BUST_X), ("right", 2 * MID_X - BUST_X)):
            outer, inner = cx - SHOULDER_HALF, cx + SHOULDER_HALF
            self.add_arc(f"shoulder-{side}-a", (outer, BOTTOM),
                         (outer + SHOULDER_R, SHOULDER_TOP), radius_x=SHOULDER_R)
            self.add_line(f"shoulders-{side}", (outer + SHOULDER_R, SHOULDER_TOP),
                          (inner - SHOULDER_R, SHOULDER_TOP))
            self.add_arc(f"shoulder-{side}-b", (inner - SHOULDER_R, SHOULDER_TOP),
                         (inner, BOTTOM), radius_x=SHOULDER_R)
            self.relate("connect", f"shoulder-{side}-a", f"shoulders-{side}")
            self.relate("connect", f"shoulders-{side}", f"shoulder-{side}-b")

            head = f"head-{side}"
            n, e = (cx, head_y - HEAD_R), (cx + HEAD_R, head_y)
            s, w = (cx, head_y + HEAD_R), (cx - HEAD_R, head_y)
            for label, a, b in (("ne", n, e), ("se", e, s), ("sw", s, w), ("nw", w, n)):
                self.add_arc(f"{head}-{label}", a, b, radius_x=HEAD_R)
            self.add_contour(head, *(f"{head}-{label}" for label in ("ne", "se", "sw", "nw")),
                             closed=True)
            self.mark_human_figure(f"audience-{side}", head=head,
                                   torso=f"shoulders-{side}", torso_junction="start")
