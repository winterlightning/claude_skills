"""hand-above-water (redraw of the new-pipeline traced SVG).

Subject: an open hand raised out of water (a call for help / drowning), the
arm entering the upper of two horizontal wave lines.

Plan: SQUARE (the suggested keyshape; centerline box (6,6)-(42,42)).
- fingers, Lucide `hand` construction (shared walls, round tips, open slits):
  three hollow fingers 8 wide on walls x=18/26/34/42, tips are r4 semicircles
  whose apexes are y=8 (index), y=6 (middle, the top extreme) and y=10 (ring).
  The slits x=26 and x=34 stop at y=23.
- thumb: a 10-wide lobe on the steep 3-4-5 axis from the crotch (18,22);
  r5 tip centred (11,21), apex on the x=6 extreme. Its lower edge flows on
  down into the water as the left side of the arm.
- palm right side: the ring wall x=42 runs to y=24, then one curve narrows
  it into the water at (38,32), far enough from the x=34 slit end.
- water: two sine waves, period 16, amplitude 1, quarter-period knots on the
  integer grid; crests at x=18 and x=34. The top wave (y 31-33) is split at
  the knots (14,32) and (38,32) where the arm enters it; the bottom wave sits 9 lower (y 40-42, the bottom
  extreme), which keeps the two lines 8 apart across their slopes.
References: the generated PNG (raised open hand, thumb out to the left, two
waves below); Lucide `hand` (shared finger walls, r=width/2 round tips, finger
slits left open into the palm).

Metric issues (svg_metrics) and what happened to them:
- stroke-width (info): fixed, redrawn at stroke 4 with every opening budgeted
  at >= 8 between centerlines.
- keyshape-short-axis (SQUARE x filled 73%): fixed, thumb apex on x=6, ring
  wall on x=42, waves span x=6..42; middle tip on y=6, bottom wave on y=42.
- clearance e0/e1, e1/e3, e1/e2, e0/e3, e0/e2 (finger walls 3.6 apart): fixed
  by dropping the pinky, the trace's five walls ~3.6 apart cannot hold stroke 4;
  four fingers and a thumb need a 40-wide centerline run, the box is 36, so
  the hand keeps three fingers on 8-unit walls.
- clearance e4/e5 (waves 3.5 apart): fixed, waves 9 apart vertically.
- clearance e0/e4, e2/e4, e0/e5, e2/e5 (wrist ends 2.6 above the wave): fixed
  by joining the arm to the top wave at shared crest knots (declared connect),
  so the hand reads as rising out of the water instead of hovering 3 above it.
Not fixed: none. Deliberate reductions: the pinky (width budget above) and
the gap between wrist and water (a detached wrist needs 8 above the top wave,
which leaves the hand 17 tall; a one-wave candidate was also rendered and
rejected because a single line reads as a surface, not water).
Asymmetry is deliberate: thumb on the left, arm entering off-centre.
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "308c7b26-332e-4a63-acca-d4c8af288d7f"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1320-hand-above-water/hand-above-water_raw.svg"
AUTHOR = "claude-opus-5-5"

WALLS = (18, 26, 34, 42)           # index | middle | ring finger walls
TIP_TOPS = (8, 6, 10)              # apex of each finger tip
FINGER_R = 4
SLIT_END = 23
CROTCH = (18, 22)                  # thumb meets the index wall
THUMB_R = 5                        # thumb 10 wide on the 3-4-5 axis
RING_WALL_END = 24                 # right palm starts to narrow
# Waves: y = MID - AMP * cos(2*pi*(x - CREST_X) / PERIOD).
WAVE_X0, WAVE_X1 = 6, 42
PERIOD, AMP, CREST_X = 16, 1, 18
TOP_MID, WAVE_GAP = 32, 9
ARM_LEFT, ARM_RIGHT = 14, 38       # where the arm meets the top wave


def wave_y(x, mid):
    return mid - AMP * math.cos(2 * math.pi * (x - CREST_X) / PERIOD)


def wave_segments(x0, x1, mid):
    """Cubic Hermite quarter-period pieces of the sine from x0 to x1."""
    step = PERIOD // 4
    k = 2 * math.pi / PERIOD
    segs = []
    x = x0
    while x < x1:
        nx = x + step
        s0 = AMP * k * math.sin(k * (x - CREST_X))
        s1 = AMP * k * math.sin(k * (nx - CREST_X))
        d = step / 3
        y0, y1 = round(wave_y(x, mid)), round(wave_y(nx, mid))
        segs.append(((x + d, y0 + s0 * d), (nx - d, y1 - s1 * d), (nx, y1)))
        x = nx
    return segs


class HandAboveWaterRedraw(Solo48):
    icon_id = "hand-above-water-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/gestures"
    aliases = ("drowning hand", "hand out of water", "help in water")
    keywords = ("hand", "water", "waves", "drowning", "help", "rescue",
                "swim", "sea", "lifeguard", "emergency")

    def build(self) -> None:
        w0, w1, w2, w3 = WALLS
        t0, t1, t2 = TIP_TOPS
        r = FINGER_R
        top = lambda y: y + r            # arc endpoints sit r below the apex

        # Ring finger and right side of the palm, down into the water.
        self.add_line("ring-slit", (w2, SLIT_END), (w2, top(t2)))
        self.add_arc("ring-tip", (w2, top(t2)), (w3, top(t2)), radius_x=r)
        self.add_line("ring-wall", (w3, top(t2)), (w3, RING_WALL_END))
        arm_r = (ARM_RIGHT, round(wave_y(ARM_RIGHT, TOP_MID)))
        self.add_bezier("palm-right", (w3, RING_WALL_END),
                        ((w3, RING_WALL_END + 5), (arm_r[0] + 1, arm_r[1] - 5), arm_r))
        self.add_contour("ring", "ring-slit", "ring-tip", "ring-wall", "palm-right")

        # Middle finger: slit up, tip, down onto the ring tip's start.
        self.add_line("middle-slit-low", (w1, SLIT_END), (w1, top(t0)))
        self.add_line("middle-slit-high", (w1, top(t0)), (w1, top(t1)))
        self.add_arc("middle-tip", (w1, top(t1)), (w2, top(t1)), radius_x=r)
        self.add_line("middle-wall", (w2, top(t1)), (w2, top(t2)))
        self.add_contour("middle", "middle-slit-low", "middle-slit-high",
                         "middle-tip", "middle-wall")

        # Left side of the arm, thumb, index finger onto the middle slit.
        cx, cy = CROTCH
        p1 = (cx - 3, cy - 4)                       # thumb upper edge end
        p2 = (p1[0] - 8, p1[1] + 6)                 # tip is a semicircle, r5
        arm_l = (ARM_LEFT, round(wave_y(ARM_LEFT, TOP_MID)))
        self.add_bezier("arm-left", arm_l,
                        ((arm_l[0] - 2.5, arm_l[1] - 3.5), (p2[0] + 1.8, p2[1] + 2.4), p2))
        self.add_arc("thumb-tip", p2, p1, radius_x=THUMB_R)
        self.add_line("thumb-top", p1, CROTCH)
        self.add_line("index-wall", CROTCH, (w0, top(t0)))
        self.add_arc("index-tip", (w0, top(t0)), (w1, top(t0)), radius_x=r)
        self.add_contour("index", "arm-left", "thumb-tip", "thumb-top",
                         "index-wall", "index-tip")

        # Water: top wave split where the arm enters, bottom wave 9 lower.
        def wave(name, x0, x1, mid):
            self.add_bezier(name, (x0, round(wave_y(x0, mid))),
                            *wave_segments(x0, x1, mid))
        wave("wave-top-left", WAVE_X0, ARM_LEFT, TOP_MID)
        wave("wave-top-mid", ARM_LEFT, ARM_RIGHT, TOP_MID)
        wave("wave-top-right", ARM_RIGHT, WAVE_X1, TOP_MID)
        wave("wave-bottom", WAVE_X0, WAVE_X1, TOP_MID + WAVE_GAP)

        self.relate("connect", "index", "middle")
        self.relate("connect", "middle", "ring")
        self.relate("connect", "index", "wave-top-left")
        self.relate("connect", "index", "wave-top-mid")
        self.relate("connect", "ring", "wave-top-mid")
        self.relate("connect", "ring", "wave-top-right")
