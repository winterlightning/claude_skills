"""bowl-with-raised-chopsticks (redraw of the new-pipeline traced SVG).

Plan: a wide shallow bowl in the lower half and a pair of parallel
chopsticks rising to the upper right above it, on SQUARE (centerline box
(6,6)-(42,42)), as the metrics suggested (fill 1.0 x 1.0).
- bowl: one closed contour, flat rim (6,29)-(42,29) and a half-ellipse
  rx 18 / ry 13 centred on (24,29) whose apex is the y=42 extreme; the
  rim ends are the x=6 / x=42 extremes. Interior 36x13, one clear hole.
- chopsticks: two equal lines on a 1:3 rise, length 3t x t with t=7:
  upper (16,13)->(37,6) touches the y=6 extreme, lower is the upper shifted
  by (5,7): (21,20)->(42,13), ending on the x=42 extreme. |5+3*7|/sqrt(10)
  = 8.22 between centerlines, and the 2.5 along-stick stagger keeps the
  lower stick a little to the right, as in the generated image.
- the lower stick's low tip (21,20) sits 9 above the rim (an exact 8 comes
  back as a validator review); the upper tip (16,13) is 16 above it.
The image's ~1:2 slope is flattened to 1:3: in the 15-unit band above the
rim, two 1:2 sticks 8 apart could only be 15.6 long; at 1:3 they are 22.
No Lucide match (Lucide has no chopsticks/bowl pair); only its plain
flat-rim soup-bowl idea was used.

Metric issues (bowl-with-raised-chopsticks_metrics.json):
- clearance e0/e1 (sticks 3.02 apart): fixed -- 8.22 on centerlines.
- clearance e0/e2 (7.16) and e1/e2 (4.32), sticks vs rim: fixed -- the rim
  drops to y=29 and the lowest stick point is y=20 (9 apart).
- stroke-width (trace 2.77 after fitting): redrawn at stroke 4.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "77a9a077-f1dd-4bee-b3cd-ef26744fdd63"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1842-bowl-with-raised-chopsticks/bowl-with-raised-chopsticks_raw.svg"
AUTHOR = "claude-opus-5-5"

RIM_Y = 29
BOWL_LEFT, BOWL_RIGHT = 6, 42
BOWL_RX, BOWL_RY = 18, 13                  # apex at y=42
STICK_START = (16, 13)
STICK_RISE = 7                             # 1:3 run, 21 across, 7 up
STICK_OFFSET = (5, 7)                      # 8.22 between centerlines


class BowlWithRaisedChopsticksRedraw(Solo48):
    icon_id = "bowl-with-raised-chopsticks-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ("rice bowl", "noodle bowl", "chopsticks and bowl")
    keywords = ("bowl", "chopsticks", "rice", "noodles", "ramen", "asian food", "meal", "eat")

    def build(self) -> None:
        # Bowl: flat rim and a half-ellipse below it, one closed contour.
        self.add_line("rim", (BOWL_LEFT, RIM_Y), (BOWL_RIGHT, RIM_Y))
        self.add_arc("basin", (BOWL_RIGHT, RIM_Y), (BOWL_LEFT, RIM_Y),
                     radius_x=BOWL_RX, radius_y=BOWL_RY, sweep=True)
        self.add_contour("bowl", "rim", "basin", closed=True)

        # Chopsticks: one stick definition, the second shifted by STICK_OFFSET.
        x, y = STICK_START
        dx, dy = STICK_OFFSET
        top = (x + 3 * STICK_RISE, y - STICK_RISE)
        self.add_line("chopstick-upper", STICK_START, top)
        self.add_line("chopstick-lower", (x + dx, y + dy), (top[0] + dx, top[1] + dy))
