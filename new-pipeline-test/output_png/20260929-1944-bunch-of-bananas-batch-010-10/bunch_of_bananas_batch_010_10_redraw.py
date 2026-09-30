"""bunch-of-bananas-batch-010-10 (redraw of the new-pipeline traced SVG).

Plan: three bananas fanning right from one short stem at the upper left, as in
the generated image, on SQUARE (centerline box (6,6)-(42,42), exact on all four
sides: stem top y=6, front banana's left belly x=6 and underside y=42, the top
and middle tips x=42).
- stem: a short slanted line (8,6)-(10,12) ending on the crown (10,12); every
  banana edge leaves the crown.
- front banana: one closed crescent. The outer edge runs down the left belly,
  under the bunch and up to its tip (36,38); the inner edge bows back to the
  crown.
- middle banana: open outline. Its upper edge runs from the crown through the
  seam (30,28) to the tip (42,28); its underside tucks behind the front banana
  at the front tip (shared node).
- top banana: open outline. A gently sagging upper edge runs from the crown to
  the tip (42,16); its underside tucks behind the middle banana at the seam.
The trace drew each banana as a full outline; at stroke 4 the 36-unit box
cannot hold six edges with 8-unit gaps and 6-unit holes, so the bananas
overlap and share edges instead. Converging edges always end on one shared
node (crown, seam, front tip), so no tapered pair counts as a near miss.

Fixed from the trace metrics:
- stroke-width (info): redrawn at stroke 4, every gap budgeted for it.
- keyshape-short-axis (y filled 87%): the bunch is re-proportioned taller so
  the stem reaches y=6 and the front banana y=42; no stretch of the trace.
- clearance e0/e1 (2.3 apart at the stem): the traced stem box and the top
  banana outline nearly touched. The stem is now one line ending on the crown,
  and every contact is a shared, declared node.
- narrow-join e1/e0 (18.75 deg at (26.3,26.7)): the top banana's underside
  now meets the middle banana at the seam at about 33 deg, so the strokes no
  longer fuse into a long wedge. It stays a slanted tuck, not a right-angle T:
  a steeper arrival bent the underside into an S that read worse.
- holes at (12.7,29.8), (26.3,23.5), (24.9,29.8) (2.2-3.3 wide): the bananas
  are widened so each interior passes the build gate's hole floor.
All issues fixed; validate_icon() valid with no warnings, build_gate pass.
Lucide `banana` informed the construction (belly edge plus a parallel inner
edge meeting at the stem). The asymmetric fan is deliberate, as in the image.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "01dfab52-1214-532b-8f84-ea5dce7a2998"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1944-bunch-of-bananas-batch-010-10/bunch-of-bananas-batch-010-10_raw.svg"
AUTHOR = "claude-opus-5-5"

STEM_TOP = (8, 6)
CROWN = (10, 12)
LEFT = (6, 24)
BOTTOM = (22, 42)
FRONT_TIP = (36, 38)
SEAM = (30, 28)
MID_TIP = (42, 28)
TOP_TIP = (42, 16)


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
        self.add_bezier("front-outer", CROWN,
                        ((8, 15), (6, 19), LEFT),
                        ((6, 34), (13, 42), BOTTOM),
                        ((29, 42), (34, 41), FRONT_TIP))
        self.add_bezier("front-inner", FRONT_TIP, ((24, 38), (12, 28), CROWN))
        self.add_contour("front", "front-outer", "front-inner", closed=True)

        self.add_bezier("mid-top-a", CROWN, ((15, 18), (22, 26), SEAM))
        self.add_bezier("mid-top-b", SEAM, ((35, 29), (39, 29), MID_TIP))
        self.add_bezier("mid-under", MID_TIP, ((42, 33), (40, 36), FRONT_TIP))
        self.add_contour("middle", "mid-top-a", "mid-top-b", "mid-under")

        self.add_bezier("top-upper", CROWN, ((18, 16), (32, 20), TOP_TIP))
        self.add_bezier("top-under", TOP_TIP, ((41, 24), (35, 26), SEAM))
        self.add_contour("top", "top-upper", "top-under")

        for a, b in (("stem", "front"), ("stem", "middle"), ("stem", "top"),
                     ("front", "middle"), ("front", "top"), ("middle", "top")):
            self.relate("connect", a, b)
