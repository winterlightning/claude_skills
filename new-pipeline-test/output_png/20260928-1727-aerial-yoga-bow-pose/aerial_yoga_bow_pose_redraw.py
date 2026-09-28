"""aerial-yoga-bow-pose (redraw of the new-pipeline traced SVG).

Subject: a person doing bow pose (dhanurasana) in an aerial yoga hammock,
side view facing right. The belly rests in the hammock, the chest lifts, the
knees bend behind, and the hands reach back to hold the ankles, so body and
arm form a bow and its string.

Plan: SQUARE (centerline box (6,6)-(42,42)), the metrics' suggested keyshape.
The trace filled only 86% of the height; the redraw hits all four extremes
exactly: strap top and head top y=6, knee x=6, head right x=42, belly y=42.
- body, one closed contour (the bow): chest quarter arc r14 (centre (23,28))
  from the belly (23,42) up to a vertical tangent at the shoulder (37,28);
  the straight arm "string" back to the ankle (11,15); the shin down to the
  knee (6,33); the thigh back to the belly. Clear knee corner (~100 deg).
- foot: a short flick from the ankle up and back to (8,11), past the hand,
  so the hand reads as holding the ankle.
- hammock strap: one vertical line x=23 from the top down to the belly.
  It crosses the arm at the lattice point (23,21) (arm slope 1/2), where
  both are split into shared endpoints with scoped connects.
- neck + head: a standalone 4-long vertical neck stub above the shoulder
  and an r5 ring head (37,11). Head bottom 16 to neck end 24 = exactly 8 on
  centerlines (4 ink), axis-aligned so the gap is certifiable; flagged with
  mark_human_figure.
References: icon_set/references/human_ref (ring head, single-stroke limbs,
detached 4-unit head gap along the upper-torso axis). No useful Lucide
match: Lucide has no yoga or hammock figure.
Dropped: the second hammock strap and the U sling. Two straps crossing the
arm split the bow into three regions, and the torso side cannot keep a
6-unit opening inside a 36 box. One strap to the belly keeps "suspended in a
hammock" and leaves two open regions (inscribed ink ~10 and ~11).

Metric issues fixed:
- clearance e0/e1, e0/e3, e0/e6, e1/e2, e1/e3, e1/e4, e1/e5, e1/e6, e2/e3,
  e2/e4, e2/e5, e3/e4, e3/e5, e4/e6 (1.7-7.8: the doubled torso/arm band,
  hammock tube and legs tangled at stroke 2.4): rebuilt as one bow contour,
  one strap and one foot. Every contact is a shared integer node with a
  scoped connect; all other parts are >= 8 apart on centerlines.
- clearance e1/e7, e3/e7 (head crowding the shoulder and arm): the head sits
  exactly 8 above the neck stub, >= 10 from the arm and 9 from the strap.
- holes 2.2, 3.05, 1.13, 2.0 wide: the only openings left are the two bow
  regions either side of the strap (>= 6 inscribed) and the r5 head ring
  (inscribed 6). The build gate passes with no hole findings.
- no-head: the head is a true circle flagged as the figure's head.
- keyshape-short-axis (y 86%): all four SQUARE extremes are exact.
- stroke-count (8 traced, budget 6): 7 strokes (body, foot, 2 strap
  segments, neck, head); the strap is one line split at the crossing, so
  6 visual strokes.
- stroke-width (2.37 trace): redrawn at stroke 4 with every gap budgeted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "4a1112c6-2f20-434b-b756-511460d08610"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1727-aerial-yoga-bow-pose/aerial-yoga-bow-pose_raw.svg"
AUTHOR = "claude-opus-5-5"

STRAP_X = 23
TORSO_R = 14                 # chest quarter arc, centre (23,28)
STRAP_TOP = (STRAP_X, 6)
HIP = (STRAP_X, 42)          # belly bottom in the hammock
SHOULDER = (37, 28)
NECK = (37, 24)
HEAD_R = 5
HEAD_C = (37, 11)            # 16 -> 24: exactly 8 on centerlines
CROSS = (STRAP_X, 21)        # bowstring meets the strap (slope 1/2)
ANKLE = (11, 15)
TOE = (8, 11)
KNEE = (6, 33)


class AerialYogaBowPoseRedraw(Solo48):
    icon_id = "aerial-yoga-bow-pose-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports/yoga"
    aliases = ("aerial bow pose", "hammock bow pose", "aerial dhanurasana")
    keywords = ("yoga", "aerial", "hammock", "bow", "dhanurasana", "backbend", "pose", "fitness")

    def build(self) -> None:
        self.add_arc("torso", HIP, SHOULDER, radius_x=TORSO_R, sweep=False)
        self.add_line("arm-front", SHOULDER, CROSS)
        self.add_line("arm-back", CROSS, ANKLE)
        self.add_line("shin", ANKLE, KNEE)
        self.add_line("thigh", KNEE, HIP)
        self.add_contour("body", "torso", "arm-front", "arm-back", "shin", "thigh", closed=True)
        self.add_line("foot", ANKLE, TOE)
        self.relate("connect", "foot", "body")

        self.add_line("strap-top", STRAP_TOP, CROSS)
        self.add_line("strap-low", CROSS, HIP)
        self.relate("connect", "strap-top", "body")
        self.relate("connect", "strap-low", "body")
        self.relate("connect", "strap-top", "strap-low")

        self.add_line("neck", SHOULDER, NECK)
        self.relate("connect", "neck", "body")

        cx, cy, r = HEAD_C[0], HEAD_C[1], HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)
        self.mark_human_figure("yogi", head="head", torso="neck", torso_junction="end")
