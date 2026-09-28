"""camper behind flagged tent (redraw of the new-pipeline traced SVG).

Plan: HRECT_L (centerline box (4,8)-(44,40)), the suggested keyshape; the
trace is wide (aspect 1.16) and the redraw reaches all four extremes exactly.
- tent: one closed contour, a 45-degree triangle about the axis x=26, apex
  A=(26,22), base (8,40)-(44,40) (bottom and right extremes). The doorway is
  an inverted V with apex (26,34) and 45-degree legs to (20,40)/(32,40), so
  each leg runs parallel to its tent side 8.49 apart, and the base stops at
  the door (no sill), as in the reference and Lucide `tent`.
- flag: a straight pole from the apex up to (26,8) (top extreme), carrying a
  12x10 rectangular flag (26,8)-(38,18) whose left edge is the upper pole.
- camper: stick figure behind the tent at left, from
  icon_set/references/human_ref (ring head, single round-ended limbs). Ring
  head r4 about (12,12) (top y=8); vertical torso from the neck (12,24),
  exactly 8 under the head outline, down to the tent's left side at (12,36),
  where the side is split and the contact declared, so the tent hides the
  legs. The raised waving arm branches 5 below the neck at (12,29) and rises
  at 45 degrees to the hand (4,21) (left extreme), 12.04 from the head centre.
Lucide `tent` informed the triangle with a small inverted-V doorway whose
legs follow the sides; Lucide `flag` informed pole + flag. Deliberate
asymmetry: the camper stands at left and the flag points right.

Metric issues fixed:
- keyshape-short-axis (HRECT_L x fill 93%): every extreme now sits on the box
  (hand x=4, base end x=44, flag and head top y=8, base y=40).
- no-head: the trace lost the head (e3 was a dot); the camper has a real r4
  ring head with the exact 8-unit centerline (4 ink) head-to-neck gap.
- clearance e0/e2 and e1/e2 geometry (flag arc into the apex): the flag is a
  rectangle on the pole, its bottom-right corner 9.9 from the tent side.
- clearances e0/e4, e0/e6 (body and arm crowding the tent side): the torso
  ENDS on the tent side at a shared node (connect), the arm leaves it
  perpendicular and the hand is 15.6 from the side.
- clearances e3/e4, e3/e6, e5/e6 (head/arm/legs tangle): the head is 12+
  from every stroke; the second arm and the legs are dropped (hidden by the
  tent, as the subject says "behind").
- loose-join e5/e0: no dangling stubs; every touch shares an exact endpoint.
- hole (doorway band 4.69 wide): the band between the door apex and the tent
  apex now holds a 5.94 ink / 9.94 centerline inscribed circle, and the flag
  opening is 6x10 ink.
- stroke width: drawn at stroke 4 with every gap sized for it (8 on
  centerlines between distinct parts).
Not fixed:
- stroke-count: the SVG emits 7 paths (tent, pole, flag, head, two torso
  pieces, arm); they form 3 connected ink parts (tent+pole+flag+body, head).
  The torso is split at the arm branch and the pole at the flag, as the
  shared-node connections require, so the path count stays above 6.
- head hole: the r4 ring head leaves a ~4-wide opening (the metrics ask for
  6). An r5 head must sit 13 from the hand, the pole and the tent side; with
  the head top on y=8 and the hand on x=4 the 45-degree arm cannot reach 13,
  and the arm must branch 5 below the neck. The validator and build gate
  accept r4, the set's standard stick-figure head.
- the pole stub between flag and apex is 4 long, so the flag sits 4 above the
  tent on centerlines; they are joined by the pole (connect), not separate.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5655244e-9c88-42c3-a2be-d90a6fab78b2"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1732-camper-behind-flagged-tent/"
    "camper-behind-flagged-tent_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 26                  # tent axis
APEX = (AXIS, 22)
BASE_Y = 40
HALF = BASE_Y - APEX[1]    # 45-degree sides: half base = height = 18
DOOR_APEX = (AXIS, 34)
DOOR_HALF = BASE_Y - DOOR_APEX[1]
FLAG = dict(top=8, bottom=18, right=38)
HEAD = (12, 12)
HEAD_R = 4
NECK = (12, 24)            # head bottom + 8
SHOULDER = (12, 29)        # arm branch, 5 below the neck
HIP = (12, 36)             # on the tent's left side x + y = 48
HAND = (4, 21)


class CamperBehindFlaggedTentRedraw(Solo48):
    icon_id = "camper-behind-flagged-tent-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "travel/camping"
    aliases = ("camper at tent", "campsite", "camping trip")
    keywords = ("camping", "camper", "tent", "flag", "campsite", "outdoors", "hiking", "person")

    def ring(self, name: str, centre: tuple[int, int], r: int) -> None:
        cx, cy = centre
        pts = [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)]
        for i in range(4):
            self.add_arc(f"{name}-{i + 1}", pts[i], pts[(i + 1) % 4], radius_x=r, sweep=True)
        self.add_contour(name, *(f"{name}-{i + 1}" for i in range(4)), closed=True)

    def build(self) -> None:
        left_foot = (AXIS - HALF, BASE_Y)
        right_foot = (AXIS + HALF, BASE_Y)
        door_left = (AXIS - DOOR_HALF, BASE_Y)
        door_right = (AXIS + DOOR_HALF, BASE_Y)
        self.add_line("tent-left-low", left_foot, HIP)
        self.add_line("tent-left-high", HIP, APEX)
        self.add_line("tent-right", APEX, right_foot)
        self.add_line("base-right", right_foot, door_right)
        self.add_line("door-right", door_right, DOOR_APEX)
        self.add_line("door-left", DOOR_APEX, door_left)
        self.add_line("base-left", door_left, left_foot)
        self.add_contour(
            "tent", "tent-left-low", "tent-left-high", "tent-right", "base-right",
            "door-right", "door-left", "base-left", closed=True,
        )

        T, B, R = FLAG["top"], FLAG["bottom"], FLAG["right"]
        self.add_line("pole", APEX, (AXIS, B))
        self.add_line("flag-hoist", (AXIS, B), (AXIS, T))
        self.add_line("flag-top", (AXIS, T), (R, T))
        self.add_line("flag-fly", (R, T), (R, B))
        self.add_line("flag-bottom", (R, B), (AXIS, B))
        self.add_contour("flag", "flag-hoist", "flag-top", "flag-fly", "flag-bottom", closed=True)
        self.relate("connect", "pole", "tent")
        self.relate("connect", "pole", "flag")

        self.ring("head", HEAD, HEAD_R)
        self.add_line("torso", NECK, SHOULDER)
        self.mark_human_figure("camper", head="head", torso="torso", torso_junction="start")
        self.add_line("torso-low", SHOULDER, HIP)
        self.add_line("arm", SHOULDER, HAND)
        self.relate("connect", "torso", "torso-low")
        self.relate("connect", "torso", "arm")
        self.relate("connect", "torso-low", "arm")
        self.relate("connect", "torso-low", "tent")
