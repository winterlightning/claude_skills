"""hand-pointing-up (redraw of the new-pipeline traced SVG).

Plan: a front-view hand raises its index finger straight up; the other
fingers fold down on the right and the thumb crosses the palm diagonally
toward the finger base, as in the generated image. Authored on VRECT_M (the
suggested keyshape), centerline box (10,4)-(38,44).
- index finger: band x 14..22 (8, like Lucide `pointer` doubled), r4 round
  tip about (18,8) reaching the top y=4.
- folded fingers: the image's three knuckles need 3 x 8 = 24 of width but only
  16 remains right of the finger, so they are reduced to two r4 knuckle arcs
  (x 22..30 and 30..38), staggered 3 lower to the right; the lower knuckle
  rises from the foot of the higher one's short separator (Lucide `pointer`
  knuckle construction).
- palm: straight pinky side x=38, r8 corners about (30,36) and (18,36) to the
  flat base y=44, short left wall x=10.
- thumb: a tube of half-width 5 on a 3-4-5 slope (direction (-4,3)), r5 round
  tip about (21,29); its upper edge runs from the palm's left wall through the
  index finger's left wall (the finger ends there) to the tip; its lower edge
  is left open one step into the palm, as in the image.
The outline is standalone primitives chained with connect.

Metric issues fixed:
- clearance e0/e1, e1/e2 (knuckle arcs 5.25 from the finger wall): the knuckles
  now share the finger wall's endpoint and are connected.
- clearance e2/e4, e3/e4 (separators 2.6-2.8 from the thumb): the separator is
  a short jog ending at y=19, 8.4 from the thumb tip; the tip is 8.04 from the
  finger/knuckle joint.
- loose-join e0/e3, e2/e3: every join is a shared grid endpoint with
  relate("connect").
- hole at (18.8,6.9), 1.6 wide (the pinched fingertip): the finger band is 8
  wide with an r4 tip; the finger interior opens into the palm.
- hole at (24.2,21.3), 1.2 wide (knuckle sliver): gone; the only enclosed
  region is the open palm interior.
- keyshape-short-axis: every extreme sits on the VRECT_M box (x 10/38,
  y 4/44).
- stroke-width (info): redrawn at stroke 4 with every gap budgeted at 8.
"""
import math

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6c5ced19-9a99-46fd-9dda-dfd6ad80f1a9"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1525-hand-pointing-up/hand-pointing-up_raw.svg"
AUTHOR = "claude-opus-5-5"

FINGER_L, FINGER_R, TOP = 14, 22, 4    # index finger band, r4 round tip
KNUCKLE_1_Y, KNUCKLE_2_Y = 16, 19      # folded-finger arcs, r4, staggered
PINKY_X = 38
PALM_L, PALM_B, PALM_R = 10, 44, 8     # palm left wall, bottom, r8 corners
THUMB_TIP = (21, 29)                   # thumb tip centre, r5 round tip
THUMB_DIR = (-4, 3)                    # thumb runs down-left on a 3-4-5 slope
THUMB_N = (3, 4)                       # tube half-width 5 (normal to THUMB_DIR)


class HandPointingUpRedraw(Solo48):
    icon_id = "hand-pointing-up-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "wayfinding"
    aliases = ("finger point", "index finger up", "raised index finger")
    keywords = ("hand", "pointing", "up", "index", "finger", "gesture", "pointer")

    def build(self) -> None:
        tx, ty = THUMB_TIP
        (dx, dy), (nx, ny) = THUMB_DIR, THUMB_N
        tip_r = (FINGER_R - FINGER_L) // 2
        k = FINGER_R - FINGER_L  # folded finger width = index finger width
        top_edge = (tx - nx, ty - ny)                    # thumb upper edge at the tip
        low_edge = (tx + nx, ty + ny)                    # thumb lower edge at the tip
        wall_join = (top_edge[0] + dx, top_edge[1] + dy)  # thumb top crosses the finger wall
        palm_join = (wall_join[0] + dx, wall_join[1] + dy)
        assert wall_join[0] == FINGER_L and palm_join[0] == PALM_L
        side_y = PALM_B - PALM_R

        self.add_line("finger-left", wall_join, (FINGER_L, TOP + tip_r))
        self.add_arc("fingertip", (FINGER_L, TOP + tip_r), (FINGER_R, TOP + tip_r), radius_x=tip_r, sweep=True)
        self.add_line("finger-right", (FINGER_R, TOP + tip_r), (FINGER_R, KNUCKLE_1_Y))
        self.add_arc("knuckle-1", (FINGER_R, KNUCKLE_1_Y), (FINGER_R + k, KNUCKLE_1_Y), radius_x=k // 2, sweep=True)
        self.add_line("separator", (FINGER_R + k, KNUCKLE_1_Y), (FINGER_R + k, KNUCKLE_2_Y))
        self.add_arc("knuckle-2", (FINGER_R + k, KNUCKLE_2_Y), (PINKY_X, KNUCKLE_2_Y), radius_x=k // 2, sweep=True)
        self.add_line("pinky", (PINKY_X, KNUCKLE_2_Y), (PINKY_X, side_y))
        self.add_arc("palm-right", (PINKY_X, side_y), (PINKY_X - PALM_R, PALM_B), radius_x=PALM_R, sweep=True)
        self.add_line("palm-bottom", (PINKY_X - PALM_R, PALM_B), (PALM_L + PALM_R, PALM_B))
        self.add_arc("palm-left", (PALM_L + PALM_R, PALM_B), (PALM_L, side_y), radius_x=PALM_R, sweep=True)
        self.add_line("palm-wall", (PALM_L, side_y), palm_join)
        self.add_line("thumb-back", palm_join, wall_join)
        self.add_line("thumb-top", wall_join, top_edge)
        self.add_arc("thumb-tip", top_edge, low_edge, radius_x=math.isqrt(nx * nx + ny * ny), sweep=True)
        self.add_line("thumb-low", low_edge, (low_edge[0] + dx, low_edge[1] + dy))
        chain = ["finger-left", "fingertip", "finger-right", "knuckle-1", "separator", "knuckle-2", "pinky",
                 "palm-right", "palm-bottom", "palm-left", "palm-wall", "thumb-back", "finger-left"]
        for a, b in zip(chain, chain[1:]):
            self.relate("connect", a, b)
        for a, b in (("thumb-back", "thumb-top"), ("finger-left", "thumb-top"),
                     ("thumb-top", "thumb-tip"), ("thumb-tip", "thumb-low")):
            self.relate("connect", a, b)
