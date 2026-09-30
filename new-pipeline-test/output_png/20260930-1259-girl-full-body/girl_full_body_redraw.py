"""girl-full-body (redraw of the new-pipeline traced SVG).

Plan: a frontal girl in an A-line dress on VRECT_M (centerline box
(10,4)-(38,44)), mirrored about the axis x=24.
- head: 4-cardinal-arc ring, r5, centre (24,9); its top is the y=4 extreme.
  A slightly large head keeps the figure young (a girl, not a woman).
- dress: closed trapezoid. A level shoulder line (20,22)-(28,22) sits exactly
  8 centerline units under the head outline (14 + 8 = 22, a 4-unit ink gap,
  human-reference.md), centred on the axis. The skirt flares to a hem on
  y=34 whose corners (10,34) and (38,34) are the x extremes. The shoulder
  line is split at the neck (24,22) so the head/torso flag names the
  primitive at the actual neck junction; its halves stay one closed contour.
- legs: two verticals from the hem at x=20 and x=28 (8 apart, a 4-unit ink
  gap) down to the feet on y=44, the bottom extreme. The hem is split at the
  leg tops so each leg shares an endpoint with it.
References: icon_set/references/human_ref/full_body_ref.png (the dress
figure: ring head detached above a flared dress, two parallel straight
legs, round ends); the generated image supplied the frontal, symmetric
stance. Lucide has no dress figure (`person-standing` is the unisex stick
figure), so no Lucide construction was used.

Metric issues:
- clearance e0/e1, e0/e2 and head-gap e0 (head 2.4-2.5 from the body):
  the shoulder line is exactly 8 under the head outline, centred on the axis.
- clearance e1/e2 (0.1 apart: the trace split the body into two touching
  parts): one closed dress contour plus two legs, every touch a shared,
  declared endpoint.
- hole at (24.0,7.4), 2.91 wide: the head ring is r5 at stroke 4, a 6-unit
  inscribed opening.
- keyshape-short-axis (x filled 47%): the hem corners reach x=10 and x=38,
  so all four extremes sit on the VRECT_M box without stretching anything.
- stroke-width (trace 2.65): redrawn at stroke 4 with 8-unit centerline gaps.
- choice warning (stick figure reads as a generic person): the stick torso,
  arms and legs became the reference's dress figure so it reads as a girl;
  the dress replaces the separate arms.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "45881775-2179-41cc-98a1-78a598c550c1"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1259-girl-full-body/girl-full-body_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
HEAD_R = 5
HEAD_CY = 9                 # head top on y=4 (VRECT_M top)
NECK_Y = HEAD_CY + HEAD_R + 8   # 22: exact detached-head gap
SHOULDER = 4                # half-width of the level shoulder line
HEM_Y = 34
HEM = 14                    # half-width of the hem: corners on x=10 / x=38
LEG = 4                     # half-spacing of the legs (8 apart)
FOOT_Y = 44                 # VRECT_M bottom


class GirlFullBodyRedraw(Solo48):
    icon_id = "girl-full-body-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/person"
    aliases = ("girl", "girl standing", "female child")
    keywords = ("girl", "child", "kid", "dress", "female", "person", "full body")

    def build(self) -> None:
        cx, cy, r = AXIS, HEAD_CY, HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        neck = (AXIS, NECK_Y)
        shoulder_r = (AXIS + SHOULDER, NECK_Y)
        shoulder_l = (AXIS - SHOULDER, NECK_Y)
        hem_r = (AXIS + HEM, HEM_Y)
        hem_l = (AXIS - HEM, HEM_Y)
        hip_r = (AXIS + LEG, HEM_Y)
        hip_l = (AXIS - LEG, HEM_Y)

        # Dress: closed A-line trapezoid, clockwise from the neck.
        self.add_line("dress-shoulder-r", neck, shoulder_r)
        self.add_line("dress-side-r", shoulder_r, hem_r)
        self.add_line("dress-hem-r", hem_r, hip_r)
        self.add_line("dress-hem-c", hip_r, hip_l)
        self.add_line("dress-hem-l", hip_l, hem_l)
        self.add_line("dress-side-l", hem_l, shoulder_l)
        self.add_line("dress-shoulder-l", shoulder_l, neck)
        self.add_contour(
            "dress", "dress-shoulder-r", "dress-side-r", "dress-hem-r", "dress-hem-c",
            "dress-hem-l", "dress-side-l", "dress-shoulder-l", closed=True,
        )
        self.mark_human_figure(
            "girl", head="head", torso="dress-shoulder-r", torso_junction="start",
        )

        # Legs hang from the hem, sharing its split points.
        self.add_line("leg-l", hip_l, (AXIS - LEG, FOOT_Y))
        self.add_line("leg-r", hip_r, (AXIS + LEG, FOOT_Y))
        self.relate("connect", "leg-l", "dress")
        self.relate("connect", "leg-r", "dress")
