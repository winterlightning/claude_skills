"""hand-gripping-plain-cup (redraw of the new-pipeline traced SVG).

Subject: a plain handleless tumbler held from the left by a forearm whose
single broad hand band wraps across the front of the cup and hooks round its
right side.

Plan: SQUARE (centerline box (6,6)-(42,42)); the hand is in front, so the cup
walls stop on the hand's upper and lower edges (T-junctions, declared connect).
- cup-top: open polyline, rim (17,6)-(37,6) on the y=6 extreme, walls tapering
  1:14 down to the hand's top edge at (18,20) and (36,20). Cup axis x=27.
- cup-bowl: the rounded bottom below the hand, mirrored about x=27: two cubics
  leave the hand's lower edge at (19,30)/(35,30) along the wall taper and turn
  through rounded corners into a flat base (23,42)-(31,42) on the y=42 extreme.
- hand: one open contour. Forearm top y=23 from the x=6 extreme, a smooth
  back-of-hand rise to y=20, straight across the cup, a semicircular hook
  (r=5, centre (37,25), tip on the x=42 extreme), back along y=30 and a
  smooth drop to the forearm bottom y=32 at x=6 (forearm 9 wide).
References: the generated PNG (hand band across the cup middle, rounded hook
past the right wall, tapered cup with rounded base); no useful Lucide match
(Lucide `cup-soda` / `glass-water` informed only the tapered tumbler walls).

Metric issues (svg_metrics) and what happened to them:
- stroke-width (info): fixed, redrawn at stroke 4 with every gap budgeted for
  it (hand band 10, forearm 9, cup openings >= 12 on centerlines).
- keyshape-short-axis (SQUARE y filled 73%): fixed by making the cup a taller
  tumbler: rim on y=6, base on y=42, forearm end x=6, hook tip x=42.
- hole 3.98 at (33.9,33.0) (the bowl under the hand): fixed, the bowl is now
  12 deep and 16 wide between centerlines (about 8 ink inscribed).
- no-head (warn): not applicable, the subject is a hand and forearm, not a
  figure, so no head is drawn and no human figure is marked.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "9264b9dc-a5f7-44e5-8956-5e45e3269681"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1311-hand-gripping-plain-cup/hand-gripping-plain-cup_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 27                  # cup axis
RIM_Y, RIM_HALF = 6, 10    # rim (17,6)-(37,6)
TOP, BOTTOM = 20, 30       # hand band edges across the cup
WALL_HALF = 9              # wall half-width where it meets the hand top
BOWL_HALF = 8              # bowl half-width where it leaves the hand bottom
BASE_Y, BASE_HALF = 42, 4  # flat base (23,42)-(31,42)
HOOK_R = (BOTTOM - TOP) // 2
HOOK_C = (42 - HOOK_R, TOP + HOOK_R)   # (37,25): tip on the x=42 extreme
ARM_X, ARM_TOP, ARM_BOTTOM = 6, 23, 32


def mirror(p):
    return (2 * AXIS - p[0], p[1])


class HandGrippingPlainCupRedraw(Solo48):
    icon_id = "hand-gripping-plain-cup-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/drink"
    aliases = ("hand holding cup", "holding a glass", "hand gripping tumbler")
    keywords = ("hand", "cup", "glass", "tumbler", "drink", "hold", "grip",
                "beverage", "water", "serve")

    def build(self) -> None:
        wall_l = (AXIS - WALL_HALF, TOP)
        wall_r = mirror(wall_l)
        bowl_l = (AXIS - BOWL_HALF, BOTTOM)
        bowl_r = mirror(bowl_l)
        hx, hy = HOOK_C

        # Cup above the hand: walls, rim.
        self.add_polyline("cup-top", wall_l, (AXIS - RIM_HALF, RIM_Y),
                          (AXIS + RIM_HALF, RIM_Y), wall_r)

        # Cup below the hand: taper-following sides into a flat base.
        base_l = (AXIS - BASE_HALF, BASE_Y)
        seg_l = ((bowl_l[0] + 0.4, bowl_l[1] + 6), (bowl_l[0] + 0.8, BASE_Y), base_l)
        self.add_bezier("bowl-left", bowl_l, seg_l)
        self.add_line("bowl-base", base_l, mirror(base_l))
        c1, c2, _ = seg_l
        self.add_bezier("bowl-right", mirror(base_l),
                        (mirror(c2), mirror(c1), bowl_r))
        self.add_contour("cup-bowl", "bowl-left", "bowl-base", "bowl-right")

        # Hand: forearm top, back of hand, band across the cup, hook, return.
        self.add_line("arm-top", (ARM_X, ARM_TOP), (8, ARM_TOP))
        self.add_bezier("hand-back", (8, ARM_TOP),
                        ((11, ARM_TOP), (13, TOP), (16, TOP)))
        self.add_line("band-top-1", (16, TOP), wall_l)
        self.add_line("band-top-2", wall_l, wall_r)
        self.add_line("band-top-3", wall_r, (hx, TOP))
        self.add_arc("hook-1", (hx, TOP), (hx + HOOK_R, hy), radius_x=HOOK_R, sweep=True)
        self.add_arc("hook-2", (hx + HOOK_R, hy), (hx, BOTTOM), radius_x=HOOK_R, sweep=True)
        self.add_line("band-bottom-1", (hx, BOTTOM), bowl_r)
        self.add_line("band-bottom-2", bowl_r, bowl_l)
        self.add_line("band-bottom-3", bowl_l, (18, BOTTOM))
        self.add_bezier("wrist", (18, BOTTOM),
                        ((15, BOTTOM), (14, ARM_BOTTOM), (11, ARM_BOTTOM)))
        self.add_line("arm-bottom", (11, ARM_BOTTOM), (ARM_X, ARM_BOTTOM))
        self.add_contour("hand", "arm-top", "hand-back", "band-top-1", "band-top-2",
                         "band-top-3", "hook-1", "hook-2", "band-bottom-1",
                         "band-bottom-2", "band-bottom-3", "wrist", "arm-bottom")

        self.relate("connect", "hand", "cup-top")
        self.relate("connect", "hand", "cup-bowl")
