"""gazelle-facing-right (redraw of the new-pipeline traced SVG).

Plan: a right-facing gazelle in side profile on SQUARE (centerline box
(6,6)-(42,42)), rebuilt on the 48 grid rather than from trace coordinates.
- body: one closed contour. A level back (y=22) flows tangent into an
  S-curved neck that rises to the poll (31,13); a long face runs to the
  muzzle tip (42,19), a short jaw returns to the throat, the neck front
  curves down into a level belly (y=30), and a radius-4 half-round haunch
  closes the rump. Back and belly are exactly 8 apart; the neck is 8+ wide.
- horn: one backward-sweeping horn from the poll; its tip ends level at
  (19,6) so the top edge sits exactly on the box.
- tail: a short upturned stroke from the rump, tip at the left edge x=6.
- legs: two long lines, the rear leg from the haunch corner slanting back to
  (13,42), the front leg from the chest slanting forward to (33,42).
Extremes: tail x=6, horn y=6, muzzle x=42, hooves y=42.

Metric issues (svg_metrics.py) and what happened to each:
- stroke-width (info, trace 2.77 vs 4): redrawn at stroke 4 with every gap
  budgeted at 8 on centerlines.
- clearance e0/e1 (neck/head outline 2.84 from the back/horn line): the
  near-touching double outline is now one closed body contour; the horn only
  meets it at the shared poll node (declared connect).
- clearance e0/e3 and e1/e3 (legs/belly crowding the body lines, 1.7-1.8):
  the belly is a single contour edge and each leg starts from a contour node
  (chest, haunch corner), declared connect, never running alongside a wall.
- clearance e2/e3 (tail 6.6 from the rear leg/belly line): the tail starts
  at the rump node and rises away; nearest unrelated ink is 8+.
- hole at (36.1,17.3), 1.56 wide: the pinched head pocket is gone; the head
  is part of the single body hole.
- hole at (29.2,27.6), 2.91 wide: the body hole is 8 tall along the back and
  wider at the chest, passing the hole gate.
Dropped: the second horn (two horns need 8 between them along their whole
length; the diverging-pair test filled the poll with an ink blob), the two
far-side legs (four legs in a 24-wide belly read as a comb), the ear and eye.
No useful Lucide match (Lucide has no hoofed animal in profile); the rabbit /
squirrel outlines informed the single closed body contour with stroke limbs.
Validation: validate_icon() valid, build_gate PASS with 0 warnings.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ad100aeb-0efd-4518-a526-a736e51e1704"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1308-gazelle-facing-right/"
    "gazelle-facing-right_raw.svg"
)
AUTHOR = "claude-opus-5-5"

BACK_Y = 20
BELLY_Y = 28
FOOT_Y = 42


class GazelleFacingRightRedraw(Solo48):
    icon_id = "gazelle-facing-right-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ("antelope", "gazelle")
    keywords = ("gazelle", "antelope", "animal", "wildlife", "savanna", "horns", "deer")

    def build(self) -> None:
        rump = (14, 22)
        withers = (22, 22)
        poll = (31, 13)
        muzzle = (42, 19)
        throat = (36, 21)
        chest = (30, 30)
        hip = (14, 30)

        self.add_line("back", rump, withers)
        self.add_bezier("neck-back", withers, ((27, 22), (29, 18), poll))
        self.add_bezier("face", poll, ((35, 11), (39, 15), muzzle))
        self.add_line("jaw", muzzle, throat)
        self.add_bezier("neck-front", throat, ((36, 26), (35, 30), chest))
        self.add_line("belly", chest, hip)
        self.add_arc("haunch", hip, rump, radius_x=4, sweep=True)
        self.add_contour(
            "body", "back", "neck-back", "face", "jaw", "neck-front", "belly", "haunch",
            closed=True,
        )

        self.add_bezier("horn", poll, ((30, 8), (26, 6), (19, 6)))
        self.relate("connect", "horn", "body")
        self.add_bezier("tail", rump, ((10, 22), (7, 19), (6, 15)))
        self.relate("connect", "tail", "body")
        self.add_line("leg-front", chest, (33, 42))
        self.relate("connect", "leg-front", "body")
        self.add_line("leg-rear", hip, (13, 42))
        self.relate("connect", "leg-rear", "body")
