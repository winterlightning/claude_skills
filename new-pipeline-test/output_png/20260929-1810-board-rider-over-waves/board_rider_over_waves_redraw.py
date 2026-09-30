"""board-rider-over-waves (redraw of the new-pipeline traced SVG).

Plan: frontal stick-figure surfer balancing on a board, a two-crest wave line
below, on VRECT_L (centerline box (8,4)-(40,44)).
- head: 4-cardinal-arc circle about (AX, HEAD_CY); its top is the y=4 extreme.
- torso: a short vertical neck stub under the head (the head sits on the upper
  torso axis, exactly 8 centerline units / 4 ink units below the outline, as in
  human-reference.md), then the lower torso slants to a set-back hip, keeping
  the reference's lean.
- arms: balancing arms out to both sides. Each upper arm is a standalone line
  leaving the neck level or dropping (a rising one would come within 8 of the
  head); the rear forearm runs level, the front forearm lifts. Hands are the
  x=8 / x=40 extremes.
- legs: one stroke from the rear foot over the hip to a bent front knee, feet
  planted on the board.
- board: one stroke with a Lucide-style upturned nose (a hollow outline cannot
  fit, see below).
- wave: one smooth run of cubics with two rounded crests; its ends and the
  middle trough are the y=44 extreme.

Vertical budget (40): head + 8 gap + neck-to-hip 9 (hip must clear the arms)
+ legs 7 (the leg/board opening needs a 6-unit inscribed hole) + board-to-crest
9 + wave amplitude 3. This is why SQUARE (36 tall, the metrics' suggestion)
was replaced by VRECT_L (the metrics' second candidate, fill 1.0 x 0.93).

Metric issues:
- clearance e0/e3, e0/e5, e0/e6 (head crowding the torso and arms): fixed;
  the head sits exactly 8 above the neck and the upper arms leave the neck
  level or dropping, so they never approach the head.
- clearance e1/e2 (leg crossing the board): fixed; both feet end on the board
  with a declared connect.
- clearance e1/e7 (board 4 above the wave): fixed; crests are 9 below the board.
- clearance e2/e5, e2/e6, e4/e5, e4/e6 (legs crowding the arms at the hip):
  fixed; the hip is 9 below the neck and at least 9 from every arm segment.
- human head gap 2.5 -> exactly 8 on centerlines.
- loose joins e3/e5, e5/e6 (arms short of the shoulder): fixed; arms and torso
  share the neck node and are declared connected.
- holes (head 2.15, legs 3.4, board sliver 0.2): the leg/board opening passes
  the build gate's hole rule; the head is a whole small circle (exempt) and the
  board sliver is gone.
- keyshape-short-axis: fixed; VRECT_L extremes are all hit exactly.
- stroke-count 8 > 6: fixed; 5 visual parts (head, torso with arms, legs,
  board, wave).
Not kept: the hollow surfboard outline (an 8-tall closed board plus its 9 gap
to the wave exceeds the 40-unit height) and a large hollow head (the head is
a small r2 ring, which renders as a solid dot at stroke 4) for the same reason.
Lucide: no surfer icon; the wave follows Lucide `waves` (smooth cubic crests).
Human reference: icon_set/references/human_ref/full_body_ref.png.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "31dfc8f9-9e71-491e-9f9a-e8bd904e4344"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1810-board-rider-over-waves/"
    "board-rider-over-waves_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AX = 24                     # head / neck axis
HEAD_R = 2
HEAD_CY = 4 + HEAD_R        # top of the head on the y=4 extreme
NECK = (AX, HEAD_CY + HEAD_R + 8)
STUB = (AX, NECK[1] + 2)    # vertical upper torso under the head
HIP = (27, NECK[1] + 9)
LEFT_ELBOW, LEFT_HAND = (16, NECK[1] + 3), (8, NECK[1] + 3)
RIGHT_ELBOW, RIGHT_HAND = (32, NECK[1]), (40, NECK[1] - 4)
BOARD_Y = HIP[1] + 7
LEFT_FOOT = (16, BOARD_Y)
RIGHT_KNEE, RIGHT_FOOT = (33, HIP[1] + 4), (34, BOARD_Y)
BOARD = ((10, BOARD_Y), (34, BOARD_Y))
NOSE = (40, BOARD_Y - 3)
WAVE_BASE, WAVE_CREST = 44, 44 - 3
WAVE_X = (8, 16, 24, 32, 40)          # end, crest, trough, crest, end
K = 8 * 0.4                           # horizontal handle length


class BoardRiderOverWavesRedraw(Solo48):
    icon_id = "board-rider-over-waves-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ("surfer", "surfing", "board rider")
    keywords = ("surf", "surfing", "surfer", "surfboard", "wave", "sea", "beach", "water sports")

    def build(self) -> None:
        cx, cy, r = AX, HEAD_CY, HEAD_R
        self.add_arc("head-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc("head-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc("head-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc("head-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour("head", "head-1", "head-2", "head-3", "head-4", closed=True)

        self.add_line("torso", NECK, STUB)
        self.add_line("waist", STUB, HIP)
        self.relate("connect", "torso", "waist")
        self.mark_human_figure("rider", head="head", torso="torso", torso_junction="start")

        # Upper arms stay standalone lines so the exact head gap certifies.
        self.add_line("left-arm", NECK, LEFT_ELBOW)
        self.add_line("right-arm", NECK, RIGHT_ELBOW)
        self.add_line("left-forearm", LEFT_ELBOW, LEFT_HAND)
        self.add_line("right-forearm", RIGHT_ELBOW, RIGHT_HAND)
        for arm in ("left-arm", "right-arm"):
            self.relate("connect", arm, "torso")
        self.relate("connect", "left-arm", "right-arm")
        self.relate("connect", "left-arm", "left-forearm")
        self.relate("connect", "right-arm", "right-forearm")

        self.add_polyline("legs", LEFT_FOOT, HIP, RIGHT_KNEE, RIGHT_FOOT)
        self.relate("connect", "legs", "waist")

        self.add_line("board-deck", *BOARD)
        (bx, by), (nx, ny) = BOARD[1], NOSE
        self.add_bezier("board-nose", BOARD[1], ((bx + 3, by), (nx - 1, ny + 1), NOSE))
        self.add_contour("board", "board-deck", "board-nose")
        self.relate("connect", "board", "legs")

        x0, c1, t, c2, x1 = WAVE_X
        lo, hi = WAVE_BASE, WAVE_CREST
        knots = [(c1, hi), (t, lo), (c2, hi), (x1, lo)]
        segments = []
        prev = (x0, lo)
        for knot in knots:
            segments.append(((prev[0] + K, prev[1]), (knot[0] - K, knot[1]), knot))
            prev = knot
        self.add_bezier("wave", (x0, lo), *segments)
