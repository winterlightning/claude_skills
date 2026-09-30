"""boxer (redraw of the new-pipeline traced SVG).

Plan: stick-figure boxer on VRECT_M (centerline box (10,4)-(38,44)), punching
to the right with the left arm up in guard. Built from shared parameters:
- head: two-half-arc circle, r5, centre (TX,9); its top is the y=4 extreme
  (r5 rather than r4 so the head keeps a clear opening at 48 px).
- torso: vertical line on the body axis TX from the neck (TX,22) to the hip (TX,32);
  the neck sits exactly 8 centerline units under the head outline (4-unit ink
  gap, human-reference.md), flagged with mark_human_figure.
- punch arm: horizontal from the neck to the fist at x=38 (right extreme).
- guard arm: shoulder -> elbow out left -> fist raised straight up; the
  forearm is the x=10 extreme, the fist kept >= 8 from the head outline.
- legs: two straight lines from the hip, mirrored about TX, feet on y=44.
Reference: icon_set/references/human_ref/full_body_ref.png (circular head,
round-ended single-stroke limbs). No useful Lucide match (Lucide has no
full-body action figure); the hiker redraw set the stick-figure vocabulary.

Metric issues:
- stroke-width (info): redrawn at stroke 4; every gap budgeted at 8 centerline.
- keyshape-short-axis (warn): fixed; guard forearm at x=10 and punch fist at
  x=38 reach both VRECT_M short-axis edges exactly, head top y=4, feet y=44.
- clearance e0/e1, e0/e2, e0/e3 (head vs arms and torso, 3.56): fixed; the
  head is detached exactly 8 above the neck (the certified human head gap).
- clearance e0/e4 (head vs guard forearm, 4.57): fixed; the guard fist sits
  at (10,15), 8.4 from the head outline on centerlines.
- clearance e1/e4, e2/e4 (guard forearm vs torso/punch, 7.11): fixed; the
  forearm is 12 from the torso axis.
- hole (3.0 wide head interior): fixed; the head is an r5 circle, a 10-wide
  centerline ring with a 6-wide visible opening at stroke 4.
- no-head (warn): fixed; the head is an explicit circle flagged as the head.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "c2a64d8a-ca70-53b9-b450-150287c2bfc6"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1929-boxer/boxer_raw.svg"
AUTHOR = "claude-opus-5-5"

TX = 22            # body axis
HEAD_R = 5
HEAD_CY = 9        # centerline top at y=4
NECK = (TX, HEAD_CY + HEAD_R + 8)   # exact 8 head-to-torso centerline gap
HIP = (TX, 32)
PUNCH_FIST = (38, NECK[1])
GUARD_ELBOW = (10, 25)
GUARD_FIST = (10, 15)
LEG_DX = 8
FOOT_Y = 44


class BoxerRedraw(Solo48):
    icon_id = "boxer-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ("boxing", "fighter", "puncher")
    keywords = ("boxer", "boxing", "punch", "fight", "sport", "martial arts", "person")

    def build(self) -> None:
        cx, cy, r = TX, HEAD_CY, HEAD_R
        # Two half arcs split at the sides, so the bottom apex facing the neck
        # is interior to one arc (certifies the exact 8 gap).
        self.add_arc("head-top", (cx - r, cy), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-bottom", (cx + r, cy), (cx - r, cy), radius_x=r, sweep=True)
        self.add_contour("head", "head-top", "head-bottom", closed=True)

        self.add_line("torso", NECK, HIP)
        self.mark_human_figure("boxer", head="head", torso="torso", torso_junction="start")

        self.add_line("punch-arm", NECK, PUNCH_FIST)
        self.relate("connect", "punch-arm", "torso")

        self.add_polyline("guard-arm", NECK, GUARD_ELBOW, GUARD_FIST)
        self.relate("connect", "guard-arm", "torso")
        self.relate("connect", "guard-arm", "punch-arm")

        self.add_line("left-leg", HIP, (TX - LEG_DX, FOOT_Y))
        self.add_line("right-leg", HIP, (TX + LEG_DX, FOOT_Y))
        self.relate("connect", "left-leg", "torso")
        self.relate("connect", "right-leg", "torso")
        self.relate("connect", "left-leg", "right-leg")
