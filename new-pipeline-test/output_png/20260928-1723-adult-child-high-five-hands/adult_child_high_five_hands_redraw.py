"""adult-child-high-five-hands (redraw of the new-pipeline traced SVG).

Plan: two stick figures on VRECT_L (centerline box (8,4)-(40,44)), a tall
adult at left and a shorter child at right, whose raised inner arms meet at
one shared hand point (the high five).
- shared vocabulary: both heads are r4 four-arc circles; each torso starts
  with a 2-long neck stub exactly 8 centerline units under its head outline
  (4-unit ink gap, human-reference.md), arms branch at the shoulder, legs
  split from the hip into a symmetric inverted V with feet on y=44.
- adult: axis x=12, head top y=4 (the y=4 extreme) and head side x=8 (the
  x=8 extreme); shoulder y=22, hip y=32, feet (8,44)/(16,44).
- child: axis x=36, head centre y=16 (8 lower than the adult), head side
  x=40 (the x=40 extreme); shoulder y=30, hip y=38, feet (33,44)/(39,44).
- high five: the adult arm rises straight from its shoulder to HAND (24,15)
  (12.1 from its head centre); the child arm leaves its shoulder level, turns
  up through an r12 quarter arc about (36,18) and runs straight up into the
  same HAND, tangent-continuous like the trace's curved arm. Every arm point
  stays 12+ from each head centre (8+ from the outline); a straight child arm
  would pass 8.4 from its own head centre, so it cannot reach up directly.
  Arc and hand line are standalone primitives joined by connect, so the
  child's exact-8 head gap still certifies.
Reference: icon_set/references/human_ref/full_body_ref.png (circular heads,
single round-ended limbs); no useful Lucide match for two figures.

Keyshape: metrics suggested HRECT_L (score 0.94) from the agent's "wide" hint,
but the trace is taller than wide (aspect 0.86) and VRECT_L scored 0.93. A
32-unit height on HRECT_L leaves the adult 8-unit legs; VRECT_L's 40 units
give the adult/child height difference room. All four VRECT_L extremes are
reached exactly: y=4 adult head, y=44 feet, x=8 adult head, x=40 child head.

Metric issues fixed:
- stroke-width: redrawn at stroke 4 with every gap budgeted at 8 centerline.
- stroke-count (9 vs 6): rebuilt as 2 heads, 2 bodies, 2 raised arms (plus
  legs); the two hanging outer arms were dropped (see below).
- keyshape-short-axis: the x axis now fills the box (x=8 and x=40 heads).
- clearance e0/e3, e0/e4, e0/e5, e0/e7, e1/e4, e3/e8, e6/e8, e5/e7 and the
  human head gap (child head 2.1 from its body): both heads sit exactly 8
  over their neck stubs, and both raised arms keep 8+ from each head outline.
- clearance e1/e5, e2/e6 and narrow-join e1/e5, e2/e6 (fused leg wedges):
  legs are split from the hip as one polyline per figure (10 wide at the
  adult feet, 6 at the child's) instead of a leg drawn over the torso line.
- clearance e2/e3: the child arm leaves the shoulder sideways, clear of the
  child's own body and legs.
- loose-join e7/e3 (1.3 gap between the hands): the hands share one exact
  endpoint with relate("connect").
- holes (2.28 and 1.13 inscribed): the head rings are r4 circles (small-
  circle exemption); the arm/torso slivers are gone.

Not kept: the adult's hanging left arm and the child's hanging right arm.
With the figures pushed to the box edges there is no room for an outer arm
that stays 8 from its own leg (adult: arm end within 7.2 of the hip), and at
48 px the pose reads from the two raised arms.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b88757c2-b1ab-49df-9283-b755a2874066"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1723-adult-child-high-five-hands/"
    "adult-child-high-five-hands_raw.svg"
)
AUTHOR = "claude-opus-5-5"

HEAD_R = 4
HEAD_GAP = 8          # head outline to neck, on centerlines
NECK_STUB = 2
FOOT_Y = 44
HAND = (24, 15)       # the shared high-five point

# (axis x, head centre y, hip y, half foot spread)
ADULT = (12, 8, 32, 4)
CHILD = (36, 16, 38, 3)
ARM_R = 12            # child arm quarter-arc radius


class AdultChildHighFiveHandsRedraw(Solo48):
    icon_id = "adult-child-high-five-hands-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people"
    aliases = ("high five", "parent and child", "adult child high five")
    keywords = ("high five", "adult", "child", "parent", "kid", "family", "celebrate", "people")

    def _figure(self, name: str, spec: tuple[int, int, int, int]) -> tuple[int, int]:
        x, cy, hip_y, spread = spec
        r = HEAD_R
        arcs = []
        for i, (a, b) in enumerate((
            ((x, cy - r), (x + r, cy)), ((x + r, cy), (x, cy + r)),
            ((x, cy + r), (x - r, cy)), ((x - r, cy), (x, cy - r)),
        )):
            self.add_arc(f"{name}-head-{i}", a, b, radius_x=r, sweep=True)
            arcs.append(f"{name}-head-{i}")
        self.add_contour(f"{name}-head", *arcs, closed=True)

        neck = (x, cy + r + HEAD_GAP)
        shoulder = (x, neck[1] + NECK_STUB)
        hip = (x, hip_y)
        self.add_line(f"{name}-torso", neck, shoulder)
        self.add_line(f"{name}-waist", shoulder, hip)
        self.relate("connect", f"{name}-torso", f"{name}-waist")
        self.mark_human_figure(name, head=f"{name}-head", torso=f"{name}-torso", torso_junction="start")

        self.add_polyline(f"{name}-legs", (x - spread, FOOT_Y), hip, (x + spread, FOOT_Y))
        self.relate("connect", f"{name}-legs", f"{name}-waist")
        return shoulder

    def build(self) -> None:
        adult_shoulder = self._figure("adult", ADULT)
        child_shoulder = self._figure("child", CHILD)

        self.add_line("adult-arm", adult_shoulder, HAND)
        # child arm: leaves the shoulder level, curves up (quarter arc about
        # (36,18)) and runs straight up into the shared hand, tangent throughout
        sx, sy = child_shoulder
        wrist = (sx - ARM_R, sy - ARM_R)
        self.add_arc("child-arm-curve", child_shoulder, wrist, radius_x=ARM_R, sweep=True)
        self.add_line("child-arm-hand", wrist, HAND)
        self.relate("connect", "child-arm-curve", "child-arm-hand")

        for arm, fig in (("adult-arm", "adult"), ("child-arm-curve", "child")):
            self.relate("connect", arm, f"{fig}-torso")
            self.relate("connect", arm, f"{fig}-waist")
        self.relate("connect", "adult-arm", "child-arm-hand")
