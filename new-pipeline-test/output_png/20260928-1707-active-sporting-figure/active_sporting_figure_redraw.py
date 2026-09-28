"""active-sporting-figure (redraw of the new-pipeline traced SVG).

Plan: right-facing running stick figure on SQUARE (centerline box (6,6)-(42,42)).
- head: 4-cardinal-arc circle, r4, centre (HX,10); its top is the y=6 extreme.
- torso: a 2-long vertical neck stub from (HX,22), exactly 8 centerline units
  under the head outline (4-unit ink gap, human-reference.md), then the lower
  torso leans back to a set-back hip so the figure runs forward.
- arms leave the shoulder at the stub end (never from the neck): the back arm
  goes level then drops; the front arm bends down to an elbow and swings up to
  the hand, which sets the x=42 extreme.
- legs from the hip: the rear leg stretches straight back to the (6,42) corner
  (x=6 and y=42 extremes); the front leg lifts the knee forward and drops the
  shin to the ground line.
Reference: icon_set/references/human_ref/full_body_ref.png (circular head,
single-stroke round-ended limbs); no useful Lucide match beyond the stick-figure
construction of `person-standing`.

Metric issues fixed:
- stroke-width: redrawn at stroke 4 with every gap budgeted at 8 centerline.
- keyshape-short-axis: the rear foot (x=6) and front hand (x=42) now reach the
  SQUARE box, so the x axis fills 100% instead of 87%.
- clearance e0/e1, e0/e2 and head-gap: the head sits straight above a vertical
  neck stub at exactly 8 (ink gap 4); both arms branch 2 lower, 14+ from the
  head centre.
- clearance e1/e2, e1/e3, e2/e3: the trace's separate strokes are rebuilt as one
  connected figure (shared shoulder and hip nodes); the back hand, front elbow
  and front knee keep 8+ from every other limb.
- hole (3.26 wide): the head is an r4 ring (6-circle exemption) and no other
  enclosed pocket remains.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "62189f84-b3c6-4b58-ba8a-fae03adee313"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1707-active-sporting-figure/"
    "active-sporting-figure_raw.svg"
)
AUTHOR = "claude-opus-5-5"

HX = 30               # head / neck axis
HEAD_R = 4
HEAD_CY = 10          # centerline top y=6
NECK = (HX, HEAD_CY + HEAD_R + 8)
SHOULDER = (HX, NECK[1] + 2)
HIP = (24, 34)
BACK_ELBOW, BACK_HAND = (20, 24), (16, 28)
FRONT_ELBOW, FRONT_HAND = (37, 28), (42, 22)
KNEE, FRONT_FOOT = (32, 36), (28, 42)
REAR_FOOT = (6, 42)


class ActiveSportingFigureRedraw(Solo48):
    icon_id = "active-sporting-figure-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ("runner", "running person", "athlete")
    keywords = ("run", "running", "sport", "exercise", "fitness", "jogging", "active")

    def build(self) -> None:
        cx, cy, r = HX, HEAD_CY, HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        self.add_line("torso", NECK, SHOULDER)
        self.add_line("waist", SHOULDER, HIP)
        self.relate("connect", "torso", "waist")
        self.mark_human_figure("runner", head="head", torso="torso", torso_junction="start")

        self.add_polyline("back-arm", SHOULDER, BACK_ELBOW, BACK_HAND)
        self.add_polyline("front-arm", SHOULDER, FRONT_ELBOW, FRONT_HAND)
        for arm in ("back-arm", "front-arm"):
            self.relate("connect", arm, "torso")
            self.relate("connect", arm, "waist")
        self.relate("connect", "back-arm", "front-arm")

        self.add_line("rear-leg", HIP, REAR_FOOT)
        self.add_polyline("front-leg", HIP, KNEE, FRONT_FOOT)
        self.relate("connect", "rear-leg", "waist")
        self.relate("connect", "front-leg", "waist")
        self.relate("connect", "front-leg", "rear-leg")
