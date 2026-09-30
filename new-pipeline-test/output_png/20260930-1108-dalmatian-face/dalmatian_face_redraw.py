"""dalmatian-face (redraw of the new-pipeline traced SVG).

Subject: the front face of a Dalmatian: a round head with two drooping ears,
two eyes, a nose and one large spot around the left eye.

PLAN
- Keyshape: CIRCLE (radius 20 centreline about (24,24)), not the suggested
  SQUARE. The trace is 36x26, so SQUARE would need a 1.38 stretch on y. The
  eye patch also needs about 32 units across the eye line: wall, 9, eye, 9,
  patch edge, 9, eye, 9, wall. The ears cannot sit beside the face at that
  height, so they hang below the eye line on the lower sides. Only the
  radius-20 disc is wide enough there, and the head is round anyway.
- Head: one closed contour. The dome is a radius-20 arc about C through the
  lattice points (12,8), (4,24) and (8,36), so it touches the keyshape all
  the way round. Each ear is the dome's lower side plus a hook that curls
  under to the jaw point (14,34). The chin is a radius-10 arc about
  (24,34), from jaw to jaw, with its bottom at (24,44).
- Ears: a straight inner edge rises from each jaw point to y=26; the chin arc
  leaves the jaw vertically, so edge and chin are tangent-continuous. The
  left edge ends on the bottom knot of the patch. The right edge ends free
  at the same height.
- Patch: one bezier from (12,8) to (4,24), both on the dome, passing about
  9 units from the left eye all the way round. The dome closes the patch;
  both ends are declared connections.
- Eyes: dots at (15,17) and (33,17), mirrored about x=24 and 8.3 or more
  from the dome. Nose: a 4-unit near-closed triangle outline that fills solid
  at stroke 4 (a closed triangle would enclose an undersized hole).

METRIC ISSUES
- keyshape-short-axis (SQUARE y fill 73%): fixed by switching to CIRCLE;
  the dome touches radius 20 exactly.
- clearance errors, all 14 (e0..e9: spot, eyes, nose, inner ear lines, chin):
  fixed. Every separate part is at least 8 from the others on centerlines
  (eye to patch about 9, patch to right eye 9, nose to inner ear lines 8,
  nose to the chin's jaw ends 8.06).
- hole errors, all 5 (slivers inside the spot, ears and nose): fixed. The
  ear lobes open into the face or are wide (left ear under the patch), the
  patch is a large hole, and the nose is open, so the build gate reports no
  undersized holes.
- loose-join infos, all 4 (e1/e2/e5 to the eye-dot fragments e3/e4): fixed.
  The dome and ears are one contour, and every contact shares an exact
  endpoint with relate('connect').
- stroke-width info: the drawing is authored at stroke 4 and every gap is
  measured at that width.
- stroke-count warning (10 strokes, budget 6): reduced to 7, not 6. Each eye
  is its own dot, and the two inner ear edges branch off the head contour,
  so none of them can join its path.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "fd0d9c0a-6ed5-48eb-b294-bbe6008deef9"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1108-dalmatian-face/dalmatian-face_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
HEAD_R = 20             # dome about (24,24): the CIRCLE keyshape radius
TOP = (24, 4)
SPOT_TOP = (12, 8)      # C + (-12,-16): lattice point where the patch starts
SIDE = (4, 24)          # C + (-20, 0): patch ends, ear side begins
EAR_TIP = (8, 36)       # C + (-16, 12): dome hands over to the ear hook
JAW = (14, 34)          # hook, chin and inner ear edge meet here
CHIN_C = (24, 34)
CHIN_R = 10             # chin bottom (24,44) also touches the keyshape
EAR_TOP = (14, 26)      # inner ear edge top; bottom knot of the patch
EYE = (15, 17)
NOSE_Y = 34


def _m(p):
    """Mirror a point or control across the vertical axis."""
    return (2 * AXIS - p[0], p[1])


class DalmatianFaceRedraw(Solo48):
    icon_id = "dalmatian-face-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/dog"
    aliases = ("dalmatian", "spotted dog", "dog face")
    keywords = ("dalmatian", "dog", "puppy", "spot", "patch", "pet", "animal",
                "face", "head", "floppy ears")

    def build(self) -> None:
        # Hook leaves the dome along its tangent (3,4) and lands vertically
        # on the jaw, where the chin arc continues downward.
        hook = ((9.5, 38.0), (14.0, 38.5), JAW)
        chin = (AXIS, CHIN_C[1] + CHIN_R)
        self.add_arc("dome-tl", TOP, SPOT_TOP, radius_x=HEAD_R, sweep=False)
        self.add_arc("dome-sl", SPOT_TOP, SIDE, radius_x=HEAD_R, sweep=False)
        self.add_arc("dome-el", SIDE, EAR_TIP, radius_x=HEAD_R, sweep=False)
        self.add_bezier("hook-l", EAR_TIP, hook)
        self.add_arc("chin-l", JAW, chin, radius_x=CHIN_R, sweep=False)
        self.add_arc("chin-r", chin, _m(JAW), radius_x=CHIN_R, sweep=False)
        self.add_bezier("hook-r", _m(JAW), (_m(hook[1]), _m(hook[0]), _m(EAR_TIP)))
        self.add_arc("dome-er", _m(EAR_TIP), _m(SIDE), radius_x=HEAD_R, sweep=False)
        self.add_arc("dome-sr", _m(SIDE), _m(SPOT_TOP), radius_x=HEAD_R, sweep=False)
        self.add_arc("dome-tr", _m(SPOT_TOP), TOP, radius_x=HEAD_R, sweep=False)
        self.add_contour("head", "dome-tl", "dome-sl", "dome-el", "hook-l", "chin-l",
                         "chin-r", "hook-r", "dome-er", "dome-sr", "dome-tr", closed=True)

        # Patch round the left eye, closed by the dome between SPOT_TOP and SIDE.
        self.add_bezier(
            "spot", SPOT_TOP,
            ((17, 8), (24, 10), (24, 16)),
            ((24, 22), (19, 26), EAR_TOP),
            ((9, 26), (6, 24), SIDE),
        )
        self.relate("connect", "spot", "dome-tl", "dome-sl")
        self.relate("connect", "spot", "dome-sl", "dome-el")

        # Inner ear edges continue the chin upward; the left one meets the patch.
        self.add_line("leg-l", JAW, EAR_TOP)
        self.add_line("leg-r", _m(JAW), _m(EAR_TOP))
        self.relate("connect", "leg-l", "hook-l", "chin-l")
        self.relate("connect", "leg-r", "chin-r", "hook-r")
        self.relate("connect", "leg-l", "spot")

        self.add_dot("eye-l", EYE)
        self.add_dot("eye-r", _m(EYE))
        # Near-closed triangle: fills solid at stroke 4 without an enclosed hole.
        self.add_polyline("nose", (AXIS, NOSE_Y + 1), (AXIS - 2, NOSE_Y - 1),
                          (AXIS + 2, NOSE_Y - 1), (AXIS + 1, NOSE_Y))
