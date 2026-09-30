"""cord sling and stone (redraw of the new-pipeline traced SVG).

Subject: a shepherd's sling -- a shallow oval pouch at the bottom, two cords
rising from its ends (a finger loop on the left cord's tip, the right cord's
tip free) and a round stone floating above the pouch between the cords.

Plan: VRECT_L, centerline box (8,4)-(40,44).
Extremes: x=8 the finger loop's left side, x=40 the right cord (and the
pouch's right tip), y=4 the loop's top, y=44 the pouch bottom.
- pouch: closed half-ellipse, a straight rim (14,34)-(40,34) and one arc
  (rx 13, ry 10, centre (27,34)) under it; 10 tall on centerlines.
- cords: each leaves a pouch tip vertically, so the cord runs tangent into
  the pouch's lower arc (one smooth U) while meeting the rim at 90 degrees.
  Right cord: straight to a round tip at (40,10). Left cord: one cubic that
  eases 1 unit left to the loop's bottom point (13,14).
- finger loop: r5 ring about (13,9), split at its bottom where the cord joins.
- stone: r4 ring about (27,21), on the pouch's axis x=27.
Budget: stone to rim 9, to right cord 9, to left cord 10, to loop 9.4.
References: generated PNG read for the subject only (oval pouch, two cords,
loop on the left, stone between). No useful Lucide sling exists; the build
follows Lucide's single-stroke construction (one line per cord, rings for
round parts). No trace coordinates copied.

Keyshape: VRECT_L as suggested (score 1.18, the only candidate with x fill
100%); all four extremes now sit on the box.

Metric issues:
- stroke-width (info): redrawn at stroke 4; every gap budgeted for it.
- keyshape-short-axis (y fill 93%): fixed; the loop top is y=4 and the pouch
  bottom y=44.
- clearance e0/e1, e1/e2 (1.73, the trace's doubled pouch rim and the cords
  crossing at the right pouch tip): fixed; each cord and the rim/arc now meet
  at one shared tip node, declared connected, no overlap.
- clearance e0/e4 (2.86, stone resting on the rim), e1/e4 (6.91), e2/e4 and
  e3/e4 (7.01): fixed; the stone sits 9 above the rim and 9-10 from each cord.
- hole [11.3,8.8] (2.63, the pinched teardrop loop): fixed; the loop is a
  round r5 ring (6 of ink inside).
- hole [23.8,39.6] (1.8, the thin pouch): fixed; the pouch is 10 tall on
  centerlines (6 of ink inside).
- hole [25.0,29.8] (4.04, inside the stone): partly; the stone is an r4 ring,
  4 of ink inside. An r5 stone would sit exactly 8 from the rim and the
  right cord (curve-to-line at the minimum is not certified) and 8.4 from the
  loop, so it cannot fit in the 32x40 box; r4 passes the build hole gate
  (1-unit-stroke inscribed radius 3.5 >= 2.5).
Dropped: the teardrop pinch of the loop (a closed pinch leaves a sliver hole)
and the slight upward arch of the pouch rim.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "feb59830-d1d6-5f9b-bea2-7f92cbc04249"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1039-cord-sling-and-stone/cord-sling-and-stone_raw.svg"
AUTHOR = "claude-opus-5-5"

PL, PR, PCX, PY = 14, 40, 27, 34  # pouch tips (PL,PY)/(PR,PY), axis x=PCX
PRY = 10                          # pouch depth: bottom at y=44
LOOP, LR = (13, 9), 5             # finger loop ring
STONE, SR = (PCX, 21), 4          # stone ring on the pouch axis
TIP_Y = 10                        # right cord's free tip


class CordSlingAndStoneRedraw(Solo48):
    icon_id = "cord-sling-and-stone-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weapons"
    aliases = ("sling", "slingshot sling", "shepherd sling")
    keywords = ("sling", "stone", "cord", "pouch", "david", "weapon", "throw", "ancient")

    def build(self) -> None:
        # Pouch: straight rim over a half-ellipse, closed at the two tips.
        left, right = (PL, PY), (PR, PY)
        self.add_line("pouch-rim", left, right)
        self.add_arc("pouch-bottom", right, left,
                     radius_x=(PR - PL) // 2, radius_y=PRY, sweep=True)
        self.add_contour("pouch", "pouch-rim", "pouch-bottom", closed=True)

        # Cords: vertical at the tips, tangent into the pouch arc.
        self.add_line("cord-right", right, (PR, TIP_Y))
        lx, ly = LOOP
        loop_bottom = (lx, ly + LR)
        self.add_bezier("cord-left", left, ((PL, 26), (lx, 22), loop_bottom))
        for cord in ("cord-left", "cord-right"):
            self.relate("connect", cord, "pouch-rim")
            self.relate("connect", cord, "pouch-bottom")

        # Finger loop: ring split at the bottom where the cord ends.
        loop_top = (lx, ly - LR)
        self.add_arc("loop-left", loop_bottom, loop_top, radius_x=LR, sweep=True)
        self.add_arc("loop-right", loop_top, loop_bottom, radius_x=LR, sweep=True)
        self.add_contour("loop", "loop-left", "loop-right", closed=True)
        self.relate("connect", "cord-left", "loop-left")
        self.relate("connect", "cord-left", "loop-right")

        # Stone: free ring above the pouch.
        sx, sy = STONE
        self.add_arc("stone-top", (sx - SR, sy), (sx + SR, sy), radius_x=SR, sweep=True)
        self.add_arc("stone-bottom", (sx + SR, sy), (sx - SR, sy), radius_x=SR, sweep=True)
        self.add_contour("stone", "stone-top", "stone-bottom", closed=True)
