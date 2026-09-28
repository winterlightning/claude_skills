"""beetle in glass dome (redraw of the new-pipeline traced SVG).

Plan: VRECT_L (centerline box (8,4)-(40,44)), everything mirrored on x=AXIS.
- dome: one closed contour. Arch = half circle radius 16 about (24,20), apex
  (24,4) on the box top; walls x=8 / x=40 run straight down to the floor line
  y=44, so all four keyshape extremes are touched exactly.
- beetle (inside the band left by the 8-unit clearance: x 16..32, y <= 36,
  and within radius 8 of (24,20) above the arch spring line):
  shell = stadium of two radius-5 ends (centres (24,24) and (24,30)) joined
  by x=19 / x=29 sides; its top end is split at the (3,4) points (21,20) and
  (27,20) so the head, a radius-3 half circle on that chord, shares both
  endpoints; the 2-unit sliver under the head paints solid, giving a solid
  head cap. Antennae are a V from the head crown (24,17) to (20,14)/(28,14);
  one front and one rear leg per side leave the shell sides to x=17.
No useful Lucide match for the dome; the beetle takes its reading from Lucide
`bug` (rounded body, head cap, paired side legs, antennae), reduced to the
room inside the dome.
Metric issues:
- stroke-width (trace 2.47): redrawn at stroke 4 on the integer grid.
- stroke-count (11, budget 6): reduced to dome, shell, head, 2 antennae and
  4 legs; the separate base plate, the shell seam and the middle leg pair
  are dropped (see below).
- keyshape-short-axis (VRECT_L y fill 93%): fixed; arch apex y=4 and floor
  y=44 sit on the box, walls on x=8 / x=40.
- clearance errors (26: base plate vs legs/shell, walls vs legs, head vs
  seam/legs, seam vs legs, legs vs legs): fixed; every free part is at
  least 8 (9 where a curve or a leg cap faces a wall, the exact-8 review
  trap) from every other part, and every touching part shares an endpoint
  and is declared `connect`.
- holes < 6 (the two slivers either side of the seam, 1.4): fixed; the
  shell hole is 6 wide x 13 tall in ink; the head sliver paints solid.
Not kept, with reason:
- base plate wider than the dome: VRECT_L caps the centerline width at 32
  and the walls already sit on it; a separate plate needs 10 units of height
  for its own 6-unit hole plus 8 of clearance, which the beetle cannot give
  up. The floor line of the dome stands in for the base.
- shell centre seam: halves of the 10-wide shell would be 1 unit of ink
  hole each; a seamed shell needs 20+ units across, more than the 16-unit
  band inside the dome.
- middle legs: a third pair cannot sit 8 from both leg pairs on a 13-unit
  side.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "9e1427e3-01db-4b03-91a2-6aedb6775a60"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1701-beetle-in-glass-dome/beetle-in-glass-dome_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
# dome: arch radius DOME_R about (AXIS, DOME_CY), walls to the floor
DOME_R = 16
DOME_CY = 20
FLOOR_Y = 44
# shell: stadium of two radius-5 ends joined by straight sides
SHELL_R = 5
SHELL_TOP_CY = 24
SHELL_BOTTOM_CY = 30
HEAD_R = 3
ANTENNA_TIP = (20, 14)       # left tip, mirrored
FRONT_LEG = ((19, 26), (17, 23))
REAR_LEG = ((19, 30), (17, 33))


class BeetleInGlassDomeRedraw(Solo48):
    icon_id = "beetle-in-glass-dome-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/insects"
    aliases = ("bug under glass", "beetle specimen", "insect bell jar")
    keywords = ("beetle", "bug", "insect", "dome", "glass", "bell jar", "cloche", "specimen", "collection", "museum")

    def build(self) -> None:
        m = lambda p: (2 * AXIS - p[0], p[1])
        left, right = AXIS - DOME_R, AXIS + DOME_R

        # glass dome: arch + walls + floor, one closed contour
        self.add_arc("dome-arch", (left, DOME_CY), (right, DOME_CY), radius_x=DOME_R)
        self.add_line("dome-wall-right", (right, DOME_CY), (right, FLOOR_Y))
        self.add_line("dome-floor", (right, FLOOR_Y), (left, FLOOR_Y))
        self.add_line("dome-wall-left", (left, FLOOR_Y), (left, DOME_CY))
        self.add_contour("dome", "dome-arch", "dome-wall-right", "dome-floor", "dome-wall-left", closed=True)

        # shell: stadium, top end split where the head sits
        r, sl, sr = SHELL_R, AXIS - SHELL_R, AXIS + SHELL_R
        nl, nr = (AXIS - HEAD_R, SHELL_TOP_CY - 4), (AXIS + HEAD_R, SHELL_TOP_CY - 4)
        self.add_arc("shell-shoulder-left", (sl, SHELL_TOP_CY), nl, radius_x=r)
        self.add_arc("shell-top", nl, nr, radius_x=r)
        self.add_arc("shell-shoulder-right", nr, (sr, SHELL_TOP_CY), radius_x=r)
        self.add_line("shell-side-right", (sr, SHELL_TOP_CY), (sr, SHELL_BOTTOM_CY))
        self.add_arc("shell-bottom", (sr, SHELL_BOTTOM_CY), (sl, SHELL_BOTTOM_CY), radius_x=r)
        self.add_line("shell-side-left", (sl, SHELL_BOTTOM_CY), (sl, SHELL_TOP_CY))
        self.add_contour("shell", "shell-shoulder-left", "shell-top", "shell-shoulder-right",
                         "shell-side-right", "shell-bottom", "shell-side-left", closed=True)

        # head: half circle on the shell's top chord; the sliver under it paints solid
        self.add_arc("head", nl, nr, radius_x=HEAD_R)
        self.relate("connect", "head", "shell")
        crown = (AXIS, nl[1] - HEAD_R)

        for side, tag in ((1, "left"), (-1, "right")):
            f = (lambda p: p) if side == 1 else m
            self.add_line(f"antenna-{tag}", crown, f(ANTENNA_TIP))
            self.relate("connect", f"antenna-{tag}", "head")
            self.add_line(f"leg-front-{tag}", f(FRONT_LEG[0]), f(FRONT_LEG[1]))
            self.relate("connect", f"leg-front-{tag}", "shell")
            self.add_line(f"leg-rear-{tag}", f(REAR_LEG[0]), f(REAR_LEG[1]))
            self.relate("connect", f"leg-rear-{tag}", "shell")
