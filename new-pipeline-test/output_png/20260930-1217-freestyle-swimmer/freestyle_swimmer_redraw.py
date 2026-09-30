"""freestyle-swimmer (redraw of the new-pipeline traced SVG).

Subject: a stick figure doing front crawl toward the right, head at the
right, one recovery arm arcing high over the water, and one wavy water line.

Plan on HRECT_M (centerline box (4,10)-(44,38)):
- torso: one level line on y=TY from the hip (left extreme x=4) to the neck,
  split at the shoulder so the arm shares a node with it.
- head: 4-cardinal-arc circle r5 on the torso axis (6-wide hole), its
  outline exactly 8 beyond the neck (level neck run, certified 4-unit ink
  gap); rightmost point on the right extreme x=44.
- arm: one polyline shoulder -> high elbow on the top extreme y=10 -> hand
  reaching forward level over the head (9 clear of the head top).
- water: one smooth line, three half-waves (period 10, horizontal tangents
  at every crest/trough) whose last trough runs level under the head to
  x=44; the level run keeps the head 9 clear, where a crest there would
  come within 6.6 of it. Troughs sit on the bottom extreme y=38.
Reference: icon_set/references/human_ref/full_body_ref.png (circular head,
round-ended single-stroke limbs); Lucide `waves` for the water line.

Metric issues repaired:
- stroke-width (info): redrawn at stroke 4 and every gap budgeted at 8.
- keyshape-short-axis: parts now reach y=10 (elbow/forearm) and y=38 (wave
  troughs) as well as x=4 and x=44, so HRECT_M fits exactly.
- clearance e0/e2 (torso-head): gap is the certified 8 on the neck axis.
- clearance e0/e3, e1/e3, e2/e3 (torso/arm/head vs water): the wave crests
  sit 10 below the torso and the level trough 9 below the head ink.
- clearance e1/e2 (arm-head): the forearm runs 9 above the head top and the
  hand is 14 from its centre.
- hole (2.4 wide): the kinked shoulder loop is gone; the arm leaves the
  torso as one straight upper arm, so no enclosed pocket remains.
- hole (head): the r5 head ring leaves an exactly 6-wide hole.
- no-head: the head is a real circle marked with mark_human_figure.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "79d7b1e9-d763-4618-aea0-fb1d2e59180b"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1217-freestyle-swimmer/"
    "freestyle-swimmer_raw.svg"
)
AUTHOR = "claude-opus-5-5"

TY = 24                              # torso axis
HEAD_R = 5
HIP = (4, TY)
SHOULDER = (20, TY)
NECK = (26, TY)
HEAD_C = (NECK[0] + 8 + HEAD_R, TY)  # (39, 24): outline 8 beyond the neck
ELBOW = (26, 10)
HAND = (42, 10)
# Wave extremes (x, y) with horizontal tangents: crest, trough, crest, trough,
# then the trough runs level under the head to the right extreme.
WAVE = [(4, 34), (14, 38), (24, 34), (34, 38)]
WAVE_END = (44, 38)


class FreestyleSwimmerRedraw(Solo48):
    icon_id = "freestyle-swimmer-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ("freestyle swimmer", "front crawl", "swimmer")
    keywords = ("swimming", "swimmer", "freestyle", "crawl", "sport", "pool", "water")

    def build(self) -> None:
        cx, cy, r = HEAD_C[0], HEAD_C[1], HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        self.add_line("waist", HIP, SHOULDER)
        self.add_line("torso", SHOULDER, NECK)
        self.relate("connect", "waist", "torso")
        self.mark_human_figure("swimmer", head="head", torso="torso", torso_junction="end")

        self.add_polyline("arm", SHOULDER, ELBOW, HAND)
        self.relate("connect", "arm", "torso")
        self.relate("connect", "arm", "waist")

        segs = []
        for (x0, y0), (x1, y1) in zip(WAVE, WAVE[1:]):
            h = (x1 - x0) / 2
            segs.append(((x0 + h, y0), (x1 - h, y1), (x1, y1)))
        x0, y0 = WAVE[-1]
        segs.append(((x0 + 3, y0), (WAVE_END[0] - 3, y0), WAVE_END))
        self.add_bezier("water", WAVE[0], *segs)
