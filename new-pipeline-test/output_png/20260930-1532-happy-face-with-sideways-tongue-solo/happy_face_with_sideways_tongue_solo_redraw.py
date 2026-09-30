"""happy-face-with-sideways-tongue-solo (redraw of the new-pipeline traced SVG).

Plan: a round emoji face on CIRCLE (the suggested keyshape, fit score 1.25),
centerline radius 20 about (24,24). Every inner part stays within radius 12
of the centre so it keeps the 8 centerline gap to the face outline.
- eyes: two short vertical strokes mirrored on x=24 at x=18 and x=30,
  y 14..17 (the top is 8.3 inside the face outline).
- smile: arc of the circle about (24,19), r10, from the left corner (16,25)
  down to its lowest point (24,29); both corners sit 8.25 below the eyes.
- tongue: instead of hanging a closed U under a continuous smile (which traps
  a hole far below the 6-unit floor), the tongue replaces the right half of
  the smile. From (24,29) it swings out as a half-ellipse lobe on the 1:2
  axis (down and to the right), 8.9 wide across its root, apex (31,33), and
  returns to the right corner (32,25), which mirrors the left corner. The
  lip-to-tongue corner at (24,29) is deliberate, as in the generated image.
  A half-circle lobe was tried first and filled in at 48 px; the deeper
  half-ellipse keeps an open tongue shape.
Lucide `smile` informed the face/eye/smile layout (circle, two short eyes,
arc mouth); the tongue follows the existing smiling-face-with-tongue-out
construction (tongue drawn as part of the mouth path), moved sideways.

Metric issues fixed:
- clearance e0/e5 (tongue 4.51 from the outline): the tongue lobe is at most
  11.5 from the centre, 8.5 inside the outline.
- clearance e1/e3, e2/e3, e2/e4, e2/e5 (eyes 6.1-7.2 from the mouth): the eyes
  are shortened to y 14..17 and the mouth corners placed at y 25, 8.25 away.
- narrow-join e3/e4 (0.01 deg wedge at the tongue root): the trace's stray
  e4 stub is dropped; the mouth is one open contour with a single corner.
- hole at (30.9,34.2), 2.24 wide: the tongue no longer closes against the
  smile, so the mouth encloses no hole.
- stroke-width (info): redrawn at stroke 4 with every gap budgeted at 8.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a2b16bc0-fda9-42be-8b90-0bef7d9dc58b"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1532-happy-face-with-sideways-tongue-solo/happy-face-with-sideways-tongue-solo_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS, FACE_R = 24, 20
EYE_DX, EYE_TOP, EYE_BOTTOM = 6, 14, 17
SMILE_R = 10                            # smile arc about (24,19)
LEFT_CORNER, SMILE_LOW, RIGHT_CORNER = (16, 25), (24, 29), (32, 25)
TONGUE_DEPTH = 1.5                      # lobe depth / half chord; apex (31,33)
KAPPA = 0.5523                          # cubic quarter-circle factor


def _lobe(start, end, depth):
    """Two cubics tracing a half ellipse from ``start`` to ``end``, bulging
    clockwise (down and right for this chord) ``depth`` half-chords deep."""
    mx, my = (start[0] + end[0]) / 2, (start[1] + end[1]) / 2
    rx, ry = start[0] - mx, start[1] - my          # radius vector at start
    tx, ty = ry * depth, -rx * depth               # midpoint to apex
    apex = (mx + tx, my + ty)
    k = KAPPA
    r = lambda p: (round(p[0], 2), round(p[1], 2))
    return (
        (r((start[0] + k * tx, start[1] + k * ty)), r((apex[0] + k * rx, apex[1] + k * ry)), r(apex)),
        (r((apex[0] - k * rx, apex[1] - k * ry)), r((end[0] + k * tx, end[1] + k * ty)), end),
    )


class HappyFaceWithSidewaysTongueSoloRedraw(Solo48):
    icon_id = "happy-face-with-sideways-tongue-solo-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    aliases = ("tongue out face", "playful face", "silly face", "cheeky emoji")
    keywords = ("face", "emoji", "tongue", "smile", "happy", "playful", "silly", "joke", "cheeky")

    def build(self) -> None:
        a, r = AXIS, FACE_R
        self.add_arc("face-top", (a - r, a), (a + r, a), radius_x=r)
        self.add_arc("face-bottom", (a + r, a), (a - r, a), radius_x=r)
        self.add_contour("face", "face-top", "face-bottom", closed=True)

        for side, x in (("left", a - EYE_DX), ("right", a + EYE_DX)):
            self.add_line(f"eye-{side}", (x, EYE_TOP), (x, EYE_BOTTOM))

        self.add_arc("smile", LEFT_CORNER, SMILE_LOW, radius_x=SMILE_R, sweep=False)
        self.add_bezier("tongue", SMILE_LOW, *_lobe(SMILE_LOW, RIGHT_CORNER, TONGUE_DEPTH))
        self.add_contour("mouth", "smile", "tongue")
