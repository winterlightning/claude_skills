"""conductor-with-raised-baton (redraw of the new-pipeline traced SVG).

Plan: stick-figure conductor on VRECT_L (centerline box (8,4)-(40,44)).
- head: two half-arc circle, r5, centre (HX,9); its top is on the y=4 extreme.
- torso: vertical line on x=HX from the neck (HX,22) to the hip; the neck is
  exactly 8 centerline units under the head outline (4-unit ink gap).
- left arm: horizontal from the neck to the x=8 extreme.
- right arm: shoulder run along the arm line, 45-degree upper arm to the elbow,
  short horizontal forearm to the hand (the wrist flick of the trace).
- baton: long straight 2:3 stroke from the hand to the (40,4) corner, the
  x=40 and y=4 extreme; it shares the hand endpoint (the conductor holds it)
  and rises steeper than the 45-degree upper arm.
- legs: one inverted V from the hip to the y=44 extreme, mirrored about HX.
Reference: icon_set/references/human_ref/full_body_ref.png (circular head,
round-ended single-stroke limbs). No useful Lucide match (Lucide has no
conductor); the straight-limb stick construction follows the human reference.

Metric issues fixed:
- head-gap / clearance e1-e2, e1-e4: head outline now exactly 8 from the neck
  on the torso axis (trace had 3.93).
- hole: head radius 4 -> 5 on centerline so the inner hole is 6 inscribed
  (trace had 2.67).
- clearance e3-e4: legs rebuilt as one mirrored inverted V sharing the hip.
- loose-join e0-e2: baton starts exactly at the hand and is related 'connect'.
- keyshape-short-axis: every VRECT_L extreme is reached exactly (head top y=4,
  feet y=44, left hand x=8, baton tip (40,4)).
- stroke-width (info): drawn at stroke 4, all gaps budgeted for it.
Deviation from the brief: the baton touches the hand instead of floating a
stroke width away; a floating baton needs an 8-unit centerline gap that
leaves no room for a readable baton inside x<=40, and at 48 px it reads as
a detached stick. The metrics' loose-join issue also asks for the join.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6659250b-ef9d-4624-8030-348af08008eb"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1053-conductor-with-raised-baton/"
    "conductor-with-raised-baton_raw.svg"
)
AUTHOR = "claude-opus-5-5"

HX = 16            # torso / head axis
HEAD_R = 5
HEAD_CY = 9        # centerline top at y=4
NECK_Y = HEAD_CY + HEAD_R + 8   # 22: exact detached-head gap
HIP = (HX, 32)
LEG_DX, FOOT_Y = 6, 44
LEFT_HAND = (8, NECK_Y)
SHOULDER = (22, NECK_Y)
ELBOW = (28, 16)
HAND = (32, 16)
BATON_TIP = (40, 4)


class ConductorWithRaisedBatonRedraw(Solo48):
    icon_id = "conductor-with-raised-baton-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/music"
    aliases = ("orchestra conductor", "maestro")
    keywords = ("conductor", "baton", "music", "orchestra", "maestro", "person")

    def build(self) -> None:
        cx, cy, r = HX, HEAD_CY, HEAD_R
        self.add_arc("head-top", (cx - r, cy), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-bottom", (cx + r, cy), (cx - r, cy), radius_x=r, sweep=True)
        self.add_contour("head", "head-top", "head-bottom", closed=True)

        neck = (HX, NECK_Y)
        self.add_line("torso", neck, HIP)
        self.mark_human_figure("conductor", head="head", torso="torso", torso_junction="start")

        self.add_line("left-arm", LEFT_HAND, neck)
        # Standalone straight members so each is certified against the head.
        self.add_line("shoulder", neck, SHOULDER)
        self.add_line("upper-arm", SHOULDER, ELBOW)
        self.add_line("forearm", ELBOW, HAND)
        self.add_line("baton", HAND, BATON_TIP)
        for a, b in (("left-arm", "torso"), ("shoulder", "torso"),
                     ("left-arm", "shoulder"), ("shoulder", "upper-arm"),
                     ("upper-arm", "forearm"), ("forearm", "baton")):
            self.relate("connect", a, b)

        self.add_polyline(
            "legs", (HX - LEG_DX, FOOT_Y), HIP, (HX + LEG_DX, FOOT_Y)
        )
        self.relate("connect", "legs", "torso")
