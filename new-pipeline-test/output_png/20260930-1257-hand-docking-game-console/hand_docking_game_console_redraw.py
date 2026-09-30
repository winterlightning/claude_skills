"""hand-docking-game-console (redraw of the new-pipeline traced SVG).

Plan: three stacked parts on VRECT_L (centerline box (8,4)-(40,44)), mirrored
about x=24 except the arm, which is deliberately off-axis (it reaches in from
the upper left).
- arm: one open bent stroke entering from the left edge. The forearm runs
  level along the top edge y=4 (exactly 8 above the console) and the wrist
  drops at 45 deg to press the console lid at (25,12); the press point is a
  shared node on the lid, declared connect, so the hand is shown pushing the
  console into the dock. (A sloped forearm would sit under 8 from the lid.)
- console: an r4 rounded rectangle, full width x 8..40, y 12..34, built as
  four joined contours (straight lid, straight base, two rounded ends) so the
  plus's exact 8 to lid and base certifies. The 22 height is the minimum that
  holds a 6-tall plus 8 from both walls.
- plus (D-pad): two 6-long strokes crossing at (20,23), 9 from the left wall
  and 8 from lid and base. button: a dot at (31,23), 9 from the right wall
  and 8 from the plus.
- cradle: an open U tray under the console, x 10..38, ends y=42 (8 below the
  lid's bottom corners), r2 corners onto the floor y=44.
Extremes: x 8/40 (console walls), y 4 (forearm), y 44 (cradle floor).

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4; every gap re-budgeted for it.
- keyshape-short-axis: HRECT_L (32 tall) cannot stack arm + 22-tall console +
  8 gap + cradle; VRECT_L (40 tall) can, and all four extremes sit on its box.
  The generated image was square (aspect 1.0), not wide, as choice.json warned.
- clearance e0/e1 (arm end 2.35 above the console): the arm now touches the
  lid at one shared node, declared connect, and its level run is 8 above it.
- clearance e1/e2, e1/e3 (plus 2.9 from the console walls), e1/e4 (ring 2.9
  from the right wall): plus and button sit 8-9 from every wall.
- clearance e2/e3 (0.0): the two plus strokes are one declared crossing.
- clearance e1/e5, e2/e5, e3/e5, e4/e5 (cradle 2-7 from console and plus): the
  cradle ends are 8.2 from the console corners, and the plus/button are
  inside the console, far from the cradle.
- holes (10.6,25.5), (10.6,30.7) 1.2-1.4 wide: slivers between the plus and
  the wall, gone with the 8 spacing. hole (13.6,36.6) 2.6 wide: the
  console/cradle pocket, now open (the cradle no longer touches the console).
Not fixed / changed on purpose:
- the hollow round button became a dot: an r3 ring needs its centre 11 from
  the right wall and 11 from the plus end, which the 32-wide console lacks.
- no-head (warn): the subject is an isolated arm by brief (no head, torso or
  hand circle), so no human figure is marked; not a defect.
Lucide: `gamepad` / `gamepad-2` (plus at left, round button at right inside a
rounded body) informed the console; no docking/hand match exists.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "fb11a30f-fb1c-4930-9aae-280bc7d071fc"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1257-hand-docking-game-console/hand-docking-game-console_raw.svg"
AUTHOR = "claude-opus-5-5"

LEFT, RIGHT = 8, 40                  # console walls
TOP, BOTTOM = 12, 34                 # console lid / base
R = 4                                # console corner radius
MID_Y = (TOP + BOTTOM) // 2          # 23: row of the plus and the button
PLUS_X, PLUS_H = 20, 3               # plus centre x, half arm length
BUTTON_X = 31
PRESS = (25, TOP)                    # wrist meets the lid here
CRADLE_L, CRADLE_R, CRADLE_TOP, FLOOR, CR = 10, 38, 42, 44, 2


class HandDockingGameConsoleRedraw(Solo48):
    icon_id = "hand-docking-game-console-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("dock game console", "console docking")
    keywords = ("hand", "game console", "dock", "docking station", "gaming",
                "handheld", "controller", "insert", "cradle")

    def build(self) -> None:
        # Arm: level forearm along the top, wrist dropping onto the lid.
        self.add_polyline("arm", (LEFT, 4), (17, 4), PRESS)

        # Console body, clockwise from the press point on the lid.
        self.add_line("lid-r", PRESS, (RIGHT - R, TOP))
        self.add_arc("corner-tr", (RIGHT - R, TOP), (RIGHT, TOP + R), radius_x=R)
        self.add_line("wall-r", (RIGHT, TOP + R), (RIGHT, BOTTOM - R))
        self.add_arc("corner-br", (RIGHT, BOTTOM - R), (RIGHT - R, BOTTOM), radius_x=R)
        self.add_line("base", (RIGHT - R, BOTTOM), (LEFT + R, BOTTOM))
        self.add_arc("corner-bl", (LEFT + R, BOTTOM), (LEFT, BOTTOM - R), radius_x=R)
        self.add_line("wall-l", (LEFT, BOTTOM - R), (LEFT, TOP + R))
        self.add_arc("corner-tl", (LEFT, TOP + R), (LEFT + R, TOP), radius_x=R)
        self.add_line("lid-l", (LEFT + R, TOP), PRESS)
        # The lid and base stay straight-only runs (the plus sits exactly 8
        # from them, which certifies only against straight contours); the two
        # rounded ends are their own contours, joined at shared nodes.
        self.add_contour("lid", "lid-l", "lid-r")
        self.add_contour("end-r", "corner-tr", "wall-r", "corner-br")
        self.add_contour("end-l", "corner-bl", "wall-l", "corner-tl")
        for a, b in (("lid", "end-r"), ("end-r", "base"), ("base", "end-l"),
                     ("end-l", "lid"), ("arm", "lid")):
            self.relate("connect", a, b)

        # Controls: plus at left, one button at right, on the console's mid row.
        self.add_line("plus-h", (PLUS_X - PLUS_H, MID_Y), (PLUS_X + PLUS_H, MID_Y))
        self.add_line("plus-v", (PLUS_X, MID_Y - PLUS_H), (PLUS_X, MID_Y + PLUS_H))
        self.relate("connect", "plus-h", "plus-v")
        self.add_dot("button", (BUTTON_X, MID_Y))

        # Cradle: open U tray below the console.
        self.add_arc("cradle-l", (CRADLE_L, CRADLE_TOP), (CRADLE_L + CR, FLOOR),
                     radius_x=CR, sweep=False)
        self.add_line("cradle-floor", (CRADLE_L + CR, FLOOR), (CRADLE_R - CR, FLOOR))
        self.add_arc("cradle-r", (CRADLE_R - CR, FLOOR), (CRADLE_R, CRADLE_TOP),
                     radius_x=CR, sweep=False)
        self.add_contour("cradle", "cradle-l", "cradle-floor", "cradle-r")
