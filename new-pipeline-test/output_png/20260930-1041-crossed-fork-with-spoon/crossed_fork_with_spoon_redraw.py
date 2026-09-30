"""crossed-fork-with-spoon (redraw of the new-pipeline traced SVG).

Plan: SQUARE keyshape (centerline box (6,6)-(42,42)), both utensils on the
45-degree diagonals so every straight run is pixel-clean at 48 px.
- crossing X = (25,25): the fork runs along (1,1) on y=x, the spoon along
  (1,-1) on x+y=50. Both handles pass through X as a shared vertex and the
  crossing is declared connect.
- fork: middle tine M->A and handle A->X->E are one straight diagonal. The
  outer tines sit 6 grid steps either side ((6,-6) = 8.49 on centerlines),
  run 3 steps straight, then close into a U whose two quarter-ellipse cubics
  (depth 4 steps) meet the middle tine at A with a perpendicular tangent.
  A is 6 steps (8.49) from the spoon line. The fork is mirrored about y=x.
- spoon: an egg-shaped bowl mirrored about x+y=50, (x,y) -> (50-y, 50-x).
  Its tip is a radius-5 arc centred on the axis at (37,13), so the arc's
  apexes are the bowl's top (y=8) and right (x=42) extremes; two mirrored
  cubic sides meet tangentially at the neck N, 6 steps (8.49) off the fork.
Extremes: fork left tine x=6, fork right tine y=6, fork handle end (42,42),
spoon bowl x=42 and spoon handle end y=42 -- the SQUARE fit is exact.

Metric issues:
- clearance e0/e1 (fork handle vs U, 0 apart): fixed -- the U is one contour
  joined to the middle tine and the handle at the shared apex A (connect).
- clearance e0/e3, e0/e4 (spoon break 2 from the fork handle) and e3/e4
  (the two break halves 4 apart): fixed by making the spoon handle one
  continuous stroke that crosses the fork handle at a shared, declared
  vertex. A clear break needs 8.49 either side of the fork line plus the
  fork U kept clear of both break ends; tried on the grid, it left a
  2.8-unit neck stub and a lollipop-sized bowl, so the break was dropped
  in favour of a readable spoon. The metrics script still reports the
  crossing as 0 apart because it cannot see the declared connect; that is
  the intended junction.
- loose-join e3/e2 (stub 0.44 short of the bowl): fixed -- the handle ends
  on the bowl's neck anchor N and is related connect.
- keyshape-short-axis (y fill 87%): fixed -- the fork tine reaches y=6 and
  the handles y=42, so the SQUARE box is filled on both axes.
- stroke-width (trace 2.35 vs 4): redrawn at stroke 4 with every gap
  between distinct parts at least 8 on centerlines; bowl hole 6.9 wide.
Lucide utensils-crossed informed the U fork with the middle tine running on
as the handle and the 45-degree crossing; the two heads differ on purpose.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "53cd4f82-ae5a-4f7a-8ddd-de64747944f4"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1041-crossed-fork-with-spoon/"
    "crossed-fork-with-spoon_raw.svg"
)
AUTHOR = "claude-opus-5-5"

X = (25, 25)             # handle crossing

# Fork (along (1,1), mirrored about y=x).
M = (12, 12)             # middle tine tip
A = (19, 19)             # U apex: middle tine / handle junction
E = (42, 42)             # fork handle end
L0, L1 = (6, 18), (9, 21)    # left tine tip -> start of the U
R0, R1 = (18, 6), (21, 9)    # right tine tip -> end of the U
U_DEPTH, U_HALF = 4, 6       # U depth and half-width in diagonal grid steps
K_TINE, K_APEX = 0.45, 0.55  # U cubic handle ratios (tine side kept a little
                             # tighter so the U shoulder clears the bowl)

# Spoon (along (1,-1) on x+y=50, mirrored about that line).
S0 = (8, 42)             # handle end
N = (31, 19)             # bowl neck
BOWL_R = 5
T = (37, 8)              # bowl top (arc apex)
RT = (42, 13)            # bowl right (arc apex); arc centre (37,13)
SIDE_N, SIDE_E = 3.0, 6.0    # side cubic handles at the neck / at T and RT


class CrossedForkWithSpoonRedraw(Solo48):
    icon_id = "crossed-fork-with-spoon-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ("fork and spoon", "cutlery", "utensils crossed")
    keywords = ("fork", "spoon", "cutlery", "crossed", "dining", "utensil", "meal", "restaurant")

    def build(self) -> None:
        kd, kh = K_TINE * U_DEPTH, K_APEX * U_HALF
        self.add_line("fork-left-tine", L0, L1)
        self.add_bezier(
            "fork-u", L1,
            ((L1[0] + kd, L1[1] + kd), (A[0] - kh, A[1] + kh), A),
            ((A[0] + kh, A[1] - kh), (R1[0] + kd, R1[1] + kd), R1),
        )
        self.add_line("fork-right-tine", R1, R0)
        self.add_contour("fork-head", "fork-left-tine", "fork-u", "fork-right-tine")
        self.add_line("fork-middle-tine", M, A)
        self.add_polyline("fork-handle", A, X, E)
        self.relate("connect", "fork-head", "fork-middle-tine")
        self.relate("connect", "fork-head", "fork-handle")
        self.relate("connect", "fork-middle-tine", "fork-handle")

        self.add_arc("spoon-tip", T, RT, radius_x=BOWL_R)
        self.add_bezier(
            "spoon-right", RT,
            ((RT[0], RT[1] + SIDE_E), (N[0] + SIDE_N, N[1] + SIDE_N), N),
        )
        self.add_bezier(
            "spoon-left", N,
            ((N[0] - SIDE_N, N[1] - SIDE_N), (T[0] - SIDE_E, T[1]), T),
        )
        self.add_contour("spoon-bowl", "spoon-tip", "spoon-right", "spoon-left", closed=True)
        self.add_polyline("spoon-handle", S0, X, N)
        self.relate("connect", "spoon-handle", "spoon-bowl")
        self.relate("connect", "spoon-handle", "fork-handle")
