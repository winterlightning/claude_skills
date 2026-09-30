"""cobra head (redraw of the new-pipeline traced SVG).

Plan: front view of a cobra, built symmetrically on the axis x=24 in the
VRECT_L keyshape (centerline box (8,4)-(40,44)), which is the one the metrics
suggest.
- head: a closed shield. Its flat crown sits on the box top (y=4), with r=4
  corners down to the shoulders at x=16/32, y=8. The jaw cubics taper to a
  rounded chin at (24,20).
- hood: each half leaves the head shoulder (a shared endpoint, declared
  `connect`) and swells to the box edge at x=8/40, y=20. It then sweeps in to
  a straight neck with walls at x=20/28 that ends on the box bottom (y=44).
  The hood is tangent-continuous from shoulder to neck.
- the trace's two eye strokes are dropped (see below).

Metric issues:
- stroke-width (info): fixed by construction. Everything is redrawn at stroke 4
  with 8-unit centerline gaps; the closest parts are the neck walls, 8 apart.
- keyshape-short-axis (warn, y filled 92%): fixed. The crown reaches y=4, the
  neck ends reach y=44 and the hood reaches x=8/40.
- clearance e1/e2 (neck walls 6.84 apart): fixed; the walls are now 8 apart.
- hole at (24,9.8), 4.6 wide: fixed. The head interior is a single open shield,
  about 12 wide and 12 tall.
- clearance e0/e3, e0/e4, e1/e4, e2/e3, e3/e4 (eyes against the head, the
  hood and each other): fixed by removing the eyes, the last step of the repair
  ladder. Two eyes need 8 between them and 8 to each head wall, so the head
  would have to be 24 of the hood's 32 units wide at eye level. That
  version was tried (the crown shared with the hood, with a chin curve and dot
  eyes). It validated, but it read as a round-headed figure, not a cobra,
  because the hood could flare only 3 units past the head. The small shield
  head under a broad hood matches the generated image and keeps the cobra
  silhouette.

validate_icon(): valid, no warnings.
Lucide construction used: none. Lucide has no cobra or snake head; its closest
match is `worm`, a side-view body with no hood or head to borrow.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "722cb33f-03cc-5935-ab1a-86a1ade0a234"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1923-cobra-head/cobra-head_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
TOP = 4                        # head crown, top of the VRECT_L centerline box
CROWN_HALF = 4                 # flat crown run each side of the axis
CORNER_R = 4                   # crown corners
HEAD_HALF = CROWN_HALF + CORNER_R   # head half-width at the shoulder (x 16..32)
CHIN_Y = 20
HOOD_X = 40                    # hood's widest point, right edge of the box
HOOD_Y = 20
NECK_X = 4                     # neck half-width: walls 8 apart
NECK_TOP = 38
BASE = 44                      # neck ends on the bottom of the box


def m(p):
    """Mirror a point about the vertical axis."""
    return (2 * AXIS - p[0], p[1])


def m_run(run):
    return tuple(tuple(m(p) for p in seg) for seg in run)


class CobraHeadRedraw(Solo48):
    icon_id = "cobra-head-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ("hooded cobra", "cobra")
    keywords = ("cobra", "snake", "hood", "reptile", "serpent", "venom", "head", "front")

    def build(self) -> None:
        crown_r = (AXIS + CROWN_HALF, TOP)
        shoulder_r = (AXIS + HEAD_HALF, TOP + CORNER_R)    # hood branches off here
        chin = (AXIS, CHIN_Y)
        jaw_r = (((shoulder_r[0], shoulder_r[1] + 6), (chin[0] + 7, CHIN_Y), chin),)
        # head: flat crown, round corners, jaw tapering to a rounded chin
        self.add_line("crown", m(crown_r), crown_r)
        self.add_arc("corner-right", crown_r, shoulder_r, radius_x=CORNER_R, sweep=True)
        self.add_bezier("jaw-right", shoulder_r, *jaw_r)
        (c1, c2, _), = m_run(jaw_r)
        self.add_bezier("jaw-left", chin, (c2, c1, m(shoulder_r)))
        self.add_arc("corner-left", m(shoulder_r), m(crown_r), radius_x=CORNER_R, sweep=True)
        self.add_contour("head", "crown", "corner-right", "jaw-right", "jaw-left", "corner-left", closed=True)
        # hood right half: out from the shoulder to the box edge, sweep in to the neck
        neck_r = (AXIS + NECK_X, NECK_TOP)
        hood_r = (
            ((shoulder_r[0] + 6, shoulder_r[1] + 1), (HOOD_X, HOOD_Y - 7), (HOOD_X, HOOD_Y)),
            ((HOOD_X, HOOD_Y + 7), (neck_r[0], NECK_TOP - 9), neck_r),
        )
        self.add_bezier("hood-right", shoulder_r, *hood_r)
        self.add_line("neck-right", neck_r, (neck_r[0], BASE))
        self.add_contour("hood-side-right", "hood-right", "neck-right")
        self.add_bezier("hood-left", m(shoulder_r), *m_run(hood_r))
        self.add_line("neck-left", m(neck_r), (m(neck_r)[0], BASE))
        self.add_contour("hood-side-left", "hood-left", "neck-left")
        self.relate("connect", "head", "hood-side-right")
        self.relate("connect", "head", "hood-side-left")
