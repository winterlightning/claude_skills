"""athlete-pole-vaulting (redraw of the new-pipeline traced SVG).

Plan: vaulter hanging from a bowed pole, on VRECT_M (centerline box
(10,4)-(38,44); the trace is tall, 0.73 aspect, and the metrics' first choice).
- head: r4 ring of two semicircles about (20,8); its top is the y=4 extreme.
- torso: vertical line from the neck (20,20), exactly 8 centerline units under
  the head outline (4-unit ink gap, human-reference.md), down to the hip (20,30).
- arm: neck -> elbow (27,20) -> grip (35,16). The upper arm leaves the neck
  level, so the arm never rises beside the head (forearm 13.9 from its centre).
- legs from the hip: the lead leg kicked up-left, knee (12,26), foot (10,18);
  the trailing leg straight to (10,38). Both feet set the x=10 extreme.
- pole: short stub (33,8)-(35,16) above the grip, then one cubic leaving the
  grip along the stub's direction (tangent join) and landing vertical on the
  plant (38,44), the x=38 and y=44 extremes.
References: icon_set/references/human_ref/full_body_ref.png (ring head,
single-stroke limbs, bent-elbow arm). No useful Lucide match for a pole vault.

Metric issues:
- clearance e0/e1 (legs 4.18 apart): fixed; the legs now spread in a V, the
  trailing leg 8.1 from the lead knee.
- clearance e0/e2 (arm on the pole, 0.88): fixed; the arm ends on a shared
  grip node of the pole, declared with `connect`.
- clearance e0/e3 and e2/e3 (head 5.0 / 7.6 from arm and pole): fixed; the
  head is 12+ from the arm and 13 from the pole top (centre distances).
- no-head (the trace kept only a dot): fixed; r4 ring head flagged with
  mark_human_figure, exact 8 centerline gap to the torso.
- keyshape-short-axis (y filled 96%): fixed; all four extremes sit on the box.
- stroke-width (trace 2.55): rebuilt at stroke 4 with 8-unit clearances.
Deliberate change: the trace leaned the torso and ran both legs parallel to
the left; at stroke 4 those legs cannot hold 8 apart inside x>=10, so the
torso is upright and the legs splay.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "756dc826-ac42-5822-a4ca-d5598175bce1"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1704-athlete-pole-vaulting/athlete-pole-vaulting_raw.svg"
AUTHOR = "claude-opus-5-5"

# Figure: head straight above the neck; the torso drops to the hip, from
# which the legs swing up and out to the left. The arm reaches right to
# the grip with a bent elbow so it never rises beside the head.
HEAD = (20, 8)
HEAD_R = 4
NECK = (20, 20)          # head bottom 12 + 8 centerline gap
HIP = (20, 30)
LEG_LEAD = ((12, 26), (10, 18))   # knee, foot: kicked up
LEG_TRAIL = ((10, 38),)           # trailing leg
ELBOW = (27, 20)
# Pole: short stub above the grip, then one smooth bow down to the plant,
# which stands vertical on the right edge of the keyshape.
POLE_TOP = (33, 8)
GRIP = (35, 16)
PLANT = (38, 44)

class AthletePoleVaultingRedraw(Solo48):
    icon_id = "athlete-pole-vaulting-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ("pole vault", "pole vaulter", "vaulting athlete")
    keywords = ("athletics", "track and field", "jump", "pole", "sport", "olympics")

    def build(self) -> None:
        cx, cy = HEAD
        r = HEAD_R
        self.add_arc("head-top", (cx - r, cy), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-bottom", (cx + r, cy), (cx - r, cy), radius_x=r, sweep=True)
        self.add_contour("head", "head-top", "head-bottom", closed=True)

        self.add_line("torso", NECK, HIP)
        self.mark_human_figure("vaulter", head="head", torso="torso", torso_junction="start")

        self.add_polyline("leg-lead", HIP, *LEG_LEAD)
        self.add_polyline("leg-trail", HIP, *LEG_TRAIL)
        self.relate("connect", "leg-lead", "torso")
        self.relate("connect", "leg-trail", "torso")
        self.relate("connect", "leg-lead", "leg-trail")

        self.add_polyline("arm", NECK, ELBOW, GRIP)
        self.relate("connect", "arm", "torso")

        # The bow leaves the grip along the stub's direction (tangent join)
        # and lands vertically on the plant, the rightmost point x=38.
        dx, dy = GRIP[0] - POLE_TOP[0], GRIP[1] - POLE_TOP[1]
        self.add_line("pole-top", POLE_TOP, GRIP)
        self.add_bezier("pole-bow", GRIP,
                        ((GRIP[0] + dx, GRIP[1] + dy), (PLANT[0], PLANT[1] - 12), PLANT))
        self.add_contour("pole", "pole-top", "pole-bow")
        self.relate("connect", "pole", "arm")
