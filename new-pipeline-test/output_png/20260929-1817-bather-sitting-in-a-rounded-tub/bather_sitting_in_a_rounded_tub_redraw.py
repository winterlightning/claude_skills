"""bather-sitting-in-a-rounded-tub (redraw of the new-pipeline traced SVG).

Subject: a person bathing, shown as a detached circular head and a rounded
shoulder bust seated inside a wide bathtub with rounded bottom corners and a
flat rim.

Plan: HRECT_L (the suggested keyshape), centerline box (4,8)-(44,40).
- head: 4 cardinal arcs, r=5 about (24,13); top extreme y=8, ink hole 6.
- shoulders: user-bust arch on the x=24 axis, flat top y=26 (exactly 8 below
  the head bottom y=18), r=5 corners ending in free ends at (16,31)/(32,31).
- tub: one contour, rim lips (4,22)-(7,22) and (41,22)-(44,22) give the left
  and right extremes; walls x=7/41 drop to r=6 corners on the bottom y=40.
  The bust sits inside the tub: shoulder ends are 9 above the bottom and 9
  from the walls.

Changed from the trace on purpose: the trace stacks head, shoulders and a
full-width rim line above the tub. At stroke 4 that stack needs head 10 +
gap 8 + shoulders + gap 8 + a tub of at least 10 = over 38 units, and the
keyshape's short axis is 32. The rim line across the body is therefore
reduced to two outward rim lips and the bust is lowered into the tub, which
keeps head, shoulders and tub as three separate readable shapes.

Metric issues:
- clearance e0/e1 (head to shoulders 2.42): fixed, exactly 8 centerline /
  4 ink at the neck; the figure is marked with mark_human_figure.
- clearance e1/e3 (shoulders to rim 2.31): fixed, the rim line no longer
  crosses the bust; shoulder ends clear the tub by 9.
- hole 3.88 (head): fixed, head r=5 leaves a 6-unit inscribed hole.
- hole 3.2 (shoulder/rim pocket): fixed, the pocket no longer exists (the
  bust is open at the bottom and not closed by a rim).
- no-head: fixed, the head is a true circle.
- keyshape-short-axis (x fill 93%): fixed; rim lips reach x=4 and x=44,
  head top y=8, tub bottom y=40.
- narrow-join e3/e4, e3/e5 (25.6 deg wedges) and loose joins e2/e3, e3/e4,
  e3/e5: fixed; rim lips and walls are one contour with 90-degree round joins.
- stroke-width (info): redrawn at stroke 4; every gap measured at 4.
References: icon_set/skills/icon-design/human-reference.md and
icon_set/references/human_ref/user.svg (circular detached head over a
rounded shoulder bust, exact 4-unit ink gap). No local Lucide original was
inspected; no useful Lucide match for a bather in a tub.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "adb04192-9291-4a64-8bd6-a8f21d407e1b"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1817-bather-sitting-in-a-rounded-tub/"
    "bather-sitting-in-a-rounded-tub_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
HEAD_CY, HEAD_R = 13, 5          # head y 8..18
SHOULDER_TOP = 26                # head bottom 18 + 8
SHOULDER_R = 5
SHOULDER_HALF = 3                # flat top 21..27, ends at x 16 / 32
RIM_Y, LIP_X, WALL_X = 22, 4, 7
BOTTOM_Y, CORNER_R = 40, 6


class BatherSittingInARoundedTubRedraw(Solo48):
    icon_id = "bather-sitting-in-a-rounded-tub-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/leisure"
    aliases = ("bather", "person in bathtub", "bath time", "bathing")
    keywords = ("bath", "bathtub", "tub", "bathing", "person", "bathroom",
                "hygiene", "relax", "spa", "wash")

    def build(self) -> None:
        cx, cy, r = AXIS, HEAD_CY, HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        top, sr, h = SHOULDER_TOP, SHOULDER_R, SHOULDER_HALF
        left_top, right_top = (AXIS - h, top), (AXIS + h, top)
        self.add_arc("shoulder-left", (AXIS - h - sr, top + sr), left_top, radius_x=sr, sweep=True)
        self.add_line("shoulder-top", left_top, right_top)
        self.add_arc("shoulder-right", right_top, (AXIS + h + sr, top + sr), radius_x=sr, sweep=True)
        self.add_contour("shoulders", "shoulder-left", "shoulder-top", "shoulder-right")
        self.mark_human_figure("bather", head="head", torso="shoulder-top", torso_junction="start")

        left, right = WALL_X, 48 - WALL_X
        corner_y = BOTTOM_Y - CORNER_R
        self.add_line("lip-left", (LIP_X, RIM_Y), (left, RIM_Y))
        self.add_line("wall-left", (left, RIM_Y), (left, corner_y))
        self.add_arc("corner-left", (left, corner_y), (left + CORNER_R, BOTTOM_Y), radius_x=CORNER_R, sweep=False)
        self.add_line("bottom", (left + CORNER_R, BOTTOM_Y), (right - CORNER_R, BOTTOM_Y))
        self.add_arc("corner-right", (right - CORNER_R, BOTTOM_Y), (right, corner_y), radius_x=CORNER_R, sweep=False)
        self.add_line("wall-right", (right, corner_y), (right, RIM_Y))
        self.add_line("lip-right", (right, RIM_Y), (48 - LIP_X, RIM_Y))
        self.add_contour("tub", "lip-left", "wall-left", "corner-left", "bottom",
                         "corner-right", "wall-right", "lip-right")
