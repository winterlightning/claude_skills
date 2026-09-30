"""camper-behind-flagged-tent (redraw of the new-pipeline traced SVG).

Plan: SQUARE (centerline box (6,6)-(42,42)), the suggested keyshape (source
aspect 1.0, fit score 1.25).
- tent: one closed outline. Base feet (6,42)/(42,42), peak (24,18); both walls
  are 3-4-5 slopes, so every wall node is a lattice point. The doorway is an
  inverted V (17,42)-(24,32)-(31,42) with no floor line under it (Tabler tent
  construction), so the door is an opening, not a sliver hole. Door legs run
  within 2 degrees of the walls, 8.8 apart at the feet and 8.4 at the apex.
- flag: the pole rises from the peak to y=6 (the top extreme); the pennant
  (24,6)-(36,12)-(24,18) is Lucide flag-triangle-right at 12x12, its lower
  edge closing back on the peak.
- camper: a bust peeking over the upper left of the tent. Head r4 circle at
  (10,10) (top and left extremes). The shoulders start 8.4 clear of the wall
  at (6,28), rise to an r3 corner, run flat under the head at y=22 (exactly 8
  below the head outline, on the head axis x=10; a straight top because an
  arc at exactly 8 comes back `review`), then fall as a quarter-ellipse cubic
  onto the wall node (18,26), so the tent hides the rest of the body.
Reference: human_ref user.svg bust (circular head, rounded shoulders, open
bottom); Tabler tent (open-floor door); Lucide flag-triangle-right.

Metric issues:
- clearance e0/e1 (door vs tent wall 7.29): fixed, legs >= 8.4 from the walls.
- clearance e0/e2 (head vs tent 4.17): fixed, head outline 12 from the wall
  and 12.1 from the peak.
- clearance e0/e3 (shoulder vs tent 1.97): fixed by making it a declared
  contact instead of a gap: the shoulder ends on a split node of the wall
  (occlusion). A detached shoulder 8 clear of the wall only fits a tent 30 wide
  or less, and then the door apex can't keep 8 from both walls.
- clearance e2/e3 + head-gap (2.26): fixed, head outline to shoulder top is
  exactly 8 on centerlines (4 ink), measured to the flat shoulder top under
  the head centre x=10 (mark_human_figure flags the pair).
- hole at the door (4.2): fixed, the door is open at the floor.
- hole in the pennant (2.24): pennant is now 12x12, centerline inradius 3.7
  (passes the build hole gate); its ink hole is still under the 6 wide the
  metrics ask for. A 6-wide ink hole needs inradius 5, a 16x16 pennant, which
  does not fit above a tent tall enough for its door.
- hole in the head: NOT fully fixed. r4 head, ink hole 4 wide (the build hole
  gate passes). An r5 head was tried: it validates, but pushes the shoulders
  flat against the wall and the bust reads as a hook, so r4 was kept.
- tent interior hole (5.22): now a large open body.
- stroke-width info: redrawn at stroke 4 throughout.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5655244e-9c88-42c3-a2be-d90a6fab78b2"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1941-camper-behind-flagged-tent/"
    "camper-behind-flagged-tent_raw.svg"
)
AUTHOR = "claude-opus-5-5"

BASE_Y = 42
FOOT_L, FOOT_R = (6, BASE_Y), (42, BASE_Y)
PEAK = (24, 18)
DOOR_L, DOOR_TOP, DOOR_R = (17, BASE_Y), (24, 32), (31, BASE_Y)
POLE_TOP = (24, 6)
PENNANT_TIP = (36, 12)
HEAD_C, HEAD_R = (10, 10), 4        # top y=6, left x=6
SH_NECK = (HEAD_C[0], 22)           # head bottom 14 + 8
SH_CORNER = 3
SH_START = (6, 28)                  # lowest point 8.4 clear of the left wall
SH_SIDE_TOP = (6, 25)               # r3 corner about (9,25)
SH_TOP_L = (9, 22)
SH_TOP_R = (11, 22)
SH_END = (18, 26)                   # lattice node of the left wall


class CamperBehindFlaggedTentRedraw(Solo48):
    icon_id = "camper-behind-flagged-tent-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "outdoors"
    aliases = ("campsite", "camping tent with flag")
    keywords = ("camping", "camper", "tent", "flag", "pennant", "campsite", "outdoors")

    def build(self) -> None:
        # Tent outline, split at the shoulder contact.
        self.add_line("base-left", DOOR_L, FOOT_L)
        self.add_line("wall-left-low", FOOT_L, SH_END)
        self.add_line("wall-left-high", SH_END, PEAK)
        self.add_line("wall-right", PEAK, FOOT_R)
        self.add_line("base-right", FOOT_R, DOOR_R)
        self.add_line("door-right", DOOR_R, DOOR_TOP)
        self.add_line("door-left", DOOR_TOP, DOOR_L)
        self.add_contour(
            "tent", "base-left", "wall-left-low", "wall-left-high", "wall-right",
            "base-right", "door-right", "door-left", closed=True,
        )

        # Flag: pole from the peak, pennant closing back on the peak.
        self.add_line("pole", PEAK, POLE_TOP)
        self.add_line("pennant-top", POLE_TOP, PENNANT_TIP)
        self.add_line("pennant-bottom", PENNANT_TIP, PEAK)
        self.add_contour("flag", "pole", "pennant-top", "pennant-bottom", closed=True)
        self.relate("connect", "flag", "tent")

        # Camper: detached head over a shoulder arc that ends on the wall.
        cx, cy, r = *HEAD_C, HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        # Rounded left shoulder, a flat top under the head (straight, so the
        # exact 8 head gap certifies), and a quarter-ellipse cubic down to the
        # wall node.
        self.add_line("shoulder-side", SH_START, SH_SIDE_TOP)
        self.add_arc("shoulder-left", SH_SIDE_TOP, SH_TOP_L, radius_x=SH_CORNER, sweep=True)
        self.add_line("shoulder-top-l", SH_TOP_L, SH_NECK)
        self.add_line("shoulder-top-r", SH_NECK, SH_TOP_R)
        k = 0.5523  # quarter-circle cubic handle ratio
        dx, dy = SH_END[0] - SH_TOP_R[0], SH_END[1] - SH_TOP_R[1]
        self.add_bezier(
            "shoulder-right", SH_TOP_R,
            ((SH_TOP_R[0] + k * dx, SH_TOP_R[1]), (SH_END[0], SH_END[1] - k * dy), SH_END),
        )
        self.add_contour(
            "shoulders", "shoulder-side", "shoulder-left", "shoulder-top-l", "shoulder-top-r",
            "shoulder-right",
        )
        self.relate("connect", "shoulders", "tent")
        self.mark_human_figure(
            "camper", head="head", torso="shoulder-top-r", torso_junction="start",
        )


if __name__ == "__main__":
    import sys
    from pathlib import Path

    here = Path(__file__).resolve().parent
    icon = CamperBehindFlaggedTentRedraw()
    print(icon.validate_icon().describe())
    if "--export" in sys.argv:
        icon.export_icon_to(here / "camper-behind-flagged-tent_redraw.svg")
