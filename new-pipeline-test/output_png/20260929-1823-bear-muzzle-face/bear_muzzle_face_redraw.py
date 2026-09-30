"""bear-muzzle-face (redraw of the new-pipeline traced SVG).

Plan: a front-facing bear head on CIRCLE (centerline radius 20 about (24,24)),
mirrored across x=24; one closed head contour plus three face marks.
- head: circle R17 centred (24,27). Its integer points (9,19)/(39,19) and
  (16,12)/(32,12) are the ear notches. The chin arc (large, through the
  bottom) reaches (24,44), exactly radius 20 from the canvas centre.
- ears: r5 arcs centred (12,15)/(36,15) through the two notches of each side,
  bulging outward (large arc). Centre distance 15 + r5 = 20, so both ears
  also touch the CIRCLE envelope; their tops (y=10) level with the forehead
  apex (y=10). Contour: left ear -> forehead -> right ear -> chin, all
  clockwise; the notches stay deliberate corners as in the trace.
- eyes: short vertical strokes x=17/31, y 23..25 (8.9 from the head arc).
- nose: a horizontal pad (21,32)-(27,32) split at the axis, with a short
  philtrum stem (24,32)-(24,35) hanging from its midpoint (shared endpoint,
  declared connect). The pad ends sit 8.06 from the eye ends
  (straight-straight) and the stem tip 9 above the chin. A closed nose
  triangle was tried first: the stroke paints it solid, but the 1-unit hole
  gate still finds a pinhole inside it, so the nose is an open T.
Extremes: chin (24,44) and ear apexes, radial 20; x 7..41, y 10..44.

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4 with every gap re-budgeted.
- hole x2 (nose pockets 2.28 wide): the hollow nose with its inner bar
  became an open T (pad + philtrum stem), which encloses nothing.
- clearance e3/e5, e3/e4 (muzzle vs nose): muzzle removed, see below.
- clearance e0/e3, e1/e3, e2/e3 (muzzle vs head and eyes): muzzle removed.
- clearance e0/e4 (nose 7.2 above the chin): nose tip now 9 above the chin.
- clearance e1/e4, e1/e5, e2/e4, e2/e5 (eyes 7.2-7.8 from the nose): eye
  ends to the nose pad ends are now 8.06, straight to straight.
Not kept: the oval muzzle ring. Inside a head of radius 17 every interior
mark must stay within radius 8 of the head centre (9 from a curved wall);
a ring holding the nose needs a band of at least 17 plus 9 to the chin and
9 to the eyes, which is about twice the room there is. Dropping the ring
(repair ladder: remove the part) keeps the nose, eyes and ears that carry
"bear". Lucide has no bear; no Lucide construction was used.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "8d5b656b-3421-5a09-b55b-b470ebf0175b"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1823-bear-muzzle-face/bear-muzzle-face_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24                 # mirror axis
HEAD_R = 17             # head circle, centre (24, 27)
EAR_R = 5               # ear circles, centres (12, 15) / (36, 15)
NOTCH_LOW = (9, 19)     # head/ear notch, left side (lower)
NOTCH_TOP = (16, 12)    # head/ear notch, left side (upper)
EYE_DX, EYE_Y0, EYE_Y1 = 7, 23, 25
NOSE_HALF, NOSE_Y, NOSE_H = 3, 32, 3


def _mirror(p):
    return (2 * AX - p[0], p[1])


class BearMuzzleFaceRedraw(Solo48):
    icon_id = "bear-muzzle-face-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ("bear-face", "bear-head")
    keywords = ("bear", "face", "head", "muzzle", "animal", "teddy", "wildlife")

    def build(self) -> None:
        low_l, top_l = NOTCH_LOW, NOTCH_TOP
        low_r, top_r = _mirror(low_l), _mirror(top_l)
        self.add_arc("ear-left", low_l, top_l, radius_x=EAR_R, large_arc=True, sweep=True)
        self.add_arc("forehead", top_l, top_r, radius_x=HEAD_R, sweep=True)
        self.add_arc("ear-right", top_r, low_r, radius_x=EAR_R, large_arc=True, sweep=True)
        self.add_arc("chin", low_r, low_l, radius_x=HEAD_R, large_arc=True, sweep=True)
        self.add_contour("head", "ear-left", "forehead", "ear-right", "chin", closed=True)

        for side, x in (("left", AX - EYE_DX), ("right", AX + EYE_DX)):
            self.add_line(f"eye-{side}", (x, EYE_Y0), (x, EYE_Y1))

        mid = (AX, NOSE_Y)
        self.add_line("nose-left", (AX - NOSE_HALF, NOSE_Y), mid)
        self.add_line("nose-right", mid, (AX + NOSE_HALF, NOSE_Y))
        self.add_line("philtrum", mid, (AX, NOSE_Y + NOSE_H))
        self.relate("connect", "nose-left", "nose-right")
        self.relate("connect", "nose-left", "philtrum")
        self.relate("connect", "nose-right", "philtrum")
