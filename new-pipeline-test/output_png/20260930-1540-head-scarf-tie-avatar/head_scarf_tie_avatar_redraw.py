"""head-scarf-tie-avatar (redraw of the new-pipeline traced SVG).

Plan: a Lucide `user` bust (icon_set/references/human_ref/user.svg) wearing a
head scarf tied at the right temple, on VRECT_L (centerline box (8,4)-(40,44)).
- head: r10 circle on the axis x=20, split into four cardinal arcs; its top
  y=4 is the top extreme. The upper half is the scarf crown, the lower half the face.
- band: the scarf's forehead edge, a straight chord through the head centre
  (10,14)-(30,14). Both halves keep a hole of 6 ink, so the band cannot sit
  lower or curve without closing one of them.
- knot + tails: two drooping ribbon tails leave the chord end (30,14); the
  upper tail reaches x=40 (right extreme), the lower hangs to (35,27).
- bust: two r12 quarter arcs meeting at the neck (20,32), 8 below the head
  (4 units of ink); feet y=44 bottom extreme, left side x=8 left extreme.
The generated image drew the scarf as a separate arch outside the head. At 48
that arch needs its own 8-unit band all round, which leaves a 5-unit head that
reads as a ring (tried first; also failed MIC at the exact-8 concentric gap), so
the scarf is drawn on the head instead. The tails are open ribbons: the ~10 units
right of the head cannot hold even one hollow loop with a 6-ink hole.

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4 with every gap budgeted at stroke 4.
- keyshape-short-axis: all four extremes sit on the VRECT_L box exactly.
- clearance e0-e1 / e0-e2 (head vs scarf tails / arch fused at 5.36 and 0.06):
  the tails are declared connects at the knot and stay >= 8 from the head
  beyond it; the separate arch is replaced by the band.
- clearance e0-e3 (head vs shoulders 1.38) and e1-e3 (tail vs shoulders 6.83):
  head exactly 8 above the neck; lower tail tip >= 11 from the bust.
- narrow-join e1-e0 / e2-e0 (wedges): the band meets the head at a 90-degree
  T; the tails leave the knot outward rather than tangent to the head.
- hole 0.57: no sliver holes; crown and face each keep a 6-ink opening.
- no-head: the head is a true circle, flagged with mark_human_figure.
None left unfixed. validate_icon(): valid, no warnings; build_gate: PASS.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d91b104f-4bd1-4359-bf72-c9162bc1c67b"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1540-head-scarf-tie-avatar/"
    "head-scarf-tie-avatar_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 20                 # head / bust axis x
HEAD_Y = 14               # head centre y; head top y=4 is the top extreme
HEAD_R = 10               # head centerline radius
SHOULDER = 32             # shoulder top y: head bottom + 8 (4 units of ink)
FOOT = 44                 # bottom extreme
HALF = 12                 # half bust width; bust side x=8 is the left extreme
TAIL_TIP_A = (40, 16)     # upper tail tip, the right extreme
TAIL_TIP_B = (35, 27)     # lower tail tip


class HeadScarfTieAvatarRedraw(Solo48):
    icon_id = "head-scarf-tie-avatar-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people"
    aliases = ("headscarf avatar", "bandana user", "head scarf person")
    keywords = ("avatar", "user", "head scarf", "bandana", "headscarf", "tie", "profile", "person")

    def build(self) -> None:
        cx, cy, r = AXIS, HEAD_Y, HEAD_R
        left, right = (cx - r, cy), (cx + r, cy)

        # Head: upper half is the scarf crown, lower half the face; the
        # forehead band is the chord between them, knotted at the right temple.
        self.add_arc("crown-l", left, (cx, cy - r), radius_x=r, sweep=True)
        self.add_arc("crown-r", (cx, cy - r), right, radius_x=r, sweep=True)
        self.add_arc("face-r", right, (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("face-l", (cx, cy + r), left, radius_x=r, sweep=True)
        self.add_contour("head", "crown-l", "crown-r", "face-r", "face-l", closed=True)
        self.add_line("band", left, right)
        self.relate("connect", "head", "band")

        # Tie tails: two ribbons fanning out of the knot.
        kx, ky = right
        ax, ay = TAIL_TIP_A
        bx, by = TAIL_TIP_B
        self.add_bezier("tail-a", right, ((kx + 3, ky - 4), (ax - 1, ay - 8), (ax, ay)))
        self.add_bezier("tail-b", right, ((kx + 4, ky + 2), (bx + 2, by - 7), (bx, by)))
        for tail in ("tail-a", "tail-b"):
            self.relate("connect", "head", tail)
            self.relate("connect", "band", tail)
        self.relate("connect", "tail-a", "tail-b")

        # Bust: two quarter ellipses meeting at the neck.
        neck = (cx, SHOULDER)
        ry = FOOT - SHOULDER
        self.add_arc("shoulder-l", (cx - HALF, FOOT), neck, radius_x=HALF, radius_y=ry, sweep=True)
        self.add_arc("shoulder-r", neck, (cx + HALF, FOOT), radius_x=HALF, radius_y=ry, sweep=True)
        self.add_contour("bust", "shoulder-l", "shoulder-r")
        self.mark_human_figure("person", head="head", torso="shoulder-r", torso_junction="start")
