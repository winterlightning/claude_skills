"""bellhop-holding-towel (redraw of the new-pipeline traced SVG).

Plan: hotel attendant bust holding a hanging towel, on VRECT_L (centerline
box (8,4)-(40,44)), rebuilt on the 48 grid from the trace's layout, not its
coordinates.
- head: 4-cardinal-arc circle, r5, centre (HX,9); its top is the y=4 extreme.
- shoulders: a r7 dome on the same axis HX, split at its apex (HX,22) so the
  right half is the torso primitive whose start is the neck point; the head
  outline sits exactly 8 centerline units above it (4-unit ink gap,
  human-reference.md). The left shoulder runs straight down to the hem as
  the body side (the x=8 extreme), giving the bust its weight.
- arm: the right shoulder drop continues as the upper arm, turns through a
  tangent r4 elbow into a horizontal forearm, and the hand grips the towel's
  left edge at (30,38) (shared endpoint, declared connect).
- towel: an upright 10x20 rectangle (30,24)-(40,44); its right edge is the
  x=40 extreme and its hem the y=44 extreme.
Reference: icon_set/references/human_ref/user.svg (circular head over an
open shoulder dome); no useful Lucide match for a bellhop with a towel.

Keyshape: the metrics suggest VRECT_M, but its 28-wide box cannot hold a
shoulder dome, an 8 clearance and a towel wide enough for a 6-unit hole
(10 on centerlines); VRECT_L (the runner-up, same tall hint) gives the 4
extra units, so the towel keeps a real opening.

Metric issues fixed:
- clearance e0/e1 and head-gap: the head is detached exactly 8 on
  centerlines above the dome apex, centred on the same axis.
- clearance e1/e2: the trace's arm started inside the shoulder dome; it now
  grows out of the right shoulder as one tangent-continuous stroke.
- clearance e1/e3, e2/e3: the upper arm stands 8 from the towel edge and the
  towel corner sits 8.6 from the dome; the hand touches the towel at one
  shared endpoint instead of hovering 2 units away.
- hole (1.4 wide towel): the towel is 10 wide on centerlines, a 6 ink hole.
- keyshape-short-axis: the figure touches x=8 and x=40 exactly, as well as
  y=4 (head) and y=44 (towel hem).
- stroke-width: redrawn at stroke 4 with 8-unit clearances throughout.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "2f063e75-85ad-52d2-8db7-bb6d3918a515"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1827-bellhop-holding-towel/"
    "bellhop-holding-towel_raw.svg"
)
AUTHOR = "claude-opus-5-5"

HX = 15                       # head / shoulder axis
HEAD_R, HEAD_CY = 5, 9        # centerline top at y=4
DOME_R = 7
APEX = (HX, 22)               # HEAD_CY + HEAD_R + 8
SHOULDER_Y = APEX[1] + DOME_R  # 29
ELBOW_Y = SHOULDER_Y + 5       # 34, where the upper arm bends
SIDE_Y = 44                    # the body's left side runs to the hem
ELBOW_R = 4
HAND = (30, ELBOW_Y + ELBOW_R)  # (30,38), on the towel's left edge
TOWEL = (30, 24, 40, 44)       # x0, y0, x1, y1


class BellhopHoldingTowelRedraw(Solo48):
    icon_id = "bellhop-holding-towel-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "hotels"
    aliases = ("hotel staff", "attendant", "valet", "room service")
    keywords = ("bellhop", "towel", "hotel", "staff", "housekeeping", "service")

    def build(self) -> None:
        cx, cy, r = HX, HEAD_CY, HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        left, right = HX - DOME_R, HX + DOME_R
        ex = right + ELBOW_R
        self.add_line("side-l", (left, SIDE_Y), (left, SHOULDER_Y))
        self.add_arc("shoulder-l", (left, SHOULDER_Y), APEX, radius_x=DOME_R, sweep=True)
        self.add_arc("torso", APEX, (right, SHOULDER_Y), radius_x=DOME_R, sweep=True)
        self.add_line("upper-arm", (right, SHOULDER_Y), (right, ELBOW_Y))
        self.add_arc("elbow", (right, ELBOW_Y), (ex, HAND[1]), radius_x=ELBOW_R, sweep=False)
        self.add_line("forearm", (ex, HAND[1]), HAND)
        self.add_contour(
            "body", "side-l", "shoulder-l", "torso",
            "upper-arm", "elbow", "forearm",
        )
        self.mark_human_figure("bellhop", head="head", torso="torso", torso_junction="start")

        x0, y0, x1, y1 = TOWEL
        self.add_line("towel-1", HAND, (x0, y1))
        self.add_line("towel-2", (x0, y1), (x1, y1))
        self.add_line("towel-3", (x1, y1), (x1, y0))
        self.add_line("towel-4", (x1, y0), (x0, y0))
        self.add_line("towel-5", (x0, y0), HAND)
        self.add_contour("towel", "towel-1", "towel-2", "towel-3", "towel-4", "towel-5", closed=True)
        self.relate("connect", "body", "towel")
