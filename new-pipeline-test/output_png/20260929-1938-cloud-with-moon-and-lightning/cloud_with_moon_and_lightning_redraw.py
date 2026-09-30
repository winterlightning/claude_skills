"""cloud-with-moon-and-lightning (redraw of the new-pipeline traced SVG).

Plan: a night thunderstorm -- crescent moon, cloud and one lightning bolt.
Keyshape SQUARE (as suggested, score 1.24): every extreme sits on the
(6,6)-(42,42) centerline box -- cloud left lobe x=6, moon top horn y=6,
moon right horn x=42, bolt tip y=42.
- moon (closed crescent, in front): outer circle r10 about (32,16) split at
  the two cloud nodes; bite arc r8 from the right horn (42,16) to the top
  horn (32,6). Crescent is 12.8 thick on the diagonal (hole 8.8 inscribed).
- cloud (open contour, behind the moon): left lobe r5 about (11,19), top
  lobe r8 from the left cusp (11,14) to the moon back at (24,10), flat base
  y=24 from (11,24) to the moon back at (26,24). Both ends are 6-8-10 grid
  points on the moon circle, so the joins are transversal (~85 and ~37 deg),
  not tangent; declared connect.
- bolt: open Z (21,33)-(18,37)-(29,37)-(25,42), 9 below the cloud base.
Lucide references: cloud-moon (moon and cloud overlap as one group instead of
floating apart) and cloud-lightning (Z bolt: two diagonals and a flat bar).

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4; every gap budgeted for it.
- keyshape-short-axis (x fill 99%): all four extremes on the SQUARE box.
- clearance e0/e1 (moon 3.4 from cloud): the moon now overlaps the cloud and
  the cloud outline ends on the moon's back at shared nodes (declared
  connect). Kept separate at 8 they cannot fit the 36-unit box: a crescent
  needs r>=8 to keep a 6-wide hole, and the cloud's right side then collides.
- clearance e1/e2 (bolt 2.5 below the cloud): bolt top is 9 below the base
  (9, not 8: an endpoint exactly 8 from a line in an arc contour is `review`).
- hole at (32.2,13.4), 1.2 wide: the moon/cloud sliver is gone; the only
  holes are the cloud interior (~12) and the crescent (8.8).
Not kept: the separate floating moon and the trace's closed cloud with its
right lobe. The moon now covers that lobe. The bolt is 9 tall rather than
the trace's ~10 because the gap under the cloud costs 9.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7eb10cf4-5263-45f8-929d-49906b04ace0"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1938-cloud-with-moon-and-lightning/cloud-with-moon-and-lightning_raw.svg"
AUTHOR = "claude-opus-5-5"

# Moon (in front): outer circle r10 about (32,16), so the cloud can meet its
# back at 6-8-10 grid points instead of tangent cardinal points.
MOON_R, BITE_R = 10, 8
HORN_TOP = (32, 6)     # top extreme of the icon
HORN_RIGHT = (42, 16)  # right extreme of the icon
BACK_P = (24, 10)      # cloud top lobe meets the moon here, ~85 deg
BACK_Q = (26, 24)      # cloud base meets the moon here

# Cloud (behind the moon): left lobe r5, top lobe r8, flat base.
LEFT_C, LEFT_R = (11, 19), 5
TOP_R = 8
BASE_Y = 24

# Bolt: open Z, 9 below the cloud base, centred under the cloud+moon group.
# Parallel-ish diagonals sit 8.8 / 8.6 apart across the bar.
BOLT = ((21, 33), (18, 37), (29, 37), (25, 42))


class CloudWithMoonAndLightningRedraw(Solo48):
    icon_id = "cloud-with-moon-and-lightning-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    aliases = ("night thunderstorm", "stormy night", "cloud moon lightning")
    keywords = ("cloud", "moon", "crescent", "lightning", "bolt", "thunder", "storm", "night", "weather")

    def build(self) -> None:
        r = MOON_R
        self.add_arc("moon-top", HORN_TOP, BACK_P, radius_x=r, sweep=False)
        self.add_arc("moon-back", BACK_P, BACK_Q, radius_x=r, sweep=False)
        self.add_arc("moon-low", BACK_Q, HORN_RIGHT, radius_x=r, sweep=False)
        self.add_arc("moon-bite", HORN_RIGHT, HORN_TOP, radius_x=BITE_R, sweep=True)
        self.add_contour("moon", "moon-top", "moon-back", "moon-low", "moon-bite", closed=True)

        lx, ly = LEFT_C
        left_top, left_bottom = (lx, ly - LEFT_R), (lx, ly + LEFT_R)
        self.add_arc("cloud-top", BACK_P, left_top, radius_x=TOP_R, sweep=False)
        self.add_arc("cloud-left", left_top, left_bottom, radius_x=LEFT_R, sweep=False)
        self.add_line("cloud-base", left_bottom, BACK_Q)
        self.add_contour("cloud", "cloud-top", "cloud-left", "cloud-base")
        self.relate("connect", "cloud", "moon")

        self.add_polyline("bolt", *BOLT)
