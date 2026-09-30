"""brain-with-undivided-centre (redraw of the new-pipeline traced SVG).

Plan: a front-view brain on CIRCLE (centerline radius 20 about (24,24)),
one closed scalloped outline with an unbroken top and bottom (no dividing
fissure), and two short folds at upper left and lower right; the centre
stays open.
- outline: one closed contour of ten minor-arc lobes, mirrored about x=24
  and y=24.  Notches of the upper-left quarter are (24,7), (15,10), (8,18);
  the left-half lobes run top -> bottom with radii 5, 6, 7, 6, 5 (the
  right half mirrors them).  All arcs share one sweep, so every lobe bulges
  outward.  The farthest lobe apex is 19.56 from the centre (touch band
  19.5-20), no point exceeds 20.
- folds: the upper-left fold is a radius-7 arc from the upper-left notch
  (15,10) curling in to (21,17); the lower-right fold is the same arc turned
  180 degrees about the centre, (33,38) -> (27,31).  Each shares its notch
  with the outline and is declared `connect`.  The two fold ends are 15.2
  apart, so the centre stays empty.
Validation: validate_icon() valid, zero warnings.
Construction reference: lucide/brain (circular-arc lobes, with fold hooks
growing from the lobe junctions of the outline).  Coordinates were rebuilt
on the 48 grid; the trace only supplied the subject and layout.

Metrics issues:
- clearance e0/e1 (5.27 on centerlines, need 8): fixed.  The upper-left fold
  now starts at the upper-left notch as a declared connection.
- clearance e0/e2 (5.13 on centerlines, need 8): fixed the same way at the
  lower-right notch.
- stroke-width (trace 2.9 after fitting, target 4): fixed.  Redrawn at
  stroke 4; all gaps between separate parts are at least 8 on centerlines.
Changed from the image: in the image the folds float just inside the
outline, curled around a notch.  At stroke 4 a floating fold needs 8 of
space from both neighbouring notches (about 8-10 away), which leaves an arc
about 2 units long.  Floating folds only validated near the middle (about
4.7 from the centre), which would fill the open centre the brief asks for.
Rooting the folds in the notches keeps both their place and the open centre.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "505cc1d4-dec0-4492-aadd-1c3ba0a9d545"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1941-brain-with-undivided-centre/brain-with-undivided-centre_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
# Notches of the upper-left quarter, top centre -> side; the other three
# quarters are mirrored about x=24 and y=24, giving ten lobes.
QUARTER_NOTCHES = ((24, 7), (15, 10), (8, 18))
# Left-half lobe radii, top -> bottom (mirrored for the right half).
LOBE_RADII = (5, 6, 7, 6, 5)
# (notch, inner end, radius, sweep): the upper-left fold grows from the
# upper-left notch; the lower-right fold is the same arc turned 180 degrees
# about the centre.
FOLD = ((15, 10), (21, 17), 7, False)


def turn(p):
    return (2 * AXIS - p[0], 2 * AXIS - p[1])


def notch_ring():
    left = list(QUARTER_NOTCHES) + [(x, 2 * AXIS - y) for x, y in reversed(QUARTER_NOTCHES)]
    right = [(2 * AXIS - x, y) for x, y in reversed(left[1:-1])]
    return left + right


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
        ring = notch_ring()
        radii = LOBE_RADII + LOBE_RADII[::-1]
        ids = []
        for i, start in enumerate(ring):
            end = ring[(i + 1) % len(ring)]
            self.add_arc(f"lobe-{i}", start, end, radius_x=radii[i], sweep=False)
            ids.append(f"lobe-{i}")
        self.add_contour("outline", *ids, closed=True)

        notch, inner, r, sweep = FOLD
        self.add_arc("fold-upper-left", notch, inner, radius_x=r, sweep=sweep)
        self.add_arc("fold-lower-right", turn(notch), turn(inner), radius_x=r, sweep=sweep)
        self.relate("connect", "fold-upper-left", "outline")
        self.relate("connect", "fold-lower-right", "outline")
