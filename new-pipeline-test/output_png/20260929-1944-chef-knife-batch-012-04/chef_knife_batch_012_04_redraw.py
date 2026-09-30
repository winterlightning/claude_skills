"""chef-knife-batch-012-04 (redraw of the new-pipeline traced SVG).

Subject: a chef's knife -- a long blade with a straight spine and a curved
belly rising to a point, and a hollow rounded handle flush with the spine,
stepped up from the heel of the blade.

Plan: SQUARE, centerline box (6,6)-(42,42). The knife is laid on the
diagonal (tip top-left, handle bottom-right) because a 3:1 knife cannot fill
a rectangle's short axis (see keyshape below).
Extremes: tip (6,6) gives x=6 and y=6 (the spine leaves it at ~39 deg and the
edge leaves it steeply, so both run inward from the tip); the handle cap, a
circle r=5 about (37,37), gives x=42 at (42,37) and y=42 at (37,42).
- handle: runs along the 3-4-5 direction (4,3). Its top edge (32,27)->(40,33)
  and bottom edge (26,35)->(34,41) are offset by (-6,8), exactly 10 apart,
  so the r=5 cap arc (40,33)->(34,41) is a tangent semicircle with integer
  knots and the hole is 6 inscribed.
- blade: one closed contour -- straight spine (6,6)->(32,27) (a 2 deg bend
  onto the handle line, hidden at the heel joint), heel on the (-3,4)
  perpendicular (32,27)->(26,35)->(23,39), and one cubic belly from the heel
  back to the tip, leaving the heel parallel to the spine and curving up
  steeply near the point (x never passes 6).
- the handle shares the heel line at (32,27) and (26,35); declared connect.
Proportions from the generated PNG: blade about 2.2x as long as it is deep
and about 1.5x as deep as the handle; handle about half the blade length.
References: generated PNG read for the subject only; Lucide has no chef knife
(`utensils` / `slice` only), so no Lucide construction was used beyond round
caps and one closed outline per part. No trace coordinates copied.

Keyshape: metrics suggested HRECT_M (score 0.72) but its own fit shows the
y axis fills only 47% (stretch 2.15 needed); HRECT_L is worse (41%). Keeping
the knife horizontal would need a 28-tall knife. The diagonal fills the
SQUARE exactly on all four sides without stretching the subject.

Metric issues:
- stroke-width (info): redrawn at stroke 4; every gap budgeted for it.
- keyshape-short-axis (HRECT_M y fills 47%): fixed by the diagonal SQUARE
  construction; ink runs exactly 4..44 on both axes.
- hole [38.6,21.1] (the handle, 3.4 inscribed): fixed; the handle is 10 wide
  on centerlines, so its hole is 6 inscribed (build gate passes).
Not kept as drawn: the slight downward curl of the spine at the tip (the
tip must sit on the box corner, so the spine runs straight into it).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "88acc3ca-ec5a-4cec-af6f-f39df121e302"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1944-chef-knife-batch-012-04/chef-knife-batch-012-04_raw.svg"
AUTHOR = "claude-opus-5-5"

TIP = (6, 6)
HEEL_TOP = (32, 27)
HEEL_MID = (26, 35)
HEEL_BOT = (23, 39)
HANDLE_TOP_END = (40, 33)
HANDLE_BOT_END = (34, 41)
CAP_R = 5


class ChefKnifeRedraw(Solo48):
    icon_id = "chef-knife-batch-012-04-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/kitchen"
    aliases = ("chef knife", "kitchen knife", "cook's knife")
    keywords = ("knife", "chef", "kitchen", "blade", "cutting", "cooking", "utensil")

    def build(self) -> None:
        self.add_line("spine", TIP, HEEL_TOP)
        self.add_line("heel-upper", HEEL_TOP, HEEL_MID)
        self.add_line("heel-lower", HEEL_MID, HEEL_BOT)
        self.add_bezier("edge", HEEL_BOT, ((15, 33), (7, 17), TIP))
        self.add_contour("blade", "spine", "heel-upper", "heel-lower", "edge", closed=True)

        self.add_line("handle-top", HEEL_TOP, HANDLE_TOP_END)
        self.add_arc("handle-cap", HANDLE_TOP_END, HANDLE_BOT_END, radius_x=CAP_R, sweep=True)
        self.add_line("handle-bottom", HANDLE_BOT_END, HEEL_MID)
        self.add_contour("handle", "handle-top", "handle-cap", "handle-bottom")
        self.relate("connect", "handle", "blade")
