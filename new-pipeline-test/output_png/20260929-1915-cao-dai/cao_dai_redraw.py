"""cao-dai (redraw of the new-pipeline traced SVG).

Subject: the Cao Dai Divine Eye -- an almond eye with a pupil, a shallow brow
above and three rays of light below.

Plan: VRECT_L (centerline box (8,4)-(40,44)), mirrored about x=24.
- brow: one shallow arc, apex (24,4), ends (9,9)/(39,9), radius 25.
- eye: two mirrored cubic lids meeting in pointed corners at (8,22)/(40,22);
  equal control heights put the apexes exactly at (24,13) and (24,31)
  (extreme = corner + 0.75 * 12). One closed contour.
- pupil: a solid dot at the eye centre (24,22).
- rays: centre ray (24,40)-(24,44); side rays splay outward on a 2:3 slope,
  (14,38)-(10,44) and mirrored.
Vertical stack: brow 4 | 9 | lid 13 | 9 | pupil 22 | 9 | lid 31 | 9 | ray 40..44.
Every gap against a curved part is 9, because an exact 8 against a curve
comes back `review` (tried first with radius-20 lids: pupil and centre ray at
exactly 8 both warned).

Keyshape: the metrics suggested SQUARE (the trace is square), but at stroke 4
the stack needs 40 units vertically and SQUARE gives 36; VRECT_L gives 40.
A SQUARE variant without the brow also validated but lost the brow that the
generated image shows; this one reads closer to it.

Metric issues:
- stroke-width (info): redrawn at stroke 4; every gap is sized for 4.
- e0/e1 brow vs eye 6.18: fixed, the brow apex is 9 above the lid apex and
  its ends flare away from the lid.
- e1/e2 iris ring vs lids 3.39: fixed by replacing the hollow iris with a solid
  pupil dot. A ring must be r>=5 to keep a 6-unit hole, which needs lids 14
  from the centre (eye 28 tall) and leaves no room for the brow or rays.
- e1/e3, e1/e4, e1/e5 rays vs lower lid ~3.4: fixed, rays start 9 below the
  lid apex (side rays further, where the lid curves up).
- e2/e5 and e3/e5 7.06 / 7.92: fixed, the iris is gone and the side rays are
  10+ from the centre ray.
Not kept: the centre ray is only 4 long (the source's is about 8); the
vertical budget has nothing more to give.
Lucide `eye` informed the construction (two mirrored lids, centred pupil).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1a804c88-15f7-4476-b406-236f03484b85"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1915-cao-dai/cao-dai_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
EYE_Y = 22        # lid corners and pupil
EYE_HALF_W = 16   # corners at x 8 / 40
LID_K = 12        # control offset; apexes 0.75 * 12 = 9 from the corners
LID_INSET = 8     # control x inset from each corner
BROW_R = 25
BROW_END = (9, 9)
RAY_TOP = 40
RAY_BOTTOM = 44
SIDE_RAY = ((14, 38), (10, 44))


def mirror(p):
    return (2 * AXIS - p[0], p[1])


class CaoDaiRedraw(Solo48):
    icon_id = "cao-dai-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "religion"
    aliases = ("divine-eye", "caodaism")
    keywords = ("cao dai", "caodaism", "divine eye", "eye", "religion", "faith", "vietnam", "rays")

    def build(self) -> None:
        self.add_arc("brow", BROW_END, mirror(BROW_END), radius_x=BROW_R, sweep=True)

        left, right = (AXIS - EYE_HALF_W, EYE_Y), (AXIS + EYE_HALF_W, EYE_Y)
        cl, cr = left[0] + LID_INSET, right[0] - LID_INSET
        self.add_bezier("lid-upper", left, ((cl, EYE_Y - LID_K), (cr, EYE_Y - LID_K), right))
        self.add_bezier("lid-lower", right, ((cr, EYE_Y + LID_K), (cl, EYE_Y + LID_K), left))
        self.add_contour("eye", "lid-upper", "lid-lower", closed=True)

        self.add_dot("pupil", (AXIS, EYE_Y))

        self.add_line("ray-centre", (AXIS, RAY_TOP), (AXIS, RAY_BOTTOM))
        self.add_line("ray-left", *SIDE_RAY)
        self.add_line("ray-right", *(mirror(p) for p in SIDE_RAY))
