"""crawling-baby (redraw of the new-pipeline traced SVG).

Plan: right-facing crawling stick baby on HRECT_L (centerline box (4,8)-(44,40)).
- head: 4-cardinal-arc circle, r7 about (37,15); its top touches y=8 and its
  right side x=44 (the top and right extremes).
- body: one stroke, like the reference: rear foot (4,40) -> knee (21,40) on the
  floor -> hip (17,30) -> flat back to the shoulder (37,30) -> supporting arm
  down to the hand (41,40). Foot is the left extreme, floor/hand the bottom.
- neck: the shoulder sits straight under the head centre, 15 below it, so the
  head's bottom cardinal point (37,22) is exactly 8 centerline units (4 ink)
  above the torso's neck end. The arm and thigh leave away from the head.
Reference: icon_set/references/human_ref/full_body_ref.png (circular detached
head, single round-ended limb strokes). No Lucide crawling figure exists; only
the Lucide stick-figure convention (round caps and joins, one stroke per limb
chain) was used.

Keyshape: metrics suggested HRECT_M (score 1.21, HRECT_L 1.16). A first draft
on HRECT_M reached the exact 8 gap only on a diagonal (9-12-15 from the head
centre). Validation sampled that arc at 8.0002 and returned `review`. The
certifiable build puts the shoulder under the head's bottom cardinal point.
That needs back-to-floor room of at least 8 (10 here) below a head 14 tall, so
the model uses HRECT_L, which the metrics rank as a near-equal fit.

Metric issues:
- clearance e0/e1 4.57 (need 8): fixed, head to body is 8 on centerlines.
- head-gap 4.57 (need exactly 8): fixed, exactly 8 between the head bottom
  (37,22) and the neck end of the torso (37,30).
- keyshape-short-axis (x filled 96%): fixed, foot x=4 and head x=44, head top
  y=8 and floor/hand y=40 land exactly on the HRECT_L box.
- stroke-width 2.56 (info): redrawn at stroke 4 with every gap budgeted for it
  (floor 10 below the back, thigh 20 from the arm).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1d74887d-18df-5bd5-97d7-55b28bd0ed99"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1104-crawling-baby/crawling-baby_raw.svg"
AUTHOR = "claude-opus-5-5"

HEAD_C = (37, 15)
HEAD_R = 7
SHOULDER = (37, 30)   # straight under the head: HEAD_C.y + HEAD_R + 8
HIP = (17, 30)
KNEE = (21, 40)
FOOT = (4, 40)
HAND = (41, 40)


class CrawlingBabyRedraw(Solo48):
    icon_id = "crawling-baby-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people"
    aliases = ("crawling infant", "baby crawling")
    keywords = ("baby", "infant", "crawl", "crawling", "toddler", "child", "kid")

    def build(self) -> None:
        (cx, cy), r = HEAD_C, HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        self.add_line("rear-shin", FOOT, KNEE)
        self.add_line("thigh", KNEE, HIP)
        self.add_line("torso", HIP, SHOULDER)
        self.add_line("arm", SHOULDER, HAND)
        self.add_contour("body", "rear-shin", "thigh", "torso", "arm")
        self.mark_human_figure("baby", head="head", torso="torso", torso_junction="end")
