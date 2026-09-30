"""furby-toy (redraw of the new-pipeline traced SVG).

Plan: a front-view Furby on VRECT_L (centerline box (8,4)-(40,44)), mirrored
exactly across x=24; the right half is authored and the left is its mirror.
- body: one closed outline. A flat crown arc (r17 about (24,25), 8-15-17 ends
  (16,10)/(32,10), apex y=8) runs into two tall ears whose tips (8,4)/(40,4)
  set the top and side extremes. Each ear's outer edge drops to a notch at
  (10,15)/(38,15), the side bulges back out to x=8/40 at y=27, then tucks into
  a second notch at (13,38)/(35,38) above an r3 foot lobe. The outline runs
  open from foot to foot; the belly (13,44)-(35,44) is a standalone straight
  line connected to both foot ends.
- eyes: two tangent r3 rings about (21,21) and (27,21), joined at (24,21)
  (the exempt 6-diameter circle; declared connect). Real Furby eyes sit close
  together, and this is the only eye pair that fits the 32-wide body.
- beak: an open V (21,33)-(24,36)-(27,33) under the eye junction.
Extremes: x 8 / 40 (ear tips and y=27 side bulges), y 4 (ear tips) / 44 (feet
and belly).

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4; every gap re-budgeted for it.
- keyshape-short-axis: ear tips now reach y=4 and the feet y=44, so both VRECT_L
  y extremes sit on the box (the trace filled 92%).
- clearance e0/e1, e0/e2 (eyes 4 from the ear notches): notches moved out to
  x=10/38 at y=15, 9.5 from the eye rings; the crown sits 9+ above them.
- clearance e1/e2 (eyes 2.5 apart): the eyes now touch at one shared node,
  declared connect, instead of hovering short of each other.
- clearance e1/e3, e2/e3 (beak 1.8 from the eyes): the beak's top corners are
  9 from the rings and its apex exactly 8 above the belly. The belly is
  split out of the arc outline so that exact 8 certifies straight-to-straight.
- hole (13.4,12.8) 5.6 wide (left ear pocket): the ear interior is now open to
  the body (no inner ear line), so no pocket is sealed.
- holes (18.6,22.4)/(29.3,22.4) 4.1 wide (eye interiors): r5 hollow eyes need
  20 + 2x9 = 38 of width, which VRECT_L (32) cannot give; the eyes became r3
  rings, the 6-diameter circle the hole gate exempts. Eye size is the one
  deliberate loss against the generated image.
- the traced closed beak triangle (a 2-unit hole at stroke 4) is an open V.
  Tried: a 4-wide V (reads as a heart at 48 px) and a T wedge (reads as a dog
  nose); the 6-wide V reads as a beak.
Lucide: no Furby exists; the construction follows Lucide `cat`/`rabbit`
(ears as tall strokes meeting a crown, a single closed head outline).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "c8ed2a82-660e-4fb3-97c4-3f6f0a34445d"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1253-furby-toy/furby-toy_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
EYE_Y, EYE_R, EYE_DX = 21, 3, 3      # tangent rings about (24 -+ 3, 21)
CROWN_R, CROWN_Y = 17, 10            # crown arc ends (16,10)/(32,10), apex 8
FOOT_R = 3                           # foot lobes about (13,41)/(35,41)
BOTTOM = 44
BEAK_L, BEAK_TIP = (21, 33), (AXIS, 36)   # open V: 9 below the rings, 8 above the belly


def m(p):
    """Mirror a point (or bezier control) across the axis."""
    return (2 * AXIS - p[0], p[1])


# Right half of the outline, from the crown end down to the belly.
EAR_BASE, EAR_TIP, NOTCH = (32, CROWN_Y), (40, 4), (38, 15)
BULGE, FOOT_TOP = (40, 27), (35, 38)
FOOT_OUT, FOOT_BOTTOM = (35 + FOOT_R, 41), (35, BOTTOM)
EAR_INNER = ((33.5, 6.5), (36.5, 4.5), EAR_TIP)
EAR_OUTER = ((40, 8), (40, 12.5), NOTCH)
SIDE = (((39.2, 18), (40, 22.5), BULGE), ((40, 31.5), (38.5, 35.5), FOOT_TOP))


class FurbyToyRedraw(Solo48):
    icon_id = "furby-toy-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/toy"
    aliases = ("furby",)
    keywords = ("furby", "toy", "electronic pet", "plush", "robot pet", "owl", "gremlin")

    def build(self) -> None:
        # Body, clockwise: crown, right ear and side, belly, left side and ear.
        self.add_arc("crown", m(EAR_BASE), EAR_BASE, radius_x=CROWN_R)
        self.add_bezier("ear-r-inner", EAR_BASE, EAR_INNER)
        self.add_bezier("ear-r-outer", EAR_TIP, EAR_OUTER)
        self.add_bezier("side-r", NOTCH, *SIDE)
        self.add_arc("foot-r-top", FOOT_TOP, FOOT_OUT, radius_x=FOOT_R)
        self.add_arc("foot-r-bottom", FOOT_OUT, FOOT_BOTTOM, radius_x=FOOT_R)
        self.add_line("belly", FOOT_BOTTOM, m(FOOT_BOTTOM))
        self.add_arc("foot-l-bottom", m(FOOT_BOTTOM), m(FOOT_OUT), radius_x=FOOT_R)
        self.add_arc("foot-l-top", m(FOOT_OUT), m(FOOT_TOP), radius_x=FOOT_R)
        # Mirrored runs are reversed: walk the right half's segments backwards.
        side_pts = [NOTCH] + [s[2] for s in SIDE]
        self.add_bezier("side-l", m(FOOT_TOP), *[
            (m(SIDE[i][1]), m(SIDE[i][0]), m(side_pts[i])) for i in (1, 0)])
        self.add_bezier("ear-l-outer", m(NOTCH), (m(EAR_OUTER[1]), m(EAR_OUTER[0]), m(EAR_TIP)))
        self.add_bezier("ear-l-inner", m(EAR_TIP), (m(EAR_INNER[1]), m(EAR_INNER[0]), m(EAR_BASE)))
        # The outline runs open from the left foot round to the right foot;
        # the belly is its own straight line so the beak can sit exactly 8
        # above it (exact 8 certifies only straight-to-straight).
        self.add_contour(
            "body", "foot-l-bottom", "foot-l-top", "side-l", "ear-l-outer",
            "ear-l-inner", "crown", "ear-r-inner", "ear-r-outer", "side-r",
            "foot-r-top", "foot-r-bottom",
        )
        self.relate("connect", "body", "belly")

        # Eyes: two r3 rings touching at (24, EYE_Y), each run counterclockwise
        # through its four cardinals from the shared node.
        for side, sign in (("l", -1), ("r", 1)):
            cx = AXIS + sign * EYE_DX
            pts = [(AXIS, EYE_Y), (cx, EYE_Y + sign * EYE_R),
                   (cx + sign * EYE_R, EYE_Y), (cx, EYE_Y - sign * EYE_R)]
            members = []
            for i, a in enumerate(pts):
                mid = f"eye-{side}-{i + 1}"
                self.add_arc(mid, a, pts[(i + 1) % 4], radius_x=EYE_R, sweep=False)
                members.append(mid)
            self.add_contour(f"eye-{side}", *members, closed=True)
        self.relate("connect", "eye-l", "eye-r")

        self.add_polyline("beak", BEAK_L, BEAK_TIP, m(BEAK_L))
