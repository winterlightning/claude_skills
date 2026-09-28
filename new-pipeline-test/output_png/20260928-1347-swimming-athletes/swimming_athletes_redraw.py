"""swimming-athletes (redraw of the new-pipeline traced SVG).

Plan: right-facing front-crawl stick swimmer on HRECT_M (centerline box (4,10)-(44,38)).
- head: 4-cardinal-arc circle r4 level beside the neck; the torso ends in a
  horizontal run so the 8-unit centerline gap (4 ink) certifies.
- torso: horizontal line hip -> shoulder -> neck on y=TY; split at the shoulder
  so the reaching arm shares a node before the neck, never near the head.
- arm: upper arm rising to the elbow on the top extreme, then a standalone
  straight forearm reaching forward over the head to the right extreme.
- legs: two straight legs trailing from the hip in a kicking V to the left extreme.
- water: one smooth wave, horizontal tangents on every crest/trough so the
  bottom extreme is exact; a trough sits under the head.
Reference: icon_set/references/human_ref/full_body_ref.png (circular head,
round-ended single-stroke limbs); Lucide `waves` for the water line.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1347-swimming-athletes/"
    "swimming-athletes_raw.svg"
)
AUTHOR = "claude-opus-5-5"

TY = 23                  # torso axis
HEAD_R = 4
HIP = (12, TY)
SHOULDER = (19, TY)
NECK = (24, TY)
HEAD_C = (NECK[0] + 8 + HEAD_R, TY)   # outline 8 beyond the neck
ELBOW = (27, 10)
HAND = (44, 10)
UPPER_FOOT = (4, 19)
LOWER_FOOT = (4, 27)
# Wave extremes (x, y) with horizontal tangents: three calm half-waves.
WAVE = [(4, 38), (17, 34), (31, 38), (44, 34)]


class SwimmingAthletesRedraw(Solo48):
    icon_id = "swimming-athletes-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ("swimmer", "swimming", "front crawl")
    keywords = ("swimming", "swimmer", "athlete", "sport", "pool", "water", "crawl")

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

        self.add_line("upper-arm", SHOULDER, ELBOW)
        self.add_line("forearm", ELBOW, HAND)
        self.relate("connect", "upper-arm", "forearm")
        self.relate("connect", "upper-arm", "torso")
        self.relate("connect", "upper-arm", "waist")

        self.add_line("upper-leg", HIP, UPPER_FOOT)
        self.add_line("lower-leg", HIP, LOWER_FOOT)
        self.relate("connect", "upper-leg", "waist")
        self.relate("connect", "lower-leg", "waist")
        self.relate("connect", "upper-leg", "lower-leg")

        segs = []
        for (x0, y0), (x1, y1) in zip(WAVE, WAVE[1:]):
            h = (x1 - x0) / 2
            segs.append(((x0 + h, y0), (x1 - h, y1), (x1, y1)))
        self.add_bezier("water", WAVE[0], *segs)
