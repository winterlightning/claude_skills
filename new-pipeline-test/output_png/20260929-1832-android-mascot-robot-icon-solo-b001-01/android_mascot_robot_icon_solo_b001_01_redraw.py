"""android-mascot-robot-icon-solo-b001-01 (redraw of the new-pipeline traced SVG).

Plan: the Android robot mascot, front view, mirrored about x=24 on VRECT_L
(centerline box (8,4)-(40,44)).
- head: a detached closed dome, 16 wide and 9 tall, flat base y=15 from
  x=16 to x=32. Each half of the dome is two cubics through an integer
  shoulder node (18,9)/(30,9) on the rx8/ry9 ellipse about (24,15), with
  the ellipse tangent there, so the dome is tangent-continuous from the
  vertical sides to the flat crown at (24,6). (An 8-tall dome failed the
  build gate's internal spacing: the crown ran 6.8 above the base.)
- antennae: two short lines leaving the shoulder nodes outward to the top
  edge, (18,9)->(15,4) and (30,9)->(33,4), sharing the node with the dome.
- body: a closed rounded rectangle x 16..32, y 23..38 (r2 top corners, r4
  bottom corners), 8 below the head base (the head-to-body gap).
- legs: two lines x=20 and x=28 from the body base (the ends of the r4
  corner arcs, shared nodes) down to y=44; 8 apart, so the crotch reads.
- arms: two detached lines x=8 and x=40, y 25..35, 8 from the body walls.
  At stroke 4 a round-capped line paints the capsule arm of the image.

Keyshape: the metrics suggest SQUARE (score 1.12, from the "square" hint),
but SQUARE needs a 1.16 x-stretch; VRECT_L fills x exactly and needs only
1.08 on y, so the mascot keeps its proportions. VRECT_L is used: arms on
x=8/x=40, antenna tips on y=4, feet on y=44.

Metric issues fixed:
- stroke-width (info): drawn at stroke 4; every gap is sized for it.
- stroke-count (warn, 8 vs 6): 6 strokes now (head, 2 antennae, body with
  legs, 2 arms); the eyes were dropped (see below).
- keyshape-short-axis (warn): moot on VRECT_L; the arms reach x=8/x=40.
- clearance e0/e7 (head/body, 1.97): the head base sits 8 above the body.
- clearance e0/e5, e0/e6, e5/e7, e6/e7 (arms, 2.4-3.8): the arms are 8
  from the body walls and >= 10 from the head corners.
- clearance e0/e3, e0/e4, e1/e3, e2/e4, e3/e7, e4/e7 (eyes): resolved by
  dropping the eyes.
- hole (error, head interior 5.0): the dome is 16 x 9 on centerlines, its
  inscribed opening about 9 on centerlines.
Not fixed (dropped instead): the two eyes. Two eyes 8 apart and 8 from a
dome and its base need a head about 25 wide and 17 tall; with the arms
and the 8-unit head gap the canvas leaves a 16 x 9 head. The source
primitive (pictographic-primitives/apps/android_5a895be7...) has no eyes
either, and the antennae + dome + arms carry the identity.
Legs are round-capped lines instead of the image's hollow U legs: two
hollow legs and the crotch need a 24-wide body base, the body is 16.

Lucide: no Android mascot in the local bundle; Lucide `bot` informed the
antenna leaving the head outline and the flat head base.
Traced shape: 20260929-1832-android-mascot-robot-icon-solo-b001-01/
android-mascot-robot-icon-solo-b001-01_raw.svg
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5a895be7-0613-57bb-9e1f-038063cbd8b8"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1832-android-mascot-robot-icon-solo-b001-01/"
    "android-mascot-robot-icon-solo-b001-01_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
HEAD_HALF = 8            # head x 16..32
HEAD_BASE, HEAD_TOP = 15, 6
SHOULDER = (18, 9)       # left dome node, on the rx8/ry9 ellipse about (24,15)
TAN = (0.8, -1.0)        # its tangent (ellipse normal (6/64, 6/81) turned)
SIDE_K, CROWN_K = 2.5, 2.4   # handles at the base corners and the crown
ANTENNA_TIP = (15, 4)
BODY_TOP, BODY_BOTTOM = 23, 38
TOP_R, BOTTOM_R = 2, 4
LEG_X, FOOT_Y = 20, 44   # left leg; right mirrors
ARM_X, ARM_TOP, ARM_BOTTOM = 8, 25, 35


def mx(x):
    return 2 * AXIS - x


class AndroidMascotRobotIconSoloB00101Redraw(Solo48):
    icon_id = "android-mascot-robot-icon-solo-b001-01-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "apps"
    aliases = ("android", "android-robot", "android-mascot")
    keywords = ("android", "robot", "mascot", "antenna", "mobile", "os")

    def build(self) -> None:
        hl, hr = AXIS - HEAD_HALF, AXIS + HEAD_HALF
        sx, sy = SHOULDER
        crown = (AXIS, HEAD_TOP)

        # Head: dome left -> right, then the flat base back.
        tx, ty = TAN
        self.add_bezier("dome-l1", (hl, HEAD_BASE),
                        ((hl, HEAD_BASE - SIDE_K), (sx - tx, sy - ty), SHOULDER))
        self.add_bezier("dome-l2", SHOULDER,
                        ((sx + 2 * tx, sy + 2 * ty), (AXIS - CROWN_K, HEAD_TOP), crown))
        self.add_bezier("dome-r2", crown,
                        ((AXIS + CROWN_K, HEAD_TOP), (mx(sx) - 2 * tx, sy + 2 * ty), (mx(sx), sy)))
        self.add_bezier("dome-r1", (mx(sx), sy),
                        ((mx(sx) + tx, sy - ty), (hr, HEAD_BASE - SIDE_K), (hr, HEAD_BASE)))
        self.add_line("head-base", (hr, HEAD_BASE), (hl, HEAD_BASE))
        self.add_contour("head", "dome-l1", "dome-l2", "dome-r2", "dome-r1",
                         "head-base", closed=True)

        self.add_line("antenna-left", SHOULDER, ANTENNA_TIP)
        self.add_line("antenna-right", (mx(sx), sy), (mx(ANTENNA_TIP[0]), ANTENNA_TIP[1]))
        self.relate("connect", "antenna-left", "head")
        self.relate("connect", "antenna-right", "head")

        # Body: clockwise from the top-left corner.
        bl, br = hl, hr
        self.add_line("body-top", (bl + TOP_R, BODY_TOP), (br - TOP_R, BODY_TOP))
        self.add_arc("corner-tr", (br - TOP_R, BODY_TOP), (br, BODY_TOP + TOP_R),
                     radius_x=TOP_R)
        self.add_line("wall-right", (br, BODY_TOP + TOP_R), (br, BODY_BOTTOM - BOTTOM_R))
        self.add_arc("corner-br", (br, BODY_BOTTOM - BOTTOM_R), (br - BOTTOM_R, BODY_BOTTOM),
                     radius_x=BOTTOM_R)
        self.add_line("body-base", (br - BOTTOM_R, BODY_BOTTOM), (bl + BOTTOM_R, BODY_BOTTOM))
        self.add_arc("corner-bl", (bl + BOTTOM_R, BODY_BOTTOM), (bl, BODY_BOTTOM - BOTTOM_R),
                     radius_x=BOTTOM_R)
        self.add_line("wall-left", (bl, BODY_BOTTOM - BOTTOM_R), (bl, BODY_TOP + TOP_R))
        self.add_arc("corner-tl", (bl, BODY_TOP + TOP_R), (bl + TOP_R, BODY_TOP),
                     radius_x=TOP_R)
        self.add_contour("body", "body-top", "corner-tr", "wall-right", "corner-br",
                         "body-base", "corner-bl", "wall-left", "corner-tl", closed=True)

        # Legs hang from the ends of the body base (shared nodes).
        self.add_line("leg-left", (LEG_X, BODY_BOTTOM), (LEG_X, FOOT_Y))
        self.add_line("leg-right", (mx(LEG_X), BODY_BOTTOM), (mx(LEG_X), FOOT_Y))
        self.relate("connect", "leg-left", "body")
        self.relate("connect", "leg-right", "body")

        # Detached arms.
        self.add_line("arm-left", (ARM_X, ARM_TOP), (ARM_X, ARM_BOTTOM))
        self.add_line("arm-right", (mx(ARM_X), ARM_TOP), (mx(ARM_X), ARM_BOTTOM))
