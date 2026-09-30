"""bearded-pirate-beside-cutlass (redraw of the new-pipeline traced SVG).

Plan: a bearded bust on the left and an upright cutlass on the right, on
SQUARE (centerline box (6,6)-(42,42)), rebuilt on the 48 grid from the
trace's layout, not its coordinates.
- head + beard: one closed contour on the axis HX. The crown is a r7
  semicircle (top on the y=6 extreme); its sides drop straight down and
  close at 45 degrees into a pointed beard tip, so the beard reads as the
  lower half of the face instead of a loose V hanging under it.
- shoulders: a r10 dome on the same axis, split at its apex (HX,32) so the
  right half is the torso primitive whose start is the neck point. The beard
  tip sits exactly 8 centerline units above it (4-unit ink gap,
  human-reference.md). Its left foot is the x=6 extreme, both feet y=42.
- cutlass: a vertical handle from the guard to the y=42 extreme, a crossguard
  split at the handle (right end is the x=42 extreme), and a single curved
  blade stroke leaving the handle vertically, bowing right and sweeping back
  to a tip at (34,6).
Reference: icon_set/references/human_ref/user.svg (circular head over an open
shoulder dome); Lucide `sword` for the guard/handle split. No Lucide cutlass.

Keyshape: SQUARE, as suggested (fill 1.0 on both axes, matches the hint).

Metric issues fixed:
- clearance e0/e1, e0/e5, e1/e5 (blade outline, guard and right shoulder
  overlapping): the blade is one stroke sharing the guard/handle node, and
  the whole cutlass stands >= 9.7 from the shoulder dome.
- clearance e2/e3, e3/e4, e3/e5 (beard crowding head and shoulders): the
  beard is part of the head contour and its tip is exactly 8 above the dome.
- hole at (39.7,19) (0.6 wide blade slit): the hollow blade is reduced to a
  single stroke, so no slit remains.
- hole at (18,25.4) (3.5 wide pocket under the chin): gone with the merged
  head/beard contour; the face opening is 10 wide in ink.
- no-head: the head is a real r7 arc crown, marked with mark_human_figure.
- stroke-width: redrawn at stroke 4 with 8-unit clearances throughout.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "c8320437-caa5-4ec9-8b7a-42c57db14a5f"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1829-bearded-pirate-beside-cutlass/"
    "bearded-pirate-beside-cutlass_raw.svg"
)
AUTHOR = "claude-opus-5-5"

HX = 16                          # head / shoulder axis
HEAD_R, HEAD_CY = 7, 13          # crown top on y=6
JAW_Y = 17                       # beard sides turn inward here
TIP = (HX, JAW_Y + HEAD_R)       # (16,24), 45-degree beard point
DOME_R = 10
APEX = (HX, TIP[1] + 8)          # (16,32), 8 below the beard tip
BASE_Y = 42
SWORD_X, GUARD_Y = 38, 34
GUARD_HALF = 4
BLADE_TIP = (34, 6)


class BeardedPirateBesideCutlassRedraw(Solo48):
    icon_id = "bearded-pirate-beside-cutlass-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "avatars"
    aliases = ("pirate", "buccaneer", "swashbuckler")
    keywords = ("pirate", "beard", "cutlass", "sword", "sabre", "person", "seafarer", "adventure")

    def build(self) -> None:
        left, right = HX - HEAD_R, HX + HEAD_R
        self.add_arc("crown-l", (left, HEAD_CY), (HX, HEAD_CY - HEAD_R), radius_x=HEAD_R, sweep=True)
        self.add_arc("crown-r", (HX, HEAD_CY - HEAD_R), (right, HEAD_CY), radius_x=HEAD_R, sweep=True)
        self.add_line("cheek-r", (right, HEAD_CY), (right, JAW_Y))
        self.add_line("beard-r", (right, JAW_Y), TIP)
        self.add_line("beard-l", TIP, (left, JAW_Y))
        self.add_line("cheek-l", (left, JAW_Y), (left, HEAD_CY))
        self.add_contour(
            "head", "crown-l", "crown-r", "cheek-r", "beard-r", "beard-l", "cheek-l",
            closed=True,
        )

        self.add_arc("shoulder-l", (HX - DOME_R, BASE_Y), APEX, radius_x=DOME_R, sweep=True)
        self.add_arc("torso", APEX, (HX + DOME_R, BASE_Y), radius_x=DOME_R, sweep=True)
        self.add_contour("shoulders", "shoulder-l", "torso")
        self.mark_human_figure("pirate", head="head", torso="torso", torso_junction="start")

        hilt = (SWORD_X, GUARD_Y)
        self.add_line("guard-l", (SWORD_X - GUARD_HALF, GUARD_Y), hilt)
        self.add_line("guard-r", hilt, (SWORD_X + GUARD_HALF, GUARD_Y))
        self.add_contour("guard", "guard-l", "guard-r")
        self.add_line("handle", hilt, (SWORD_X, BASE_Y))
        self.add_bezier("blade", hilt, ((SWORD_X, 22), (SWORD_X + 2, 12), BLADE_TIP))
        self.relate("connect", "guard", "handle")
        self.relate("connect", "guard", "blade")
        self.relate("connect", "handle", "blade")
