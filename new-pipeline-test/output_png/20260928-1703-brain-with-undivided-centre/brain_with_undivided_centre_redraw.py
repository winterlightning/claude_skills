"""brain-with-undivided-centre (redraw of the new-pipeline traced SVG).

Plan: a frontal scalloped brain on CIRCLE (centerline radius 20 about
(24,24)), mirrored about x=24, with a short stem and two folds per
hemisphere; the centre stays open (no dividing fissure).
- outline: one open contour.  Each half runs from a top end (20,10) that
  hooks back down (the open cleft, 8 wide between the two ends), over a
  top lobe to the upper notch (10,12), an upper side lobe to the mid notch
  (7,24), a lower side lobe to the lower notch (10,36) and a bottom lobe
  to the stem top (20,39).  All lobes are integer-radius arcs, so every
  scallop is a true circular bump; the stem is 8 wide (the parallel-side
  minimum) and ends at y=43, inside the radius-20 circle.
- folds: in each hemisphere an upper fold grows from the upper notch
  down and in to (18,20) and a lower fold from the lower notch up and in
  to (18,28), both radius-8 quarter arcs, declared `connect` to the
  outline where they share the notch.  The inner fold ends sit 8 apart
  vertically and 12 apart across the open centre.
Validation: validate_icon() valid, zero warnings.
Construction reference: lucide/brain (folds rooted in the lobe notches of
the outline); coordinates rebuilt on the 48 grid, the trace only supplied
the subject and layout.

Metrics issues:
- clearance (7 errors: top ends 3.1 apart, folds 3.6-3.7 from the outline,
  upper/lower folds 7.0 apart): fixed.  The top ends are 8 apart, each fold
  shares an endpoint with the outline at a notch (a declared connection,
  not a near miss), and the fold ends are 8 apart on centerlines.
- stroke-count (7 strokes, budget 6): fixed, 5 strokes (outline + four
  folds).
- stroke-width (trace 2.9 after fit): fixed by redrawing at stroke 4 with
  8-unit centerline gaps.
Changed from the image: the folds are attached to the notches instead of
floating.  Detached, each fold needs 8 to the outline and 9 to its
partner; the hemisphere leaves a vertical band of ~14 (y 18-32) for both,
so they shrank to 2-3 unit ticks.  The image's five scallops per side are
reduced to four so each lobe stays inside radius 20.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "505cc1d4-dec0-4492-aadd-1c3ba0a9d545"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1703-brain-with-undivided-centre/brain-with-undivided-centre_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24

# Left half of the outline, top end -> stem top: (lobe end, arc radius).
TOP_END = (20, 10)
LEFT_LOBES = (
    ((10, 12), 6),     # top lobe to the upper notch
    ((7, 24), 8),      # upper side lobe to the mid notch
    ((10, 36), 8),     # lower side lobe to the lower notch
    ((20, 39), 7),     # bottom lobe to the stem
)
STEM_BOTTOM = 43
# (notch, inner end, radius, sweep): quarter arcs rooted in the notches.
UPPER_FOLD = ((10, 12), (18, 20), 8, False)
LOWER_FOLD = ((10, 36), (18, 28), 8, True)


def mirror(p):
    return (2 * AXIS - p[0], p[1])


class BrainWithUndividedCentreRedraw(Solo48):
    icon_id = "brain-with-undivided-centre-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/science"
    aliases = ("brain", "mind")
    keywords = ("brain", "mind", "think", "neurology", "intelligence",
                "psychology", "memory")

    def build(self) -> None:
        ids = []
        start = TOP_END
        knots = [TOP_END]
        for i, (end, r) in enumerate(LEFT_LOBES):
            self.add_arc(f"left-{i}", start, end, radius_x=r, sweep=False)
            ids.append(f"left-{i}")
            start = end
            knots.append(end)
        stem_top = LEFT_LOBES[-1][0]
        stem_foot = (stem_top[0], STEM_BOTTOM)
        self.add_line("stem-left", stem_top, stem_foot)
        self.add_line("stem-bottom", stem_foot, mirror(stem_foot))
        self.add_line("stem-right", mirror(stem_foot), mirror(stem_top))
        ids += ["stem-left", "stem-bottom", "stem-right"]
        # Right half walked back from the stem to its top end.
        for i in reversed(range(len(LEFT_LOBES))):
            end, r = LEFT_LOBES[i]
            self.add_arc(f"right-{i}", mirror(end), mirror(knots[i]),
                         radius_x=r, sweep=False)
            ids.append(f"right-{i}")
        self.add_contour("outline", *ids)

        for name, (notch, inner, r, sweep) in (("upper", UPPER_FOLD),
                                               ("lower", LOWER_FOLD)):
            self.add_arc(f"fold-{name}-left", notch, inner, radius_x=r, sweep=sweep)
            self.add_arc(f"fold-{name}-right", mirror(inner), mirror(notch),
                         radius_x=r, sweep=sweep)
            self.relate("connect", f"fold-{name}-left", "outline")
            self.relate("connect", f"fold-{name}-right", "outline")
