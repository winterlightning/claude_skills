"""bunch-of-bananas-batch-010-10 (redraw of the new-pipeline traced SVG).

Plan: three bananas hanging from one short stem and fanning down to the left,
bellies facing lower-right, on SQUARE (centerline box (6,6)-(42,42)).
- stem: a short vertical line from the top extreme (28,6) to the crown
  (28,10). Every banana edge leaves the crown heading down, so the bunch reads
  as one hand of fruit.
- front banana: one closed crescent. The belly swings out to the right
  extreme (42,28) and around the bottom to its tip on the bottom extreme
  (26,42); the inner edge bows right, parallel to the belly, back to the crown.
- middle banana: open outline. Its upper edge hooks from the crown down to
  its tip at (8,37); its underside runs back to the front banana's tip, where
  it tucks behind the front banana (shared endpoint).
- left banana: open outline. Its upper edge hooks from the crown to the left
  extreme (6,24); its underside ends on the middle banana's upper edge at
  (18,31), where it tucks behind the middle banana.
Occlusion is used instead of three separate outlines: 36 units cannot hold
six banana edges at 8-unit spacing plus holes of 6. Each banana keeps its
own hole: front 5.1, middle 9.6, left 5.1 inscribed at stroke 4 (build gate
floor 5.0 at stroke 4, i.e. 8 on centerlines).

Fixed from the trace metrics:
- stroke-width (info): redrawn at stroke 4; every gap is budgeted for it.
- clearance e0/e1 (2.23 apart): the trace's stem outline and the front
  banana's inner edge nearly touched. All edges now meet at shared nodes (the
  crown, the front tip and the left seam) and are declared connected, so no
  near-miss is left.
- holes at (39.0,24.2), (27.6,30.1) and (17.7,25.8) (1.3-2.8 wide): the
  thin traced bananas left slivers at stroke 4. The three bananas are widened
  into the fan so each interior passes the hole gate.
All issues fixed; validate_icon() valid with no warnings, build_gate pass.
Lucide `banana` informed the construction (crescent with a belly edge and a
parallel inner edge meeting at the stem). The bunch is deliberately
asymmetric: the fruit hang to the left, as in the image.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "01dfab52-1214-532b-8f84-ea5dce7a2998"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1751-bunch-of-bananas-batch-010-10/bunch-of-bananas-batch-010-10_raw.svg"
AUTHOR = "claude-opus-5-5"

STEM_TOP = (28, 6)     # top extreme
CROWN = (28, 10)       # every banana edge leaves the crown heading down
BELLY = (42, 28)       # right extreme
FRONT_TIP = (26, 42)   # bottom extreme; the middle banana tucks in here
MIDDLE_TIP = (8, 37)
LEFT_TIP = (6, 24)     # left extreme
LEFT_SEAM = (18, 31)   # left banana's underside meets the middle banana


class BunchOfBananasBatch01010Redraw(Solo48):
    icon_id = "bunch-of-bananas-batch-010-10-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ("banana bunch", "bananas")
    keywords = ("banana", "bananas", "bunch", "fruit", "tropical", "produce", "food")

    def build(self) -> None:
        self.add_line("stem", STEM_TOP, CROWN)
        # Front banana: closed crescent, belly on the right.
        self.add_bezier("front-belly", CROWN,
                        ((36, 11), (42, 19), BELLY), ((42, 37), (35, 42), FRONT_TIP))
        self.add_bezier("front-inner", FRONT_TIP,
                        ((31, 39), (33, 34), (33, 27)), ((33, 20), (31, 14), CROWN))
        self.add_contour("front", "front-belly", "front-inner", closed=True)
        # Middle banana: upper edge hooks to its tip, underside tucks behind the front one.
        self.add_bezier("middle-top", CROWN,
                        ((27, 20), (24, 26), LEFT_SEAM), ((14, 34), (11, 36), MIDDLE_TIP))
        self.add_bezier("middle-under", MIDDLE_TIP, ((13, 41), (20, 42), FRONT_TIP))
        self.add_contour("middle", "middle-top", "middle-under")
        # Left banana: upper edge hooks to its tip, underside tucks behind the middle one.
        self.add_bezier("left-top", CROWN, ((26, 17), (17, 23), LEFT_TIP))
        self.add_bezier("left-under", LEFT_TIP, ((9, 28), (13, 31), LEFT_SEAM))
        self.add_contour("left", "left-top", "left-under")
        for a, b in (("stem", "front"), ("stem", "middle"), ("stem", "left"),
                     ("front", "middle"), ("front", "left"), ("middle", "left")):
            self.relate("connect", a, b)
