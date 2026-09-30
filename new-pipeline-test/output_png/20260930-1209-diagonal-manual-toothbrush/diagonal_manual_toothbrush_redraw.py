"""diagonal-manual-toothbrush: a manual toothbrush lying on the diagonal,
handle at the lower left, head at the upper right, three bristles standing
off the upper-left edge of the head (redraw of the new-pipeline traced SVG).

Plan: SQUARE (centerline box (6,6)-(42,42)), everything on the 45-degree
axis x+y=48 and its perpendicular.
- body: one closed hollow pill. Cap centres L=(11,37) (handle end) and
  H=(37,11) (head end), radius 5, joined at 3-4-5 lattice points so both
  caps are mirror images about the axis: upper edge x+y=41 from (7,34) to
  (34,7), lower edge x+y=55 from (41,14) to (14,41). The L cap touches
  left 6 / bottom 42, the H cap top 6 / right 42 (the keyshape extremes).
  The upper edge is split at each bristle root so the bristles share a
  node with it.
- bristles: one repeat definition, three 45-degree strokes of
  (-5,-5) from roots (30,11), (24,17), (18,23) on the upper edge; root
  step (6,-6) keeps them 8.49 apart on centerlines.

Metric issues fixed by the rebuild:
- clearance e1/e2 (2.46), e1/e3 (2.55), e2/e3 (5.01): the bristles are
  re-spaced to 8.49 on centerlines (4.49 ink) instead of the trace's 2.5.
- hole at (39.6,11.3), 0.28 wide: that sliver was the trace's notch where
  the bristle roots met the head arc; the head is now one smooth r5 cap
  and the bristles root on the straight edge, so no enclosed sliver
  remains. The only hole is the handle interior (edges 9.9 apart; the
  metrics script measures it at 5.94 inscribed and passes it).
- keyshape-short-axis (x fill 99%): both caps are built to reach the
  SQUARE box exactly on all four sides; nothing stretched.
- stroke-width (2.75): drawn at the profile stroke 4, gaps budgeted for it.
Nothing left unfixed. Trade-offs: the r5 3-4-5 joins leave a ~8 degree
kink where each cap meets its edge (no true semicircle lands on lattice
points on a 45-degree axis), and with 8.49 bristle spacing the three
bristles cover about 40% of the upper edge, more than on the trace.
Lucide: no toothbrush in the set; the pill follows the Lucide `pill`
style rounded tube, drawn with the repo's 45-degree r5 3-4-5 cap recipe.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "c34cfd53-4164-42f5-92e3-fa800780972e"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1209-diagonal-manual-toothbrush/diagonal-manual-toothbrush_raw.svg"
AUTHOR = "claude-opus-5-5"

CAP_R = 5
HANDLE_C = (11, 37)          # lower-left cap centre
HEAD_C = (37, 11)            # upper-right cap centre


def at(c, d):
    return (c[0] + d[0], c[1] + d[1])


UPPER_TAIL = at(HANDLE_C, (-4, -3))   # (7,34), on x+y=41
LOWER_TAIL = at(HANDLE_C, (3, 4))     # (14,41), on x+y=55
UPPER_HEAD = at(HEAD_C, (-3, -4))     # (34,7)
LOWER_HEAD = at(HEAD_C, (4, 3))       # (41,14)

BRISTLE_ROOTS = ((30, 11), (24, 17), (18, 23))   # step (6,-6) on x+y=41
BRISTLE = (-5, -5)


class DiagonalManualToothbrushRedraw(Solo48):
    icon_id = "diagonal-manual-toothbrush-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/personal-care"
    aliases = ("toothbrush", "manual toothbrush", "tooth brush")
    keywords = ("toothbrush", "teeth", "dental", "brush", "hygiene", "bathroom", "oral care")

    def build(self) -> None:
        # Body, clockwise from the handle end along the upper edge.
        nodes = (UPPER_TAIL, *reversed(BRISTLE_ROOTS), UPPER_HEAD)
        edges = []
        for i, (a, b) in enumerate(zip(nodes, nodes[1:])):
            self.add_line(f"upper-{i}", a, b)
            edges.append(f"upper-{i}")
        self.add_arc("head-cap", UPPER_HEAD, LOWER_HEAD, radius_x=CAP_R, sweep=True)
        self.add_line("lower", LOWER_HEAD, LOWER_TAIL)
        self.add_arc("handle-cap", LOWER_TAIL, UPPER_TAIL, radius_x=CAP_R, sweep=True)
        self.add_contour("body", *edges, "head-cap", "lower", "handle-cap", closed=True)

        for i, root in enumerate(BRISTLE_ROOTS):
            self.add_line(f"bristle-{i}", root, at(root, BRISTLE))
            self.relate("connect", f"bristle-{i}", "body")
