"""mexican-hard-shell-taco (redraw of the new-pipeline traced SVG).

Plan: wide taco on HRECT_L (centerline box (4,8)-(44,40)), mirrored about x=24.
- shell: one closed contour, a semicircle r=20 about (24,40) on the base line
  y=40 (ends (4,40)/(44,40), apex y=20). It is split at the 3-4-5 points
  (12,24)/(36,24) where the lettuce lands.
- lettuce: one open contour hugging the shell. The tails leave the shell
  radially ((12,24) -> (6,16) is (-6,-8), along the radius), so they meet it
  at a right angle, with no slivers. Three scallops follow: r=6 side lobes
  (6,16)->(16,12) and an r=10 crown (16,12)->(32,12) whose apex is y=8.
  Every cusp sits 29-30 from the shell centre, so 9-10 clear of the shell.
Dropped from the trace: the two small shoulder nubs and the vertical tails.
In the trace they left 0.8-1.4 unit slivers and a 2.3 unit gap against the
shell (metrics hole/clearance errors). At stroke 4, vertical tails also boxed
the lettuce into a hat or crown shape. HRECT_L over the suggested HRECT_M: the
half-moon shell needs the height to dominate the ruffle. No useful Lucide
match (Lucide has no taco).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1443-mexican-hard-shell-taco/"
    "mexican-hard-shell-taco_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
# Shell: semicircle on the base line
SHELL_C = (AXIS, 40)
SHELL_R = 20
LAND_L = (12, 24)           # 3-4-5 point on the shell
# Lettuce
TAIL_TOP = (6, 16)          # LAND_L + (-6,-8): radial, 10 long
CUSP_L = (16, 12)           # crown cusp, 29.1 from the shell centre
LOBE_R = 6
CROWN_R = 10                # chord 16, sagitta 4: apex (24,8)


def mx(p):
    return (2 * AXIS - p[0], p[1])


class MexicanHardShellTacoRedraw(Solo48):
    icon_id = "mexican-hard-shell-taco-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/dishes"
    aliases = ("taco", "hard shell taco", "crunchy taco")
    keywords = ("taco", "mexican", "food", "tortilla", "lettuce", "tex-mex", "fast food")

    def build(self) -> None:
        cx, cy = SHELL_C
        left, right = (cx - SHELL_R, cy), (cx + SHELL_R, cy)
        land_l, land_r = LAND_L, mx(LAND_L)

        # Shell, clockwise from the base's left end.
        self.add_arc("dome-l", left, land_l, radius_x=SHELL_R)
        self.add_arc("dome-c", land_l, land_r, radius_x=SHELL_R)
        self.add_arc("dome-r", land_r, right, radius_x=SHELL_R)
        self.add_line("base", right, left)
        self.add_contour("shell", "dome-l", "dome-c", "dome-r", "base", closed=True)

        # Lettuce, left tail over the three scallops to the right tail.
        self.add_line("tail-l", land_l, TAIL_TOP)
        self.add_arc("lobe-l", TAIL_TOP, CUSP_L, radius_x=LOBE_R)
        self.add_arc("crown", CUSP_L, mx(CUSP_L), radius_x=CROWN_R)
        self.add_arc("lobe-r", mx(CUSP_L), mx(TAIL_TOP), radius_x=LOBE_R)
        self.add_line("tail-r", mx(TAIL_TOP), land_r)
        self.add_contour("lettuce", "tail-l", "lobe-l", "crown", "lobe-r", "tail-r")
        self.relate("connect", "lettuce", "shell")
