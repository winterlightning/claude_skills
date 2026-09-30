"""cricket-batter-with-raised-bat (redraw of the new-pipeline traced SVG).

Plan: stick-figure batter on VRECT_L (centerline box (8,4)-(40,44)), the bat
raised up and to the right of the head.
- head: 4-cardinal-arc circle, r5 (6-unit hole), centre (HX,9): top y=4 and
  left x=8 extremes.
- torso: vertical line on HX from the neck, exactly 8 centerline units under
  the head outline (4-unit ink gap, human-reference.md), split at the
  shoulder where the arm leaves it, down to the hip.
- legs: one inverted-V stance from the hip to both feet on the y=44 extreme.
- arm: one straight arm from the shoulder to the hands (the trace's two arms
  closed a 1.8-wide pocket).
- bat: built on the 3-4-5 direction so every node is an integer and the toe
  is tangent: the handle runs from the hands along UP=(3,-4) to the middle of
  the blade's flat shoulder edge; the blade has straight sides 5*BLADE_K long,
  10 apart (ACROSS=(4,3) each way), closed by an r5 semicircular toe whose
  centre (35,12) puts its right apex on the x=40 extreme. Blade and handle
  share one axis, so the bat is mirror-symmetric about it.
Reference: icon_set/references/human_ref/full_body_ref.png (circular head,
single-stroke round-ended limbs). No useful Lucide match for a cricket bat;
Lucide's round-cap / tangent-arc construction only.

Metric issues repaired:
- stroke-width: redrawn at stroke 4; every gap budgeted for 4.
- keyshape-short-axis: VRECT_M (28 wide) cannot hold the head (10) + 9
  clearance + a 10-wide tilted blade, so VRECT_L is used; all four extremes
  land exactly on its box (head top/left, toe right, feet bottom).
- no-head: the head is a true r5 circle, flagged with mark_human_figure;
  head-to-torso gap is exactly 8 on centerlines (4 ink).
- clearance e3/e4 and e2/e4 (torso/arms on the head): vertical torso under
  the head; the arm leaves the torso 3 below the neck.
- clearance e0/e4 (bat on head): the blade sits right of and below the
  head, its nearest corner 14.3 from the head centre (>= 9 from the outline).
- clearance e0/e3 (blade on arm) and both holes (1.8 / 2.0 wide): single arm,
  no arm pocket; the blade hole is 10 wide (6 inscribed).
- clearance e1/e3 (arm near the legs): the arm now meets the torso above
  the hip and rises away from the legs.
Validation: valid, no warnings.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1f09cd41-0bfa-474e-aa21-4f4bf44d8ab4"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1044-cricket-batter-with-raised-bat/"
    "cricket-batter-with-raised-bat_raw.svg"
)
AUTHOR = "claude-opus-5-5"

HX = 13                   # head / torso axis
HEAD_R = 5
HEAD_CY = 9               # top of head centerline at y=4
NECK_Y = HEAD_CY + HEAD_R + 8
SHOULDER = (HX, 25)
HIP = (HX, 32)
FEET = ((8, 44), (20, 44))

UP = (3, -4)              # bat axis, hands -> toe
ACROSS = (4, 3)           # blade half-width direction (|ACROSS| = 5)
TOE = (35, 12)            # r5 toe arc centre: right extreme x=40
TOE_R = 5
BLADE_K = 2               # straight blade sides = 5 * BLADE_K along UP
HANDLE_K = 2              # handle length below the blade, in 5s along UP


def _p(base, d, k):
    return (base[0] + d[0] * k, base[1] + d[1] * k)


class CricketBatterWithRaisedBatRedraw(Solo48):
    icon_id = "cricket-batter-with-raised-bat-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports/cricket"
    aliases = ("cricketer", "batsman", "batter")
    keywords = ("cricket", "batter", "batsman", "bat", "sport", "player", "batting")

    def build(self) -> None:
        cx, cy, r = HX, HEAD_CY, HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        self.add_line("torso", (HX, NECK_Y), SHOULDER)
        self.add_line("waist", SHOULDER, HIP)
        self.relate("connect", "torso", "waist")
        self.mark_human_figure("batter", head="head", torso="torso", torso_junction="start")

        self.add_polyline("legs", FEET[0], HIP, FEET[1])
        self.relate("connect", "legs", "waist")

        tr = _p(TOE, ACROSS, 1)
        tl = _p(TOE, ACROSS, -1)
        br = _p(tr, UP, -BLADE_K)
        bl = _p(tl, UP, -BLADE_K)
        mid = _p(TOE, UP, -BLADE_K)
        splice = mid                   # handle meets the blade's shoulder edge
        hands = _p(splice, UP, -HANDLE_K)

        self.add_polyline("arm", SHOULDER, hands)
        self.relate("connect", "arm", "torso")
        self.relate("connect", "arm", "waist")

        self.add_line("handle", hands, splice)
        self.relate("connect", "handle", "arm")

        self.add_line("blade-shoulder-r", splice, br)
        self.add_line("blade-side-r", br, tr)
        self.add_arc("blade-toe", tr, tl, radius_x=TOE_R, sweep=False)
        self.add_line("blade-side-l", tl, bl)
        self.add_line("blade-shoulder-l", bl, splice)
        self.add_contour("blade", "blade-shoulder-r", "blade-side-r", "blade-toe",
                         "blade-side-l", "blade-shoulder-l", closed=True)
        self.relate("connect", "blade", "handle")
