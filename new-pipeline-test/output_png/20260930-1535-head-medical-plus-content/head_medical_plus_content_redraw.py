"""head-medical-plus-content (redraw of the new-pipeline traced SVG).

Plan: a left-facing human head in side profile with a short neck, and a medical
plus inside the cranium, on VRECT_L (the suggested keyshape, fit score 1.17),
centerline box (8,4)-(40,44).
- cranium: two elliptical quarters about (26,19), rx 14 / ry 15, from the
  forehead extreme (12,19) over the crown (26,4) to the back extreme (40,19).
  The top and back reach the box edges at the arc apexes.
- face: the nose bridge drops from the forehead to the tip (8,25) on the box's
  left edge, returns to (11,27), and the jaw runs down to a radius-4 chin
  (11,31)-(15,35); a radius-2 corner turns the chin into the front of the neck
  at x=19.
- back: one smooth cubic from (40,19) (vertical tangent, continuing the
  cranium) into the nape and down the back of the neck at x=33, again with a
  vertical tangent, so the skull and neck join without a kink.
- neck: a closed base at y=44 from x=19 to x=33, as in the generated image.
- plus: two strokes of half-length 5 crossing at (26,21), split at the centre
  and declared connected. The arm ends sit 9 from the forehead and about 9 from
  the back of the head, 12 below the crown.
Lucide `plus` informed the cross; no useful Lucide profile-head match exists
(the construction follows the image, not the older gpt-6 module).

Metric issues fixed:
- clearance e0/e1 (plus 6.74 from the forehead): the plus is shorter (10
  instead of ~14) and centred in the cranium; every arm end is >= 8.5 from the
  head outline on centerlines.
- clearance e1/e2 (0.0): the two plus strokes cross on purpose; they now share
  the centre point (26,21) and are declared `connect`, so this is a joint, not
  a collision.
- keyshape-short-axis (y filled 92%): the crown is at y=4 and the neck base at
  y=44, filling VRECT_L exactly on both axes.
- stroke-width (info): redrawn at stroke 4 with every gap budgeted at 8.
Not applicable:
- no-head (warn): the subject is a single profile silhouette, not a stick
  figure with a detached head, so there is no head/torso gap to certify.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "348cbff9-1f65-4ac0-894f-5968b56f3054"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1535-head-medical-plus-content/head-medical-plus-content_raw.svg"
AUTHOR = "claude-opus-5-5"

CX, CY, RX, RY = 26, 19, 14, 15        # cranium ellipse
NOSE_TIP, NOSE_BASE = (8, 25), (11, 27)
JAW_Y, CHIN_R, CHIN_Y = 31, 4, 35
NECK_FRONT, NECK_BACK, NECK_TOP, BASE_Y = 19, 33, 37, 44
PLUS_C, PLUS_ARM = (26, 21), 5


class HeadMedicalPlusContentRedraw(Solo48):
    icon_id = "head-medical-plus-content-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ("mental health", "head plus", "medical head", "brain health")
    keywords = ("head", "profile", "medical", "plus", "health", "mind", "psychology", "care")

    def build(self) -> None:
        front, crown, back = (CX - RX, CY), (CX, CY - RY), (CX + RX, CY)
        nape = (NECK_BACK, 35)
        self.add_line("neck-base", (NECK_FRONT, BASE_Y), (NECK_BACK, BASE_Y))
        self.add_line("neck-back", (NECK_BACK, BASE_Y), nape)
        self.add_bezier("nape", nape, ((NECK_BACK, 28), (CX + RX, 27), back))
        self.add_arc("crown-back", back, crown, radius_x=RX, radius_y=RY, sweep=False)
        self.add_arc("crown-front", crown, front, radius_x=RX, radius_y=RY, sweep=False)
        self.add_line("nose-bridge", front, NOSE_TIP)
        self.add_line("nose-under", NOSE_TIP, NOSE_BASE)
        self.add_line("jaw", NOSE_BASE, (NOSE_BASE[0], JAW_Y))
        self.add_arc(
            "chin", (NOSE_BASE[0], JAW_Y), (NOSE_BASE[0] + CHIN_R, CHIN_Y),
            radius_x=CHIN_R, sweep=False,
        )
        self.add_line("chin-under", (NOSE_BASE[0] + CHIN_R, CHIN_Y), (NECK_FRONT - 2, CHIN_Y))
        self.add_arc("throat", (NECK_FRONT - 2, CHIN_Y), (NECK_FRONT, NECK_TOP), radius_x=2)
        self.add_line("neck-front", (NECK_FRONT, NECK_TOP), (NECK_FRONT, BASE_Y))
        self.add_contour(
            "head", "neck-base", "neck-back", "nape", "crown-back", "crown-front",
            "nose-bridge", "nose-under", "jaw", "chin", "chin-under", "throat",
            "neck-front", closed=True,
        )

        x, y = PLUS_C
        self.add_polyline("plus-horizontal", (x - PLUS_ARM, y), PLUS_C, (x + PLUS_ARM, y))
        self.add_polyline("plus-vertical", (x, y - PLUS_ARM), PLUS_C, (x, y + PLUS_ARM))
        self.relate("connect", "plus-horizontal", "plus-vertical")
