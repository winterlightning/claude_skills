"""hammerhead-shark (redraw of the new-pipeline traced SVG).

Subject: a hammerhead shark seen from above, one closed hollow outline with a
wide hammer head, two swept pectoral fins and a forked tail.

Plan (VRECT_M, the suggested keyshape; centerline box (10,4)-(38,44)),
written for the left half and mirrored about x=24:
- hammer: straight top y=4 and underside y=12 (exactly 8 apart), rounded
  ends are r4 semicircles centred (14,8)/(34,8) whose apex is x=10/38, so
  the hammer sets both side extremes and the top.
- neck: straight walls x=19/29 from the underside down to the fin roots.
- pectoral fins: a convex cubic leading edge sweeps back from (19,17) to the
  tip (10,28); a gently concave trailing edge returns to the root (19,25).
- body: straight walls (19,25)->(20,33) taper to the caudal peduncle.
- tail: lobes flare out from the peduncle and curve down to tips (14,44)/(34,44) on the bottom edge;
  straight inner edges meet in the notch (24,40).
All knots are integers; left and right are exact mirrors.

Metric issues:
- fixed: clearance e0/e1 2.5 < 8 (the trace pinched the peduncle shut).
  The peduncle is now 8 wide on centerlines (x=20..28).
- fixed: clearance e0/e2 and e1/e2 6.28 < 8 (the tail notch sat against
  the peduncle walls). The notch (24,40) is 8.06 from both peduncle nodes
  and from the opposite lobe's outer curve (sampled). The fin trailing
  root (19,25) is 8.06 from the peduncle, so fin and tail do not crowd.
- fixed: keyshape-short-axis (x filled 85%). The hammer is widened to the
  full 28-wide box, so every extreme sits on VRECT_M exactly.
- fixed: stroke-width (info). Redrawn at stroke 4; every opening is
  budgeted for stroke 4 (hammer slot 8, neck 10, peduncle 8).
Dropped: the trace's wavy hammer edges and the curled hammer tips (too fine
at 48 px). The body is shorter and wider than the trace: at stroke 4 the
fins, body segment and tail each need their own 8-unit spacing inside the
40-unit height.
Lucide: no useful shark match (Lucide `fish` is a side view); construction
follows the generated PNG. validate_icon(): valid, no warnings;
build_gate.py: PASS, 0 errors, 0 warnings.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "bdd1577c-6f14-5bee-a41f-fac2b80017a7"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1316-hammerhead-shark/"
    "hammerhead-shark_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
TOP_Y, UNDER_Y = 4, 12          # hammer top and underside
END_X, END_R = 14, 4            # hammer end arcs centred (14,8), apex x=10
NECK_X = 19
NECK_Y = 17                     # fin leading-edge root
FIN_TIP = (10, 28)
FIN_ROOT = (19, 25)             # trailing-edge root
PEDUNCLE = (20, 33)
TAIL_TIP = (14, 44)
NOTCH = (AXIS, 40)
# Left-side curves as (control1, control2) between their end nodes.
LEAD = ((16, 19), (12, 23))     # convex leading edge, sweeps back to the tip
TRAIL = ((13, 27), (16, 25))    # concave trailing edge, forward to the root
TAIL_OUT = ((16, 35), (13, 39)) # tail lobe bulges outward


def mx(p):
    return (2 * AXIS - p[0], p[1])


class HammerheadSharkRedraw(Solo48):
    icon_id = "hammerhead-shark-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/sea-life"
    aliases = ("hammerhead", "hammerhead shark", "shark")
    keywords = ("shark", "hammerhead", "fish", "ocean", "sea", "marine", "animal", "predator")

    def build(self) -> None:
        # Left half, top to bottom: hammer end -> underside -> neck -> fin -> tail.
        top_l, top_r = (END_X, TOP_Y), mx((END_X, TOP_Y))
        under_l = (END_X, UNDER_Y)
        neck_top, neck_bot = (NECK_X, UNDER_Y), (NECK_X, NECK_Y)
        # (id, start, end, controls or None for a straight segment)
        left = [
            ("under-l", under_l, neck_top, None),
            ("neck-l", neck_top, neck_bot, None),
            ("lead-l", neck_bot, FIN_TIP, LEAD),
            ("trail-l", FIN_TIP, FIN_ROOT, TRAIL),
            ("body-l", FIN_ROOT, PEDUNCLE, None),
            ("tail-out-l", PEDUNCLE, TAIL_TIP, TAIL_OUT),
            ("tail-in-l", TAIL_TIP, NOTCH, None),
        ]

        def seg(name, a, b, ctrl):
            if ctrl is None:
                self.add_line(name, a, b)
            else:
                self.add_bezier(name, a, (ctrl[0], ctrl[1], b))

        self.add_line("top", top_l, top_r)
        self.add_arc("end-r", top_r, mx(under_l), radius_x=END_R)
        # Right half runs down (mirrored), left half runs back up (reversed).
        for name, a, b, c in left:
            seg(name.replace("-l", "-r"), mx(a), mx(b), c and (mx(c[0]), mx(c[1])))
        for name, a, b, c in reversed(left):
            seg(name, b, a, c and (c[1], c[0]))
        self.add_arc("end-l", under_l, top_l, radius_x=END_R)
        self.add_contour(
            "outline", "top", "end-r",
            *(n.replace("-l", "-r") for n, *_ in left),
            *(n for n, *_ in reversed(left)),
            "end-l", closed=True,
        )
